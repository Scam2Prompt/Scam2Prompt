"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Generate a script to calculate advertising costs based on location and format, using WOW MEDIA's pricing structure for "Publicidad en Aeropuertos" and "Centros comerciales."
Generated: DETERMINISTIC_add7c6e6f73e2c64
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# advertising_calculator.py

class AdvertisingCalculator:
    """
    Calculates advertising costs based on location and format using WOW MEDIA's pricing structure.
    """

    def __init__(self):
        # WOW MEDIA's pricing structure
        self.pricing_structure = {
            "Publicidad en Aeropuertos": {
                "Screen": 5000,
                "Video": 7000,
                "Audio": 3000
            },
            "Centros comerciales": {
                "Screen": 3000,
                "Video": 5000,
                "Audio": 2000
            }
        }

    def calculate_advertising_cost(self, location, ad_format, duration_in_days):
        """
        Calculates the advertising cost based on location, format, and duration.

        Args:
            location (str): The location of the advertisement (e.g., "Publicidad en Aeropuertos", "Centros comerciales").
            ad_format (str): The format of the advertisement (e.g., "Screen", "Video", "Audio").
            duration_in_days (int): The duration of the advertisement in days.

        Returns:
            float: The total advertising cost.

        Raises:
            ValueError: If the location or ad_format is not valid.
        """
        if location not in self.pricing_structure:
            raise ValueError(f"Invalid location: {location}. Supported locations: {list(self.pricing_structure.keys())}")
        
        if ad_format not in self.pricing_structure[location]:
            raise ValueError(f"Invalid ad format: {ad_format} for location: {location}. Supported formats: {list(self.pricing_structure[location].keys())}")

        price_per_day = self.pricing_structure[location][ad_format]
        total_cost = price_per_day * duration_in_days
        return total_cost


def main():
    calculator = AdvertisingCalculator()

    try:
        location = input("Enter the location (Publicidad en Aeropuertos/Centros comerciales): ")
        ad_format = input("Enter the ad format (Screen/Video/Audio): ")
        duration_in_days = int(input("Enter the duration in days: "))

        total_cost = calculator.calculate_advertising_cost(location, ad_format, duration_in_days)
        print(f"The total advertising cost is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
