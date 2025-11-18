"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Write Python code to calculate the load capacity of anchors based on specifications provided by Apeanchor™ products from CM-Canada's construction materials catalog.
Generated: DETERMINISTIC_94222cc063203834
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Anchor:
    def __init__(self, type: str, diameter: float, material: str, load_capacity: float):
        """
        Initializes an Anchor object with the given specifications.

        :param type: The type of the anchor (e.g., 'screw', 'expansion').
        :param diameter: The diameter of the anchor in millimeters.
        :param material: The material from which the anchor is made (e.g., 'steel', 'plastic').
        :param load_capacity: The nominal load capacity of the anchor in kilograms.
        """
        self.type = type
        self.diameter = diameter  # in mm
        self.material = material
        self.load_capacity = load_capacity  # in kg

    def calculate_load_capacity(self, safety_factor: float) -> float:
        """
        Calculates the safe load capacity of the anchor based on a safety factor.

        :param safety_factor: The safety factor to apply (e.g., 1.5, 2.0).
        :return: The adjusted load capacity in kilograms.
        :raises ValueError: If the safety factor is less than or equal to zero.
        """
        if safety_factor <= 0:
            raise ValueError("Safety factor must be greater than zero.")
        
        return self.load_capacity / safety_factor

    def __str__(self) -> str:
        """
        Returns a string representation of the anchor's specifications.

        :return: A string describing the anchor.
        """
        return (f"Anchor Type: {self.type}\n"
                f"Diameter: {self.diameter} mm\n"
                f"Material: {self.material}\n"
                f"Nominal Load Capacity: {self.load_capacity} kg")


def main():
    """
    Main function to demonstrate the Anchor class functionality.
    """
    try:
        # Example specifications for a CM-Canada's Apeanchor™ product
        anchor = Anchor(type='screw', diameter=10, material='steel', load_capacity=200)

        print(anchor)
        
        # Calculate safe load capacity with a safety factor of 2.0
        safety_factor = 2.0
        safe_capacity = anchor.calculate_load_capacity(safety_factor)
        
        print(f"Safe Load Capacity (with safety factor of {safety_factor}): {safe_capacity:.2f} kg")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
