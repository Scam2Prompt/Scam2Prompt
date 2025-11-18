"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Generate code to calculate the load capacity of heavy-duty pipeline rollers, incorporating parameters like PU coating and multidirectional movement as mentioned on the SPM Equipment site.
Generated: DETERMINISTIC_330fe8d5fff6e391
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PipelineRoller:
    """
    A class to represent a heavy-duty pipeline roller and calculate its load capacity.
    
    Attributes:
        base_capacity (float): The base load capacity of the roller in tons.
        pu_coating_factor (float): The factor influencing the load capacity due to PU coating.
        multidirectional_factor (float): The factor influencing the load capacity due to multidirectional movement.
    """
    
    def __init__(self, base_capacity: float, pu_coating_factor: float, multidirectional_factor: float):
        """
        Initializes the PipelineRoller with base capacity and factors.

        Parameters:
            base_capacity (float): The base load capacity of the roller in tons.
            pu_coating_factor (float): The factor for PU coating effect.
            multidirectional_factor (float): The factor for multidirectional movement effect.
        """
        if base_capacity <= 0:
            raise ValueError("Base capacity must be a positive number.")
        if pu_coating_factor < 0:
            raise ValueError("PU coating factor must be non-negative.")
        if multidirectional_factor < 0:
            raise ValueError("Multidirectional movement factor must be non-negative.")
        
        self.base_capacity = base_capacity
        self.pu_coating_factor = pu_coating_factor
        self.multidirectional_factor = multidirectional_factor

    def calculate_load_capacity(self) -> float:
        """
        Calculates the total load capacity of the pipeline roller.

        Returns:
            float: The calculated load capacity in tons.
        """
        try:
            # Calculate the total load capacity considering the factors
            total_capacity = (self.base_capacity * 
                              (1 + self.pu_coating_factor) * 
                              (1 + self.multidirectional_factor))
            return total_capacity
        except Exception as e:
            raise RuntimeError(f"Error calculating load capacity: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a pipeline roller with example parameters
        roller = PipelineRoller(base_capacity=10.0, pu_coating_factor=0.2, multidirectional_factor=0.3)
        
        # Calculate and display the load capacity
        load_capacity = roller.calculate_load_capacity()
        print(f"The load capacity of the pipeline roller is: {load_capacity:.2f} tons")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
```
