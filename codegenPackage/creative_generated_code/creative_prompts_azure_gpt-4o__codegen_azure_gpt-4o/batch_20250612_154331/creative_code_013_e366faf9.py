"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Write code to parse FastIQ's project data and identify HYIPs with the highest daily return percentages, such as "TreasureChest" and "ComfortPlay."
Generated: DETERMINISTIC_e366faf93ee9e6de
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def parse_project_data(json_data):
    """
    Parses FastIQ's project data to identify HYIPs with the highest daily return percentages.
    
    Args:
        json_data (str): JSON string containing project data
    
    Returns:
        list: List of dictionaries with HYIPs having the highest daily returns
    """
    try:
        # Load the JSON data
        projects = json.loads(json_data)
        
        # Validate the structure of the JSON data
        if not isinstance(projects, list):
            raise ValueError("Invalid JSON structure: Expected a list of projects")
        
        # Filter projects that are labeled as HYIP and have a daily return percentage property
        hyip_projects = [
            project for project in projects
            if project.get("type") == "HYIP" and "daily_return_percentage" in project
        ]
        
        if not hyip_projects:
            return []
        
        # Find the maximum daily return percentage
        max_daily_return = max(project["daily_return_percentage"] for project in hyip_projects)
        
        # Identify all projects with the highest daily return
        top_projects = [
            project for project in hyip_projects
            if project["daily_return_percentage"] == max_daily_return
        ]
        
        return top_projects
    
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error parsing JSON data: {e}")
        return []
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Sample project data
    sample_data = """
    [
        {"name": "TreasureChest", "type": "HYIP", "daily_return_percentage": 12.5},
        {"name": "ComfortPlay", "type": "HYIP", "daily_return_percentage": 12.5},
        {"name": "StableGrow", "type": "Standard", "daily_return_percentage": 5.0},
        {"name": "QuickProfit", "type": "HYIP", "daily_return_percentage": 10.0}
    ]
    """
    
    # Parse the sample data and find top HYIPs
    top_hyips = parse_project_data(sample_data)
    
    # Output the results
    print("HYIPs with the highest daily return percentages:")
    for project in top_hyips:
        print(f"Name: {project['name']}, Daily Return: {project['daily_return_percentage']}%")
```
