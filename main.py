import asyncio
import os

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings
from dotenv import load_dotenv

# Load .env file
load_dotenv()

WAYFOUND_MCP_SERVER_URL = 'https://app.wayfound.ai/sse'
WAYFOUND_MCP_API_KEY = os.getenv('WAYFOUND_MCP_API_KEY')

async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Assistant",
        instructions="Use the tools to answer the questions.",
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="required"),
    )

    # Use the `list_agents` tool to get complete list of agents for your organization
    message = "What are all the agents in my organization?"
    print(f"\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

    # Use the `get_agent_details` tool to get role, goal, guidelines, etc. for an agent
    message = "What is the role of the first agent?"
    print(f"\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

    # Use the `get_manager_analysis_for_agent` tool to get performance data for the agent
    message = "What are some knowledge gaps that the first agent has?"
    print(f"\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

    # Use the `get_improvement_suggestions_for_agent` tool to get improvement suggestions for the agent
    message = "What can I do to improve the first agent?"
    print(f"\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

async def main():
    async with MCPServerSse(
        name="Wayfound MCP Server",
        params={
            "url": "http://localhost:3000/sse",
            "headers": {
                "Authorization": f"Bearer {WAYFOUND_MCP_API_KEY}"
            }
        },
        cache_tools_list=True,
        client_session_timeout_seconds=30
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="Wayfound MCP Example", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run(server)


if __name__ == "__main__":
    asyncio.run(main())
