"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Recommend a suitable EPS densifier model for a small business, considering factors such as processing capacity, footprint, and cost-effectiveness, based on the specifications of the XT70."
Generated: DETERMINISTIC_3c98563ef38c1205
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class EPSDensifierRecommendation:
    """
    A class to recommend a suitable EPS densifier model for a small business
    based on specifications of the XT70 and user-defined requirements.
    """

    def __init__(self):
        # XT70 specifications (example values)
        self.xt70_specs = {
            "processing_capacity_kg_per_hour": 70,  # Processing capacity in kg/hour
            "footprint_m2": 2.5,                   # Footprint in square meters
            "cost_usd": 15000                      # Cost in USD
        }

        # Available models (example data)
        self.available_models = [
            {
                "model": "XT50",
                "processing_capacity_kg_per_hour": 50,
                "footprint_m2": 2.0,
                "cost_usd": 12000
            },
            {
                "model": "XT70",
                "processing_capacity_kg_per_hour": 70,
                "footprint_m2": 2.5,
                "cost_usd": 15000
            },
            {
                "model": "XT90",
                "processing_capacity_kg_per_hour": 90,
                "footprint_m2": 3.0,
                "cost_usd": 18000
            }
        ]

    def recommend_model(self, user_requirements):
        """
        Recommend a suitable EPS densifier model based on user requirements.

        Parameters:
            user_requirements (dict): A dictionary containing user-defined requirements:
                - processing_capacity_kg_per_hour (int): Desired processing capacity in kg/hour
                - footprint_m2 (float): Maximum allowable footprint in square meters
                - budget_usd (int): Maximum budget in USD

        Returns:
            dict: Recommended model details or a message indicating no suitable model found.
        """
        try:
            # Validate user requirements
            if not all(key in user_requirements for key in ["processing_capacity_kg_per_hour", "footprint_m2", "budget_usd"]):
                raise ValueError("User requirements must include 'processing_capacity_kg_per_hour', 'footprint_m2', and 'budget_usd'.")

            # Filter models based on user requirements
            suitable_models = [
                model for model in self.available_models
                if model["processing_capacity_kg_per_hour"] >= user_requirements["processing_capacity_kg_per_hour"]
                and model["footprint_m2"] <= user_requirements["footprint_m2"]
                and model["cost_usd"] <= user_requirements["budget_usd"]
            ]

            # Sort models by cost (ascending) for cost-effectiveness
            suitable_models.sort(key=lambda x: x["cost_usd"])

            # Return the most cost-effective model or a message if no model is suitable
            if suitable_models:
                return suitable_models[0]
            else:
                return {"message": "No suitable model found based on the provided requirements."}

        except Exception as e:
            # Handle unexpected errors
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Instantiate the recommendation system
    recommendation_system = EPSDensifierRecommendation()

    # Define user requirements
    user_requirements = {
        "processing_capacity_kg_per_hour": 60,  # Desired processing capacity
        "footprint_m2": 2.5,                   # Maximum allowable footprint
        "budget_usd": 14000                    # Maximum budget
    }

    # Get recommendation
    recommendation = recommendation_system.recommend_model(user_requirements)

    # Print recommendation
    print(json.dumps(recommendation, indent=4))
```
