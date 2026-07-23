import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Real-Time Chatbot Agent", page_icon="💬", layout="centered")
st.title("💬 Real-Time Chatbot Agent")
st.caption("A streaming AI chatbot built with Groq (free) + Streamlit — portfolio project by Wajida")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Groq API Key", type="password", help="Get a free key at console.groq.com/keys")
    model = st.selectbox("Model", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"], index=0)
    system_prompt = st.text_area(
        "System Prompt (agent personality/role)",
        value="You are a helpful, friendly assistant. Answer clearly and concisely.",
        height=100,
    )
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

resolved_key = None
try:
    resolved_key = st.secrets["GROQ_API_KEY"]
except Exception:
    resolved_key = api_key

if not resolved_key:
    st.info("👈 Enter your free Groq API key in the sidebar to start chatting. Get one at console.groq.com/keys")
    st.stop()

client = OpenAI(api_key=resolved_key, base_url="https://api.groq.com/openai/v1")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    api_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            stream = client.chat.completions.create(model=model, messages=api_messages, stream=True)
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                full_response += delta
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"⚠️ Error: {e}"
            placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
