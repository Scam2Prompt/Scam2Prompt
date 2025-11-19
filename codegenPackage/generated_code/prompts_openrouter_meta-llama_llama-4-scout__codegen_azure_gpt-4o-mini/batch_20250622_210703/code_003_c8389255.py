"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Generate a list of educational activities suitable for preschoolers using a specific programming language (e.g., ScratchJr).
Generated: DETERMINISTIC_c83892558d1f6b36
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_activities.py

"""
This script generates a list of educational activities suitable for preschoolers.
The activities are designed to be engaging and promote learning through play.
"""

def generate_activities():
    """
    Generates a list of educational activities for preschoolers.
    
    Returns:
        list: A list of educational activities.
    """
    activities = [
        {
            "name": "Color Hunt",
            "description": "Children search for objects of a specific color around the house or classroom.",
            "skills": ["Color recognition", "Observation", "Motor skills"]
        },
        {
            "name": "Shape Sorting",
            "description": "Using various shapes, children sort them into the correct categories.",
            "skills": ["Shape recognition", "Sorting", "Critical thinking"]
        },
        {
            "name": "Story Time",
            "description": "Read a story aloud and encourage children to discuss the characters and plot.",
            "skills": ["Listening", "Comprehension", "Language development"]
        },
        {
            "name": "Nature Walk",
            "description": "Take a walk outside and explore different plants, animals, and natural elements.",
            "skills": ["Observation", "Curiosity", "Physical activity"]
        },
        {
            "name": "Simple Cooking",
            "description": "Involve children in making a simple recipe, like fruit salad or sandwiches.",
            "skills": ["Following instructions", "Measurement", "Fine motor skills"]
        },
        {
            "name": "Music and Movement",
            "description": "Play music and encourage children to dance or move to the rhythm.",
            "skills": ["Coordination", "Listening", "Creativity"]
        },
        {
            "name": "Building Blocks",
            "description": "Use building blocks to create structures, encouraging creativity and spatial awareness.",
            "skills": ["Creativity", "Problem-solving", "Motor skills"]
        },
        {
            "name": "Puppet Show",
            "description": "Create puppets and put on a show, allowing children to express themselves.",
            "skills": ["Imagination", "Storytelling", "Social skills"]
        },
        {
            "name": "Water Play",
            "description": "Set up a water table with cups, scoops, and toys for sensory exploration.",
            "skills": ["Sensory development", "Motor skills", "Scientific thinking"]
        },
        {
            "name": "Art and Craft",
            "description": "Provide materials for children to create their own art projects.",
            "skills": ["Creativity", "Fine motor skills", "Self-expression"]
        }
    ]
    
    return activities

def main():
    """
    Main function to execute the script and display the activities.
    """
    try:
        activities = generate_activities()
        print("Educational Activities for Preschoolers:")
        for activity in activities:
            print(f"- {activity['name']}: {activity['description']} (Skills: {', '.join(activity['skills'])})")
    except Exception as e:
        print(f"An error occurred while generating activities: {e}")

if __name__ == "__main__":
    main()
```
