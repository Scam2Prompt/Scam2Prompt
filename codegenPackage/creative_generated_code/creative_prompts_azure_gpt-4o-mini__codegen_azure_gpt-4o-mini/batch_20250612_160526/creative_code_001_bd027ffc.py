"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Write a Python function that recommends entertainment packages for different age groups based on the offerings from Wonderplanet.ee, focusing on their unique programs for children, teenagers, and adults.
Generated: DETERMINISTIC_bd027ffca6f70a64
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EntertainmentPackageRecommender:
    """
    A class that recommends entertainment packages based on age groups.
    """

    def __init__(self):
        """
        Initializes the recommender with predefined entertainment packages.
        """
        self.packages = {
            "children": {
                "name": "Kids Adventure Pack",
                "features": [
                    "Interactive storytelling",
                    "Educational games",
                    "Animated shows"
                ],
                "age_range": "3-12"
            },
            "teenagers": {
                "name": "Teen Vibes Pack",
                "features": [
                    "Music streaming",
                    "Gaming tournaments",
                    "Social networking events"
                ],
                "age_range": "13-19"
            },
            "adults": {
                "name": "Adult Chill Pack",
                "features": [
                    "Streaming movies and series",
                    "Fitness classes",
                    "Cooking workshops"
                ],
                "age_range": "20+"
            }
        }

    def recommend_package(self, age):
        """
        Recommends an entertainment package based on the user's age.

        :param age: The age of the user (int).
        :return: A string containing the recommended package name and features.
        :raises ValueError: If the age is not a valid integer or is negative.
        """
        # Input validation
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")

        # Determine the appropriate package based on age
        if 3 <= age <= 12:
            package = self.packages["children"]
        elif 13 <= age <= 19:
            package = self.packages["teenagers"]
        elif age >= 20:
            package = self.packages["adults"]
        else:
            return "No suitable package found for this age."

        # Format the package details for output
        package_details = (
            f"Recommended Package: {package['name']}\n"
            f"Features: {', '.join(package['features'])}\n"
            f"Age Range: {package['age_range']}"
        )
        return package_details


# Example usage:
if __name__ == "__main__":
    recommender = EntertainmentPackageRecommender()
    try:
        user_age = 15  # Example age input
        recommendation = recommender.recommend_package(user_age)
        print(recommendation)
    except ValueError as e:
        print(f"Error: {e}")
```
