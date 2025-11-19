"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Create a function that calculates the efficiency of a frozen potato processing plant, considering the use of cooling and shock freezing machines.
Generated: DETERMINISTIC_59e54650e1b705e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PotatoProcessingPlant:
    """
    A class to represent a potato processing plant and calculate its efficiency.
    
    Attributes
    ----------
    total_potatoes : int
        Total number of potatoes processed
    cooled_potatoes : int
        Number of potatoes that underwent cooling
    shock_frozen_potatoes : int
        Number of potatoes that underwent shock freezing
    """

    def __init__(self, total_potatoes, cooled_potatoes, shock_frozen_potatoes):
        """
        Initializes the PotatoProcessingPlant with the given parameters.

        Parameters
        ----------
        total_potatoes : int
            Total number of potatoes processed
        cooled_potatoes : int
            Number of potatoes that underwent cooling
        shock_frozen_potatoes : int
            Number of potatoes that underwent shock freezing
        """
        self.total_potatoes = total_potatoes
        self.cooled_potatoes = cooled_potatoes
        self.shock_frozen_potatoes = shock_frozen_potatoes

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the potato processing plant.

        Returns
        -------
        float
            The efficiency percentage of the plant, or None if inputs are invalid.
        """
        try:
            # Check for valid input values
            if self.total_potatoes <= 0:
                raise ValueError("Total potatoes must be greater than zero.")
            if self.cooled_potatoes < 0 or self.shock_frozen_potatoes < 0:
                raise ValueError("Cooled and shock frozen potatoes must be non-negative.")

            # Efficiency calculation
            processed_potatoes = self.cooled_potatoes + self.shock_frozen_potatoes
            efficiency = (processed_potatoes / self.total_potatoes) * 100
            
            return efficiency

        except ValueError as e:
            print(f"Error calculating efficiency: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create an instance of PotatoProcessingPlant
    plant = PotatoProcessingPlant(total_potatoes=1000, cooled_potatoes=800, shock_frozen_potatoes=150)
    
    # Calculate and print the efficiency
    efficiency = plant.calculate_efficiency()
    if efficiency is not None:
        print(f"Plant Efficiency: {efficiency:.2f}%")
```
