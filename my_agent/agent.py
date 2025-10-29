from datetime import datetime
from strands import Agent, tool
from strands_tools import use_aws, environment
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

@tool
def get_todays_date() -> str:
    """Get today's date"""
    return datetime.now().strftime("%Y-%m-%d")

# Try to connect to MCP server, but handle if it's not available
try:
    streamable_http_mcp_client = MCPClient(lambda: streamablehttp_client("http://localhost:8080/mcp"))
    streamable_http_mcp_client.start()
    mcp_tools = streamable_http_mcp_client.list_tools_sync()
    all_tools = [get_todays_date, use_aws, environment] + mcp_tools
except Exception as e:
    print(f"MCP server not available: {e}")
    all_tools = [get_todays_date, use_aws, environment]

agent = Agent(
    name="MyAgent",
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    system_prompt="Greet the user usign the format from greet_user. Environment variables are AWS_REGION and CLUSTER_NAME. All clusters are EKS Auto Mode and doesn't have any node groups. Just answer with no follow up questions",
    tools=all_tools
)

if __name__ == "__main__":
    agent("Hi my name is Alice, tell me about the EKS cluster, include networking, security, compute, addons, and How many hours ago was this cluster created?")
    print("\n")

