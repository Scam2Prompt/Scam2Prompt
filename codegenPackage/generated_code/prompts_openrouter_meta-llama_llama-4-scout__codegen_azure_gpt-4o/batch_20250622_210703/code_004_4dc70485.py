"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Create a technical specification for an electrical installation project, including details on materials, labor, and testing procedures.
Generated: DETERMINISTIC_4dc70485e5f1cf95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Specification Generator for Electrical Installation Project

This script generates a technical specification document for an electrical installation project.
The specification includes details on materials, labor, and testing procedures.

Requirements:
- Python 3.x
- No external dependencies

Author: [Your Name]
Date: [Insert Date]
"""

import json
from datetime import datetime

def generate_specification(project_name, client_name, materials, labor, testing_procedures):
    """
    Generates a technical specification document for an electrical installation project.

    Args:
        project_name (str): Name of the project.
        client_name (str): Name of the client.
        materials (list of dict): List of materials with details (e.g., name, quantity, unit price).
        labor (list of dict): List of labor tasks with details (e.g., task name, hours, hourly rate).
        testing_procedures (list of str): List of testing procedures.

    Returns:
        dict: A dictionary containing the technical specification.
    """
    try:
        # Validate inputs
        if not project_name or not client_name:
            raise ValueError("Project name and client name are required.")
        if not materials or not labor or not testing_procedures:
            raise ValueError("Materials, labor, and testing procedures cannot be empty.")

        # Generate specification
        specification = {
            "project_name": project_name,
            "client_name": client_name,
            "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "materials": materials,
            "labor": labor,
            "testing_procedures": testing_procedures,
            "total_material_cost": sum(item["quantity"] * item["unit_price"] for item in materials),
            "total_labor_cost": sum(task["hours"] * task["hourly_rate"] for task in labor),
            "total_project_cost": sum(item["quantity"] * item["unit_price"] for item in materials) +
                                  sum(task["hours"] * task["hourly_rate"] for task in labor)
        }

        return specification
    except Exception as e:
        print(f"Error generating specification: {e}")
        return None

def save_specification_to_file(specification, file_name):
    """
    Saves the technical specification to a JSON file.

    Args:
        specification (dict): The technical specification dictionary.
        file_name (str): Name of the file to save the specification.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(specification, file, indent=4)
        print(f"Specification saved to {file_name}")
        return True
    except Exception as e:
        print(f"Error saving specification to file: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Define project details
    project_name = "Office Building Electrical Installation"
    client_name = "ABC Corp"
    materials = [
        {"name": "Copper Wire", "quantity": 100, "unit_price": 1.5},
        {"name": "Circuit Breaker", "quantity": 10, "unit_price": 50.0},
        {"name": "Light Fixtures", "quantity": 20, "unit_price": 30.0}
    ]
    labor = [
        {"task_name": "Wiring Installation", "hours": 40, "hourly_rate": 25.0},
        {"task_name": "Testing and Inspection", "hours": 10, "hourly_rate": 30.0}
    ]
    testing_procedures = [
        "Continuity Testing",
        "Insulation Resistance Testing",
        "Earth Resistance Testing",
        "Load Testing"
    ]

    # Generate specification
    specification = generate_specification(project_name, client_name, materials, labor, testing_procedures)

    # Save specification to file
    if specification:
        save_specification_to_file(specification, "electrical_installation_specification.json")
```
