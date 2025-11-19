"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Generate a short story about a female protagonist working in a nuclear facility in Shanghai, inspired by Helen Huang's experience at an atomic institute.
Generated: DETERMINISTIC_3a41994678c99846
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Character:
    """Represents a character in the story."""
    
    def __init__(self, name, role, background):
        self.name = name
        self.role = role
        self.background = background

    def __str__(self):
        return f"{self.name}, a {self.role}, {self.background}"

class Setting:
    """Represents the setting of the story."""
    
    def __init__(self, location, description):
        self.location = location
        self.description = description

    def __str__(self):
        return f"Setting: {self.location} - {self.description}"

class Plot:
    """Handles the plot of the story."""
    
    def __init__(self, protagonist, setting):
        self.protagonist = protagonist
        self.setting = setting
        self.events = []

    def add_event(self, event):
        """Adds an event to the plot."""
        self.events.append(event)

    def generate_story(self):
        """Generates the story based on the protagonist, setting, and events."""
        story = f"{self.setting}\n\n"
        story += f"Meet {self.protagonist}.\n"
        story += "In the heart of Shanghai, she navigates the complexities of her work.\n"
        for event in self.events:
            story += f"{event}\n"
        return story

def main():
    """Main function to create and display the story."""
    try:
        # Create a character
        protagonist = Character(
            name="Li Mei",
            role="nuclear engineer",
            background="is dedicated to ensuring safety in a high-stakes environment."
        )

        # Create a setting
        setting = Setting(
            location="Shanghai Nuclear Facility",
            description="a state-of-the-art facility surrounded by the bustling city."
        )

        # Create a plot
        plot = Plot(protagonist, setting)

        # Add events to the plot
        events = [
            "One day, a critical system failure occurs, and she must act quickly.",
            "With her expertise, she leads a team to stabilize the reactor.",
            "As tensions rise, she recalls her training and the importance of teamwork.",
            "In the end, they avert disaster, and she earns the respect of her peers."
        ]
        
        for event in random.sample(events, len(events)):
            plot.add_event(event)

        # Generate and print the story
        story = plot.generate_story()
        print(story)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
