"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Write a code snippet to create a search function that filters pediatric dentists in Pune based on location and specialties.
Generated: DETERMINISTIC_92cb9831720f94c5
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Sample data representing pediatric dentists in Pune
dentists_data = [
    {"name": "Dr. A", "location": "Koregaon Park", "specialties": ["Orthodontics", "Preventive Dentistry"]},
    {"name": "Dr. B", "location": "Baner", "specialties": ["Cosmetic Dentistry", "Preventive Dentistry"]},
    {"name": "Dr. C", "location": "Kothrud", "specialties": ["Orthodontics", "Restorative Dentistry"]},
    {"name": "Dr. D", "location": "Koregaon Park", "specialties": ["Preventive Dentistry", "Restorative Dentistry"]},
]

def search_pediatric_dentists(location=None, specialties=None):
    """
    Filters pediatric dentists based on location and specialties.

    Args:
        location (str): The location to filter dentists by (optional).
        specialties (list): A list of specialties to filter dentists by (optional).

    Returns:
        list: A list of dentists matching the criteria.
    """
    try:
        # Validate input
        if specialties and not isinstance(specialties, list):
            raise ValueError("Specialties must be a list of strings.")

        # Filter dentists based on location and specialties
        filtered_dentists = [
            dentist for dentist in dentists_data
            if (location is None or dentist["location"].lower() == location.lower()) and
               (specialties is None or any(specialty.lower() in map(str.lower, dentist["specialties"]) for specialty in specialties))
        ]

        return filtered_dentists

    except Exception as e:
        # Log the error and return an empty list
        print(f"Error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Search for dentists in Koregaon Park with Preventive Dentistry specialty
    location_filter = "Koregaon Park"
    specialties_filter = ["Preventive Dentistry"]
    
    results = search_pediatric_dentists(location=location_filter, specialties=specialties_filter)
    
    # Print results in a readable format
    print(json.dumps(results, indent=4))
```
