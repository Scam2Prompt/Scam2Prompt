"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: What are some unique event design ideas for a social gathering in Bogotá, and how can they be tailored for a corporate client?
Generated: DETERMINISTIC_9c646a0e272cb8ad
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_design_ideas.py

class EventDesignIdea:
    """Represents an event design idea."""

    def __init__(self, name, description, tags):
        """
        Initializes an EventDesignIdea.

        Args:
            name (str): The name of the event design idea.
            description (str): A brief description of the event design idea.
            tags (list[str]): A list of tags associated with the event design idea.
        """
        self.name = name
        self.description = description
        self.tags = tags

class EventDesigner:
    """Provides event design ideas for social gatherings in Bogotá."""

    def __init__(self):
        """Initializes an EventDesigner."""
        self.ideas = [
            EventDesignIdea(
                "Tropical Night",
                "Transform the event space into a tropical oasis with vibrant colors, lush greenery, and exotic flowers.",
                ["outdoor", "bogota", "corporate"]
            ),
            EventDesignIdea(
                "Colombian Culture",
                "Celebrate Colombian culture with traditional music, dance, and cuisine.",
                ["cultural", "bogota", "social"]
            ),
            EventDesignIdea(
                "Modern Minimalist",
                "Create a sleek and modern atmosphere with clean lines, monochromatic colors, and industrial textures.",
                ["modern", "minimalist", "corporate"]
            ),
            EventDesignIdea(
                "Gastronomic Experience",
                "Focus on Bogotá's culinary scene with a food and wine tasting event featuring local chefs and ingredients.",
                ["foodie", "bogota", "social"]
            ),
            EventDesignIdea(
                "Sustainable Eco-Friendly",
                "Design an eco-friendly event with recycled materials, sustainable lighting, and locally sourced products.",
                ["sustainable", "eco-friendly", "corporate"]
            ),
        ]

    def get_ideas(self, tags=None):
        """
        Retrieves event design ideas.

        Args:
            tags (list[str], optional): A list of tags to filter ideas by. Defaults to None.

        Returns:
            list[EventDesignIdea]: A list of event design ideas.
        """
        if tags is None:
            return self.ideas
        else:
            return [idea for idea in self.ideas if any(tag in idea.tags for tag in tags)]

    def tailor_idea(self, idea_name, client_type):
        """
        Tailors an event design idea for a corporate client.

        Args:
            idea_name (str): The name of the event design idea.
            client_type (str): The type of client (e.g., corporate, social).

        Returns:
            EventDesignIdea: The tailored event design idea.
        """
        idea = next((idea for idea in self.ideas if idea.name == idea_name), None)
        if idea is None:
            raise ValueError("Event design idea not found")

        if client_type == "corporate":
            # Tailor the idea for a corporate client
            idea.description += " Incorporate corporate branding and messaging to create a cohesive brand experience."
        elif client_type == "social":
            # Tailor the idea for a social client
            idea.description += " Focus on creating a memorable and engaging experience for guests."

        return idea

def main():
    designer = EventDesigner()

    # Get all event design ideas
    ideas = designer.get_ideas()
    print("Event Design Ideas:")
    for idea in ideas:
        print(f"- {idea.name}: {idea.description}")

    # Get event design ideas for a corporate client in Bogotá
    corporate_ideas = designer.get_ideas(["corporate", "bogota"])
    print("\nCorporate Event Design Ideas in Bogotá:")
    for idea in corporate_ideas:
        print(f"- {idea.name}: {idea.description}")

    # Tailor an event design idea for a corporate client
    tailored_idea = designer.tailor_idea("Tropical Night", "corporate")
    print(f"\nTailored Event Design Idea: {tailored_idea.name}")
    print(tailored_idea.description)

if __name__ == "__main__":
    main()
```
