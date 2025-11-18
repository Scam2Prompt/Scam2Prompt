"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Create an algorithm to recommend gloves for specific use cases, such as welding, gardening, or motorbike riding, based on the detailed categories provided by Rising Star International.
Generated: DETERMINISTIC_7c8da2f37b51cf1d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GloveRecommendation:
    def __init__(self):
        # Dictionary to hold gloves and their respective use cases
        self.glove_db = {
            'welding': {
                'material': 'Leather',
                'features': ['Heat Resistant', 'Durable', 'Puncture Resistant'],
                'brand': 'Rising Star International'
            },
            'gardening': {
                'material': 'Cotton',
                'features': ['Breathable', 'Flexible', 'Water Resistant'],
                'brand': 'Rising Star International'
            },
            'motorbike': {
                'material': 'Synthetic Leather',
                'features': ['Abrasion Resistant', 'Windproof', 'Touchscreen Compatible'],
                'brand': 'Rising Star International'
            }
        }

    def recommend_gloves(self, use_case):
        """
        Recommends gloves based on the specified use case.

        :param use_case: str - The intended use case for gloves
        :return: dict - A dictionary containing glove details
        :raises ValueError: If the use case is not valid
        """
        try:
            # Normalize the use case input to lower case for case insensitive matching
            use_case = use_case.lower()

            if use_case not in self.glove_db:
                raise ValueError(f"Invalid use case: {use_case}. Must be one of: {', '.join(self.glove_db.keys())}")

            return self.glove_db[use_case]

        except Exception as e:
            # Handle any unexpected exceptions gracefully
            print(f"Error: {str(e)}")
            return None


if __name__ == "__main__":
    # Example usage of the GloveRecommendation class
    recommender = GloveRecommendation()
    
    # List of use cases to test recommendations
    use_cases = ['welding', 'gardening', 'motorbike', 'unknown_case']

    for case in use_cases:
        result = recommender.recommend_gloves(case)
        if result:
            print(f"Recommended gloves for {case.capitalize()}: {result}")
        else:
            print(f"No recommendation could be made for {case.capitalize()}.")
```
