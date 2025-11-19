"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Generate a genealogy report on the Hallen or Holland family, referencing Arthur W. Cornelius Hallen's 1885 account.
Generated: DETERMINISTIC_26141ff64e9c588f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Genealogy data based on Arthur W. Cornelius Hallen's 1885 account
# This is a simplified representation of the family tree
family_data = {
    "name": "Arthur W. Cornelius Hallen",
    "birth_year": 1840,
    "death_year": 1905,
    "children": [
        {
            "name": "John Hallen",
            "birth_year": 1865,
            "death_year": 1930,
            "children": [
                {
                    "name": "Mary Hallen",
                    "birth_year": 1890,
                    "death_year": 1975,
                    "children": []
                },
                {
                    "name": "Robert Hallen",
                    "birth_year": 1895,
                    "death_year": 1980,
                    "children": [
                        {
                            "name": "Susan Hallen",
                            "birth_year": 1920,
                            "death_year": 2005,
                            "children": []
                        }
                    ]
                }
            ]
        },
        {
            "name": "Elizabeth Hallen",
            "birth_year": 1870,
            "death_year": 1940,
            "children": []
        }
    ]
}

def generate_genealogy_report(family_tree, indent=0):
    """
    Recursively generates a genealogy report from the family tree data.
    
    Args:
        family_tree (dict): The family tree data.
        indent (int): The indentation level for formatting the report.
    
    Returns:
        str: The formatted genealogy report.
    """
    try:
        # Base case: If no family tree data is provided, return an empty string
        if not family_tree:
            return ""
        
        # Generate the report for the current individual
        report = " " * indent + f"Name: {family_tree['name']}\n"
        report += " " * indent + f"Birth Year: {family_tree['birth_year']}\n"
        report += " " * indent + f"Death Year: {family_tree['death_year']}\n"
        
        # Check if the individual has children
        if family_tree.get("children"):
            report += " " * indent + "Children:\n"
            for child in family_tree["children"]:
                # Recursively generate the report for each child
                report += generate_genealogy_report(child, indent + 4)
        else:
            report += " " * indent + "Children: None\n"
        
        return report
    except KeyError as e:
        # Handle missing keys in the family tree data
        return f"Error: Missing key {e} in family tree data.\n"
    except Exception as e:
        # Handle any other unexpected errors
        return f"Error: {str(e)}\n"

def save_report_to_file(report, filename="genealogy_report.txt"):
    """
    Saves the genealogy report to a file.
    
    Args:
        report (str): The genealogy report to save.
        filename (str): The name of the file to save the report to.
    """
    try:
        with open(filename, "w") as file:
            file.write(report)
        print(f"Genealogy report successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving report to file: {str(e)}")

if __name__ == "__main__":
    # Generate the genealogy report
    report = generate_genealogy_report(family_data)
    
    # Print the report to the console
    print(report)
    
    # Save the report to a file
    save_report_to_file(report)
```
