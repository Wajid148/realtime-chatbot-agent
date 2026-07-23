# 💬 Real-Time Chatbot Agent

A streaming AI chatbot built with **OpenAI's API** and **Streamlit**, featuring:
- Real-time streaming responses (word-by-word, like ChatGPT)
- Conversation memory across turns
- Configurable system prompt (change the agent's role/personality)
- Model selector (gpt-4o-mini, gpt-4o, gpt-3.5-turbo)

Built as a portfolio project to demonstrate AI chatbot development for freelance/client work.

---

## 🚀 Run Locally

1. Clone this repo and enter the folder:
   ```bash
   git clone <your-repo-url>
   cd realtime-chatbot-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key. Copy the example secrets file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```
   Then open `.streamlit/secrets.toml` and paste your real key in place of the placeholder.

4. Run the app:
   ```bash
   streamlit run app.py
   ```

   The app opens at `http://localhost:8501`.

---

## ☁️ Deploy for Free (Streamlit Community Cloud)

1. Push this project to a **public GitHub repo** (make sure `.streamlit/secrets.toml` is NOT included — `.gitignore` already handles this).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select your repo, branch `main`, and set the main file to `app.py`.
4. Under **Advanced settings → Secrets**, paste:
   ```toml
   OPENAI_API_KEY = "sk-your-real-key-here"
   ```
5. Click **Deploy**. You'll get a live public URL like:
   `https://your-app-name.streamlit.app`

That live link is what you share with Upwork clients as your portfolio demo.

---

## 🛠️ Tech Stack
- Python
- Streamlit (UI)
- OpenAI API (chat completions, streaming)

## 📌 Notes
- Get an API key at [platform.openai.com](https://platform.openai.com/api-keys)
- gpt-4o-mini is recommended for demos — it's fast and very cheap
- This project can be extended into a RAG chatbot (answering from your own documents) — see Project ideas in the freelancer roadmap
