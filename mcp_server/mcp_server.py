from mcp.server.fastmcp import FastMCP

mcp = FastMCP("echoserver")

@mcp.tool(description="Returns the message on how to greet the user by name")
def greet_user(name: str) -> str:
    return f"Hello, {name}! Nice to meet you."

@mcp.tool(description="Test tool that returns a secret word")
def secret_phrase() -> str:
    return "The secret word is 'eureka'"

if __name__ == "__main__":
    mcp.settings.port = 8080
    mcp.run(transport='streamable-http')
