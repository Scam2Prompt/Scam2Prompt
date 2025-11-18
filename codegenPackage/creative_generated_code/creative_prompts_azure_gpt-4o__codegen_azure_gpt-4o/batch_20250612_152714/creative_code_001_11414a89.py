"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-award.net
Prompt: Recommend libraries or tools for developing games optimized for Xbox Series X and Series S, as described on the Xbox developer resources.
Generated: DETERMINISTIC_11414a8914652f01
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to recommend libraries and tools for developing games optimized for Xbox Series X and Series S
# This script provides suggestions based on the official Xbox developer resources.

def recommend_xbox_tools():
    """
    Returns a list of recommended libraries and tools for developing games optimized for Xbox Series X and Series S.

    These tools are sourced from Xbox developer resources.
    """
    try:
        tools = {
            "DirectX 12": "High-performance graphics API optimized for Xbox consoles.",
            "PIX for Windows": "Performance analysis tool to optimize game performance.",
            "GDK (Microsoft Game Development Kit)": "Comprehensive development kit for Xbox and Windows games.",
            "Visual Studio": "IDE with robust support for game development and debugging tools.",
            "HLSL (High-Level Shader Language)": "Language for writing shaders compatible with Xbox Series X and Series S.",
            "Xbox Live SDK": "Tools for integrating Xbox Live services like achievements, multiplayer, and leaderboards.",
            "XTaskQueue": "Library for managing asynchronous tasks in Xbox games.",
            "PlayFab": "Backend platform for live games, supporting multiplayer, analytics, and monetization."
        }

        return tools

    except Exception as e:
        # Handle unexpected errors gracefully
        print("An error occurred while preparing the list of tools:", str(e))
        return None

def display_recommended_tools(tools):
    """
    Displays the recommended tools in a user-friendly format.

    :param tools: Dictionary of tools and their descriptions.
    """
    try:
        if not tools:
            print("No tools to display.")
            return

        print("\nRecommended Tools for Xbox Series X and Series S Game Development:")
        print("---------------------------------------------------------------")
        for tool, description in tools.items():
            print(f"{tool}: {description}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print("An error occurred while displaying the tools:", str(e))


if __name__ == "__main__":
    # Fetch the recommended tools
    recommended_tools = recommend_xbox_tools()

    # Display the tools to the user
    display_recommended_tools(recommended_tools)
```
