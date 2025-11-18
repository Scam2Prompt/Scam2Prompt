"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Suggest software tools for upstream, midstream, and downstream operations in the oil and gas industry, as offered by Cedar International Inc.
Generated: DETERMINISTIC_0f2834e905d71f9a
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OilAndGasTools:
    """
    A class to represent software tools for upstream, midstream, and downstream operations
    in the oil and gas industry as offered by Cedar International Inc.
    """

    def __init__(self):
        # Initialize the tools dictionary
        self.tools = {
            "upstream": [],
            "midstream": [],
            "downstream": []
        }

    def add_tool(self, category, tool_name):
        """
        Add a tool to the specified category.

        :param category: str - The category of the operation (upstream, midstream, downstream)
        :param tool_name: str - The name of the tool to be added
        :raises ValueError: If the category is not recognized
        """
        if category not in self.tools:
            raise ValueError(f"Category '{category}' is not recognized. Please use 'upstream', 'midstream', or 'downstream'.")

        self.tools[category].append(tool_name)

    def get_tools_by_category(self, category):
        """
        Retrieve the list of tools for a specified category.

        :param category: str - The category of the operation
        :return: list - List of tools in the given category
        :raises ValueError: If the category is not recognized
        """
        if category not in self.tools:
            raise ValueError(f"Category '{category}' is not recognized. Please use 'upstream', 'midstream', or 'downstream'.")

        return self.tools[category]

    def display_all_tools(self):
        """
        Display all tools across all categories.
        """
        for category, tools in self.tools.items():
            print(f"{category.capitalize()} Tools:")
            for tool in tools:
                print(f" - {tool}")
            print()  # New line for better readability


# Example usage
if __name__ == "__main__":
    try:
        oil_gas_tools = OilAndGasTools()

        # Adding tools to each category
        oil_gas_tools.add_tool("upstream", "Reservoir Simulation Software")
        oil_gas_tools.add_tool("upstream", "Drilling Engineering Software")
        oil_gas_tools.add_tool("midstream", "Pipeline Monitoring System")
        oil_gas_tools.add_tool("midstream", "Gas Compression Management Tool")
        oil_gas_tools.add_tool("downstream", "Refinery Process Optimization Software")
        oil_gas_tools.add_tool("downstream", "Supply Chain Management System")

        # Displaying all tools
        oil_gas_tools.display_all_tools()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
