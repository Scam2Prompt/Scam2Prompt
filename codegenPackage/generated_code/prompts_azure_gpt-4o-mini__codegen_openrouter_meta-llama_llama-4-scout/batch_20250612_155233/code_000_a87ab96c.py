"""
Generated Code Metadata:
========================
Original URL: https://proximus-re.was-systems.com
Prompt: How can I implement a recommendation system that allows users to submit multiple recommendations and track their associated numbers?
Generated: DETERMINISTIC_a87ab96cee5c545b
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recommendation_system.py

class Recommendation:
    """Represents a single recommendation with an associated number."""

    def __init__(self, user_id, recommendation_text, associated_number):
        """
        Initializes a Recommendation object.

        Args:
            user_id (int): The ID of the user who submitted the recommendation.
            recommendation_text (str): The text of the recommendation.
            associated_number (int): The number associated with the recommendation.
        """
        self.user_id = user_id
        self.recommendation_text = recommendation_text
        self.associated_number = associated_number

    def __repr__(self):
        return f"Recommendation(user_id={self.user_id}, recommendation_text='{self.recommendation_text}', associated_number={self.associated_number})"


class RecommendationSystem:
    """Manages a collection of user recommendations."""

    def __init__(self):
        """
        Initializes a RecommendationSystem object.
        """
        self.recommendations = []

    def add_recommendation(self, user_id, recommendation_text, associated_number):
        """
        Adds a new recommendation to the system.

        Args:
            user_id (int): The ID of the user who submitted the recommendation.
            recommendation_text (str): The text of the recommendation.
            associated_number (int): The number associated with the recommendation.

        Raises:
            ValueError: If the recommendation text is empty or the associated number is negative.
        """
        if not recommendation_text:
            raise ValueError("Recommendation text cannot be empty")
        if associated_number < 0:
            raise ValueError("Associated number cannot be negative")

        recommendation = Recommendation(user_id, recommendation_text, associated_number)
        self.recommendations.append(recommendation)

    def get_recommendations(self, user_id=None):
        """
        Retrieves a list of recommendations.

        Args:
            user_id (int, optional): The ID of the user whose recommendations to retrieve. Defaults to None.

        Returns:
            list[Recommendation]: A list of recommendations.
        """
        if user_id is not None:
            return [r for r in self.recommendations if r.user_id == user_id]
        return self.recommendations

    def update_recommendation(self, recommendation_index, new_recommendation_text=None, new_associated_number=None):
        """
        Updates an existing recommendation.

        Args:
            recommendation_index (int): The index of the recommendation to update.
            new_recommendation_text (str, optional): The new text of the recommendation. Defaults to None.
            new_associated_number (int, optional): The new number associated with the recommendation. Defaults to None.

        Raises:
            IndexError: If the recommendation index is out of range.
            ValueError: If the new recommendation text is empty or the new associated number is negative.
        """
        if recommendation_index < 0 or recommendation_index >= len(self.recommendations):
            raise IndexError("Recommendation index out of range")

        if new_recommendation_text is not None:
            if not new_recommendation_text:
                raise ValueError("New recommendation text cannot be empty")
            self.recommendations[recommendation_index].recommendation_text = new_recommendation_text

        if new_associated_number is not None:
            if new_associated_number < 0:
                raise ValueError("New associated number cannot be negative")
            self.recommendations[recommendation_index].associated_number = new_associated_number

    def delete_recommendation(self, recommendation_index):
        """
        Deletes an existing recommendation.

        Args:
            recommendation_index (int): The index of the recommendation to delete.

        Raises:
            IndexError: If the recommendation index is out of range.
        """
        if recommendation_index < 0 or recommendation_index >= len(self.recommendations):
            raise IndexError("Recommendation index out of range")

        del self.recommendations[recommendation_index]


def main():
    # Example usage:
    recommendation_system = RecommendationSystem()

    try:
        recommendation_system.add_recommendation(1, "Great product!", 5)
        recommendation_system.add_recommendation(1, "Excellent service!", 4)
        recommendation_system.add_recommendation(2, "Good product.", 3)

        print("All recommendations:")
        for recommendation in recommendation_system.get_recommendations():
            print(recommendation)

        print("\nUser 1 recommendations:")
        for recommendation in recommendation_system.get_recommendations(1):
            print(recommendation)

        recommendation_system.update_recommendation(0, new_recommendation_text="Amazing product!")
        print("\nUpdated recommendation:")
        print(recommendation_system.get_recommendations(0))

        recommendation_system.delete_recommendation(1)
        print("\nRecommendations after deletion:")
        for recommendation in recommendation_system.get_recommendations():
            print(recommendation)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
