# Book p. 157: a minimal MCP server built with FastMCP, exposing one tool over HTTP.
# Run it in its own terminal:  uv run python adk_agent_samples/fastmcp_server.py
from fastmcp import FastMCP

# Initialize the FastMCP server.
mcp_server = FastMCP()


# The `@mcp_server.tool` decorator registers this Python function as an MCP tool.
# The docstring becomes the tool's description for the LLM.
@mcp_server.tool
def greet(name: str) -> str:
    """
    Generates a personalized greeting.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Nice to meet you."


if __name__ == "__main__":
    # Streamable HTTP; the MCP endpoint is served at http://127.0.0.1:8000/mcp
    mcp_server.run(transport="http", host="127.0.0.1", port=8000)
