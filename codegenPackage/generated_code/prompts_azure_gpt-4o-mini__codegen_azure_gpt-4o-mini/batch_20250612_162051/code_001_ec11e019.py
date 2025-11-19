"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: Write a Python function that estimates the durability of UPVC roofing tiles under various weather conditions, referencing their resistance to UV radiation and chemical corrosion.
Generated: DETERMINISTIC_ec11e0198bb87650
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UPVCRoofingTile:
    """
    A class to represent UPVC roofing tiles and estimate their durability
    under various weather conditions based on UV radiation and chemical corrosion.
    """

    def __init__(self, uv_resistance: float, chemical_resistance: float):
        """
        Initializes the UPVC roofing tile with specified resistances.

        :param uv_resistance: Resistance to UV radiation (scale 0-100)
        :param chemical_resistance: Resistance to chemical corrosion (scale 0-100)
        """
        if not (0 <= uv_resistance <= 100):
            raise ValueError("UV resistance must be between 0 and 100.")
        if not (0 <= chemical_resistance <= 100):
            raise ValueError("Chemical resistance must be between 0 and 100.")

        self.uv_resistance = uv_resistance
        self.chemical_resistance = chemical_resistance

    def estimate_durability(self, weather_conditions: dict) -> str:
        """
        Estimates the durability of the UPVC roofing tile based on weather conditions.

        :param weather_conditions: A dictionary containing weather factors
                                  such as 'uv_index' and 'chemical_exposure'.
        :return: A string indicating the estimated durability.
        """
        try:
            uv_index = weather_conditions.get('uv_index', 0)
            chemical_exposure = weather_conditions.get('chemical_exposure', 0)

            # Validate input values
            if not (0 <= uv_index <= 10):
                raise ValueError("UV index must be between 0 and 10.")
            if chemical_exposure < 0:
                raise ValueError("Chemical exposure cannot be negative.")

            # Calculate durability score
            durability_score = (self.uv_resistance * (10 - uv_index) +
                                self.chemical_resistance * (100 - chemical_exposure)) / 100

            # Determine durability category
            if durability_score > 75:
                return "Excellent durability"
            elif durability_score > 50:
                return "Good durability"
            elif durability_score > 25:
                return "Fair durability"
            else:
                return "Poor durability"

        except Exception as e:
            return f"Error estimating durability: {str(e)}"


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of UPVCRoofingTile with specific resistances
        tile = UPVCRoofingTile(uv_resistance=85, chemical_resistance=90)

        # Define weather conditions
        weather = {
            'uv_index': 7,
            'chemical_exposure': 20
        }

        # Estimate durability
        durability = tile.estimate_durability(weather)
        print(durability)

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
