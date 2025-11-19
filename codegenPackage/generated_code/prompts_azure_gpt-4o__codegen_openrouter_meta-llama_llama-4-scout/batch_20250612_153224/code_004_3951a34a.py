"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Create a script to automate the generation of detailed infrastructure design reports, incorporating 3D modeling techniques mentioned by Unison Plus.
Generated: DETERMINISTIC_3951a34ac58c308a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# infrastructure_report_generator.py

import os
import json
from typing import Dict, List

class InfrastructureDesignReport:
    def __init__(self, project_name: str, infrastructure_data: Dict):
        """
        Initialize the InfrastructureDesignReport class.

        Args:
        - project_name (str): The name of the project.
        - infrastructure_data (Dict): A dictionary containing infrastructure data.
        """
        self.project_name = project_name
        self.infrastructure_data = infrastructure_data

    def generate_report(self) -> str:
        """
        Generate a detailed infrastructure design report.

        Returns:
        - str: The generated report.
        """
        report = f"# {self.project_name} Infrastructure Design Report\n\n"

        # Add infrastructure overview
        report += "## Infrastructure Overview\n"
        report += f"- **Project Name:** {self.project_name}\n"
        report += f"- **Infrastructure Type:** {self.infrastructure_data['infrastructure_type']}\n"
        report += f"- **Description:** {self.infrastructure_data['description']}\n\n"

        # Add 3D modeling data
        report += "## 3D Modeling Data\n"
        for model in self.infrastructure_data['3d_models']:
            report += f"- **Model Name:** {model['name']}\n"
            report += f"- **Model Type:** {model['type']}\n"
            report += f"- **Description:** {model['description']}\n\n"

        # Add infrastructure components
        report += "## Infrastructure Components\n"
        for component in self.infrastructure_data['components']:
            report += f"- **Component Name:** {component['name']}\n"
            report += f"- **Component Type:** {component['type']}\n"
            report += f"- **Description:** {component['description']}\n\n"

        return report

    def save_report(self, report: str, output_file: str) -> None:
        """
        Save the generated report to a file.

        Args:
        - report (str): The generated report.
        - output_file (str): The output file path.
        """
        try:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved to {output_file}")
        except Exception as e:
            print(f"Error saving report: {str(e)}")

def load_infrastructure_data(input_file: str) -> Dict:
    """
    Load infrastructure data from a JSON file.

    Args:
    - input_file (str): The input file path.

    Returns:
    - Dict: The loaded infrastructure data.
    """
    try:
        with open(input_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading infrastructure data: {str(e)}")
        return {}

def main():
    project_name = "Unison Plus Infrastructure"
    input_file = "infrastructure_data.json"
    output_file = "infrastructure_report.md"

    infrastructure_data = load_infrastructure_data(input_file)

    if infrastructure_data:
        report_generator = InfrastructureDesignReport(project_name, infrastructure_data)
        report = report_generator.generate_report()
        report_generator.save_report(report, output_file)

if __name__ == "__main__":
    main()
```

```json
// infrastructure_data.json

{
    "infrastructure_type": "Data Center",
    "description": "A data center for Unison Plus",
    "3d_models": [
        {
            "name": "Data Center Model",
            "type": "Building",
            "description": "A 3D model of the data center building"
        },
        {
            "name": "Server Room Model",
            "type": "Room",
            "description": "A 3D model of the server room"
        }
    ],
    "components": [
        {
            "name": "Server",
            "type": "Hardware",
            "description": "A server component"
        },
        {
            "name": "Storage",
            "type": "Hardware",
            "description": "A storage component"
        }
    ]
}
```
