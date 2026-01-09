from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

#Call real search function
from tavily import TavilyClient

# Call Langchain integration of Tavily
from langchain_tavily import TavilySearch


# Call pydantic objects fro creating Response format
from typing import List
from pydantic import BaseModel, Field
# BaseModel is basically a class to be inherited by other classes
#  to create pydantic objects for functions like data parsing
# Field - function  used to add metadata to attributes, for the LLM to understand


tavily = TavilyClient()

# Below is the very basic implementation of a tool
# @tool
# def search(query:str) -> str:
#     """
#     It is a tool that searches over the internet
#     Arguments:
#         query : The query to search for 
#     Returns:
#         The searched result    
#     """

#     print(f"The serach begins for {query}")
#     return "The weather is sunny in Tokyo"

# Tool using Tavily
@tool
def search(query:str) -> str:
    """
    It is a tool that searches over the internet
    Arguments:
        query : The query to search for 
    Returns:
        The searched result    
    """

    print(f"The serach begins for {query}")
    return tavily.search(query = query)


# Creating the format of the output
class Source(BaseModel):
    """Schema for a source used by the agent"""

    url : str = Field(description="The Source for the Agent's answer")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The Agent's answer to the query")
    sources: List[Source] = Field(description = "The source for agent's answer",
                                  default_factory=list)
    # default factory is what you give if there are no output matching the given description
    # we can also mention the type of attributes when it comes to classes


llm = ChatOllama(model = 'llama3.1', temperature=0.8)
# tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools = tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content={"Search for 3 job posting for Data Scientist in Hyderabad"})})
    print(result)


if __name__ == "__main__":
    main()
