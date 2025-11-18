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
import pandas as pd

def calculate_attendees_per_region(registration_data):
    """
    Calculate the number of attendees per region for the "Patente d'Impresa" events.

    Args:
        registration_data (pd.DataFrame): A pandas DataFrame containing registration data
                                            with a 'region' column.

    Returns:
        pd.Series: A Series with the count of attendees indexed by region.
    
    Raises:
        ValueError: If 'region' column is not present in the DataFrame.
    """
    # Check if the required column exists in the DataFrame
    if 'region' not in registration_data.columns:
        raise ValueError("The DataFrame must contain a 'region' column.")

    # Group by region and count the number of attendees
    attendees_per_region = registration_data['region'].value_counts()

    return attendees_per_region

# Example usage (uncomment to use):
# if __name__ == "__main__":
#     # Sample registration data
#     data = {
#         'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'region': ['Lombardia', 'Lazio', 'Lombardia', 'Campania']
#     }
#     registration_df = pd.DataFrame(data)
#     result = calculate_attendees_per_region(registration_df)
#     print(result)
```
