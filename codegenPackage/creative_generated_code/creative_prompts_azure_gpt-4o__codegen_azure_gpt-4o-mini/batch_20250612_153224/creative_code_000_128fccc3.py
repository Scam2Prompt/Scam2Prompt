"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Write Python code to simulate the operation of a "طاحونة عمودية-LM" using parameters for grinding efficiency and material classification as described on the Sardinia Meets Azores website.
Generated: DETERMINISTIC_128fccc375e2a522
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VerticalMill:
    """
    A class to simulate the operation of a Vertical Mill (طاحونة عمودية-LM).
    The mill operates based on grinding efficiency and material classification.
    """

    def __init__(self, grinding_efficiency: float, material_classification: str):
        """
        Initializes the Vertical Mill with specified grinding efficiency and material classification.

        Parameters:
        - grinding_efficiency: A float representing the efficiency of the grinding process (0.0 to 1.0).
        - material_classification: A string representing the type of material to be processed.
        """
        if not (0.0 <= grinding_efficiency <= 1.0):
            raise ValueError("Grinding efficiency must be between 0.0 and 1.0.")
        self.grinding_efficiency = grinding_efficiency
        self.material_classification = material_classification
        self.processed_material = None

    def process_material(self, material_weight: float):
        """
        Simulates processing of a material through the vertical mill.

        Parameters:
        - material_weight: A float representing the weight of material to be processed in kilograms.

        Returns:
        - A float representing the weight of the processed material.
        """
        if material_weight <= 0:
            raise ValueError("Material weight must be a positive value.")

        # Calculate the processed material weight based on grinding efficiency
        processed_weight = material_weight * self.grinding_efficiency
        self.processed_material = processed_weight
        return processed_weight

    def get_summary(self):
        """
        Provides a summary of the mill's operation including grinding efficiency, material classification,
        and the last processed material weight.

        Returns:
        - A dictionary containing the operational parameters and processed material weight.
        """
        summary = {
            "Grinding Efficiency": self.grinding_efficiency,
            "Material Classification": self.material_classification,
            "Last Processed Material Weight": self.processed_material if self.processed_material else 0.0
        }
        return summary

def main():
    """
    Main function to demonstrate the Vertical Mill operation.
    Initializes the mill and processes some materials, handling potential errors.
    """
    try:
        # Initialize the Vertical Mill with specified parameters
        mill = VerticalMill(grinding_efficiency=0.85, material_classification="Cement")
        
        # Process a material
        weight_input = 100  # Weight of material in kilograms
        processed_weight = mill.process_material(weight_input)
        print(f"Processed {weight_input} kg of material into {processed_weight:.2f} kg.")

        # Output the operational summary
        summary = mill.get_summary()
        print("Mill Summary:", summary)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
