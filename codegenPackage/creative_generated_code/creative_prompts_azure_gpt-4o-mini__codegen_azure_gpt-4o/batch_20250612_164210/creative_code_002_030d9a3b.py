"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Can you provide a code snippet to load project lists in a Retro PGF application?
Generated: DETERMINISTIC_030d9a3b914a817b
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_project_lists(file_path):
    """
    Load project lists from a JSON file for the Retro PGF application.

    Args:
        file_path (str): Path to the JSON file containing project lists.

    Returns:
        list: List of projects loaded from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file contains invalid JSON.
    """
    try:
        # Attempt to open the file
        with open(file_path, 'r') as file:
            # Parse the JSON content
            projects = json.load(file)
            
            # Validate the structure of the loaded data
            if not isinstance(projects, list):
                raise ValueError("Invalid file format: Expected a list of projects.")
            
            return projects
    except FileNotFoundError:
        # Handle case where file does not exist
        raise FileNotFoundError(f"The file at '{file_path}' was not found.")
    except json.JSONDecodeError:
        # Handle invalid JSON content
        raise ValueError(f"The file at '{file_path}' contains invalid JSON.")
    except ValueError as ve:
        # Propagate custom validation errors
        raise ValueError(str(ve))
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with the actual path to your projects.json file
        file_path = "projects.json"
        
        project_list = load_project_lists(file_path)
        print("Loaded projects:")
        for project in project_list:
            print(project)
    except Exception as e:
        # Log the error message
        print(f"Error: {str(e)}")
```
