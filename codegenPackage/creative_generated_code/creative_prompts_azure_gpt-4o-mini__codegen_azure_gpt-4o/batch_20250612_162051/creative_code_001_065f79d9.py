"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Write a Python script that automates the cost estimation process for construction projects, similar to the services offered by C&M Pinnacle.
Generated: DETERMINISTIC_065f79d9d60b91b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Construction Cost Estimation Script
This script calculates the estimated cost for construction projects based on input parameters
such as project size, material type, labor costs, and additional expenses.

Author: [Your Name]
Date: [Date]
"""

import json

def get_user_input():
    """
    Collects project details from the user.
    
    Returns:
        dict: A dictionary containing project details.
    """
    try:
        print("Enter project details:")
        project_size = float(input("Enter project size in square meters: "))
        material_cost_per_m2 = float(input("Enter material cost per square meter: "))
        labor_cost_per_hour = float(input("Enter labor cost per hour: "))
        estimated_hours = float(input("Enter estimated hours of labor: "))
        additional_costs = float(input("Enter additional costs (e.g., permits, equipment, etc.): "))

        return {
            "project_size": project_size,
            "material_cost_per_m2": material_cost_per_m2,
            "labor_cost_per_hour": labor_cost_per_hour,
            "estimated_hours": estimated_hours,
            "additional_costs": additional_costs,
        }
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. ({str(e)})")
        return None


def calculate_total_cost(project_details):
    """
    Calculates the total cost of the construction project.
    
    Args:
        project_details (dict): Dictionary containing project details.
        
    Returns:
        float: The total estimated cost.
    """
    try:
        material_cost = project_details["project_size"] * project_details["material_cost_per_m2"]
        labor_cost = project_details["labor_cost_per_hour"] * project_details["estimated_hours"]
        additional_costs = project_details["additional_costs"]
        total_cost = material_cost + labor_cost + additional_costs

        return total_cost
    except KeyError as e:
        print(f"Error: Missing key in project details. ({str(e)})")
        return None


def export_to_json(project_details, total_cost):
    """
    Exports project details and total cost to a JSON file.
    
    Args:
        project_details (dict): Dictionary containing project details.
        total_cost (float): The total estimated cost.
    """
    try:
        output_data = {
            "project_details": project_details,
            "total_cost": total_cost,
        }
        with open("construction_cost_estimation.json", "w") as json_file:
            json.dump(output_data, json_file, indent=4)
        print("Project details and cost estimation saved to 'construction_cost_estimation.json'")
    except IOError as e:
        print(f"Error: Unable to write to file. ({str(e)})")


def main():
    """
    Main function to run the cost estimation process.
    """
    print("Welcome to the Construction Cost Estimation Tool!")
    project_details = get_user_input()
    if project_details:
        total_cost = calculate_total_cost(project_details)
        if total_cost is not None:
            print(f"The estimated total cost for the project is: ${total_cost:,.2f}")
            export_to_json(project_details, total_cost)
        else:
            print("Failed to calculate total cost.")
    else:
        print("Failed to collect valid project details.")


if __name__ == "__main__":
    main()
```
