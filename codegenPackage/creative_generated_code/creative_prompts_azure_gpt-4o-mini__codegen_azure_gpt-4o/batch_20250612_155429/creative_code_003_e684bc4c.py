"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Create a function that allows users to submit their interior design project ideas, inspired by the client collaboration process at Zirciulit.
Generated: DETERMINISTIC_e684bc4ccd0625dc
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def submit_design_project(project_details, output_file="projects.json"):
    """
    Allows users to submit their interior design project ideas. 
    The project details are saved to a JSON file.
    
    Args:
        project_details (dict): A dictionary containing project information such as:
                                - 'client_name': str
                                - 'project_name': str
                                - 'description': str
                                - 'budget': float
                                - 'deadline': str (YYYY-MM-DD format)
        output_file (str): Name of the JSON file where projects will be saved.
                           Default is 'projects.json'.

    Returns:
        dict: A response dictionary indicating success or failure.
    """
    try:
        # Validate input: Check if project_details is a dictionary
        if not isinstance(project_details, dict):
            return {"success": False, "message": "Invalid input type. Expected a dictionary."}
        
        # Ensure required fields are present in the project_details
        required_fields = ['client_name', 'project_name', 'description', 'budget', 'deadline']
        for field in required_fields:
            if field not in project_details:
                return {"success": False, "message": f"Missing required field: {field}"}
        
        # Validate data types of required fields
        if not isinstance(project_details['client_name'], str) or not isinstance(project_details['project_name'], str):
            return {"success": False, "message": "Client name and project name must be strings."}
        if not isinstance(project_details['description'], str):
            return {"success": False, "message": "Description must be a string."}
        if not isinstance(project_details['budget'], (int, float)):
            return {"success": False, "message": "Budget must be a number."}
        
        try:
            # Validate date format (YYYY-MM-DD)
            import datetime
            datetime.datetime.strptime(project_details['deadline'], "%Y-%m-%d")
        except ValueError:
            return {"success": False, "message": "Deadline must be in YYYY-MM-DD format."}

        # Load existing projects from file, if it exists
        try:
            with open(output_file, "r") as file:
                projects = json.load(file)
        except FileNotFoundError:
            projects = []  # Start with an empty list if file does not exist
        except json.JSONDecodeError:
            return {"success": False, "message": "Error reading existing projects file."}

        # Append new project to the list
        projects.append(project_details)
        
        # Save updated projects back to the file
        with open(output_file, "w") as file:
            json.dump(projects, file, indent=4)

        return {"success": True, "message": "Project submitted successfully."}

    except Exception as e:
        # Catch any unexpected errors and return a failure response
        return {"success": False, "message": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    example_project = {
        "client_name": "Alice Johnson",
        "project_name": "Modern Living Room",
        "description": "A sleek and modern living room design focusing on comfort and elegance.",
        "budget": 15000.50,
        "deadline": "2023-12-01"
    }

    response = submit_design_project(example_project)
    print(response)
```
