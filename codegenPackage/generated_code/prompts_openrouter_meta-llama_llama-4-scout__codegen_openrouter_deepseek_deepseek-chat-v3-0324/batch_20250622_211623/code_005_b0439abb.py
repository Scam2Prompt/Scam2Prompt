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
from datetime import datetime

def generate_labels(input_csv, output_dir="labels"):
    """
    Generate labels for sports teams' equipment and personal belongings from a CSV file.
    
    Args:
        input_csv (str): Path to the input CSV file containing team member information.
        output_dir (str): Directory where label files will be saved. Defaults to "labels".
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate a timestamp for unique filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"labels_{timestamp}.txt")
        
        # Read CSV file and process each row
        with open(input_csv, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Validate required fields
            required_fields = ['name', 'team', 'jersey_number']
            if not all(field in csv_reader.fieldnames for field in required_fields):
                raise ValueError(f"CSV file must contain these fields: {required_fields}")
            
            # Open output file and write labels
            with open(output_file, mode='w', encoding='utf-8') as f:
                for row in csv_reader:
                    name = row['name'].strip()
                    team = row['team'].strip()
                    jersey_number = row['jersey_number'].strip()
                    
                    # Generate label format
                    label = (
                        f"--------------------\n"
                        f"Team: {team}\n"
                        f"Name: {name}\n"
                        f"Jersey #: {jersey_number}\n"
                        f"--------------------\n\n"
                    )
                    
                    f.write(label)
        
        print(f"Labels generated successfully: {output_file}")
        return True
    
    except FileNotFoundError:
        print(f"Error: Input file not found: {input_csv}")
        return False
    except PermissionError:
        print(f"Error: Permission denied when accessing files.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

# Example usage (commented out for production)
# if __name__ == "__main__":
#     generate_labels("team_members.csv")
```
