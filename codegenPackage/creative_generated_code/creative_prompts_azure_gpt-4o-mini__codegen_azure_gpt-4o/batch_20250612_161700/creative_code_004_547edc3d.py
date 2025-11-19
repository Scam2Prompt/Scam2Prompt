"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Write a code example that demonstrates how to integrate personal protective equipment (PPE) recommendations into a training application, based on insights from Blue Training Academy.
Generated: DETERMINISTIC_547edc3d7f4c1241
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class PPERecommendationSystem:
    """
    A class to integrate PPE recommendations into a training application
    based on insights from Blue Training Academy.
    """

    def __init__(self, recommendations_file="ppe_recommendations.json"):
        """
        Initializes the PPERecommendationSystem with a data file containing recommendations.

        :param recommendations_file: Path to the JSON file containing PPE recommendations.
        """
        self.recommendations_file = recommendations_file
        self.recommendations = self.load_recommendations()

    def load_recommendations(self):
        """
        Loads PPE recommendations from a JSON file.

        :return: A dictionary containing PPE recommendations.
        """
        try:
            with open(self.recommendations_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.recommendations_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in '{self.recommendations_file}'.")
            return {}

    def get_recommendation(self, training_type):
        """
        Provides PPE recommendation for a given training type.

        :param training_type: Type of training (e.g., 'construction', 'firefighting').
        :return: Recommended PPE items as a list, or None if the training type is not found.
        """
        return self.recommendations.get(training_type, None)

    def display_recommendation(self, training_type):
        """
        Displays PPE recommendation for a given training type.

        :param training_type: Type of training (e.g., 'construction', 'firefighting').
        """
        recommendation = self.get_recommendation(training_type)
        if recommendation:
            print(f"PPE Recommended for '{training_type}' Training:")
            for item in recommendation:
                print(f" - {item}")
        else:
            print(f"No PPE recommendation found for '{training_type}' training.")


# Example Usage
if __name__ == "__main__":
    # Create an instance of the PPERecommendationSystem
    ppe_system = PPERecommendationSystem()

    # Prompt user for a training type
    training_type = input("Enter training type (e.g., 'construction', 'firefighting'): ").strip()

    # Display the PPE recommendations for the specified training type
    ppe_system.display_recommendation(training_type)

# Example JSON file structure (`ppe_recommendations.json`):
# {
#     "construction": ["Hard hat", "Safety goggles", "Steel-toe boots", "High-visibility vest"],
#     "firefighting": ["Fire-resistant suit", "Helmet", "Gloves", "Boots", "Breathing apparatus"],
#     "medical": ["Face mask", "Gloves", "Scrubs", "Eye protection"]
# }
```
