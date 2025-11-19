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
from typing import List, Dict, Any

class Dentist:
    """Class representing a pediatric dentist."""
    
    def __init__(self, name: str, location: str, specialties: List[str]):
        """
        Initialize a new Dentist instance.

        :param name: Name of the dentist
        :param location: Location of the dentist
        :param specialties: List of specialties of the dentist
        """
        self.name = name
        self.location = location
        self.specialties = specialties

def filter_dentists(dentists: List[Dentist], location: str, specialty: str) -> List[Dict[str, Any]]:
    """
    Filter pediatric dentists based on location and specialty.

    :param dentists: List of Dentist objects to filter
    :param location: Location to filter dentists by
    :param specialty: Specialty to filter dentists by
    :return: List of dictionaries containing filtered dentist information
    """
    filtered_dentists = []

    for dentist in dentists:
        # Check if the dentist's location and specialty match the criteria
        if dentist.location.lower() == location.lower() and specialty.lower() in map(str.lower, dentist.specialties):
            filtered_dentists.append({
                'name': dentist.name,
                'location': dentist.location,
                'specialties': dentist.specialties
            })

    return filtered_dentists

# Example usage
if __name__ == "__main__":
    # Sample data
    dentists_list = [
        Dentist("Dr. A", "Pune", ["Orthodontics", "Pediatric Dentistry"]),
        Dentist("Dr. B", "Pune", ["General Dentistry"]),
        Dentist("Dr. C", "Mumbai", ["Pediatric Dentistry"]),
        Dentist("Dr. D", "Pune", ["Pediatric Dentistry", "Oral Surgery"]),
    ]

    # Search parameters
    search_location = "Pune"
    search_specialty = "Pediatric Dentistry"

    # Perform the search
    try:
        results = filter_dentists(dentists_list, search_location, search_specialty)
        if results:
            print("Filtered Dentists:")
            for dentist in results:
                print(f"Name: {dentist['name']}, Location: {dentist['location']}, Specialties: {', '.join(dentist['specialties'])}")
        else:
            print("No dentists found matching the criteria.")
    except Exception as e:
        print(f"An error occurred while filtering dentists: {e}")
```
