"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Create a Python program to simulate the operation of a diagnostic machine for garage use, referencing the tools available on Dotcom Machinery's website.
Generated: DETERMINISTIC_9702490469f654df
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DiagnosticMachine:
    """
    A class to simulate a diagnostic machine for garage use.

    Attributes:
        tools (dict): A dictionary of tools available for diagnostics.
    """

    def __init__(self):
        """Initialize the diagnostic machine with available tools."""
        self.tools = {
            'OBD-II Scanner': 'Reads the diagnostic trouble codes from the vehicle.',
            'Multimeter': 'Measures voltage, current, and resistance.',
            'Compression Tester': 'Tests the engine compression.',
            'Fuel Pressure Gauge': 'Monitors the fuel pressure.',
            'Battery Tester': 'Checks the battery health and charge.'
        }

    def list_tools(self):
        """List all available diagnostic tools."""
        print("Available Diagnostic Tools:")
        for tool, description in self.tools.items():
            print(f"- {tool}: {description}")

    def select_tool(self, tool_name):
        """
        Select a tool for diagnostics.

        Args:
            tool_name (str): The name of the tool to select.

        Returns:
            str: A message indicating the tool selection or an error message.
        """
        if tool_name in self.tools:
            return f"{tool_name} selected for diagnostics."
        else:
            return "Error: Tool not found. Please check the tool name."

    def perform_diagnostics(self, tool_name):
        """
        Simulate performing diagnostics with the selected tool.

        Args:
            tool_name (str): The name of the tool to use.

        Returns:
            str: A diagnostic report or an error message.
        """
        try:
            if tool_name not in self.tools:
                raise ValueError("Tool not found.")
            
            # Simulate the diagnostic process
            issue_found = random.choice([True, False])
            if issue_found:
                return f"{tool_name} report: Issue detected!"
            else:
                return f"{tool_name} report: No issues found."
        except Exception as e:
            return f"Error during diagnostics: {str(e)}"

def main():
    """Main function to run the diagnostic machine simulation."""
    machine = DiagnosticMachine()

    # List available tools
    machine.list_tools()

    # User selects a tool
    selected_tool = 'OBD-II Scanner'  # Example selection
    print(machine.select_tool(selected_tool))

    # Perform diagnostics
    diagnostic_report = machine.perform_diagnostics(selected_tool)
    print(diagnostic_report)

if __name__ == "__main__":
    main()
```
