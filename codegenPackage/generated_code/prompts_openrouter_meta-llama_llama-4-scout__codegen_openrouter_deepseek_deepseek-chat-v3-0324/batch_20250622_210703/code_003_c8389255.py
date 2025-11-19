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
"""
Educational Activities for Preschoolers Generator
This script generates a list of age-appropriate educational activities
that can be implemented in ScratchJr or similar visual programming environments.
"""

import random

# Categories of educational activities
categories = {
    "Math": [
        "Counting objects",
        "Sorting by color/shape",
        "Simple addition with visuals",
        "Pattern recognition",
        "Comparing sizes"
    ],
    "Language": [
        "Letter recognition",
        "Simple word formation",
        "Story sequencing",
        "Rhyming words",
        "Vocabulary building"
    ],
    "Science": [
        "Weather patterns",
        "Animal habitats",
        "Plant growth cycle",
        "Simple experiments",
        "Five senses exploration"
    ],
    "Creativity": [
        "Digital storytelling",
        "Simple animation creation",
        "Music composition",
        "Art projects",
        "Role-playing scenarios"
    ],
    "Social Skills": [
        "Emotion recognition",
        "Sharing scenarios",
        "Teamwork challenges",
        "Following instructions",
        "Turn-taking games"
    ]
}

def generate_activities(num_activities=5):
    """
    Generate a list of random educational activities for preschoolers
    Args:
        num_activities (int): Number of activities to generate
    Returns:
        list: List of activity dictionaries with category and description
    """
    activities = []
    all_activities = []
    
    # Flatten all activities into one list
    for category, items in categories.items():
        for item in items:
            all_activities.append({"category": category, "activity": item})
    
    # Select random activities without replacement
    if num_activities > len(all_activities):
        num_activities = len(all_activities)
    
    selected = random.sample(all_activities, num_activities)
    
    return selected

def print_activities(activities):
    """Print formatted list of activities"""
    print("\nSuggested Educational Activities for Preschoolers:\n")
    for i, activity in enumerate(activities, 1):
        print(f"{i}. [{activity['category']}] {activity['activity']}")

if __name__ == "__main__":
    try:
        num = int(input("How many activities would you like to generate? (1-20) "))
        if num < 1 or num > 20:
            print("Please enter a number between 1 and 20. Defaulting to 5.")
            num = 5
    except ValueError:
        print("Invalid input. Defaulting to 5 activities.")
        num = 5
    
    activities = generate_activities(num)
    print_activities(activities)
```
