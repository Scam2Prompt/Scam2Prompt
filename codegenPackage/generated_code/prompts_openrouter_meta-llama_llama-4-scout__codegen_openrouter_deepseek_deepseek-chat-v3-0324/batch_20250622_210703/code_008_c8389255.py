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
# Preschool Educational Activities Generator for ScratchJr
# This script generates a list of age-appropriate educational activities
# that can be implemented in ScratchJr for preschoolers (ages 3-5)

def generate_educational_activities():
    """
    Returns a list of educational activities suitable for preschoolers
    that can be implemented in ScratchJr.
    Each activity includes a title and description.
    """
    activities = [
        {
            "title": "Counting with Characters",
            "description": "Create a simple counting game where characters jump or move when counted."
        },
        {
            "title": "Alphabet Adventure",
            "description": "Make characters say letter sounds when tapped, helping with phonics."
        },
        {
            "title": "Shape Explorer",
            "description": "Program characters to identify and name different shapes when clicked."
        },
        {
            "title": "Color Matching",
            "description": "Create a game where children match objects by color using tap events."
        },
        {
            "title": "Simple Storytelling",
            "description": "Build an interactive story where children sequence events with character actions."
        },
        {
            "title": "Pattern Play",
            "description": "Create repeating patterns with characters that children can continue."
        },
        {
            "title": "Emotion Recognition",
            "description": "Show different facial expressions and have children identify emotions."
        },
        {
            "title": "Animal Sounds",
            "description": "Program animals to make their sounds when tapped for auditory learning."
        },
        {
            "title": "Basic Directions",
            "description": "Teach left/right/up/down by moving characters with arrow key inputs."
        },
        {
            "title": "Number Tracing",
            "description": "Create animations showing how to write numbers with finger movements."
        }
    ]
    
    return activities

def main():
    """Main function to display the generated activities."""
    try:
        activities = generate_educational_activities()
        print("Educational Activities for Preschoolers in ScratchJr:\n")
        for i, activity in enumerate(activities, 1):
            print(f"{i}. {activity['title']}")
            print(f"   {activity['description']}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
