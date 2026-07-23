
🗨️ Real-Time Chatbot Agent

A production-style, real-time streaming AI chatbot built with Streamlit and the Groq API. This project demonstrates core skills required for building custom AI chat applications: streaming responses, conversation memory, configurable agent behavior, and cloud deployment.

Developed as a portfolio piece to showcase AI chatbot development capabilities for freelance and client engagements.

✨ Features
Feature	Description
Real-time streaming	Responses render word-by-word, similar to ChatGPT
Conversation memory	Full chat history is retained and sent with each request
Configurable system prompt	Adjust the assistant's role, tone, and behavior on the fly
Model selection	Switch between llama-3.3-70b-versatile, llama-3.1-8b-instant, and gemma2-9b-it
Secure key handling	Supports both Streamlit Secrets (recommended) and manual key entry
One-click deploy	Ready for free hosting on Streamlit Community Cloud

🖥️ Demo

Live app: https://realtime-chatbot-agent-myw7jc63emqbt7qzxwiruh.streamlit.app/

🚀 Getting Started

Prerequisites
Python 3.9+
A free Groq API key
Local Setup
Clone the repository
bash
   git clone <your-repo-url>
   cd realtime-chatbot-agent
Install dependencies
bash
   pip install -r requirements.txt
Configure your API key Copy the example secrets file:
bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml

Open .streamlit/secrets.toml and replace the placeholder with your key:

toml
   GROQ_API_KEY = "gsk_your-real-key-here"
Run the app
bash
   streamlit run app.py

The app will be available at http://localhost:8501.

☁️ Deployment (Streamlit Community Cloud)

Push the project to a public GitHub repository. Ensure .streamlit/secrets.toml is not committed — this is already handled by .gitignore.
Go to share.streamlit.io and sign in with GitHub.
Click New app, select the repository and main branch, and set the main file path to app.py.
Under Advanced settings → Secrets, add:
toml
   GROQ_API_KEY = "gsk_your-real-key-here"
Click Deploy. Streamlit will provision a live URL in the form:
   https://realtime-chatbot-agent-myw7jc63emqbt7qzxwiruh.streamlit.app/

Use this link to showcase the project to clients or in your portfolio.

🛠️ Tech Stack
Language: Python
Frontend/UI: Streamlit
AI Provider: Groq API (OpenAI-compatible, free tier, streaming chat completions)

🗺️ Roadmap

 Add Retrieval-Augmented Generation (RAG) to answer questions from custom documents
 Add persistent chat history (database-backed sessions)
 Add usage/token tracking
 Add authentication for multi-user deployments
 
📄 License

This project is available for personal and portfolio use. Feel free to fork and adapt it for your own projects.

Author: Wajida
