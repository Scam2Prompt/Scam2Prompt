"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write Python code to recommend airbrush stencil collections for nail art based on user preferences, using categories like "L-Stencils," "K-Stencils," and "XL-Stencils" from AirstyleArt.
Generated: DETERMINISTIC_ef3f324a676440c2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airbrush_stencil_recommender.py

class AirbrushStencilRecommender:
    """
    Recommends airbrush stencil collections for nail art based on user preferences.

    Attributes:
        stencils (dict): A dictionary of stencil categories with their descriptions.
    """

    def __init__(self):
        # Initialize stencil categories from AirstyleArt
        self.stencils = {
            "L-Stencils": [
                {"name": "L-Stencil 1", "description": "Description for L-Stencil 1"},
                {"name": "L-Stencil 2", "description": "Description for L-Stencil 2"},
            ],
            "K-Stencils": [
                {"name": "K-Stencil 1", "description": "Description for K-Stencil 1"},
                {"name": "K-Stencil 2", "description": "Description for K-Stencil 2"},
            ],
            "XL-Stencils": [
                {"name": "XL-Stencil 1", "description": "Description for XL-Stencil 1"},
                {"name": "XL-Stencil 2", "description": "Description for XL-Stencil 2"},
            ],
        }

    def get_user_preferences(self):
        """
        Gets user preferences for stencil categories and designs.

        Returns:
            dict: A dictionary of user preferences.
        """
        print("Available stencil categories:")
        for i, category in enumerate(self.stencils.keys()):
            print(f"{i+1}. {category}")

        preferences = {}
        while True:
            try:
                choice = int(input("Enter the number of your preferred category (or 0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.stencils):
                    category = list(self.stencils.keys())[choice - 1]
                    design = input(f"Enter your preferred design for {category} (e.g., floral, geometric): ")
                    preferences.setdefault(category, []).append(design)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return preferences

    def recommend_stencils(self, user_preferences):
        """
        Recommends airbrush stencil collections based on user preferences.

        Args:
            user_preferences (dict): A dictionary of user preferences.

        Returns:
            dict: A dictionary of recommended stencil collections.
        """
        recommended_stencils = {}
        for category, designs in user_preferences.items():
            matching_stencils = [stencil for stencil in self.stencils[category] if any(design in stencil["description"] for design in designs)]
            recommended_stencils[category] = matching_stencils

        return recommended_stencils

    def print_recommendations(self, recommended_stencils):
        """
        Prints the recommended stencil collections.

        Args:
            recommended_stencils (dict): A dictionary of recommended stencil collections.
        """
        if not recommended_stencils:
            print("No matching stencils found. Please try again.")
            return

        print("Recommended stencil collections:")
        for category, stencils in recommended_stencils.items():
            if stencils:
                print(f"\n{category}:")
                for stencil in stencils:
                    print(f"- {stencil['name']}: {stencil['description']}")


def main():
    try:
        recommender = AirbrushStencilRecommender()
        user_preferences = recommender.get_user_preferences()
        recommended_stencils = recommender.recommend_stencils(user_preferences)
        recommender.print_recommendations(recommended_stencils)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
