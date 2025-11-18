"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Write a script to generate a cost estimate for a manufacturing structure project, referencing the diverse project list provided by Bismillah Traders.
Generated: DETERMINISTIC_32e43c39a3a0b47b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_project_list(file_path):
    """
    Load the project list from a JSON file.
    
    :param file_path: Path to the JSON file containing project data
    :return: A dictionary of project data
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}")
        return None


def calculate_cost(project_data, project_name, quantity):
    """
    Calculate the cost estimate for a given project and quantity.
    
    :param project_data: Dictionary containing project data
    :param project_name: Name of the project to estimate cost for
    :param quantity: Quantity of structures to manufacture
    :return: Estimated cost or None if project_name is invalid
    """
    if project_name not in project_data:
        print(f"Error: Project '{project_name}' not found in the project list.")
        return None
    
    project_info = project_data[project_name]
    unit_cost = project_info.get('unit_cost', 0)
    labor_cost = project_info.get('labor_cost', 0)
    other_expenses = project_info.get('other_expenses', 0)
    
    # Calculate total cost for the given quantity
    total_cost = (unit_cost + labor_cost + other_expenses) * quantity
    return total_cost


def main():
    # File path to the project list JSON file
    project_list_file = "bismillah_traders_projects.json"
    
    # Load the project list from the file
    project_data = load_project_list(project_list_file)
    if project_data is None:
        return
    
    # Get user input for project name and quantity
    project_name = input("Enter the project name: ").strip()
    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Error: Quantity must be an integer.")
        return
    
    # Calculate cost estimate
    total_cost = calculate_cost(project_data, project_name, quantity)
    if total_cost is not None:
        print(f"Estimated cost for {quantity} units of '{project_name}': ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```

### Notes:
- Ensure that a JSON file named `bismillah_traders_projects.json` exists in the same directory or provide the correct path. The JSON file should contain a dictionary of projects with the structure:
  ```json
  {
      "ProjectA": {
          "unit_cost": 100,
          "labor_cost": 50,
          "other_expenses": 20
      },
      "ProjectB": {
          "unit_cost": 200,
          "labor_cost": 100,
          "other_expenses": 50
      }
  }
  ```
