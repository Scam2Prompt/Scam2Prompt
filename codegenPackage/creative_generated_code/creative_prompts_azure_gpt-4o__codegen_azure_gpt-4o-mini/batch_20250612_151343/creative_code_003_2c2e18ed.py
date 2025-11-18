"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Write a Python program to recommend baking tools from Condi Shop based on user input, such as "cake decorating tools" or "silicone spatulas."
Generated: DETERMINISTIC_2c2e18ed2bb0aef4
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BakingToolRecommender:
    """A class to recommend baking tools based on user input."""

    def __init__(self):
        """Initializes the recommender with a list of available baking tools."""
        self.tools = self.load_tools()

    def load_tools(self):
        """Loads the available baking tools from a JSON file."""
        try:
            with open('baking_tools.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: The tools data file was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The tools data file is not a valid JSON.")
            return []

    def recommend_tools(self, user_input):
        """Recommends baking tools based on the user's input.

        Args:
            user_input (str): The user's request for specific baking tools.

        Returns:
            list: A list of recommended baking tools matching the user's input.
        """
        recommendations = []
        for tool in self.tools:
            if user_input.lower() in tool['category'].lower() or user_input.lower() in tool['name'].lower():
                recommendations.append(tool)

        if not recommendations:
            print("No recommendations found for your request.")
        
        return recommendations

    def display_recommendations(self, recommendations):
        """Displays the recommended baking tools.

        Args:
            recommendations (list): A list of recommended baking tools.
        """
        if recommendations:
            print("\nRecommended Baking Tools:")
            for tool in recommendations:
                print(f"- {tool['name']} (Category: {tool['category']}, Price: ${tool['price']})")
        else:
            print("No tools to display.")

def main():
    """Main function to run the baking tool recommender program."""
    recommender = BakingToolRecommender()
    
    user_input = input("Enter your baking tool request (e.g., 'cake decorating tools', 'silicone spatulas'): ")
    
    recommendations = recommender.recommend_tools(user_input)
    recommender.display_recommendations(recommendations)

if __name__ == "__main__":
    main()
```

```json
// baking_tools.json
[
    {"name": "Silicone Spatula", "category": "Silicone Tools", "price": 5.99},
    {"name": "Piping Bags", "category": "Cake Decorating Tools", "price": 9.99},
    {"name": "Offset Spatula", "category": "Cake Decorating Tools", "price": 12.49},
    {"name": "Whisk", "category": "Mixing Tools", "price": 3.99},
    {"name": "Baking Mat", "category": "Silicone Tools", "price": 15.99}
]
```

Make sure to create a `baking_tools.json` file with the provided JSON content for the program to work correctly.
