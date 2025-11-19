"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: How can I implement ultrasonic cleaning for industrial parts, and what specific contaminants can it effectively remove?
Generated: DETERMINISTIC_420b0cf5aa7f049a
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for industrial parts.
    
    Attributes:
        frequency (float): The frequency of the ultrasonic waves in kHz.
        power (float): The power of the ultrasonic cleaner in Watts.
        cleaning_solution (str): The cleaning solution used in the cleaning process.
    """
    
    def __init__(self, frequency: float, power: float, cleaning_solution: str):
        """
        Initializes the UltrasonicCleaner with specified frequency, power, and cleaning solution.
        
        Parameters:
            frequency (float): Frequency in kHz.
            power (float): Power in Watts.
            cleaning_solution (str): The cleaning solution to be used.
        """
        self.frequency = frequency
        self.power = power
        self.cleaning_solution = cleaning_solution
        
    def clean_part(self, part_weight: float, cleaning_time: int) -> str:
        """
        Simulates the ultrasonic cleaning process for a given part.
        
        Parameters:
            part_weight (float): The weight of the part to be cleaned in grams.
            cleaning_time (int): The time for cleaning in seconds.
        
        Returns:
            str: A message indicating the cleaning status of the part.
        
        Raises:
            ValueError: If part_weight or cleaning_time is not positive.
        """
        if part_weight <= 0:
            raise ValueError("Part weight must be a positive value.")
        if cleaning_time <= 0:
            raise ValueError("Cleaning time must be a positive value.")
        
        # Simulated cleaning process
        print(f"Cleaning part weighing {part_weight}g using {self.cleaning_solution}...")
        print(f"Ultrasonic cleaning at {self.frequency}kHz with {self.power}W for {cleaning_time}s.")
        
        return f"Part cleaned successfully using {self.cleaning_solution}."

    def contaminants_effectively_removed(self) -> list:
        """
        Returns a list of contaminants that can be effectively removed by ultrasonic cleaning.
        
        Returns:
            list: A list of common contaminants.
        """
        return [
            "Grease",
            "Oil",
            "Dust",
            "Oxidation",
            "Resin",
            "Dirt",
            "Paint",
            "Carbon deposits"
        ]

def main():
    """Main function to demonstrate the ultrasonic cleaner functionality."""
    try:
        # Create an instance of UltrasonicCleaner
        cleaner = UltrasonicCleaner(frequency=40.0, power=300.0, cleaning_solution="Deionized Water")
        
        # Clean a part
        part_weight = 150.0  # in grams
        cleaning_time = 300  # in seconds
        
        cleaning_result = cleaner.clean_part(part_weight, cleaning_time)
        print(cleaning_result)
        
        # Get and display contaminants that can be removed
        contaminants = cleaner.contaminants_effectively_removed()
        print("Contaminants effectively removed:")
        print(", ".join(contaminants))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
