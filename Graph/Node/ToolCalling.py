from Config.llm import llm
from Graph.Tool.Tools import get_vector_response
from Graph.OutputParser.parsers import FinalOutput
from Graph.Prompt.prompts import Agent_prompt
from langchain.agents import Tool, initialize_agent

tools_list = [
    Tool(
        name="VectorSearch",
        func=get_vector_response,
        description="Recherche des informations dans les tweets"
    )
]

AgentToolCall = initialize_agent(
    tools=tools_list,
    llm=llm,
    agent="react",
    verbose=True
)
