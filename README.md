# Langchain API Calls using FastAPI, Langserve, and Streamlit

This repository demonstrates how to build an API server using **FastAPI**, **Langchain**, and **Langserve** to make LLM-powered API calls. The application allows users to generate essays and poems through a simple user interface powered by **Streamlit**.


## Overview

This project sets up an API server that integrates with Langchain's language models via **Langserve**. It provides two main functionalities:
1. Generate a detailed essay on a given topic (1000 words).
2. Generate a poem on a given topic (200 words, aimed at a 5-year-old child).

The user interface is created using **Streamlit**, which allows users to interact with the API and generate responses in real-time.

## Overview

This project sets up an API server that integrates with Langchain's language models via **Langserve**. It provides two main functionalities:
1. Generate a detailed essay on a given topic (1000 words).
2. Generate a poem on a given topic (200 words, aimed at a 5-year-old child).

The user interface is created using **Streamlit**, which allows users to interact with the API and generate responses in real-time.

## Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Langserve**: A server framework for serving Langchain models.
- **Langchain**: A framework for developing applications powered by language models.
- **Ollama (Llama2 model)**: A large language model provided by the Langchain community.
- **Streamlit**: A web framework for creating interactive, data-driven applications.
- **Uvicorn**: A lightning-fast ASGI server used to run FastAPI.


## Installation

### Prerequisites
- Python 3.8+
- Pipenv or any other package manager

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/ashzad123/LangServe.git
    cd LangServe
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate 
     # On Windows, use 
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project and add any required environment variables (e.g., API keys for language models).

5. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload --host 127.0.0.1 --port 3535
    ```

6. Run the Streamlit client:
    ```bash
    streamlit run client.py
    ```