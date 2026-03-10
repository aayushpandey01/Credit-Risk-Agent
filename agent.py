import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
from tools.pd_tool import predict_pd
from tools.ews_tool import early_warning_tool
from tools.drift_tool import drift_tool


load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama2-13b-4096"
)


@tool
def predict_pd_tool(customer_id: int) -> str:
    """Calculate Probability of Default for a given customer ID"""
    return str(predict_pd(customer_id))


@tool
def early_warning_tool_wrapper(customer_id: int) -> str:
    """Check early warning signals for a given customer ID"""
    return str(early_warning_tool(customer_id))



def drift_check_tool() -> str:
    """Calculate portfolio drift using PSI"""
    return f"Portfolio PSI: {drift_tool()}"

from langchain_core.tools import Tool
drift_check_tool = Tool(
    name="drift_check_tool",
    func=drift_check_tool,
    description="Calculate portfolio drift using PSI."
)


tools = [
    predict_pd_tool,
    early_warning_tool_wrapper,
    drift_check_tool,
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


def run_agent(query: str):
    response = agent.invoke({"input": query})
    return response