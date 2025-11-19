"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a program to classify carpet types and recommend the best fit for residential rooms based on traffic flow and star ratings, as outlined in Perfect Melbourne Carpet's guidelines.
Generated: DETERMINISTIC_7a6d8fa91eec7c84
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_classifier.py

class Carpet:
    def __init__(self, name, traffic_flow_rating, star_rating):
        """
        Initialize a Carpet object.

        Args:
            name (str): Carpet name
            traffic_flow_rating (int): Traffic flow rating (1-5)
            star_rating (int): Star rating (1-5)
        """
        self.name = name
        self.traffic_flow_rating = traffic_flow_rating
        self.star_rating = star_rating

class CarpetClassifier:
    def __init__(self):
        """
        Initialize a CarpetClassifier object.
        """
        self.carpet_types = []

    def add_carpet_type(self, carpet):
        """
        Add a carpet type to the classifier.

        Args:
            carpet (Carpet): Carpet object
        """
        self.carpet_types.append(carpet)

    def classify(self, traffic_flow, star_rating):
        """
        Classify the best carpet type based on traffic flow and star ratings.

        Args:
            traffic_flow (int): Traffic flow rating (1-5)
            star_rating (int): Star rating (1-5)

        Returns:
            Carpet: Recommended carpet type
        """
        recommended_carpet = None
        max_score = 0

        for carpet in self.carpet_types:
            score = self.calculate_score(carpet, traffic_flow, star_rating)
            if score > max_score:
                max_score = score
                recommended_carpet = carpet

        return recommended_carpet

    def calculate_score(self, carpet, traffic_flow, star_rating):
        """
        Calculate a score for a carpet type based on traffic flow and star ratings.

        Args:
            carpet (Carpet): Carpet object
            traffic_flow (int): Traffic flow rating (1-5)
            star_rating (int): Star rating (1-5)

        Returns:
            int: Score
        """
        traffic_flow_diff = abs(carpet.traffic_flow_rating - traffic_flow)
        star_rating_diff = abs(carpet.star_rating - star_rating)
        return 10 - (traffic_flow_diff + star_rating_diff)

def main():
    classifier = CarpetClassifier()

    # Add carpet types based on Perfect Melbourne Carpet's guidelines
    classifier.add_carpet_type(Carpet("Low Traffic", 2, 3))
    classifier.add_carpet_type(Carpet("Medium Traffic", 4, 4))
    classifier.add_carpet_type(Carpet("High Traffic", 5, 5))

    try:
        traffic_flow = int(input("Enter traffic flow rating (1-5): "))
        star_rating = int(input("Enter star rating (1-5): "))

        if traffic_flow < 1 or traffic_flow > 5:
            raise ValueError("Traffic flow rating must be between 1 and 5")
        if star_rating < 1 or star_rating > 5:
            raise ValueError("Star rating must be between 1 and 5")

        recommended_carpet = classifier.classify(traffic_flow, star_rating)
        print(f"Recommended carpet type: {recommended_carpet.name}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
