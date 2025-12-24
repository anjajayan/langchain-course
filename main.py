from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()
# This function is used to load the environment variables from .env file of the project

def main():
    print("Hello from langchain-course!")

    # Defining a PromptTemplate

    # Place holder is information
    information = '''
    Bon Appétit, Your Majesty (Korean: 폭군의 셰프 lit: 'Tyrant's Chef') is a 2025 South Korean fantasy romantic television series with elements of time travel and historical fiction. Written by fGRD and directed by Jang Tae-yoo, it stars Im Yoon-ah, Lee Chae-min, Kang Han-na, and Choi Gwi-hwa. The series follows the story of a South Korean French cuisine chef who, upon reaching the pinnacle of her profession, time-slips to the past and encounters the king, who is regarded as both the best gourmet and the worst tyrant. It aired on tvN from August 23, to September 28, 2025, every Saturday and Sunday at 21:10 (KST). It is also available for streaming on Netflix.
    '''

    # Define the template, with information as the input variable that gets plugged in during run time
    # Here we have defined the placeholder in code, but ideally, its for run time
    summary_prompt =  '''Given the information : {information}, 
    generate an output which contains the below items
        1. A short summary
        2. An interesting fact
    '''
    summary_template = PromptTemplate(
        input_variables=["information"],
        template = summary_prompt
    )
    
    # LLM object as a chat interface
    llm = ChatOllama(model = 'llama3', temperature=0)

    # Create a chain 
    chain = summary_template|llm

    # Invoke the chain
    response = chain.invoke(input={'information': information})

    print(response.content)
if __name__ == "__main__":
    main()
