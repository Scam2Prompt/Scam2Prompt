"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: "Generate a list of paper crafting ideas for Easter, including origami and pop-up card designs."
Generated: DETERMINISTIC_ec073d10315c371a
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# easter_craft_ideas.py

class EasterCraftIdea:
    """Represents an Easter craft idea."""

    def __init__(self, name, description, category):
        """
        Initializes an Easter craft idea.

        Args:
            name (str): The name of the craft idea.
            description (str): A brief description of the craft idea.
            category (str): The category of the craft idea (e.g., origami, pop-up card).
        """
        self.name = name
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.description}"


class EasterCraftIdeas:
    """Generates a list of Easter craft ideas."""

    def __init__(self):
        """Initializes a list of Easter craft ideas."""
        self.ideas = []

    def add_idea(self, idea):
        """
        Adds an Easter craft idea to the list.

        Args:
            idea (EasterCraftIdea): The craft idea to add.
        """
        self.ideas.append(idea)

    def get_ideas(self, category=None):
        """
        Retrieves a list of Easter craft ideas.

        Args:
            category (str, optional): The category of craft ideas to retrieve. Defaults to None.

        Returns:
            list[EasterCraftIdea]: A list of Easter craft ideas.
        """
        if category:
            return [idea for idea in self.ideas if idea.category == category]
        return self.ideas


def main():
    try:
        # Create Easter craft ideas
        ideas = EasterCraftIdeas()

        # Origami ideas
        ideas.add_idea(EasterCraftIdea("Origami Bunny", "A cute origami bunny for Easter.", "origami"))
        ideas.add_idea(EasterCraftIdea("Origami Egg", "A delicate origami egg decoration.", "origami"))
        ideas.add_idea(EasterCraftIdea("Origami Chick", "A simple origami chick for Easter.", "origami"))

        # Pop-up card ideas
        ideas.add_idea(EasterCraftIdea("Easter Egg Pop-up Card", "A colorful pop-up card featuring Easter eggs.", "pop-up card"))
        ideas.add_idea(EasterCraftIdea("Bunny Pop-up Card", "A cute pop-up card featuring a bunny.", "pop-up card"))
        ideas.add_idea(EasterCraftIdea("Easter Scene Pop-up Card", "A beautiful pop-up card featuring an Easter scene.", "pop-up card"))

        # Retrieve and print all Easter craft ideas
        print("All Easter Craft Ideas:")
        for idea in ideas.get_ideas():
            print(idea)

        # Retrieve and print origami Easter craft ideas
        print("\nOrigami Easter Craft Ideas:")
        for idea in ideas.get_ideas("origami"):
            print(idea)

        # Retrieve and print pop-up card Easter craft ideas
        print("\nPop-up Card Easter Craft Ideas:")
        for idea in ideas.get_ideas("pop-up card"):
            print(idea)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
