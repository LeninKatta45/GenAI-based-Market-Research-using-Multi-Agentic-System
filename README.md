# Multi-Agent AI-Powered Company Analysis and Use Case Generator

This project is a multi-agent system built using Crew AI, Streamlit, and various AI tools to provide comprehensive industry research and generate AI and Generative AI use cases tailored for strategic needs. The system integrates advanced language models and data search tools to streamline complex analysis, research, and data collection.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Agents and Tasks](#agents-and-tasks)
- [Contributing](#contributing)

## Overview
This project leverages a multi-agent framework to execute the following:
1. Market research analysis on a specified topic.
2. Generation of AI and Generative AI use cases with detailed explanations.
3. Aggregation of relevant datasets from Kaggle and other sources to support AI use cases.

## Features
- **Market Research**: Provides in-depth insights into a company's financial performance, supply chain, and customer service.
- **Use Case Generation**: Generates tailored AI and Generative AI use cases with objectives, applications, and benefits.
- **Dataset Collection**: Searches and compiles datasets from Kaggle, HuggingFace, and GitHub related to specified use cases.

## Tech Stack
- **Python**
- **Streamlit**: For building the user interface.
- **Crew AI**: Framework for orchestrating multi-agent systems.
- **LLM (Large Language Model)**: Groq's `llama3-70b-8192` for natural language understanding.
- **Kaggle API**: For dataset searches.
- **SerperDev Tool**: For enhanced search capabilities.
- **dotenv**: For environment variable management.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/multi-agent-research-usecase-generator.git
    cd multi-agent-research-usecase-generator
    ```

2. **Install the Required Packages**:
    Ensure you have Python 3.8+ installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**:
    Create a `.env` file and add your API keys:
    ```
    MY_SECRET_KEY=your_groq_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

4. **Configure Kaggle API**:
    - Create a directory for your Kaggle configuration:
      ```bash
      mkdir ~/.kaggle
      ```
    - Place your `kaggle.json` (API credentials) in this directory.

5. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open the Streamlit app in your browser.
2. Enter the company or topic you want to research (e.g., `SpaceX`).
3. Click on the "Run Agents" button to start the tasks.
4. Review the output displayed in the text area and access detailed results in the output files.

## Agents and Tasks

### Agents
- **Market Research Analyst**:
  - Role: Provides insights into the specified topic.
  - Tools: SerperDev Tool for enhanced search capabilities.

- **Use Case Specialist**:
  - Role: Generates AI and Generative AI use cases.
  - Tools: SerperDev Tool.

- **Resource Collector**:
  - Role: Searches for relevant datasets.
  - Tools: Kaggle Dataset Search Tool, SerperDev Tool.

### Tasks
- **Task 1**: Analyze financial performance with a focus on operational areas.
- **Task 2**: Generate AI and GenAI use cases with detailed explanations.
- **Task 3**: Search for datasets related to proposed use cases.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any features or bug fixes.

