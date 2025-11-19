"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Generate a list of potential activity programming ideas for aging services, as discussed by MN SWAP.
Generated: DETERMINISTIC_af4bb61395b5673e
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# activity_ideas.py

class ActivityIdea:
    """Represents a potential activity programming idea for aging services."""

    def __init__(self, title, description, category, duration):
        """
        Initializes an ActivityIdea object.

        Args:
            title (str): The title of the activity idea.
            description (str): A brief description of the activity idea.
            category (str): The category of the activity idea (e.g., "Social", "Physical", etc.).
            duration (int): The estimated duration of the activity idea in minutes.
        """
        self.title = title
        self.description = description
        self.category = category
        self.duration = duration

    def __str__(self):
        return f"{self.title}: {self.description} ({self.category}, {self.duration} minutes)"


class ActivityIdeaGenerator:
    """Generates a list of potential activity programming ideas for aging services."""

    def __init__(self):
        self.activity_ideas = []

    def generate_ideas(self):
        """
        Generates a list of potential activity programming ideas for aging services.

        Returns:
            list[ActivityIdea]: A list of ActivityIdea objects.
        """
        # Ideas discussed by MN SWAP
        ideas = [
            {"title": "Mindfulness Meditation", "description": "Guided meditation session", "category": "Wellness", "duration": 30},
            {"title": "Chair Yoga", "description": "Modified yoga session using chairs", "category": "Physical", "duration": 45},
            {"title": "Bingo Night", "description": "Classic bingo game with prizes", "category": "Social", "duration": 60},
            {"title": "Art Therapy", "description": "Creative art session with guided prompts", "category": "Cognitive", "duration": 90},
            {"title": "Walking Club", "description": "Short walk around the facility or neighborhood", "category": "Physical", "duration": 60},
            {"title": "Trivia Night", "description": "General knowledge trivia game with teams", "category": "Social", "duration": 75},
            {"title": "Gardening Club", "description": "Planting and maintaining a small garden", "category": "Physical", "duration": 90},
            {"title": "Music Therapy", "description": "Interactive music session with singing and instruments", "category": "Cognitive", "duration": 45},
            {"title": "Cooking Class", "description": "Hands-on cooking class with healthy recipes", "category": "Cognitive", "duration": 90},
            {"title": "Storytelling Session", "description": "Sharing life stories and experiences", "category": "Social", "duration": 60},
        ]

        for idea in ideas:
            self.activity_ideas.append(ActivityIdea(**idea))

        return self.activity_ideas


def main():
    try:
        generator = ActivityIdeaGenerator()
        activity_ideas = generator.generate_ideas()

        print("Potential Activity Programming Ideas:")
        for i, idea in enumerate(activity_ideas, start=1):
            print(f"{i}. {idea}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
