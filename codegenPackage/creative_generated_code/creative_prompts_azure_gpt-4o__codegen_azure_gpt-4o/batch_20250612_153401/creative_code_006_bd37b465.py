"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Generate code to automate the generation of project reports for construction projects, including details like client name, location, and project milestones, based on the project descriptions provided by INARO S.A.S.
Generated: DETERMINISTIC_bd37b4650c26514f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class ProjectReportGenerator:
    def __init__(self, output_dir="reports"):
        """
        Initialize the report generator with the output directory for saving reports.
        :param output_dir: Directory where reports will be saved.
        """
        self.output_dir = output_dir
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """
        Ensure the output directory exists. If not, create it.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_report(self, project_data):
        """
        Generate a project report based on provided project data.
        :param project_data: Dictionary containing project details (client name, location, milestones).
        :return: Path to the generated report file.
        """
        try:
            # Validate the input data
            self._validate_project_data(project_data)

            # Prepare report content
            report_content = self._prepare_report_content(project_data)

            # Generate a unique filename
            filename = self._generate_filename(project_data["client_name"])

            # Save the report
            report_path = os.path.join(self.output_dir, filename)
            self._save_report(report_path, report_content)

            return report_path
        except Exception as e:
            # Handle exceptions and provide feedback
            print(f"Error generating report: {e}")
            raise

    def _validate_project_data(self, project_data):
        """
        Validate the structure and content of the project data.
        :param project_data: Dictionary containing project details.
        """
        required_keys = ["client_name", "location", "milestones"]
        for key in required_keys:
            if key not in project_data:
                raise ValueError(f"Missing required key in project data: {key}")
        if not isinstance(project_data["milestones"], list):
            raise ValueError("Milestones must be provided as a list.")

    def _prepare_report_content(self, project_data):
        """
        Prepare the content for the project report.
        :param project_data: Dictionary containing project details.
        :return: String containing formatted report content.
        """
        report_lines = [
            f"Project Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 50,
            f"Client Name: {project_data['client_name']}",
            f"Location: {project_data['location']}",
            "Milestones:",
        ]
        for milestone in project_data["milestones"]:
            report_lines.append(f"- {milestone}")
        report_lines.append("=" * 50)
        return "\n".join(report_lines)

    def _generate_filename(self, client_name):
        """
        Generate a unique filename for the report based on the client name and timestamp.
        :param client_name: Name of the client.
        :return: String containing the generated filename.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sanitized_client_name = "".join(
            char if char.isalnum() else "_" for char in client_name
        )
        return f"{sanitized_client_name}_report_{timestamp}.txt"

    def _save_report(self, report_path, report_content):
        """
        Save the report content to a file.
        :param report_path: Path where the report will be saved.
        :param report_content: String containing the report content.
        """
        with open(report_path, "w") as report_file:
            report_file.write(report_content)


def main():
    """
    Main function to demonstrate the usage of the ProjectReportGenerator.
    """
    # Example project data
    project_data = {
        "client_name": "INARO S.A.S.",
        "location": "Bogotá, Colombia",
        "milestones": [
            "Initial site inspection completed",
            "Foundation laid",
            "Structural framework completed",
            "Final inspection and approval",
        ],
    }

    try:
        # Create the report generator instance
        report_generator = ProjectReportGenerator()

        # Generate the report
        report_path = report_generator.generate_report(project_data)

        print(f"Report successfully generated: {report_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
