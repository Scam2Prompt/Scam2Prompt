"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function to estimate the cost of installing rubber flooring for a jogging track, incorporating the pricing details and material options (e.g., EPDM, TPV Rubber) provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f7ee3a3bf5838d17
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FlooringEstimator:
    """
    A class to estimate the cost of installing rubber flooring for a jogging track.
    """

    # Pricing details per square meter for different materials
    MATERIAL_PRICES = {
        'EPDM': 50.0,  # Price per square meter for EPDM rubber
        'TPV': 60.0    # Price per square meter for TPV rubber
    }

    def __init__(self, length: float, width: float, material: str):
        """
        Initializes the FlooringEstimator with track dimensions and material type.

        :param length: Length of the jogging track in meters
        :param width: Width of the jogging track in meters
        :param material: Type of rubber flooring material ('EPDM' or 'TPV')
        """
        self.length = length
        self.width = width
        self.material = material.upper()  # Normalize material input to uppercase

    def calculate_area(self) -> float:
        """
        Calculates the area of the jogging track.

        :return: Area in square meters
        """
        return self.length * self.width

    def get_material_price(self) -> float:
        """
        Retrieves the price per square meter for the selected material.

        :return: Price per square meter
        :raises ValueError: If the material is not recognized
        """
        if self.material not in self.MATERIAL_PRICES:
            raise ValueError(f"Material '{self.material}' is not recognized. "
                             f"Choose from {list(self.MATERIAL_PRICES.keys())}.")
        return self.MATERIAL_PRICES[self.material]

    def estimate_cost(self) -> float:
        """
        Estimates the total cost of installing the rubber flooring.

        :return: Total estimated cost
        """
        area = self.calculate_area()
        price_per_square_meter = self.get_material_price()
        total_cost = area * price_per_square_meter
        return total_cost

def main():
    """
    Main function to execute the flooring cost estimation.
    """
    try:
        # Example dimensions and material
        length = 100.0  # Length of the track in meters
        width = 5.0     # Width of the track in meters
        material = 'EPDM'  # Material type

        # Create an instance of FlooringEstimator
        estimator = FlooringEstimator(length, width, material)

        # Estimate the cost
        total_cost = estimator.estimate_cost()
        print(f"The estimated cost for installing {material} flooring is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
