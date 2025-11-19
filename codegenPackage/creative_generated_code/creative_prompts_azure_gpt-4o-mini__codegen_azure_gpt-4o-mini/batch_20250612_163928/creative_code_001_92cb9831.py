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
import json
from typing import List, Dict, Any

# Sample data structure for pediatric dentists
DENTISTS_DATA = [
    {
        "name": "Dr. A",
        "location": "Pune",
        "specialties": ["orthodontics", "behavioral management"]
    },
    {
        "name": "Dr. B",
        "location": "Mumbai",
        "specialties": ["general dentistry"]
    },
    {
        "name": "Dr. C",
        "location": "Pune",
        "specialties": ["orthodontics", "pulp therapy"]
    },
    {
        "name": "Dr. D",
        "location": "Pune",
        "specialties": ["preventive care"]
    },
]

def search_pediatric_dentists(location: str, specialty: str) -> List[Dict[str, Any]]:
    """
    Search for pediatric dentists based on location and specialty.

    Args:
        location (str): The location to filter dentists.
        specialty (str): The specialty to filter dentists.

    Returns:
        List[Dict[str, Any]]: A list of dentists that match the criteria.
    """
    # Validate input parameters
    if not isinstance(location, str) or not isinstance(specialty, str):
        raise ValueError("Location and specialty must be strings.")

    # Filter dentists based on location and specialty
    filtered_dentists = [
        dentist for dentist in DENTISTS_DATA
        if dentist['location'].lower() == location.lower() and specialty.lower() in [s.lower() for s in dentist['specialties']]
    ]

    # Return the filtered list of dentists
    return filtered_dentists

def main():
    try:
        # Define search criteria
        location = "Pune"
        specialty = "orthodontics"
        
        # Perform search
        results = search_pediatric_dentists(location, specialty)

        # Output results
        if results:
            print(json.dumps(results, indent=4))
        else:
            print("No dentists found matching the criteria.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
