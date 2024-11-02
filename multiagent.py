import streamlit as st
from crewai import Crew, Task, Agent, LLM
from crewai_tools import SerperDevTool, tool
import os
import kaggle
from dotenv import load_dotenv
load_dotenv()
# Set up environment variables

os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\lenin\.kaggle'

# Initialize tools
search_tool = SerperDevTool()

# Define Kaggle dataset search function with the @tool decorator
@tool("Kaggle Dataset Search Tool")
def search_kaggle_datasets(question: str) -> str:
    """
    Searches for datasets on Kaggle based on the user's query.
    This tool is useful for finding datasets relevant to a specific topic or keyword.
    """
    kaggle.api.authenticate()
    datasets = kaggle.api.dataset_list(search=question)
    results = []
    for dataset in datasets:
        results.append({
            'title': dataset.title,
            'url': f"https://www.kaggle.com/{dataset.ref}",
            'description': dataset.subtitle
        })
    
    # Format the response
    if results:
        response = f"Found {len(results)} datasets:\n" + "\n".join(
            [f"{res['title']} - {res['url']}" for res in results]
        )
    else:
        response = "No datasets found for your query."
    
    return response

# Set up LLM
llm = LLM(
    model="groq/llama3-70b-8192",
    temperature=0.3,
    max_tokens=4096,
    api_key=os.getenv("MY_SECRET_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Define agents and tasks
industry_research_agent = Agent(
    llm=llm,
    function_calling_llm=llm,
    role="Market Research Analyst",
    goal="Provide insights about {topic} through market analysis",
    backstory=("""You are a Market Research Analyst conducting research on {topic}.
    Your main role is to gather and analyze market data to understand market trends, consumer behavior, and competitive dynamics.
    Currently, you are working on a project to assess the market potential for {topic} and analyze the competitive landscape."""),
    allow_delegation=False,
    tools=[search_tool],
    verbose=1
)

task1 = Task(
    description="Analyze the financial performance of {topic}, focusing on operational areas like supply chain and customer service for {topic}.",
    expected_output="A detailed financial report of {topic} including key financial trends with structured summary and also give its competitor financial report",
    output_file="industry_research_output.txt",
    agent=industry_research_agent,
)

use_case_agent = Agent(
    llm=llm,
    function_calling_llm=llm,
    role="Use Case Specialist",
    goal="AI and Generative AI use cases tailored to company’s strategic needs like supply chain,predictive maintenance, customer service and company's strategic needs.",
    backstory="An AI expert in applying AI solutions for industry challenges.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=1,
)

task2 = Task(
    description="Generate AI and GenAI use cases with explanation of each usecase with objective,application,benefit for {topic}",
    expected_output="A list of use cases with explanation of each usecase with objective,application,benefit.",
    output_file="use_case_generation_output.txt",
    agent=use_case_agent,
)

resource_agent = Agent(
    llm=llm,
    function_calling_llm=llm,
    role="Resource Collector",
    goal="Aggregate relevant datasets from Kaggle, HuggingFace, and GitHub to support AI use cases for the company.",
    backstory="Experienced in dataset collection for machine learning and AI projects.",
    allow_delegation=False,
    tools=[search_kaggle_datasets, search_tool],
    verbose=1,
)

task3 = Task(
    description="Search for datasets related to each usecase among all the proposed AI use cases for {topic}",
    expected_output="Give me the list of usecases and dataset links for each usecase with brief descriptions of each usecase relevant to {topic}.",
    output_file="Resource_output.txt",
    agent=resource_agent,
)

crew = Crew(agents=[industry_research_agent, use_case_agent, resource_agent], tasks=[task1, task2, task3], verbose=1)

# Streamlit Interface
st.title("Multi-Agent System Interface")
st.markdown("### Run multi-agent tasks for industry research and AI use case generation")

# Input form for topic
topic = st.text_input("Enter the company or topic for the agents to research:", "SpaceX")

if st.button("Run Agents"):
    st.write("Running agents with the topic:", topic)
    output = crew.kickoff(inputs={'topic': topic})
    st.text_area("Agent Output", output, height=300)

    st.success("Task completed. Check the output files for detailed results.")
