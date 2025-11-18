"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Write a Python script to automate the generation of personalized supplement recommendations for bariatric patients based on products like "ELAN Weight Loss" and "ELAN Balance" from the PlusMedica Shop.
Generated: DETERMINISTIC_6f518a73efe3dd4f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SupplementRecommendationSystem:
    """
    A class to generate personalized supplement recommendations for bariatric patients
    based on products from the PlusMedica Shop (e.g., ELAN Weight Loss and ELAN Balance).
    """

    def __init__(self):
        """
        Constructor to initialize the recommendation system with available products.
        """
        self.products = {
            "ELAN Weight Loss": {
                "description": "Supports weight loss and improves metabolic health.",
                "recommended_for": ["Weight Loss", "Metabolism Support"],
                "key_ingredients": ["Green Tea Extract", "Chromium", "Vitamin B12"]
            },
            "ELAN Balance": {
                "description": "Promotes overall balance and well-being.",
                "recommended_for": ["General Wellness", "Digestive Health"],
                "key_ingredients": ["Probiotics", "Magnesium", "Vitamin D"]
            }
        }

    def recommend_supplements(self, patient_profile):
        """
        Generate personalized supplement recommendations based on patient profile.

        Args:
            patient_profile (dict): A dictionary containing patient information such as:
                - age (int): Patient's age
                - weight (float): Patient's weight
                - health_goals (list): List of health goals
                - dietary_restrictions (list): List of dietary restrictions
        
        Returns:
            list: A list of recommended supplements.
        """
        recommendations = []

        # Validate input
        if not isinstance(patient_profile, dict):
            raise ValueError("Patient profile must be a dictionary.")
        if "age" not in patient_profile or "weight" not in patient_profile or "health_goals" not in patient_profile:
            raise ValueError("Patient profile must include 'age', 'weight', and 'health_goals'.")

        # Match products to patient's health goals
        for product_name, product_info in self.products.items():
            # Check if product matches any of the patient's health goals
            if any(goal in product_info["recommended_for"] for goal in patient_profile["health_goals"]):
                recommendations.append({
                    "product_name": product_name,
                    "description": product_info["description"],
                    "key_ingredients": product_info["key_ingredients"]
                })

        return recommendations

    def save_recommendations_to_file(self, recommendations, filename):
        """
        Save the generated recommendations to a JSON file.

        Args:
            recommendations (list): List of recommended supplements.
            filename (str): Name of the file to save recommendations.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(recommendations, file, indent=4)
            print(f"Recommendations successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving recommendations to file: {e}")


# Example usage
if __name__ == "__main__":
    # Define a sample patient profile
    patient_profile = {
        "age": 35,
        "weight": 85.0,  # weight in kilograms
        "health_goals": ["Weight Loss", "Metabolism Support"],
        "dietary_restrictions": ["Gluten Free"]
    }

    # Instantiate the recommendation system
    recommendation_system = SupplementRecommendationSystem()

    # Generate supplement recommendations
    try:
        recommendations = recommendation_system.recommend_supplements(patient_profile)
        print("Generated Recommendations:")
        for rec in recommendations:
            print(f"- {rec['product_name']}: {rec['description']}")

        # Save recommendations to a JSON file
        recommendation_system.save_recommendations_to_file(recommendations, "recommendations.json")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
