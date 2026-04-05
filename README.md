
>>>>  Local AI Agent with Memory (Docker + Ollama)  <<<<

Overview
This project is a **local AI agent** that runs entirely on your machine using:

* 🐳 Docker (for containerization)
* 🤖 Ollama (local LLM)
* 🧠 LangChain (agent + memory)
* 💾 ChromaDB (persistent memory)

The agent can:
* Maintain conversation context
* Store long-term memory
* Run fully offline (after setup)

--------------------------------------------------------

Architecture:
User → Docker Container (Python Agent) → Ollama (LLM)
↓
ChromaDB (Memory)

--------------------------------------------------------

## ⚙️ Setup Instructions

1. Install Ollama

Download from: https://ollama.com

Start server:

```bash
ollama serve
```

Pull model:

```bash
ollama pull llama3
```

--------------------------------------------------------

 2. Build Docker Image

```bash
docker build -t ai-agent .
```

--------------------------------------------------------

3. Run the Agent

Mac / Windows:

```bash
docker run -it -v $(pwd)/memory_db:/app/memory_db ai-agent
```

Linux:

```bash
docker run -it \
--add-host=host.docker.internal:host-gateway \
-v $(pwd)/memory_db:/app/memory_db \
ai-agent
```

--------------------------------------------------------

🧠 Memory (ChromaDB)

* Stored in: `./memory_db`
* Persists across runs
* Stores embeddings of conversations

---

💬 Example

```
You: my name is Lakshita
You: what is my name?
Agent: Your name is Lakshita
```

---------------------------------------------------------
 Tech Stack

* Python
* LangChain
* Ollama
* ChromaDB
* Docker

