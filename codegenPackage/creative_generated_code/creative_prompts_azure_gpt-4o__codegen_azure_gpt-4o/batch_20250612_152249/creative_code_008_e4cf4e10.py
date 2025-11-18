"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of attendees per region for the "Patente d'Impresa" events, using data collected from the registration form.
Generated: DETERMINISTIC_e4cf4e1020018d04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from collections import defaultdict

def calculate_attendees_per_region(registration_data):
    """
    Calculate the number of attendees per region for the 'Patente d'Impresa' events.

    Args:
        registration_data (list of dict): A list of dictionaries containing registration information.
                                          Each dictionary must have a 'region' key.

    Returns:
        dict: A dictionary with regions as keys and the number of attendees as values.
    """
    # Validate input
    if not isinstance(registration_data, list):
        raise ValueError("registration_data must be a list of dictionaries")
    
    # Initialize a dictionary to store the count of attendees per region
    attendees_per_region = defaultdict(int)
    
    # Iterate over the registration data and count attendees per region
    for entry in registration_data:
        # Validate each entry in registration_data
        if not isinstance(entry, dict):
            raise ValueError("Each entry in registration_data must be a dictionary")
        if 'region' not in entry:
            raise KeyError("Each entry must contain a 'region' key")
        
        # Increment the count for the region
        region = entry['region']
        attendees_per_region[region] += 1
    
    # Convert the defaultdict to a regular dict before returning
    return dict(attendees_per_region)

# Example usage:
if __name__ == "__main__":
    # Sample registration data
    sample_data = [
        {"name": "Alice", "region": "North"},
        {"name": "Bob", "region": "South"},
        {"name": "Charlie", "region": "North"},
        {"name": "Diana", "region": "East"},
        {"name": "Edward", "region": "South"}
    ]
    
    # Calculate attendees per region
    try:
        result = calculate_attendees_per_region(sample_data)
        print("Attendees per region:", result)
    except (ValueError, KeyError) as e:
        print(f"Error processing registration data: {e}")
```
