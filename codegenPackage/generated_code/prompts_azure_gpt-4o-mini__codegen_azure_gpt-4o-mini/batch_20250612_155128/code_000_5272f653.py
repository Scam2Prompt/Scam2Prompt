"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# resin_calculator.py

class CompensadoResinCalculator:
    """
    A class to calculate the amount of resin needed for producing compensados
    used in construction based on specified production techniques.
    """

    def __init__(self, wood_volume: float, resin_ratio: float):
        """
        Initializes the resin calculator with the volume of wood and resin ratio.

        :param wood_volume: Volume of wood in cubic meters (m³)
        :param resin_ratio: Ratio of resin to wood (e.g., 0.1 for 10%)
        """
        if wood_volume <= 0:
            raise ValueError("Wood volume must be greater than zero.")
        if resin_ratio < 0:
            raise ValueError("Resin ratio cannot be negative.")

        self.wood_volume = wood_volume
        self.resin_ratio = resin_ratio

    def calculate_resin_needed(self) -> float:
        """
        Calculates the amount of resin needed based on wood volume and resin ratio.

        :return: Amount of resin needed in liters
        """
        # Calculate the volume of resin needed
        resin_volume = self.wood_volume * self.resin_ratio
        
        # Convert cubic meters to liters (1 m³ = 1000 liters)
        resin_volume_liters = resin_volume * 1000
        
        return resin_volume_liters

def main():
    """
    Main function to execute the resin calculation.
    """
    try:
        # Example input values
        wood_volume = float(input("Enter the volume of wood in cubic meters (m³): "))
        resin_ratio = float(input("Enter the resin ratio (e.g., 0.1 for 10%): "))

        # Create an instance of the resin calculator
        calculator = CompensadoResinCalculator(wood_volume, resin_ratio)

        # Calculate the resin needed
        resin_needed = calculator.calculate_resin_needed()

        # Output the result
        print(f"Amount of resin needed: {resin_needed:.2f} liters")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
