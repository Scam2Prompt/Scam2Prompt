"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-dojo.pages.dev
Prompt: Write a script to calculate the total DOJO tokens allocated across all presale projects in the DojoSwap ecosystem.
Generated: DETERMINISTIC_f3be67879801ed19
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Example JSON data representing presale projects (this would typically be fetched from an API or database)
presale_projects_data = '''
[
    {"project_name": "Project Alpha", "allocated_tokens": 150000},
    {"project_name": "Project Beta", "allocated_tokens": 275000},
    {"project_name": "Project Gamma", "allocated_tokens": 320000},
    {"project_name": "Project Delta", "allocated_tokens": 50000}
]
'''

def load_presale_projects(data):
    """
    Loads presale project data from a JSON string.

    :param data: JSON string containing presale project information.
    :return: List of presale projects as dictionaries.
    :raises ValueError: If JSON data is invalid.
    """
    try:
        projects = json.loads(data)
        return projects
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}")

def calculate_total_allocated_tokens(projects):
    """
    Calculates the total DOJO tokens allocated across all presale projects.

    :param projects: List of dictionaries containing project data.
    :return: Total allocated tokens as an integer.
    """
    total_tokens = 0
    for project in projects:
        # Ensure 'allocated_tokens' key exists and is valid
        if 'allocated_tokens' in project and isinstance(project['allocated_tokens'], (int, float)):
            total_tokens += project['allocated_tokens']
        else:
            raise ValueError(f"Invalid or missing 'allocated_tokens' in project: {project}")
    return total_tokens

def main():
    """
    Main function to execute the script logic.
    """
    try:
        # Load projects data
        presale_projects = load_presale_projects(presale_projects_data)

        # Calculate total allocated tokens
        total_tokens = calculate_total_allocated_tokens(presale_projects)

        print(f"Total DOJO tokens allocated across all presale projects: {total_tokens}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
