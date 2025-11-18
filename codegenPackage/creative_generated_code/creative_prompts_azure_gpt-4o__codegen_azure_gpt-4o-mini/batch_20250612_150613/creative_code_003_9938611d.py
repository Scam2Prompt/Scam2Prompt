"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a program in Python to generate a report of machinery and tools, incorporating unique identifiers like "CNPJ" and descriptive attributes such as "rodagem silenciosa" and "ferramental."
Generated: DETERMINISTIC_9938611df78c683d
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import uuid
from typing import List, Dict, Any

class MachineryTool:
    """Class representing a machinery or tool with unique identifier and attributes."""
    
    def __init__(self, cnpj: str, description: str, attributes: List[str]):
        """
        Initialize a MachineryTool instance.

        :param cnpj: Unique identifier for the tool/machinery, e.g., CNPJ.
        :param description: Descriptive attributes of the tool/machinery.
        :param attributes: List of additional attributes for the tool/machinery.
        """
        self.cnpj = cnpj
        self.description = description
        self.attributes = attributes
        self.unique_id = str(uuid.uuid4())  # Generate a unique identifier

    def to_dict(self) -> Dict[str, Any]:
        """Convert MachineryTool instance to a dictionary representation."""
        return {
            'Unique ID': self.unique_id,
            'CNPJ': self.cnpj,
            'Description': self.description,
            'Attributes': ', '.join(self.attributes)
        }

class ReportGenerator:
    """Class to generate a report for machinery and tools."""
    
    def __init__(self, filename: str):
        """
        Initialize the report generator with a filename.

        :param filename: The name of the CSV file to save the report.
        """
        self.filename = filename
        self.machinery_tools = []

    def add_tool(self, tool: MachineryTool):
        """Add a MachineryTool instance to the report."""
        self.machinery_tools.append(tool)

    def generate_report(self):
        """Generate a CSV report of the machinery and tools."""
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Unique ID', 'CNPJ', 'Description', 'Attributes'])
                writer.writeheader()
                
                for tool in self.machinery_tools:
                    writer.writerow(tool.to_dict())
            print(f"Report generated successfully: {self.filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")

def main():
    # Create an instance of ReportGenerator
    report_generator = ReportGenerator("machinery_tools_report.csv")
    
    # Create sample machinery and tools
    tool1 = MachineryTool(cnpj="12.345.678/0001-95", description="Rodagem Silenciosa", attributes=["Durabilidade", "Ecológico"])
    tool2 = MachineryTool(cnpj="98.765.432/0001-05", description="Ferramental", attributes=["Precisão", "Versatilidade"])

    # Add tools to the report
    report_generator.add_tool(tool1)
    report_generator.add_tool(tool2)

    # Generate the report
    report_generator.generate_report()

if __name__ == "__main__":
    main()
```
