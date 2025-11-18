"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Generate code to parse the SOMTU MBA curriculum details and output a structured JSON file for each specialization (e.g., MBA FC, MBA GLM, MBA IT).
Generated: DETERMINISTIC_cf530c7fbdcf2d34
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Function to parse curriculum details from a given source
def parse_curriculum(source_file):
    """
    Parses SOMTU MBA curriculum details from a source file and outputs structured JSON files
    for each specialization.
    
    Parameters:
    - source_file (str): Path to the file containing curriculum details.
    
    Returns:
    None. Generates JSON files for each specialization.
    """
    try:
        # Initialize a dictionary to store specialization data
        specializations = {}

        # Read the source file line by line
        with open(source_file, 'r') as file:
            for line in file:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue
                
                # Extract specialization name and details (assuming a specific format)
                # For example: "MBA FC: Financial Management, Marketing, Accounting"
                if ":" in line:
                    specialization, details = line.split(":", 1)
                    specialization = specialization.strip()
                    details = [detail.strip() for detail in details.split(",")]

                    # Add specialization and its details to the dictionary
                    specializations[specialization] = details

        # Generate JSON files for each specialization
        for specialization, details in specializations.items():
            json_file_name = specialization.replace(" ", "_") + ".json"
            with open(json_file_name, 'w') as json_file:
                json.dump({specialization: details}, json_file, indent=4)

            print(f"Generated: {json_file_name}")

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main function to execute the script
if __name__ == "__main__":
    # Example source file containing curriculum details
    source_file = "somtu_mba_curriculum.txt"

    # Call the function to parse curriculum and generate JSON files
    parse_curriculum(source_file)
```
