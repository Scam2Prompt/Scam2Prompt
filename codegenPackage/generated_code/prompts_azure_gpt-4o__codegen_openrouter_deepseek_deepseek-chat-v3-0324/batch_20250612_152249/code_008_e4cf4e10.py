"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of attendees per region for the "Patente d'Impresa" events, using data collected from the registration form.
Generated: DETERMINISTIC_e4cf4e1020018d04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from collections import defaultdict

def calculate_attendees_per_region(csv_file_path):
    """
    Calculate the number of attendees per region from a CSV file containing registration data.
    
    Args:
        csv_file_path (str): Path to the CSV file containing registration data.
                            Expected columns: 'name', 'email', 'region', etc.
    
    Returns:
        dict: A dictionary with regions as keys and attendee counts as values.
    
    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        ValueError: If the CSV file is malformed or missing required columns.
    """
    try:
        region_counts = defaultdict(int)
        
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            if 'region' not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'region' column")
            
            for row in reader:
                region = row['region'].strip()
                if region:  # Only count if region is not empty
                    region_counts[region] += 1
        
        return dict(region_counts)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {csv_file_path} was not found")
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {str(e)}")

# Example usage:
# attendees_by_region = calculate_attendees_per_region('registrations.csv')
# print(attendees_by_region)
```
