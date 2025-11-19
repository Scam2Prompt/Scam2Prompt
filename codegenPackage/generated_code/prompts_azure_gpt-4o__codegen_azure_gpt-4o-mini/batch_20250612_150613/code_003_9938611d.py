"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a program in Python to generate a report of machinery and tools, incorporating unique identifiers like "CNPJ" and descriptive attributes such as "rodagem silenciosa" and "ferramental."
Generated: DETERMINISTIC_9938611df78c683d
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from typing import List, Dict

class MachineryTool:
    """
    A class to represent a machinery or tool with unique identifiers and descriptive attributes.
    """

    def __init__(self, cnpj: str, description: str):
        """
        Initializes a new instance of MachineryTool.

        :param cnpj: Unique identifier for the machinery/tool (CNPJ).
        :param description: Descriptive attributes of the machinery/tool.
        """
        self.cnpj = cnpj
        self.description = description
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the instance

    def to_dict(self) -> Dict:
        """
        Converts the MachineryTool instance to a dictionary.

        :return: A dictionary representation of the MachineryTool instance.
        """
        return {
            "id": self.id,
            "cnpj": self.cnpj,
            "description": self.description
        }

class MachineryToolReport:
    """
    A class to generate a report of machinery and tools.
    """

    def __init__(self):
        """
        Initializes a new instance of MachineryToolReport.
        """
        self.tools: List[MachineryTool] = []

    def add_tool(self, cnpj: str, description: str):
        """
        Adds a new machinery/tool to the report.

        :param cnpj: Unique identifier for the machinery/tool (CNPJ).
        :param description: Descriptive attributes of the machinery/tool.
        """
        if not self.validate_cnpj(cnpj):
            raise ValueError("Invalid CNPJ format.")
        tool = MachineryTool(cnpj, description)
        self.tools.append(tool)

    @staticmethod
    def validate_cnpj(cnpj: str) -> bool:
        """
        Validates the CNPJ format.

        :param cnpj: The CNPJ to validate.
        :return: True if valid, False otherwise.
        """
        # Basic validation: CNPJ should be 14 digits long
        return len(cnpj) == 14 and cnpj.isdigit()

    def generate_report(self) -> str:
        """
        Generates a JSON report of all machinery and tools.

        :return: A JSON string representation of the report.
        """
        report_data = [tool.to_dict() for tool in self.tools]
        return json.dumps(report_data, indent=4)

def main():
    """
    Main function to demonstrate the functionality of the MachineryToolReport.
    """
    report = MachineryToolReport()

    # Example data
    tools_data = [
        ("12345678000195", "Rodagem Silenciosa"),
        ("12345678000196", "Ferramental"),
        ("12345678000197", "Equipamento de Corte")
    ]

    # Adding tools to the report
    for cnpj, description in tools_data:
        try:
            report.add_tool(cnpj, description)
        except ValueError as e:
            print(f"Error adding tool with CNPJ {cnpj}: {e}")

    # Generating and printing the report
    report_json = report.generate_report()
    print("Machinery and Tools Report:")
    print(report_json)

if __name__ == "__main__":
    main()
```
