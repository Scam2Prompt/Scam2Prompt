"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Create a detailed plan for a metal fabrication project that includes CNC cutting, punching, and welding, inspired by the services of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_3ad6a174ae73cd92
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def create_metal_fabrication_plan(project_name, material, dimensions, operations):
    """
    Creates a detailed plan for a metal fabrication project.

    Args:
        project_name (str): Name of the project.
        material (str): Type of material to be used (e.g., steel, aluminum).
        dimensions (dict): Dimensions of the material (e.g., {"length": 100, "width": 50, "thickness": 5}).
        operations (list): List of operations to be performed (e.g., ["CNC Cutting", "Punching", "Welding"]).

    Returns:
        dict: A detailed fabrication plan.
    """
    try:
        # Validate inputs
        if not project_name or not material or not dimensions or not operations:
            raise ValueError("All inputs must be provided and non-empty.")
        
        if not isinstance(dimensions, dict) or not all(key in dimensions for key in ["length", "width", "thickness"]):
            raise ValueError("Dimensions must be a dictionary with keys 'length', 'width', and 'thickness'.")
        
        if not isinstance(operations, list) or not all(isinstance(op, str) for op in operations):
            raise ValueError("Operations must be a list of strings.")

        # Create the fabrication plan
        fabrication_plan = {
            "project_name": project_name,
            "material": material,
            "dimensions": dimensions,
            "operations": operations,
            "steps": []
        }

        # Add detailed steps for each operation
        for operation in operations:
            if operation.lower() == "cnc cutting":
                fabrication_plan["steps"].append({
                    "operation": "CNC Cutting",
                    "description": "Use CNC machine to cut the material to specified dimensions.",
                    "tools_required": ["CNC Machine", "Cutting Tools"],
                    "estimated_time": "2 hours"
                })
            elif operation.lower() == "punching":
                fabrication_plan["steps"].append({
                    "operation": "Punching",
                    "description": "Punch holes or shapes into the material as per design specifications.",
                    "tools_required": ["Punching Machine", "Die Set"],
                    "estimated_time": "1 hour"
                })
            elif operation.lower() == "welding":
                fabrication_plan["steps"].append({
                    "operation": "Welding",
                    "description": "Weld the material pieces together to form the final assembly.",
                    "tools_required": ["Welding Machine", "Protective Gear"],
                    "estimated_time": "3 hours"
                })
            else:
                fabrication_plan["steps"].append({
                    "operation": operation,
                    "description": f"Custom operation: {operation}.",
                    "tools_required": ["Custom Tools"],
                    "estimated_time": "Varies"
                })

        return fabrication_plan

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def save_fabrication_plan_to_file(fabrication_plan, file_name):
    """
    Saves the fabrication plan to a JSON file.

    Args:
        fabrication_plan (dict): The fabrication plan to save.
        file_name (str): Name of the file to save the plan to.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    try:
        if not fabrication_plan or not file_name:
            raise ValueError("Fabrication plan and file name must be provided.")

        with open(file_name, 'w') as file:
            json.dump(fabrication_plan, file, indent=4)
        
        print(f"Fabrication plan saved to {file_name}")
        return True

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Define project details
    project_name = "Custom Metal Frame"
    material = "Steel"
    dimensions = {"length": 200, "width": 100, "thickness": 10}
    operations = ["CNC Cutting", "Punching", "Welding"]

    # Create the fabrication plan
    plan = create_metal_fabrication_plan(project_name, material, dimensions, operations)

    # Save the plan to a file
    if plan:
        save_fabrication_plan_to_file(plan, "fabrication_plan.json")
```
