from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.llms import Ollama
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import ConversationChain
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# ----------- SETUP AGENT (same as before) -----------

llm = Ollama(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

embedding = OllamaEmbeddings(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

vectorstore = Chroma(
    collection_name="chat_memory",
    embedding_function=embedding,
    persist_directory="./memory_db"
)

retriever = vectorstore.as_retriever()

memory = VectorStoreRetrieverMemory(retriever=retriever)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# ----------- FASTAPI APP -----------
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Agent is running !!!"}

@app.post("/chat")
def chat(user_input: UserInput):
    response = conversation.predict(input=user_input.message)
    return {
        "user": user_input.message,
        "response": response
    }

