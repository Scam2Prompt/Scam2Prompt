"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Create an algorithm to recommend gloves for specific use cases, such as welding, gardening, or motorbike riding, based on the detailed categories provided by Rising Star International.
Generated: DETERMINISTIC_7c8da2f37b51cf1d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GloveRecommendation:
    """
    A class to recommend gloves based on specific use cases.
    """

    def __init__(self):
        # Define glove categories and their recommended use cases
        self.glove_categories = {
            "welding": {
                "material": "leather",
                "features": ["heat resistant", "puncture resistant"],
                "recommended_brands": ["Brand A", "Brand B"]
            },
            "gardening": {
                "material": "cotton",
                "features": ["breathable", "flexible"],
                "recommended_brands": ["Brand C", "Brand D"]
            },
            "motorbike_riding": {
                "material": "synthetic",
                "features": ["waterproof", "impact resistant"],
                "recommended_brands": ["Brand E", "Brand F"]
            }
        }

    def recommend_gloves(self, use_case):
        """
        Recommend gloves based on the provided use case.

        :param use_case: str - The use case for which gloves are needed.
        :return: dict - A dictionary containing glove recommendations.
        :raises ValueError: If the use case is not recognized.
        """
        try:
            # Normalize the use case to lower case for case-insensitive matching
            use_case = use_case.lower()
            if use_case not in self.glove_categories:
                raise ValueError(f"Use case '{use_case}' is not recognized. Please choose from {list(self.glove_categories.keys())}.")

            # Return the glove recommendations for the specified use case
            return {
                "use_case": use_case,
                "material": self.glove_categories[use_case]["material"],
                "features": self.glove_categories[use_case]["features"],
                "recommended_brands": self.glove_categories[use_case]["recommended_brands"]
            }

        except ValueError as e:
            # Handle the error by logging it and re-raising
            print(f"Error: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the GloveRecommendation class
    glove_recommender = GloveRecommendation()
    
    try:
        # Get recommendations for gardening gloves
        recommendations = glove_recommender.recommend_gloves("gardening")
        print(recommendations)
        
        # Get recommendations for an unrecognized use case
        recommendations = glove_recommender.recommend_gloves("unknown_use_case")
        print(recommendations)

    except Exception as e:
        print(f"An error occurred: {e}")
```
