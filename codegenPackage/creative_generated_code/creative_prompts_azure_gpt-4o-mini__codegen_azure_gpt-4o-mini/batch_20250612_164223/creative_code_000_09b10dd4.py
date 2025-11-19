"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Generate a Python function that recommends the best mattress firmness for back pain relief based on user input regarding their body type and sleeping posture, referencing the Spinetress medium-firm mattress guidelines.
Generated: DETERMINISTIC_09b10dd424a3d754
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MattressFirmnessRecommender:
    """
    A class to recommend mattress firmness based on user body type and sleeping posture.
    """

    def __init__(self):
        # Define firmness recommendations based on body type and sleeping posture
        self.firmness_guidelines = {
            "side": {
                "lightweight": "soft",
                "average": "medium-soft",
                "heavy": "medium-firm"
            },
            "back": {
                "lightweight": "medium-soft",
                "average": "medium-firm",
                "heavy": "firm"
            },
            "stomach": {
                "lightweight": "medium-firm",
                "average": "firm",
                "heavy": "extra-firm"
            }
        }

    def recommend_firmness(self, body_type: str, sleeping_posture: str) -> str:
        """
        Recommends the best mattress firmness based on the user's body type and sleeping posture.

        :param body_type: The body type of the user - options: "lightweight", "average", "heavy".
        :param sleeping_posture: The sleeping posture of the user - options: "side", "back", "stomach".
        :return: Recommended mattress firmness as a string.
        :raises ValueError: If an invalid body type or sleeping posture is provided.
        """
        # Validate inputs
        body_types = ["lightweight", "average", "heavy"]
        sleeping_postures = ["side", "back", "stomach"]

        if body_type not in body_types:
            raise ValueError(f"Invalid body type. Choose from: {body_types}")
        if sleeping_posture not in sleeping_postures:
            raise ValueError(f"Invalid sleeping posture. Choose from: {sleeping_postures}")

        # Get firmness recommendation
        firmness = self.firmness_guidelines[sleeping_posture][body_type]
        return f"For {body_type} individuals sleeping on their {sleeping_posture}, a {firmness} mattress is recommended."


# Example usage of the MattressFirmnessRecommender class
if __name__ == "__main__":
    recommender = MattressFirmnessRecommender()
    
    try:
        # Sample input
        body_type_input = "average"  # User-defined body type
        sleeping_posture_input = "side"  # User-defined sleeping posture
        
        # Get recommendation
        recommendation = recommender.recommend_firmness(body_type_input, sleeping_posture_input)
        print(recommendation)
    except ValueError as e:
        print(f"Error: {e}")
```
