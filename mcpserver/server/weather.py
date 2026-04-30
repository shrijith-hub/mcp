from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for any city worldwide.

    Use this when the user asks about weather in a city.
    Example: "weather in Chennai", "temperature in London"
    """
    url = f"https://wttr.in/{city}?format=3"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            return response.text
        except Exception:
            return "Unable to fetch weather data."


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"