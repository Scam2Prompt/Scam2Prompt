"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: Generate a code snippet to calculate the thermal insulation efficiency of UPVC-ASA roofing materials based on their multi-layer structure.
Generated: DETERMINISTIC_75b60392e2f1cda8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RoofingMaterial:
    """
    A class to represent a roofing material and calculate its thermal insulation efficiency.
    """

    def __init__(self, layers):
        """
        Initializes the RoofingMaterial with a list of layers.

        :param layers: List of tuples where each tuple contains (thickness in meters, thermal conductivity in W/mK)
        """
        self.layers = layers

    def calculate_efficiency(self):
        """
        Calculates the thermal insulation efficiency based on the multi-layer structure.

        :return: Total thermal resistance (R-value) of the roofing material
        """
        try:
            total_resistance = 0.0
            
            for thickness, conductivity in self.layers:
                if thickness <= 0 or conductivity <= 0:
                    raise ValueError("Thickness and thermal conductivity must be positive values.")
                
                # Calculate the resistance for the current layer
                resistance = thickness / conductivity
                total_resistance += resistance
            
            return total_resistance
        
        except Exception as e:
            print(f"Error calculating efficiency: {e}")
            return None

def main():
    """
    Main function to demonstrate the calculation of thermal insulation efficiency.
    """
    # Example layers: (thickness in meters, thermal conductivity in W/mK)
    layers = [
        (0.05, 0.15),  # Layer 1
        (0.10, 0.10),  # Layer 2
        (0.02, 0.20)   # Layer 3
    ]

    # Create a RoofingMaterial instance
    roofing_material = RoofingMaterial(layers)

    # Calculate and print the thermal insulation efficiency
    efficiency = roofing_material.calculate_efficiency()
    if efficiency is not None:
        print(f"Total Thermal Resistance (R-value): {efficiency:.2f} m²K/W")

if __name__ == "__main__":
    main()
```
