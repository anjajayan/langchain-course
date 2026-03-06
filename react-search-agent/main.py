# Load the environment variables
from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

# from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTION
from schemas import AgentResponse

load_dotenv()

tools = [TavilySearch()]
llm = ChatOllama(model="llama3.1", temperature=0.2)
structured_llm = llm.with_structured_output(AgentResponse)
react_prompt = hub.pull("hwchase17/react")

# output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format = PromptTemplate(
    template = REACT_PROMPT_WITH_FORMAT_INSTRUCTION,
    inpit_variables= ['input', 'agent_scratchpad', "tool_names"]
    ).partial(format_instructions = "")
#output_parser.get_format_instructions()


agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_format)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
# chain = agent_executor

# Using LCEL to achieve output parsing
output_extractor = RunnableLambda(lambda x: x['output'])
output_parser = RunnableLambda(lambda x: output_parser.parse())
# chain = agent_executor|output_extractor|output_parser
chain = agent_executor|output_extractor|structured_llm





def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings in the AI engineer field in Hyderabad area"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
