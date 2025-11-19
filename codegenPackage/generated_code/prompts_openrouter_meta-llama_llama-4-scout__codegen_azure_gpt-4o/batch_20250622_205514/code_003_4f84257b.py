"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Generate a list of activities for a children's holiday party in Tallinn, including games and contests."
Generated: DETERMINISTIC_4f84257b8fa1d850
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_activities():
    """
    Generate a list of activities for a children's holiday party in Tallinn.
    
    Returns:
        list: A list of dictionaries containing activity details.
    """
    try:
        # List of activities with descriptions
        activities = [
            {
                "name": "Musical Chairs",
                "description": "A fun game where children compete for chairs as music plays.",
                "age_group": "5-12",
                "location": "Main Hall"
            },
            {
                "name": "Treasure Hunt",
                "description": "Children search for hidden treasures around the venue.",
                "age_group": "7-12",
                "location": "Outdoor Garden"
            },
            {
                "name": "Face Painting",
                "description": "Kids can get their faces painted with holiday-themed designs.",
                "age_group": "All ages",
                "location": "Art Corner"
            },
            {
                "name": "Holiday Quiz Contest",
                "description": "A fun quiz about holiday traditions and stories.",
                "age_group": "8-12",
                "location": "Conference Room"
            },
            {
                "name": "Cookie Decorating",
                "description": "Children decorate holiday cookies with icing and sprinkles.",
                "age_group": "5-10",
                "location": "Dining Area"
            },
            {
                "name": "Balloon Popping Game",
                "description": "Kids compete to pop balloons filled with surprises.",
                "age_group": "6-10",
                "location": "Play Area"
            },
            {
                "name": "Storytelling Session",
                "description": "A cozy session where holiday-themed stories are read aloud.",
                "age_group": "All ages",
                "location": "Library"
            }
        ]
        
        return activities
    except Exception as e:
        # Log the error and return an empty list
        print(f"An error occurred while generating activities: {e}")
        return []

def save_activities_to_file(activities, filename="holiday_party_activities.json"):
    """
    Save the list of activities to a JSON file.
    
    Args:
        activities (list): The list of activity dictionaries.
        filename (str): The name of the file to save the activities to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(activities, file, indent=4)
        print(f"Activities successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving activities to file: {e}")

def main():
    """
    Main function to generate and save activities for the holiday party.
    """
    # Generate the list of activities
    activities = generate_activities()
    
    # Save the activities to a file
    save_activities_to_file(activities)

if __name__ == "__main__":
    main()
```
