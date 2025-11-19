"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: What types of pedagogical tools does Immediate Peak connect users with to improve their investment knowledge?
Generated: DETERMINISTIC_c430bf0410a4a010
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentKnowledgeTools:
    """
    A class to represent various pedagogical tools for improving investment knowledge.
    """

    def __init__(self):
        """
        Initializes the list of pedagogical tools.
        """
        self.tools = []

    def add_tool(self, tool_name: str, tool_description: str):
        """
        Adds a new pedagogical tool to the list.

        Parameters:
        tool_name (str): The name of the pedagogical tool.
        tool_description (str): A brief description of the tool.

        Raises:
        ValueError: If the tool name or description is empty.
        """
        if not tool_name or not tool_description:
            raise ValueError("Tool name and description cannot be empty.")

        self.tools.append({
            'name': tool_name,
            'description': tool_description
        })

    def get_tools(self):
        """
        Returns the list of pedagogical tools.

        Returns:
        list: A list of dictionaries containing tool names and descriptions.
        """
        return self.tools

    def find_tool_by_name(self, tool_name: str):
        """
        Finds a pedagogical tool by name.

        Parameters:
        tool_name (str): The name of the pedagogical tool to find.

        Returns:
        dict: The tool details if found, None otherwise.
        """
        for tool in self.tools:
            if tool['name'].lower() == tool_name.lower():
                return tool
        return None


# Example usage:
if __name__ == "__main__":
    investment_tools = InvestmentKnowledgeTools()
    
    try:
        investment_tools.add_tool("Online Courses", "Comprehensive courses on various investment topics.")
        investment_tools.add_tool("Webinars", "Live sessions with experts discussing current market trends.")
        investment_tools.add_tool("Investment Simulators", "Practice investment strategies in a risk-free environment.")
        
        # Retrieve and print all tools
        all_tools = investment_tools.get_tools()
        print("Available Investment Knowledge Tools:")
        for tool in all_tools:
            print(f"- {tool['name']}: {tool['description']}")
        
        # Find a specific tool
        tool_to_find = "Webinars"
        found_tool = investment_tools.find_tool_by_name(tool_to_find)
        if found_tool:
            print(f"Found Tool: {found_tool['name']} - {found_tool['description']}")
        else:
            print(f"Tool '{tool_to_find}' not found.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
