from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from compute_engine.agent import compute_engine_agent
from big_query.agent import big_query_agent
from cloud_SQL.agent import cloud_sql_agent
from cloud_storage.agent import cloud_storage_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about a Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about a Google Cloud service."
    ),
    tools=[
        AgentTool(agent=compute_engine_agent),
        AgentTool(cloud_storage_agent),
        AgentTool(cloud_sql_agent),
        AgentTool(big_query_agent),
    ],
)