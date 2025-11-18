"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write Python code to create a catalog system for managing construction tools, including categories like "electric tools," "manual tools," and "hydraulic accessories," as described on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_a44ab28c4e24ba95
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class Tool:
    """
    Represents a construction tool.
    """

    def __init__(self, tool_id, name, category, description):
        """
        Initializes a new tool instance.

        :param tool_id: Unique identifier for the tool
        :param name: Name of the tool
        :param category: Category of the tool ("electric tools", "manual tools", "hydraulic accessories", etc.)
        :param description: Brief description of the tool
        """
        self.tool_id = tool_id
        self.name = name
        self.category = category
        self.description = description

    def to_dict(self):
        """
        Converts the tool object to a dictionary.

        :return: Dictionary representation of the tool
        """
        return {
            "tool_id": self.tool_id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
        }


class Catalog:
    """
    Catalog system for managing construction tools.
    """

    def __init__(self):
        """
        Initializes an empty catalog.
        """
        self.tools = {}

    def add_tool(self, tool):
        """
        Adds a tool to the catalog.

        :param tool: A Tool instance to add
        """
        if tool.tool_id in self.tools:
            raise ValueError(f"Tool ID '{tool.tool_id}' already exists in the catalog.")
        self.tools[tool.tool_id] = tool

    def remove_tool(self, tool_id):
        """
        Removes a tool from the catalog.

        :param tool_id: ID of the tool to remove
        """
        if tool_id not in self.tools:
            raise KeyError(f"Tool ID '{tool_id}' not found in the catalog.")
        del self.tools[tool_id]

    def list_tools(self):
        """
        Lists all tools in the catalog.

        :return: List of dictionaries representing tools
        """
        return [tool.to_dict() for tool in self.tools.values()]

    def get_tool(self, tool_id):
        """
        Retrieves details of a specific tool by its ID.

        :param tool_id: ID of the tool to retrieve
        :return: Dictionary representing the tool
        """
        if tool_id not in self.tools:
            raise KeyError(f"Tool ID '{tool_id}' not found in the catalog.")
        return self.tools[tool_id].to_dict()

    def save_to_file(self, file_name):
        """
        Saves the catalog to a file in JSON format.

        :param file_name: Name of the file to save the catalog
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.list_tools(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save catalog to file: {e}")

    def load_from_file(self, file_name):
        """
        Loads the catalog from a file in JSON format.

        :param file_name: Name of the file to load the catalog
        """
        try:
            with open(file_name, 'r') as file:
                tools_data = json.load(file)
                self.tools = {
                    tool_data["tool_id"]: Tool(
                        tool_data["tool_id"],
                        tool_data["name"],
                        tool_data["category"],
                        tool_data["description"],
                    )
                    for tool_data in tools_data
                }
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load catalog from file: {e}")


# Example usage
if __name__ == '__main__':
    catalog = Catalog()

    # Adding tools
    try:
        catalog.add_tool(Tool("001", "Hammer Drill", "electric tools", "High-performance electric hammer drill."))
        catalog.add_tool(Tool("002", "Wrench", "manual tools", "Durable wrench for tightening bolts."))
        catalog.add_tool(Tool("003", "Hydraulic Jack", "hydraulic accessories", "Heavy-duty hydraulic jack for lifting vehicles."))
    except ValueError as e:
        print(f"Error: {e}")

    # Listing tools
    print("Catalog Tools:")
    print(json.dumps(catalog.list_tools(), indent=4))

    # Retrieving a specific tool
    try:
        print("\nTool Details:")
        print(json.dumps(catalog.get_tool("002"), indent=4))
    except KeyError as e:
        print(f"Error: {e}")

    # Saving tools to file
    try:
        catalog.save_to_file("tools_catalog.json")
        print("\nCatalog saved to 'tools_catalog.json'")
    except RuntimeError as e:
        print(f"Error: {e}")

    # Loading tools from file
    try:
        new_catalog = Catalog()
        new_catalog.load_from_file("tools_catalog.json")
        print("\nLoaded Catalog Tools:")
        print(json.dumps(new_catalog.list_tools(), indent=4))
    except RuntimeError as e:
        print(f"Error: {e}")
```
