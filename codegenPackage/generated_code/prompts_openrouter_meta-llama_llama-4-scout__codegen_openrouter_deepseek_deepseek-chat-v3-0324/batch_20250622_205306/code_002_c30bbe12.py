"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Generate a list of potential comedy class offerings for kids and teens at The Second City, including improv, acting, and comedy writing.
Generated: DETERMINISTIC_c30bbe123094356d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ComedyClass:
    """Represents a comedy class offering at The Second City."""
    
    def __init__(self, name, age_range, description, duration_weeks):
        """
        Initialize a comedy class.
        
        Args:
            name (str): Name of the class
            age_range (str): Age range (e.g. "8-10", "13-17")
            description (str): Brief description of the class
            duration_weeks (int): Duration in weeks
        """
        self.name = name
        self.age_range = age_range
        self.description = description
        self.duration_weeks = duration_weeks
    
    def __str__(self):
        """String representation of the class."""
        return f"{self.name} (Ages {self.age_range}): {self.description} - {self.duration_weeks} weeks"

def generate_comedy_classes():
    """Generate a list of comedy class offerings for kids and teens."""
    
    classes = [
        ComedyClass(
            "Improv Playtime",
            "8-10",
            "Introduction to improvisation through fun games and exercises",
            6
        ),
        ComedyClass(
            "Acting Out Loud",
            "10-12",
            "Fundamentals of acting with focus on comedy and expression",
            8
        ),
        ComedyClass(
            "Sketch Comedy Lab",
            "13-17",
            "Writing and performing original comedy sketches",
            10
        ),
        ComedyClass(
            "Improv for Teens",
            "13-17",
            "Advanced improvisation techniques and scene work",
            8
        ),
        ComedyClass(
            "Stand-Up Stars",
            "12-15",
            "Developing and performing original stand-up comedy material",
            6
        ),
        ComedyClass(
            "Comedy Characters",
            "9-12",
            "Creating and performing funny characters through improv",
            6
        ),
        ComedyClass(
            "Storytelling with Laughs",
            "11-13",
            "Writing and performing humorous stories",
            8
        ),
        ComedyClass(
            "Improv Olympics",
            "10-12",
            "Team-based improv games and friendly competition",
            6
        ),
        ComedyClass(
            "Comedy Writing Workshop",
            "14-17",
            "Developing jokes, sketches, and comedic writing skills",
            10
        ),
        ComedyClass(
            "Acting for Camera",
            "13-17",
            "Techniques for acting in comedy TV and film",
            8
        )
    ]
    
    return classes

def display_classes(classes):
    """Display all comedy classes in a formatted list."""
    print("The Second City Comedy Classes for Kids and Teens:\n")
    for i, class_ in enumerate(classes, 1):
        print(f"{i}. {class_}")

if __name__ == "__main__":
    try:
        comedy_classes = generate_comedy_classes()
        display_classes(comedy_classes)
    except Exception as e:
        print(f"Error generating class list: {e}")
```
