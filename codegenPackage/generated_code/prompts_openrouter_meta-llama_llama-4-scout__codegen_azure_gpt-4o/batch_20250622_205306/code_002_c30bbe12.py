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
import json

def generate_comedy_class_offerings():
    """
    Generate a list of potential comedy class offerings for kids and teens at The Second City.
    Includes improv, acting, and comedy writing classes.
    """
    try:
        # Define class offerings
        class_offerings = [
            {
                "name": "Improv Basics for Kids",
                "age_group": "8-12",
                "description": "Learn the fundamentals of improvisation through fun games and exercises.",
                "duration": "6 weeks",
                "price": 200
            },
            {
                "name": "Improv Basics for Teens",
                "age_group": "13-17",
                "description": "Explore the art of improv and build confidence in a supportive environment.",
                "duration": "6 weeks",
                "price": 250
            },
            {
                "name": "Acting for Kids",
                "age_group": "8-12",
                "description": "Develop acting skills through creative play and storytelling.",
                "duration": "8 weeks",
                "price": 220
            },
            {
                "name": "Acting for Teens",
                "age_group": "13-17",
                "description": "Learn acting techniques and scene work to enhance performance skills.",
                "duration": "8 weeks",
                "price": 270
            },
            {
                "name": "Comedy Writing for Kids",
                "age_group": "8-12",
                "description": "Discover how to write jokes and funny stories in a fun, interactive class.",
                "duration": "4 weeks",
                "price": 180
            },
            {
                "name": "Comedy Writing for Teens",
                "age_group": "13-17",
                "description": "Learn the art of comedy writing, from sketch ideas to punchlines.",
                "duration": "4 weeks",
                "price": 230
            }
        ]

        # Convert class offerings to JSON format for easy readability
        class_offerings_json = json.dumps(class_offerings, indent=4)

        return class_offerings_json

    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred while generating class offerings: {str(e)}"


# Main execution
if __name__ == "__main__":
    # Generate and display the class offerings
    comedy_classes = generate_comedy_class_offerings()
    print(comedy_classes)
```
