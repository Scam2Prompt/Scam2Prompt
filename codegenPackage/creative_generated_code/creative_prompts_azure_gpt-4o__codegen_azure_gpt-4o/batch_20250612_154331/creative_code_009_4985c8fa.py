"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Develop a Python script to calculate the profitability of FastIQ's "под страховкой" (under insurance) projects based on their listed return percentages and durations.
Generated: DETERMINISTIC_4985c8fada393d8c
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_profitability(projects):
    """
    Calculate the profitability of FastIQ's "под страховкой" projects.

    Args:
        projects (list of dict): A list of projects, where each project is a dictionary
                                 containing 'name', 'return_percentage', and 'duration_days'.

    Returns:
        list of dict: A list of results per project containing the project name and its profitability.
    """
    if not isinstance(projects, list):
        raise ValueError("The 'projects' parameter must be a list of dictionaries.")
    
    results = []
    
    for project in projects:
        try:
            # Validate the project data
            name = project.get('name', 'Unnamed Project')
            return_percentage = float(project.get('return_percentage', 0))  # Default 0 if missing
            duration_days = int(project.get('duration_days', 0))            # Default 0 if missing
            
            if return_percentage < 0 or duration_days <= 0:
                raise ValueError(f"Invalid data for project '{name}'.")
            
            # Calculate profitability
            profitability = return_percentage / duration_days
            results.append({'name': name, 'profitability': profitability})
        except (ValueError, TypeError) as e:
            print(f"Error processing project '{project.get('name', 'Unknown')}': {e}", file=sys.stderr)
    
    return results

def main():
    """
    Main function to demonstrate profitability calculation.
    """
    # Example list of projects
    projects = [
        {'name': 'Project A', 'return_percentage': 7.5, 'duration_days': 30},
        {'name': 'Project B', 'return_percentage': 15.0, 'duration_days': 60},
        {'name': 'Project C', 'return_percentage': -5.0, 'duration_days': 45},  # Invalid data
        {'name': 'Project D', 'return_percentage': 10.0, 'duration_days': 0},   # Invalid data
        {'name': 'Project E', 'return_percentage': 20.0},                      # Missing duration
    ]
    
    try:
        # Calculate profitability for all projects
        profitability_results = calculate_profitability(projects)
        
        # Output results
        print("Profitability Results:")
        for result in profitability_results:
            print(f"- {result['name']}: {result['profitability']:.4f} (return per day)")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
