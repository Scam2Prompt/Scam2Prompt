"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Recommend tools or libraries to build an investment management platform that incorporates transparency and client alignment, as emphasized by Grade World Investment Limited.
Generated: DETERMINISTIC_a602ca28c7becf61
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_management_tools.py

"""
This module provides a list of recommended tools and libraries 
for building an investment management platform that emphasizes 
transparency and client alignment.
"""

class InvestmentManagementTools:
    def __init__(self):
        """Initialize the list of recommended tools."""
        self.tools = []

    def add_tool(self, name, description):
        """
        Adds a tool to the list.

        Args:
            name (str): The name of the tool.
            description (str): A brief description of the tool.

        Raises:
            ValueError: If the tool name is empty or if the tool already exists.
        """
        if not name:
            raise ValueError("Tool name cannot be empty.")
        if any(tool['name'] == name for tool in self.tools):
            raise ValueError(f"Tool '{name}' already exists in the list.")
        
        self.tools.append({"name": name, "description": description})

    def get_tools(self):
        """Returns the list of recommended tools."""
        return self.tools

    def display_tools(self):
        """Prints the list of recommended tools in a user-friendly format."""
        if not self.tools:
            print("No tools have been added yet.")
            return
        
        print("Recommended Investment Management Tools:")
        for tool in self.tools:
            print(f"- {tool['name']}: {tool['description']}")

# Main execution for demonstration purposes
if __name__ == "__main__":
    try:
        investment_tools = InvestmentManagementTools()

        # Adding recommended tools
        investment_tools.add_tool("QuantConnect", "An open-source algorithmic trading platform.")
        investment_tools.add_tool("Portfolio Visualizer", "A web-based tool for portfolio analysis and optimization.")
        investment_tools.add_tool("OpenFigi", "A financial instrument identification service.")
        investment_tools.add_tool("FactSet", "Provides financial data and analytics to investment professionals.")

        # Display the recommended tools
        investment_tools.display_tools()

    except Exception as e:
        print(f"An error occurred: {e}")
```
