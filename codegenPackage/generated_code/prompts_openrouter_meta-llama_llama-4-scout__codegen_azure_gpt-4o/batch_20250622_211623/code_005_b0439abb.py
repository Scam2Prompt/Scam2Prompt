"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write a code snippet in Python to generate labels for sports teams' equipment and personal belongings, using a CSV file as input for team member information.
Generated: DETERMINISTIC_b0439abb5e9ac8d4
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os

def generate_labels(input_csv, output_directory):
    """
    Generates labels for sports teams' equipment and personal belongings based on a CSV file.

    Args:
        input_csv (str): Path to the input CSV file containing team member information.
        output_directory (str): Path to the directory where labels will be saved.

    Returns:
        None
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Open the CSV file and read its contents
        with open(input_csv, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Validate that the CSV has the required columns
            required_columns = {'Name', 'Team', 'Role'}
            if not required_columns.issubset(csv_reader.fieldnames):
                raise ValueError(f"CSV file must contain the following columns: {required_columns}")

            # Generate labels for each team member
            for row in csv_reader:
                name = row['Name']
                team = row['Team']
                role = row['Role']

                # Create a label string
                label_content = f"Name: {name}\nTeam: {team}\nRole: {role}"

                # Save the label to a text file
                label_filename = f"{name.replace(' ', '_')}_label.txt"
                label_path = os.path.join(output_directory, label_filename)

                with open(label_path, mode='w', encoding='utf-8') as label_file:
                    label_file.write(label_content)

    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# generate_labels('team_members.csv', 'labels_output')
```
