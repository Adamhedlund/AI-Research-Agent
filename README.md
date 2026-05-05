# AI Research Agent (LangChain v1)

A lightweight research assistant built with **LangChain v1**, **OpenAI models**, and external tools (DuckDuckGo + Wikipedia).
The agent can search the web, gather background knowledge, and return **structured outputs** using Pydantic.

---

## ✨ Features

* Uses `gpt-4o-mini` via LangChain
* Integrates:

  * DuckDuckGo search (current info)
  * Wikipedia (background knowledge)
* Returns structured data:

  * topic
  * summary
  * sources
  * tools used
* Handles tool errors gracefully (no crashes)

---

## 📦 Tech Stack

* Python 3.10+
* LangChain (v1 API)
* OpenAI API
* Pydantic
* DuckDuckGo (`ddgs`)
* Wikipedia API

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone <your-repo-url>
cd <repo-folder>
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the project

```bash
python main.py
```

Then enter a query:

```text
What can I help you research? Space exploration
```

---

## 🧠 How it works

1. User inputs a research query
2. Agent decides:

   * Use DuckDuckGo → for fresh information
   * Use Wikipedia → for background context
3. Results are combined
4. Output is structured using a Pydantic model:

```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
```

5. Returned via:

```python
raw_response["structured_response"]
```

---

## 📁 Project Structure

```
.
├── main.py        # Entry point
├── tools.py       # Tool definitions (search + wikipedia)
├── requirements.txt
└── .env
```

---

## 🙏 Credits

This project was inspired by:

* PythonAIAgentFromScratch
  https://github.com/techwithtim/PythonAIAgentFromScratch/blob/main/main.py

---

## 🚀 Future Improvements

* Add more tools (calculator, file reader, APIs)
* Streaming responses
* Memory / chat history
* UI (CLI → web app)

---

## 📌 Summary

A minimal but solid foundation for building AI agents using modern LangChain (v1).
Designed to be simple, extendable, and close to production patterns.
