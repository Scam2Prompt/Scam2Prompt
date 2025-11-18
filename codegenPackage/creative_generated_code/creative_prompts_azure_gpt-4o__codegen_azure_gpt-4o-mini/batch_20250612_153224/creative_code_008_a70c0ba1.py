"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Write a script to generate personalized "Linguagem do Amor" recommendations based on user input, as described in Sabrina Alves' program.
Generated: DETERMINISTIC_a70c0ba19a29f01a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LoveLanguageRecommendation:
    """
    A class to generate personalized recommendations for 'Linguagem do Amor'.
    """

    def __init__(self):
        # Define love languages and their descriptions
        self.love_languages = {
            "Words of Affirmation": "Expressing love through words of praise and appreciation.",
            "Acts of Service": "Showing love through actions that help your partner.",
            "Receiving Gifts": "Giving thoughtful gifts to show love and appreciation.",
            "Quality Time": "Spending meaningful time together to strengthen the bond.",
            "Physical Touch": "Expressing love through physical affection."
        }

    def get_user_input(self):
        """
        Get user preferences for love languages.
        """
        print("Please enter your top 3 love languages from the following options:")
        for idx, language in enumerate(self.love_languages.keys(), start=1):
            print(f"{idx}. {language}")

        user_input = input("Enter the numbers (comma-separated): ")
        return user_input

    def validate_input(self, user_input):
        """
        Validate the user input to ensure it contains valid selections.
        """
        try:
            indices = list(map(int, user_input.split(',')))
            if all(1 <= index <= len(self.love_languages) for index in indices):
                return indices
            else:
                raise ValueError("Invalid numbers entered.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
            return None

    def generate_recommendations(self, indices):
        """
        Generate love language recommendations based on validated user input.
        """
        recommendations = []
        for index in indices:
            language = list(self.love_languages.keys())[index - 1]
            recommendations.append({
                "language": language,
                "description": self.love_languages[language]
            })
        return recommendations

    def display_recommendations(self, recommendations):
        """
        Display the recommendations in a user-friendly format.
        """
        print("\nYour Personalized Love Language Recommendations:")
        for recommendation in recommendations:
            print(f"- {recommendation['language']}: {recommendation['description']}")

    def run(self):
        """
        Execute the recommendation program.
        """
        user_input = self.get_user_input()
        indices = self.validate_input(user_input)
        if indices:
            recommendations = self.generate_recommendations(indices)
            self.display_recommendations(recommendations)

if __name__ == '__main__':
    try:
        love_language_recommender = LoveLanguageRecommendation()
        love_language_recommender.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This script can be run in any standard Python environment and will prompt the user for their preferences regarding love languages, validate the input, and display personalized recommendations based on their selections.
