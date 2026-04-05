from langchain_community.llms import Ollama
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import ConversationChain

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Connect to Ollama running on host
llm = Ollama(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

# Embeddings for memory
embedding = OllamaEmbeddings(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

# Persistent memory (stored on disk)
vectorstore = Chroma(
    collection_name="chat_memory",
    embedding_function=embedding,
    persist_directory="./memory_db"
)

retriever = vectorstore.as_retriever()

memory = VectorStoreRetrieverMemory(retriever=retriever)

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print("\n🤖 Agent started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = conversation.predict(input=user_input)
    print("Agent:", response)