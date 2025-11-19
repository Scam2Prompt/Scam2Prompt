"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Develop a Python script to calculate the weight and portability of Engel UltraLite coolers based on their advanced insulation and lightweight design.
Generated: DETERMINISTIC_6e8451db6edd7665
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EngelUltraLiteCooler:
    """
    A class to represent an Engel UltraLite cooler and calculate its weight and portability.
    """

    def __init__(self, capacity_liters, insulation_thickness_cm):
        """
        Initializes the EngelUltraLiteCooler with capacity and insulation thickness.

        :param capacity_liters: Capacity of the cooler in liters.
        :param insulation_thickness_cm: Thickness of the insulation in centimeters.
        """
        self.capacity_liters = capacity_liters
        self.insulation_thickness_cm = insulation_thickness_cm
        self.weight_kg = self.calculate_weight()
        self.portability_score = self.calculate_portability()

    def calculate_weight(self):
        """
        Calculates the weight of the cooler based on its capacity and insulation thickness.

        :return: Weight of the cooler in kilograms.
        """
        # Base weight for the cooler (in kg)
        base_weight = 1.5  
        # Weight contribution from capacity (0.2 kg per liter)
        capacity_weight = self.capacity_liters * 0.2  
        # Weight contribution from insulation (0.1 kg per cm of insulation)
        insulation_weight = self.insulation_thickness_cm * 0.1  
        
        total_weight = base_weight + capacity_weight + insulation_weight
        return round(total_weight, 2)

    def calculate_portability(self):
        """
        Calculates the portability score of the cooler based on its weight.

        :return: Portability score (higher is better).
        """
        # Portability score is inversely related to weight
        if self.weight_kg <= 0:
            raise ValueError("Weight must be greater than zero for portability calculation.")
        
        # A simple formula for portability score
        portability_score = max(0, 10 - self.weight_kg)
        return round(portability_score, 2)

    def display_info(self):
        """
        Displays the cooler's information including weight and portability score.
        """
        print(f"Engel UltraLite Cooler Info:")
        print(f"Capacity: {self.capacity_liters} liters")
        print(f"Insulation Thickness: {self.insulation_thickness_cm} cm")
        print(f"Weight: {self.weight_kg} kg")
        print(f"Portability Score: {self.portability_score}")

def main():
    """
    Main function to create an Engel UltraLite cooler and display its information.
    """
    try:
        # Example cooler parameters
        capacity = 30  # in liters
        insulation_thickness = 5  # in cm

        # Create an instance of EngelUltraLiteCooler
        cooler = EngelUltraLiteCooler(capacity, insulation_thickness)
        # Display cooler information
        cooler.display_info()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
