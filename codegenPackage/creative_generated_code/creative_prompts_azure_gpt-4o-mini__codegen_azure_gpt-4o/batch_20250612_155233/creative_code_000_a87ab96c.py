"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: How can I implement a recommendation system that allows users to submit multiple recommendations and track their associated numbers?
Generated: DETERMINISTIC_a87ab96cee5c545b
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Recommendation System Implementation
------------------------------------
This script allows users to submit multiple recommendations and track their associated numbers.
It uses a dictionary to store recommendations and their counts.
"""

class RecommendationSystem:
    def __init__(self):
        """
        Initializes the RecommendationSystem with an empty dictionary to store recommendations.
        """
        self.recommendations = {}  # Key: Recommendation, Value: Count

    def add_recommendation(self, recommendation):
        """
        Adds a recommendation to the system. If it already exists, its count is incremented.

        Args:
            recommendation (str): The recommendation text provided by the user.
        """
        if not isinstance(recommendation, str):
            raise ValueError("Recommendation must be a string.")

        if recommendation.strip() == "":
            raise ValueError("Recommendation cannot be empty or blank.")

        if recommendation in self.recommendations:
            self.recommendations[recommendation] += 1  # Increment count
        else:
            self.recommendations[recommendation] = 1  # Add as new recommendation

    def get_recommendations(self):
        """
        Retrieves all recommendations with their associated counts.

        Returns:
            dict: A dictionary containing recommendations and their counts.
        """
        return self.recommendations

    def display_recommendations(self):
        """
        Displays all recommendations and their counts in a user-friendly format.
        """
        print("Recommendations & Counts:")
        if not self.recommendations:
            print("No recommendations yet.")
            return

        for recommendation, count in self.recommendations.items():
            print(f"{recommendation}: {count}")

# Example usage
if __name__ == "__main__":
    try:
        system = RecommendationSystem()
        
        # Adding sample recommendations
        system.add_recommendation("Learn Python")
        system.add_recommendation("Learn Python")  # Increment count
        system.add_recommendation("Read Clean Code")
        
        # Display the recommendations and counts
        system.display_recommendations()
    except Exception as e:
        print(f"An error occurred: {e}")
```
