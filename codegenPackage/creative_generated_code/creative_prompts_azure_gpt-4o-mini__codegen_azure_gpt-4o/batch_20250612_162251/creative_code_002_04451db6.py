"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate a Python script that automates the selection process for BerlinerLuft's Confortcond climatizers based on room specifications.
Generated: DETERMINISTIC_04451db61ff98509
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ClimatizerSelector:
    """
    A class to automate the selection process for BerlinerLuft's Confortcond climatizers
    based on room specifications.
    """

    def __init__(self):
        """
        Initialize available climatizer models with their cooling capacities (in BTU).
        """
        self.models = {
            "Confortcond-9000": 9000,  # Suitable for small rooms
            "Confortcond-12000": 12000,  # Medium rooms
            "Confortcond-18000": 18000,  # Large rooms
            "Confortcond-24000": 24000   # Very large rooms
        }

    def calculate_cooling_capacity(self, room_area, room_height, num_occupants, sun_exposure):
        """
        Calculate the required cooling capacity (in BTU) based on room specifications.
        :param room_area: Area of the room in square meters.
        :param room_height: Height of the room in meters.
        :param num_occupants: Number of people typically present in the room.
        :param sun_exposure: Sun exposure level ('low', 'medium', 'high').
        :return: Required cooling capacity in BTU.
        """
        # Base cooling requirement (600 BTU per square meter)
        base_capacity = room_area * 600

        # Adjustment for room height (add 10% per meter above 2.5 meters)
        if room_height > 2.5:
            base_capacity *= 1 + 0.1 * (room_height - 2.5)

        # Adjustment for number of occupants (600 BTU per person)
        occupant_capacity = num_occupants * 600

        # Adjustment for sun exposure
        sun_exposure_factor = {"low": 1.0, "medium": 1.2, "high": 1.5}
        if sun_exposure not in sun_exposure_factor:
            raise ValueError("Invalid sun exposure level. Choose 'low', 'medium', or 'high'.")
        base_capacity *= sun_exposure_factor[sun_exposure]

        return math.ceil(base_capacity + occupant_capacity)

    def select_climatizer(self, required_capacity):
        """
        Select the most appropriate climatizer model based on the required cooling capacity.
        :param required_capacity: Required cooling capacity in BTU.
        :return: Recommended climatizer model.
        """
        for model, capacity in self.models.items():
            if capacity >= required_capacity:
                return model
        return None  # If no model is sufficient

def main():
    """
    Main function to interact with the user and automate the selection process.
    """
    print("Welcome to BerlinerLuft's Confortcond Climatizer Selector!")
    
    try:
        # Gather room specifications from the user
        room_area = float(input("Enter the room area in square meters: "))
        room_height = float(input("Enter the room height in meters: "))
        num_occupants = int(input("Enter the number of occupants: "))
        sun_exposure = input("Enter the sun exposure level ('low', 'medium', 'high'): ").strip().lower()

        # Instantiate the selector
        selector = ClimatizerSelector()

        # Calculate required cooling capacity
        required_capacity = selector.calculate_cooling_capacity(
            room_area, room_height, num_occupants, sun_exposure
        )
        print(f"Calculated cooling capacity required: {required_capacity} BTU")

        # Select the appropriate climatizer model
        recommended_model = selector.select_climatizer(required_capacity)
        if recommended_model:
            print(f"Recommended Climatizer Model: {recommended_model}")
        else:
            print("No available climatizer models can meet the required capacity. Please consult an expert.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
