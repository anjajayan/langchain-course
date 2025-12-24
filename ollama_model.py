
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Ollama LLM
llm = OllamaLLM(model="llama3") # Or "llama3.1", "llama2"

# Create a prompt template
prompt = ChatPromptTemplate.from_template("Tell me a short story about {topic}")
chain = prompt | llm

# Invoke the chain
response = chain.invoke({"topic": "a mischievous cat"})
print(response)
