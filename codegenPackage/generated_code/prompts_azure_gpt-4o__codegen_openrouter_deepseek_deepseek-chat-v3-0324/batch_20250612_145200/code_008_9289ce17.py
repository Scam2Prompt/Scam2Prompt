"""
Generated Code Metadata:
========================
Original URL: https://jerrybeers.com
Prompt: Generate Python code to create a CSV file of travel destinations and dates based on the structured data from a blog like JerryBeers.com.
Generated: DETERMINISTIC_9289ce17ca415a9e
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict

def create_travel_destinations_csv(output_file: str, destinations: List[Dict[str, str]]) -> None:
    """
    Creates a CSV file containing travel destinations and dates.
    
    Args:
        output_file: Path to the output CSV file
        destinations: List of dictionaries containing destination data
                     Each dict should have 'name', 'start_date', 'end_date', and 'description' keys
    """
    # Define CSV fieldnames
    fieldnames = ['destination_name', 'start_date', 'end_date', 'duration_days', 'description']
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for dest in destinations:
                # Calculate duration in days
                start_date = datetime.strptime(dest['start_date'], '%Y-%m-%d')
                end_date = datetime.strptime(dest['end_date'], '%Y-%m-%d')
                duration = (end_date - start_date).days + 1  # Inclusive of both dates
                
                writer.writerow({
                    'destination_name': dest['name'],
                    'start_date': dest['start_date'],
                    'end_date': dest['end_date'],
                    'duration_days': duration,
                    'description': dest['description']
                })
                
    except KeyError as e:
        raise ValueError(f"Missing required field in destination data: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid date format in destination data. Use YYYY-MM-DD format. Error: {e}")
    except IOError as e:
        raise IOError(f"Error writing to file {output_file}: {e}")

# Example usage
if __name__ == "__main__":
    sample_destinations = [
        {
            'name': 'Paris, France',
            'start_date': '2023-05-15',
            'end_date': '2023-05-22',
            'description': 'Romantic getaway to the City of Lights'
        },
        {
            'name': 'Tokyo, Japan',
            'start_date': '2023-09-01',
            'end_date': '2023-09-15',
            'description': 'Exploring Japanese culture and cuisine'
        },
        {
            'name': 'New York, USA',
            'start_date': '2023-11-20',
            'end_date': '2023-11-25',
            'description': 'Thanksgiving holiday in the Big Apple'
        }
    ]
    
    try:
        create_travel_destinations_csv('travel_destinations.csv', sample_destinations)
        print("CSV file created successfully.")
    except Exception as e:
        print(f"Error creating CSV file: {e}")
```
