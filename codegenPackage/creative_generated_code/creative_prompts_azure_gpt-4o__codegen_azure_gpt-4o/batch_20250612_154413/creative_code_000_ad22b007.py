"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write Python code to recommend the best fabric type for yoga wear using the specifications provided by Shaoxing Eagles Textile Co., Ltd., such as "zurich 50d+40d" or "scuba 75d+30d."
Generated: DETERMINISTIC_ad22b007173f9425
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FabricRecommendationSystem:
    """
    A system to recommend the best fabric type for yoga wear based on specifications.
    """
    def __init__(self):
        # Predefined fabric types with their strengths for yoga wear
        self.fabric_database = {
            "zurich 50d+40d": "Lightweight and breathable, ideal for dynamic yoga.",
            "scuba 75d+30d": "Durable and supportive, ideal for intense yoga sessions.",
            "lycra 60d+50d": "Stretchy and comfortable, great for flexibility-oriented yoga.",
            "neoprene 70d+40d": "Moisture-resistant and insulating, good for outdoor yoga.",
        }

    def recommend_fabric(self, spec):
        """
        Recommend the best fabric type based on the given specification.
        
        Parameters:
        - spec (str): Fabric specification string, e.g., "zurich 50d+40d"
        
        Returns:
        - str: Recommendation or error message.
        """
        try:
            # Validate input format
            if not isinstance(spec, str) or not re.match(r'^[a-zA-Z]+\s\d+d\+\d+d$', spec):
                raise ValueError("Invalid specification format. Please use 'name Xd+Yd'.")

            # Normalize specification string for case-insensitivity
            spec = spec.lower()

            # Check if the fabric exists in the database
            if spec in self.fabric_database:
                return f"Recommended fabric: {self.fabric_database[spec]}"
            else:
                return "No recommendation found for the given specification. Please check the database."
        except Exception as e:
            return f"Error: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Initialize the recommendation system
    fabric_recommender = FabricRecommendationSystem()

    # User input for fabric specifications
    user_input = input("Enter fabric specification (e.g., 'zurich 50d+40d'): ").strip()
    
    # Get and display the recommendation
    recommendation = fabric_recommender.recommend_fabric(user_input)
    print(recommendation)
```
