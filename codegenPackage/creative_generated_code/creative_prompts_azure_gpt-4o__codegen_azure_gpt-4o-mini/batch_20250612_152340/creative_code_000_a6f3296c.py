"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to recommend Spanish language classes for foreigners based on their proficiency level, using the structure described on the "Clases de Español para Extranjeros" page of SpanishUpdate.com.
Generated: DETERMINISTIC_a6f3296c7ad0a1e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SpanishClassRecommendation:
    """
    A class to recommend Spanish language classes for foreigners based on their proficiency level.
    """

    def __init__(self):
        # Sample data simulating class recommendations based on proficiency levels.
        self.class_data = {
            "beginners": {
                "description": "Classes for absolute beginners with no prior knowledge of Spanish.",
                "duration": "12 weeks",
                "schedule": "Monday and Wednesday, 6 PM - 8 PM",
                "cost": 300
            },
            "intermediate": {
                "description": "Classes for those with basic knowledge aiming to improve their skills.",
                "duration": "8 weeks",
                "schedule": "Tuesday and Thursday, 5 PM - 7 PM",
                "cost": 250
            },
            "advanced": {
                "description": "Classes for fluent speakers looking to refine their language skills and learn advanced topics.",
                "duration": "10 weeks",
                "schedule": "Saturday, 10 AM - 1 PM",
                "cost": 350
            }
        }

    def get_class_recommendation(self, proficiency_level):
        """
        Get class recommendation based on the proficiency level provided.

        :param proficiency_level: str - The proficiency level (beginners, intermediate, advanced)
        :return: dict - Details of the recommended class or an error message
        """
        try:
            proficiency_level = proficiency_level.lower()  # Normalize input
            if proficiency_level in self.class_data:
                return {
                    "level": proficiency_level,
                    "details": self.class_data[proficiency_level]
                }
            else:
                raise ValueError("Proficiency level not recognized. Please choose from: beginners, intermediate, advanced.")
        except Exception as e:
            return {"error": str(e)}

def main():
    """
    Main function to run the class recommendation system.
    """
    recommender = SpanishClassRecommendation()
    
    # Example proficiency levels; in a real application, this could be user input.
    levels_to_test = ["beginners", "intermediate", "advanced", "expert"]
    
    for level in levels_to_test:
        recommendation = recommender.get_class_recommendation(level)
        print(json.dumps(recommendation, indent=4))

if __name__ == "__main__":
    main()
```
