"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a program to classify carpet types and recommend the best fit for residential rooms based on traffic flow and star ratings, as outlined in Perfect Melbourne Carpet's guidelines.
Generated: DETERMINISTIC_7a6d8fa91eec7c84
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarpetType:
    """Class representing a type of carpet."""

    def __init__(self, name, traffic_flow, star_rating, recommended_rooms):
        """
        Initialize a new carpet type.

        :param name: Name of the carpet type.
        :param traffic_flow: Expected traffic flow (low, medium, high).
        :param star_rating: Star rating of the carpet (1 to 5).
        :param recommended_rooms: List of rooms where the carpet is recommended.
        """
        self.name = name
        self.traffic_flow = traffic_flow
        self.star_rating = star_rating
        self.recommended_rooms = recommended_rooms

    def __str__(self):
        """Return a string representation of the carpet type."""
        return f"{self.name} (Traffic: {self.traffic_flow}, Rating: {self.star_rating})"


class CarpetClassifier:
    """Class to classify carpet types and recommend based on criteria."""

    def __init__(self):
        """Initialize the classifier with a list of carpet types."""
        self.carpet_types = []

    def add_carpet_type(self, carpet_type):
        """
        Add a carpet type to the classifier.

        :param carpet_type: Instance of CarpetType to add.
        """
        if not isinstance(carpet_type, CarpetType):
            raise ValueError("Expected an instance of CarpetType.")
        self.carpet_types.append(carpet_type)

    def recommend(self, room_type, expected_traffic):
        """
        Recommend carpet types based on room type and expected traffic flow.

        :param room_type: Type of the room (e.g., 'living room', 'bedroom').
        :param expected_traffic: Expected traffic flow (low, medium, high).
        :return: List of recommended carpet types.
        """
        recommendations = []

        for carpet in self.carpet_types:
            if room_type in carpet.recommended_rooms and carpet.traffic_flow == expected_traffic:
                recommendations.append(carpet)

        if not recommendations:
            raise Exception("No suitable carpet types found for the given criteria.")
        
        return recommendations


def main():
    """Main function to demonstrate carpet classification and recommendation."""
    # Create instances of CarpetType
    carpet1 = CarpetType("Plush Carpet", "low", 5, ["bedroom", "living room"])
    carpet2 = CarpetType("Berber Carpet", "medium", 4, ["living room", "hallway"])
    carpet3 = CarpetType("Frieze Carpet", "high", 3, ["hallway", "living room"])

    # Initialize the classifier
    classifier = CarpetClassifier()

    # Add carpet types to the classifier
    try:
        classifier.add_carpet_type(carpet1)
        classifier.add_carpet_type(carpet2)
        classifier.add_carpet_type(carpet3)
    except ValueError as e:
        print(f"Error adding carpet type: {e}")

    # Get recommendations
    room_type = "living room"
    expected_traffic = "medium"

    try:
        recommendations = classifier.recommend(room_type, expected_traffic)
        print("Recommended carpets:")
        for carpet in recommendations:
            print(carpet)
    except Exception as e:
        print(f"Recommendation error: {e}")


if __name__ == "__main__":
    main()
```
