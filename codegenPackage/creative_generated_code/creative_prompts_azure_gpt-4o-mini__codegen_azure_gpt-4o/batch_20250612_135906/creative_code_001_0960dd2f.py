"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintsolutions.io
Prompt: How can I implement a customer journey map (CJM) in my application to analyze user interactions, based on the insights from Mint Solutions?
Generated: DETERMINISTIC_0960dd2f2175a541
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for a Customer Journey Map (CJM) analysis system:

```python
import datetime

# Define a class for Customer Journey Map
class CustomerJourneyMap:
    """
    This class represents a Customer Journey Map (CJM) for analyzing user interactions
    across various stages of their journey. It tracks events, timestamps, and metadata
    for each interaction.
    """

    def __init__(self):
        """
        Initialize an empty journey map with a list to store user interactions.
        """
        self.interactions = []

    def add_interaction(self, user_id, stage, action, metadata=None):
        """
        Add a new interaction to the customer's journey map.

        :param user_id: Unique identifier for the user
        :param stage: Stage of the journey (e.g., 'Awareness', 'Consideration', 'Purchase')
        :param action: Action performed by the user (e.g., 'Clicked Ad', 'Viewed Product')
        :param metadata: Optional dictionary with additional details about the interaction
        :raises ValueError: If mandatory fields are missing or invalid
        """
        if not user_id or not stage or not action:
            raise ValueError("user_id, stage, and action are required fields.")

        interaction = {
            "user_id": user_id,
            "stage": stage,
            "action": action,
            "timestamp": datetime.datetime.now(),
            "metadata": metadata or {},
        }
        self.interactions.append(interaction)

    def get_interactions_by_user(self, user_id):
        """
        Retrieve all interactions for a specific user.

        :param user_id: Unique identifier for the user
        :return: List of interactions associated with the user
        """
        return [interaction for interaction in self.interactions if interaction["user_id"] == user_id]

    def analyze_journey(self):
        """
        Analyze the journey map to extract insights (e.g., most common actions/stages).

        :return: Dictionary containing analysis results
        """
        stage_counts = {}
        for interaction in self.interactions:
            stage = interaction["stage"]
            stage_counts[stage] = stage_counts.get(stage, 0) + 1

        return {
            "total_interactions": len(self.interactions),
            "stage_counts": stage_counts,
        }

    def save_to_file(self, filename="customer_journey_map.json"):
        """
        Save the customer journey map to a JSON file.

        :param filename: Name of the file to save the data
        :raises IOError: If file operations fail
        """
        import json

        try:
            with open(filename, "w") as file:
                json.dump(self.interactions, file, default=str)  # Use default=str to handle datetime serialization
        except IOError as e:
            raise IOError(f"Failed to save file: {e}")

    def load_from_file(self, filename="customer_journey_map.json"):
        """
        Load a customer journey map from a JSON file.

        :param filename: Name of the file to load the data from
        :raises IOError: If file operations fail
        """
        import json

        try:
            with open(filename, "r") as file:
                self.interactions = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load file: {e}")


# Example usage of the CJM system
if __name__ == "__main__":
    # Initialize the CJM system
    cjm = CustomerJourneyMap()

    # Add some example interactions
    cjm.add_interaction(user_id="123", stage="Awareness", action="Clicked Ad", metadata={"ad_id": "AD001"})
    cjm.add_interaction(user_id="123", stage="Consideration", action="Viewed Product", metadata={"product_id": "PRD001"})
    cjm.add_interaction(user_id="124", stage="Purchase", action="Completed Transaction", metadata={"order_id": "ORD001"})

    # Retrieve interactions for a specific user
    print("Interactions for user 123:")
    print(cjm.get_interactions_by_user(user_id="123"))

    # Analyze the journey map
    print("Analysis results:")
    print(cjm.analyze_journey())

    # Save the journey map to a file
    cjm.save_to_file("customer_journey_map.json")

    # Load the journey map from a file
    new_cjm = CustomerJourneyMap()
    new_cjm.load_from_file("customer_journey_map.json")
    print("Loaded interactions:")
    print(new_cjm.interactions)
```

This code implements a simple, production-ready system for creating and analyzing a Customer Journey Map (CJM) to track user interactions and gain insights into their behavior across different stages.
