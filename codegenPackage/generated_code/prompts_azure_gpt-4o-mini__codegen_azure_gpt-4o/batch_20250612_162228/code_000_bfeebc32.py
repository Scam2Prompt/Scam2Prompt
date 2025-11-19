"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Generate a Python script that utilizes M J Pigment & Additives' color masterbatches for plastic manufacturing, focusing on specific organic pigments like green, violet, and blue.
Generated: DETERMINISTIC_bfeebc32aa2a2186
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to simulate the utilization of M J Pigment & Additives' color masterbatches 
for plastic manufacturing, focusing on organic pigments like green, violet, and blue.

This script demonstrates the process of selecting pigments, mixing them into a 
plastic base, and calculating the final color composition. 

Note: This is a simulation and does not interact with actual manufacturing equipment.
"""

# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define a class to represent a pigment
class Pigment:
    def __init__(self, name, color_code, concentration):
        """
        Initialize a pigment object.

        :param name: Name of the pigment (e.g., "Green", "Violet", "Blue").
        :param color_code: Hexadecimal color code representing the pigment.
        :param concentration: Concentration percentage of the pigment in the masterbatch.
        """
        self.name = name
        self.color_code = color_code
        self.concentration = concentration

    def __str__(self):
        """
        Return a string representation of the pigment.
        """
        return f"{self.name} (Color Code: {self.color_code}, Concentration: {self.concentration}%)"


# Define a function to mix pigments into a plastic base
def mix_pigments(pigments, base_weight):
    """
    Mix pigments into a plastic base.

    :param pigments: List of Pigment objects to be mixed.
    :param base_weight: Weight of the plastic base in kilograms.
    :return: Dictionary containing the final composition of the mixture.
    """
    try:
        if base_weight <= 0:
            raise ValueError("Base weight must be greater than zero.")

        final_composition = {}
        total_pigment_weight = 0

        # Calculate the weight of each pigment and add to the final composition
        for pigment in pigments:
            pigment_weight = (pigment.concentration / 100) * base_weight
            final_composition[pigment.name] = {
                "Color Code": pigment.color_code,
                "Weight (kg)": round(pigment_weight, 2)
            }
            total_pigment_weight += pigment_weight

        # Add the base plastic weight to the composition
        final_composition["Plastic Base"] = {
            "Weight (kg)": round(base_weight - total_pigment_weight, 2)
        }

        return final_composition

    except Exception as e:
        logging.error(f"Error occurred while mixing pigments: {e}")
        return None


# Main function to demonstrate the script
def main():
    """
    Main function to simulate the mixing process.
    """
    try:
        # Define the pigments
        green_pigment = Pigment(name="Green", color_code="#00FF00", concentration=5)
        violet_pigment = Pigment(name="Violet", color_code="#8A2BE2", concentration=3)
        blue_pigment = Pigment(name="Blue", color_code="#0000FF", concentration=7)

        # List of pigments to be mixed
        pigments = [green_pigment, violet_pigment, blue_pigment]

        # Define the weight of the plastic base
        base_weight = 100  # in kilograms

        # Mix the pigments into the plastic base
        final_composition = mix_pigments(pigments, base_weight)

        # Display the final composition
        if final_composition:
            logging.info("Final Composition of the Mixture:")
            for component, details in final_composition.items():
                logging.info(f"{component}: {details}")

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
