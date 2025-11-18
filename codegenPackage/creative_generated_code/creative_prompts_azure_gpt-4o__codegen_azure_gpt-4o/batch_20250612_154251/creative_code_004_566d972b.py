"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Provide a code example for implementing a search feature that allows users to find medical specialists by name, specialty, or location, as described on Grupo Clínico IDET's website.
Generated: DETERMINISTIC_566d972bd814f983
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Search Medical Specialists by Name, Specialty, or Location

This script implements a search feature that allows users to find medical specialists 
based on their name, specialty, or location. Results are filtered dynamically based 
on user input and returned in a readable format.

Dependencies:
- Python 3.x
"""

# Import required libraries
import json

# Sample database of medical specialists (mocked as a JSON object for simplicity)
SAMPLE_DATABASE = [
    {"name": "Dr. Ana López", "specialty": "Cardiology", "location": "Mexico City"},
    {"name": "Dr. Juan Pérez", "specialty": "Neurology", "location": "Guadalajara"},
    {"name": "Dr. María González", "specialty": "Orthopedics", "location": "Monterrey"},
    {"name": "Dr. Carlos Martínez", "specialty": "Dermatology", "location": "Tijuana"},
    {"name": "Dr. Sofia Ramírez", "specialty": "Pediatrics", "location": "Mexico City"}
]

def search_specialists(database, name=None, specialty=None, location=None):
    """
    Search for medical specialists in the provided database based on filters.

    Parameters:
        database (list): List of dictionaries representing the medical specialists.
        name (str): Optional, filter by name.
        specialty (str): Optional, filter by specialty.
        location (str): Optional, filter by location.

    Returns:
        list: A list of dictionaries representing the filtered medical specialists.
    """
    try:
        # Filter specialists based on provided criteria
        filtered_specialists = [
            specialist for specialist in database
            if (name is None or name.lower() in specialist["name"].lower())
            and (specialty is None or specialty.lower() in specialist["specialty"].lower())
            and (location is None or location.lower() in specialist["location"].lower())
        ]
        return filtered_specialists
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while searching: {str(e)}")
        return []

def display_results(results):
    """
    Display search results in a readable format.

    Parameters:
        results (list): List of dictionaries representing the filtered medical specialists.
    """
    if results:
        print("\nSearch Results:")
        for specialist in results:
            print(f"Name: {specialist['name']}, Specialty: {specialist['specialty']}, Location: {specialist['location']}")
    else:
        print("\nNo specialists found matching the criteria.")

def main():
    """
    Main function to run the search feature.
    """
    print("Welcome to the Medical Specialists Search!")
    print("You can search by name, specialty, or location. Leave blank to skip a filter.\n")

    # Get user input for search criteria
    name = input("Enter the name of the specialist (or press Enter to skip): ").strip()
    specialty = input("Enter the specialty (or press Enter to skip): ").strip()
    location = input("Enter the location (or press Enter to skip): ").strip()

    # Perform the search
    search_results = search_specialists(SAMPLE_DATABASE, name=name, specialty=specialty, location=location)

    # Display the search results
    display_results(search_results)

if __name__ == "__main__":
    # Execute the main function
    main()
```
