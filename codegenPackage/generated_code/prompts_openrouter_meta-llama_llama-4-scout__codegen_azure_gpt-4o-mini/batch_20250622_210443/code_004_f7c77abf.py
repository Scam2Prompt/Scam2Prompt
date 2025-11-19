"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Write a code snippet in a programming language of your choice to create a simple aromatherapy product recommendation system based on user input (e.g., stress relief, sleep improvement).
Generated: DETERMINISTIC_f7c77abfed088c80
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aromatherapy_recommendation.py

class AromatherapyRecommendation:
    def __init__(self):
        # Define a dictionary to hold essential oils and their benefits
        self.oils = {
            "Lavender": ["sleep improvement", "stress relief"],
            "Peppermint": ["energy boost", "focus enhancement"],
            "Eucalyptus": ["respiratory support", "stress relief"],
            "Chamomile": ["sleep improvement", "anxiety reduction"],
            "Bergamot": ["stress relief", "mood enhancement"],
            "Lemon": ["energy boost", "focus enhancement"],
        }

    def get_recommendations(self, user_input):
        """
        Get essential oil recommendations based on user input.

        :param user_input: A string representing the user's desired benefit.
        :return: A list of recommended essential oils.
        """
        # Normalize user input to lower case for case-insensitive matching
        user_input = user_input.lower()
        recommendations = []

        # Iterate through the oils dictionary to find matches
        for oil, benefits in self.oils.items():
            if user_input in benefits:
                recommendations.append(oil)

        # Handle case where no recommendations are found
        if not recommendations:
            raise ValueError("No essential oils found for the specified benefit.")

        return recommendations


def main():
    # Create an instance of the recommendation system
    recommendation_system = AromatherapyRecommendation()

    # Get user input
    user_input = input("Enter the benefit you are looking for (e.g., stress relief, sleep improvement): ")

    try:
        # Get and display recommendations
        recommended_oils = recommendation_system.get_recommendations(user_input)
        print("Recommended essential oils for '{}':".format(user_input))
        for oil in recommended_oils:
            print(f"- {oil}")
    except ValueError as e:
        # Handle errors gracefully
        print(e)


if __name__ == "__main__":
    main()
```
