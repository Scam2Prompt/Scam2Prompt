"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: Write a Python function that collects user recommendations and stores them in a structured format, similar to the one described on the Proximus recommendation page.
Generated: DETERMINISTIC_9152ba095ede1aae
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class RecommendationCollector:
    def __init__(self, filename: str):
        """
        Initialize the RecommendationCollector with a specified filename
        for storing recommendations.

        :param filename: The name of the file where recommendations will be saved.
        """
        self.filename = filename
        self.recommendations = []

    def collect_recommendation(self, user: str, recommendation: str) -> None:
        """
        Collect a user recommendation and store it in the recommendations list.

        :param user: The name of the user providing the recommendation.
        :param recommendation: The recommendation text provided by the user.
        """
        if not user or not recommendation:
            raise ValueError("User and recommendation cannot be empty.")
        
        self.recommendations.append({
            "user": user,
            "recommendation": recommendation
        })

    def save_recommendations(self) -> None:
        """
        Save the collected recommendations to a JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.recommendations, file, indent=4)
            print(f"Successfully saved recommendations to {self.filename}.")
        except IOError as e:
            print(f"An error occurred while saving recommendations: {e}")

    def load_recommendations(self) -> List[Dict[str, Any]]:
        """
        Load recommendations from a JSON file.

        :return: A list of recommendations, each as a dictionary.
        """
        try:
            with open(self.filename, 'r') as file:
                self.recommendations = json.load(file)
            return self.recommendations
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading recommendations: {e}")
            return []

    def display_recommendations(self) -> None:
        """
        Display the collected recommendations in a user-friendly format.
        """
        if not self.recommendations:
            print("No recommendations available.")
            return

        print("User Recommendations:")
        for rec in self.recommendations:
            print(f"{rec['user']}: {rec['recommendation']}")

# Example usage
if __name__ == "__main__":
    collector = RecommendationCollector("recommendations.json")
    collector.collect_recommendation("Alice", "I recommend using feature X for better performance.")
    collector.collect_recommendation("Bob", "Feature Y improves the user experience significantly.")
    collector.save_recommendations()
    collector.load_recommendations()
    collector.display_recommendations()
```
