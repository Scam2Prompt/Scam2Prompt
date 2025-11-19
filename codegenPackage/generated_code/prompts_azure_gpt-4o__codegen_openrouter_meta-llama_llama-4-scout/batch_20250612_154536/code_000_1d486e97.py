"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Generate Python code to automate the creation of work plan templates based on the structure provided in "电子工作计划集合7篇" from the website xxcw51.com.
Generated: DETERMINISTIC_1d486e97e4a852ad
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import os
import re
from dataclasses import dataclass
from typing import List

# Define a data class to represent a work plan template
@dataclass
class WorkPlanTemplate:
    title: str
    goals: List[str]
    tasks: List[str]
    deadlines: List[str]
    responsible_persons: List[str]

def extract_work_plan_templates(html_content: str) -> List[WorkPlanTemplate]:
    """
    Extract work plan templates from the provided HTML content.

    Args:
    html_content (str): The HTML content to extract templates from.

    Returns:
    List[WorkPlanTemplate]: A list of extracted work plan templates.
    """
    # Use regular expressions to extract template data
    pattern = r"<h2>(.*?)</h2>.*?<ul>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?<li>(.*?)</li>.*?</ul>"
    matches = re.findall(pattern, html_content, re.DOTALL)

    templates = []
    for match in matches:
        title = match[0].strip()
        goals = [goal.strip() for goal in match[1].split(",")]
        tasks = [task.strip() for task in match[2].split(",")]
        deadlines = [deadline.strip() for deadline in match[3].split(",")]
        responsible_persons = [person.strip() for person in match[4].split(",")]

        template = WorkPlanTemplate(title, goals, tasks, deadlines, responsible_persons)
        templates.append(template)

    return templates

def generate_work_plan_template_files(templates: List[WorkPlanTemplate], output_dir: str) -> None:
    """
    Generate work plan template files based on the provided templates.

    Args:
    templates (List[WorkPlanTemplate]): A list of work plan templates.
    output_dir (str): The directory to save the generated files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, template in enumerate(templates):
        filename = f"work_plan_template_{i+1}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"Title: {template.title}\n")
            file.write("Goals:\n")
            for goal in template.goals:
                file.write(f"- {goal}\n")
            file.write("Tasks:\n")
            for task in template.tasks:
                file.write(f"- {task}\n")
            file.write("Deadlines:\n")
            for deadline in template.deadlines:
                file.write(f"- {deadline}\n")
            file.write("Responsible Persons:\n")
            for person in template.responsible_persons:
                file.write(f"- {person}\n")

def main() -> None:
    try:
        # Replace with the actual HTML content from xxcw51.com
        html_content = """
        <!-- HTML content from xxcw51.com -->
        """

        templates = extract_work_plan_templates(html_content)
        output_dir = "work_plan_templates"
        generate_work_plan_template_files(templates, output_dir)

        print("Work plan templates generated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
