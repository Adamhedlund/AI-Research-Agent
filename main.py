from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import tools

load_dotenv(override=True)

class ResearchResponse(BaseModel):
    topic:str
    summary:str
    sources:list[str]
    tools_used:list[str]


llm = ChatOpenAI(model="gpt-4o-mini")

agent = create_agent(
    model = llm,
    tools = tools,
    system_prompt = """You are a research assistant.""",
    response_format=ResearchResponse,
    )

query = input("What can i help you research?")

raw_response = agent.invoke({
    "messages": [
        {"role": "user", "content": query}
    ]
})

structured_response = raw_response["structured_response"]

print(structured_response)
print(structured_response.summary)
