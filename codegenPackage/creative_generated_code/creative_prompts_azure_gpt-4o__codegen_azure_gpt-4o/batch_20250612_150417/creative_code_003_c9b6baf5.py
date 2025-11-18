"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.com
Prompt: Write a function to parse and display the special roles table from the RedStone Expedition, highlighting roles with unique significance.
Generated: DETERMINISTIC_c9b6baf562f8ef24
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import csv
import os


def parse_and_display_roles_table(file_path):
    """
    Parses the special roles table from the RedStone Expedition CSV file and displays
    roles with unique significance. Unique roles are highlighted.

    Args:
        file_path (str): Path to the CSV file containing the roles table.

    Returns:
        None
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at path: {file_path}")
        return

    try:
        # Open the CSV file and parse its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            # Ensure the CSV has the required headers
            required_headers = {'Role', 'Description', 'Significance'}
            if not required_headers.issubset(set(csv_reader.fieldnames)):
                print("Error: Missing required headers in the file.")
                return

            print("Roles Table (Highlighting Unique Significance):")
            print("------------------------------------------------")

            for row in csv_reader:
                # Extract role information
                role = row.get('Role', '').strip()
                description = row.get('Description', '').strip()
                significance = row.get('Significance', '').strip()

                # Highlight roles with unique significance
                if significance.lower() == 'unique':
                    print(f"* [Unique] Role: {role}")
                else:
                    print(f"  Role: {role}")

                print(f"    Description: {description}")
                print(f"    Significance: {significance}")
                print("------------------------------------------------")

    except csv.Error as e:
        print(f"Error: Failed to parse CSV file. Details: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")


# Example usage:
# Provide the path to your CSV file containing the roles table.
# parse_and_display_roles_table('redstone_expedition_roles.csv')
```
