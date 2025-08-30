# Q‑A Chatbot with LangChain

An end‑to‑end question‑answering chatbot that can run on **OpenAI** or **open‑source models** (e.g., via **Ollama**), with **LangSmith** for tracing/observability.



---

## Features

* 🔁 **Pluggable LLM backends:** OpenAI and open‑source models via **Ollama**; optionally Together/HF Inference.
* 🧪 **LangSmith tracing:** enable run‑tree traces, latency, and token usage with env flags only.
* 🚀 **API or UI:** start as an API (FastAPI‑style) or a simple UI (Streamlit/Gradio) depending on how `app.py` is wired.

* Link: https://q-a-chatbot-with-langchain-ac47dfbmsguszgqjfyjucd.streamlit.app
---

## Quick Start

### 1) Clone & env

```bash
git clone https://github.com/Vatsal-Founder/Q-A-Chatbot-with-LangChain.git
cd Q-A-Chatbot-with-LangChain
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # create if missing
```

### 2) Choose a model backend

Set these in `.env` (or in your hosting platform’s secrets):

```ini
# one of: openai | ollama | together | azure
MODEL_BACKEND=openai

# model names
MODEL_NAME=gpt-4o-mini                # for OpenAI
# MODEL_NAME=llama3.1:8b               # for Ollama (example)

# OpenAI / Azure OpenAI
OPENAI_API_KEY={{your_openai_key}}



# LangSmith (observability)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY={{your_langsmith_key}}
LANGCHAIN_PROJECT=qa-chatbot
```


### 3) Run the app

Pick the command that matches your `app.py` wiring:

** Streamlit UI**

```bash
streamlit run app.py
```

* Open `http://localhost:8501` for a web UI.


### Open‑source via Ollama

1. Install **Ollama** from [https://ollama.com](https://ollama.com) and start it.
2. Pull a model, e.g. `ollama pull llama3.1` (or `mistral`/`phi4` etc.).
3. Set `MODEL_BACKEND=ollama`, `MODEL_NAME=llama3.1`.
4. Ensure `OLLAMA_HOST` is reachable by your app container/host.



---

## LangSmith Tracing

Enable with only environment variables (no code changes if you use LangChain’s standard clients):

```ini
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY={{your_langsmith_key}}
LANGCHAIN_PROJECT=qa-chatbot
```

You’ll see runs, chains, tool calls, and token/latency metrics in your LangSmith workspace. Name your chains/tools to keep traces tidy.

---


## Deployment

Link to access the app: 

## Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md (this file)
```

---

## License

GPL‑3.0 © {{your\_name\_or\_org}}

---

