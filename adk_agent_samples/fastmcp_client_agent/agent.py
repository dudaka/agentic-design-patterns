# Book p. 158: an ADK agent that consumes the FastMCP server as an MCP client.
# Ported to google-adk 2.7.1: the book's HttpServerParameters does not exist; the HTTP
# transport is StreamableHTTPConnectionParams, and FastMCP serves it at the /mcp path.
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StreamableHTTPConnectionParams

# Make sure fastmcp_server.py (one directory up) is running on this port.
FASTMCP_SERVER_URL = "http://127.0.0.1:8000/mcp"

root_agent = LlmAgent(
    model="gemini-flash-latest",
    name="fastmcp_greeter_agent",
    instruction='You are a friendly assistant that can greet people by their name. Use the "greet" tool.',
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(url=FASTMCP_SERVER_URL),
            # Optional: Filter which tools from the MCP server are exposed.
            # For this example, we're expecting only 'greet'
            tool_filter=["greet"],
        )
    ],
)
