"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Generate code to automate the generation of project reports for construction projects, including details like client name, location, and project milestones, based on the project descriptions provided by INARO S.A.S.
Generated: DETERMINISTIC_bd37b4650c26514f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from dataclasses import dataclass
from typing import List, Optional
import os
from jinja2 import Environment, FileSystemLoader

# Constants
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "reports"
DATE_FORMAT = "%Y-%m-%d"

@dataclass
class Milestone:
    name: str
    description: str
    due_date: str
    status: str

@dataclass
class Project:
    client_name: str
    project_name: str
    location: str
    start_date: str
    end_date: str
    description: str
    milestones: List[Milestone]

class ReportGenerator:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        self._ensure_directories_exist()

    def _ensure_directories_exist(self):
        """Ensure required directories exist."""
        os.makedirs(TEMPLATE_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def load_project_data(self, json_file: str) -> Project:
        """Load project data from JSON file."""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            milestones = [
                Milestone(
                    name=m["name"],
                    description=m["description"],
                    due_date=m["due_date"],
                    status=m["status"]
                ) for m in data.get("milestones", [])
            ]
            
            return Project(
                client_name=data["client_name"],
                project_name=data["project_name"],
                location=data["location"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                description=data["description"],
                milestones=milestones
            )
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Error loading project data: {str(e)}")

    def generate_report(self, project: Project, template_name: str = "report_template.html") -> str:
        """Generate report from project data using specified template."""
        try:
            template = self.env.get_template(template_name)
            report_date = datetime.datetime.now().strftime(DATE_FORMAT)
            
            output = template.render(
                project=project,
                report_date=report_date
            )
            
            filename = f"{OUTPUT_DIR}/{project.client_name}_{project.project_name}_report_{report_date}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(output)
            
            return filename
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")

def main():
    try:
        generator = ReportGenerator()
        
        # Example usage - in production, this would come from command line or config
        project_data_file = "project_data.json"
        project = generator.load_project_data(project_data_file)
        report_file = generator.generate_report(project)
        
        print(f"Report generated successfully: {report_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

```html
<!-- templates/report_template.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Report - {{ project.project_name }}</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        .header { border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
        .project-info { margin-bottom: 30px; }
        .milestones { margin-top: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .status-completed { color: green; }
        .status-pending { color: orange; }
        .status-delayed { color: red; }
    </style>
</head>
<body>
    <div class="header">
        <h1>INARO S.A.S. - Project Report</h1>
        <p>Generated on: {{ report_date }}</p>
    </div>

    <div class="project-info">
        <h2>Project Overview</h2>
        <p><strong>Client:</strong> {{ project.client_name }}</p>
        <p><strong>Project Name:</strong> {{ project.project_name }}</p>
        <p><strong>Location:</strong> {{ project.location }}</p>
        <p><strong>Duration:</strong> {{ project.start_date }} to {{ project.end_date }}</p>
        <p><strong>Description:</strong> {{ project.description }}</p>
    </div>

    <div class="milestones">
        <h2>Project Milestones</h2>
        <table>
            <thead>
                <tr>
                    <th>Milestone</th>
                    <th>Description</th>
                    <th>Due Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for milestone in project.milestones %}
                <tr>
                    <td>{{ milestone.name }}</td>
                    <td>{{ milestone.description }}</td>
                    <td>{{ milestone.due_date }}</td>
                    <td class="status-{{ milestone.status.lower() }}">{{ milestone.status }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

```json
// Example project_data.json
{
    "client_name": "ABC Construction",
    "project_name": "Downtown Office Tower",
    "location": "123 Main St, New York, NY",
    "start_date": "2023-01-15",
    "end_date": "2024-06-30",
    "description": "Construction of a 50-story office tower with retail space and underground parking.",
    "milestones": [
        {
            "name": "Foundation Complete",
            "description": "Completion of all foundation work including pilings and concrete pouring.",
            "due_date": "2023-03-15",
            "status": "Completed"
        },
        {
            "name": "Structural Steel Complete",
            "description": "Erection of all structural steel components.",
            "due_date": "2023-07-30",
            "status": "Pending"
        },
        {
            "name": "Exterior Enclosure",
            "description": "Completion of building envelope including windows and cladding.",
            "due_date": "2023-12-15",
            "status": "Pending"
        }
    ]
}
```
