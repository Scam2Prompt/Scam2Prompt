"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Generate a Python script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles, considering their carbon content and operational temperature.
Generated: DETERMINISTIC_65758dd0c1100209
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class MgO_C_Refractory:
    """
    A class to calculate the lifespan of MgO-C refractory bricks used in steel ladles.
    
    Attributes:
        carbon_content (float): The carbon content of the refractory brick in percentage.
        operational_temperature (float): The operational temperature in degrees Celsius.
    """

    def __init__(self, carbon_content: float, operational_temperature: float):
        """
        Initializes the MgO_C_Refractory class with carbon content and operational temperature.
        
        Args:
            carbon_content (float): The carbon content of the refractory brick.
            operational_temperature (float): The operational temperature of the steel ladle.
        """
        if not (0 <= carbon_content <= 100):
            raise ValueError("Carbon content must be between 0 and 100 percent.")
        if operational_temperature <= 0:
            raise ValueError("Operational temperature must be greater than 0 degrees Celsius.")

        self.carbon_content = carbon_content
        self.operational_temperature = operational_temperature

    def lifespan_estimation(self) -> float:
        """
        Estimates the lifespan of the MgO-C refractory brick based on carbon content and operational temperature.
        
        Returns:
            float: Estimated lifespan in hours.
        """
        # Base lifespan for the refractory without any carbon
        base_lifespan = 1000.0  # in hours, for example

        # Adjusting lifespan based on carbon content (assumption)
        carbon_factor = 0.5 * (self.carbon_content / 100)
        
        # Adjusting lifespan based on operational temperature (assumption)
        temperature_factor = 1 - (self.operational_temperature / 2000)  # assuming 2000°C is a critical temp

        # Ensuring the temperature factor does not lead to negative lifespan
        if temperature_factor < 0:
            temperature_factor = 0
        
        # Calculating final lifespan
        estimated_lifespan = base_lifespan * (1 + carbon_factor) * temperature_factor
        
        return estimated_lifespan

def main():
    """
    Main function to execute the lifespan estimation.
    """
    try:
        # Example input
        carbon_content = float(input("Enter carbon content (0-100%): "))
        operational_temperature = float(input("Enter operational temperature (°C): "))

        # Creating an instance of MgO_C_Refractory
        refractory_brick = MgO_C_Refractory(carbon_content, operational_temperature)

        # Estimating lifespan
        lifespan = refractory_brick.lifespan_estimation()
        print(f"Estimated lifespan of the MgO-C refractory brick: {lifespan:.2f} hours")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
