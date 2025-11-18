"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Generate code to calculate the durability of UPVC materials based on weatherproof and anti-fungi properties, as detailed on the Dexodoor webpage.
Generated: DETERMINISTIC_90d88159c8940223
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UPVCProperties:
    """
    A class to represent the properties of UPVC materials
    and to calculate their durability based on weatherproof 
    and anti-fungi characteristics.
    """

    def __init__(self, weatherproof_rating: int, anti_fungi_rating: int):
        """
        Initializes the UPVCProperties instance with weatherproof
        and anti-fungi ratings.

        :param weatherproof_rating: An integer rating (0-10) for weatherproofing
        :param anti_fungi_rating: An integer rating (0-10) for anti-fungi properties
        """
        self.weatherproof_rating = self._validate_rating(weatherproof_rating)
        self.anti_fungi_rating = self._validate_rating(anti_fungi_rating)

    @staticmethod
    def _validate_rating(rating: int) -> int:
        """
        Validates the rating ensuring it is within the acceptable range (0-10).

        :param rating: An integer representing the rating
        :return: Validated rating
        :raises ValueError: If the rating is not in the range 0-10
        """
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")
        return rating

    def calculate_durability(self) -> float:
        """
        Calculates the durability of UPVC material based on its properties.

        The formula for durability is a weighted average of the 
        weatherproof and anti-fungi ratings.

        :return: A float representing the durability score
        """
        # Define weights for the ratings
        weatherproof_weight = 0.6
        anti_fungi_weight = 0.4

        # Calculate durability score
        durability_score = (self.weatherproof_rating * weatherproof_weight +
                            self.anti_fungi_rating * anti_fungi_weight)
        return round(durability_score, 2)

if __name__ == "__main__":
    try:
        # Example usage
        weatherproof_rating_input = int(input("Enter weatherproof rating (0-10): "))
        anti_fungi_rating_input = int(input("Enter anti-fungi rating (0-10): "))

        upvc_material = UPVCProperties(weatherproof_rating_input, anti_fungi_rating_input)
        durability = upvc_material.calculate_durability()

        print(f"The durability score of the UPVC material is: {durability}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
