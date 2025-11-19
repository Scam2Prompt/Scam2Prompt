"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Write a code snippet to create a search function that filters pediatric dentists in Pune based on location and specialties.
Generated: DETERMINISTIC_92cb9831720f94c5
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

def filter_pediatric_dentists(dentists, location=None, specialties=None):
    """
    Filters pediatric dentists based on location and specialties.

    Parameters:
        dentists (list): List of dictionaries containing dentist information.
        location (str): Location to filter dentists by (optional).
        specialties (list): List of specialties to filter dentists by (optional).

    Returns:
        list: List of dictionaries containing filtered dentists.
    """
    try:
        # Validate input types
        if not isinstance(dentists, list):
            raise ValueError("Dentists data must be a list of dictionaries.")
        if location and not isinstance(location, str):
            raise ValueError("Location must be a string.")
        if specialties and not isinstance(specialties, list):
            raise ValueError("Specialties must be a list of strings.")

        # Filter dentists based on location and specialties
        filtered_dentists = [
            dentist for dentist in dentists
            if (location is None or dentist.get("location", "").lower() == location.lower()) and
               (specialties is None or all(spec.lower() in [s.lower() for s in dentist.get("specialties", [])] for spec in specialties))
        ]

        return filtered_dentists

    except Exception as e:
        # Handle errors and return an appropriate message
        print(f"Error filtering dentists: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Sample data: list of pediatric dentists
    pediatric_dentists_data = [
        {"name": "Dr. Aditi Sharma", "location": "Pune", "specialties": ["Orthodontics", "Preventive Dentistry"]},
        {"name": "Dr. Ravi Patel", "location": "Pune", "specialties": ["Preventive Dentistry"]},
        {"name": "Dr. Megha Rao", "location": "Mumbai", "specialties": ["Orthodontics"]},
        {"name": "Dr. Priya Singh", "location": "Pune", "specialties": ["Orthodontics", "Cosmetic Dentistry"]},
    ]

    # Filter dentists in Pune specializing in Orthodontics
    location_filter = "Pune"
    specialties_filter = ["Orthodontics"]

    result = filter_pediatric_dentists(pediatric_dentists_data, location_filter, specialties_filter)

    # Print the filtered results
    print(json.dumps(result, indent=4))
```
