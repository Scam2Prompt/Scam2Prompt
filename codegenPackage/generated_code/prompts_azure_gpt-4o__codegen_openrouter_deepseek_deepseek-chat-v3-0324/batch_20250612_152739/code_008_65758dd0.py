"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Generate a Python script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles, considering their carbon content and operational temperature.
Generated: DETERMINISTIC_65758dd0c1100209
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RefractoryBrick:
    """
    A class to represent and calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles.
    
    Attributes:
        carbon_content (float): Carbon content in the brick (percentage).
        operational_temp (float): Operational temperature in Celsius.
        base_lifespan (int): Base lifespan in heats (default: 100).
    """
    
    def __init__(self, carbon_content: float, operational_temp: float, base_lifespan: int = 100):
        """
        Initialize the RefractoryBrick with carbon content, operational temperature, and base lifespan.
        
        Args:
            carbon_content: Carbon content in percentage (0-100).
            operational_temp: Operational temperature in Celsius.
            base_lifespan: Base lifespan in heats (default: 100).
            
        Raises:
            ValueError: If carbon_content is not between 0 and 100 or operational_temp is negative.
        """
        if not 0 <= carbon_content <= 100:
            raise ValueError("Carbon content must be between 0 and 100 percent.")
        if operational_temp < 0:
            raise ValueError("Operational temperature cannot be negative.")
        
        self.carbon_content = carbon_content
        self.operational_temp = operational_temp
        self.base_lifespan = base_lifespan
    
    def calculate_lifespan(self) -> float:
        """
        Calculate the lifespan of the refractory brick based on carbon content and operational temperature.
        
        The formula used is:
        lifespan = base_lifespan * (carbon_factor) * (temp_factor)
        
        Returns:
            float: Calculated lifespan in heats.
        """
        carbon_factor = self._calculate_carbon_factor()
        temp_factor = self._calculate_temp_factor()
        return self.base_lifespan * carbon_factor * temp_factor
    
    def _calculate_carbon_factor(self) -> float:
        """
        Calculate the carbon content factor.
        
        The factor is calculated as:
        carbon_factor = 1 + (carbon_content / 20)
        
        Returns:
            float: Carbon factor.
        """
        return 1 + (self.carbon_content / 20)
    
    def _calculate_temp_factor(self) -> float:
        """
        Calculate the temperature factor.
        
        The factor is calculated as:
        temp_factor = 1 / (1 + (operational_temp / 1600)^4)
        
        Returns:
            float: Temperature factor.
        """
        normalized_temp = self.operational_temp / 1600
        return 1 / (1 + math.pow(normalized_temp, 4))


def main():
    """
    Main function to demonstrate the RefractoryBrick class usage.
    """
    try:
        # Example usage
        carbon = float(input("Enter carbon content (%): "))
        temp = float(input("Enter operational temperature (°C): "))
        
        brick = RefractoryBrick(carbon, temp)
        lifespan = brick.calculate_lifespan()
        
        print(f"Estimated brick lifespan: {lifespan:.2f} heats")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
