"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Provide Python code for a script that organizes laminating sheets by size and type, inspired by Gadgetexa's guide on choosing laminating sheets for home organization.
Generated: DETERMINISTIC_4e805600fcd97413
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
from collections import defaultdict

def organize_laminating_sheets(input_file, output_directory):
    """
    Organizes laminating sheets by size and type from a given CSV file.

    Args:
        input_file (str): Path to the input CSV file containing laminating sheet data.
                         The CSV file should have the columns: "Name", "Size", "Type".
        output_directory (str): Path to the directory where organized files will be saved.
    """
    try:
        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Dictionary to hold sheets organized by size and type
        laminating_sheets = defaultdict(lambda: defaultdict(list))
        
        # Read data from the input CSV file
        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if not {"Name", "Size", "Type"}.issubset(reader.fieldnames):
                raise ValueError("CSV file must include 'Name', 'Size', and 'Type' columns.")
            
            for row in reader:
                name = row["Name"].strip()
                size = row["Size"].strip()
                sheet_type = row["Type"].strip()
                
                if name and size and sheet_type:
                    laminating_sheets[size][sheet_type].append(name)
        
        # Write organized data to output files
        for size, types in laminating_sheets.items():
            for sheet_type, names in types.items():
                # Create file names based on size and type
                output_file = os.path.join(
                    output_directory,
                    f"{size.replace(' ', '_')}_{sheet_type.replace(' ', '_')}.txt"
                )
                
                # Write sheet names to the file
                with open(output_file, mode='w', encoding='utf-8') as file:
                    file.write(f"Laminating Sheets ({size} - {sheet_type})\n")
                    file.write("=" * 40 + "\n")
                    file.write("\n".join(names))
                    file.write("\n")
        
        print(f"Laminating sheets successfully organized in '{output_directory}'.")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# organize_laminating_sheets("laminating_sheets.csv", "organized_sheets")
```
