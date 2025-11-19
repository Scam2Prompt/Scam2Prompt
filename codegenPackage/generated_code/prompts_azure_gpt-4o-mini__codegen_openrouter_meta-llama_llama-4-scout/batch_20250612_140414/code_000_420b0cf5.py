"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: How can I implement ultrasonic cleaning for industrial parts, and what specific contaminants can it effectively remove?
Generated: DETERMINISTIC_420b0cf5aa7f049a
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ultrasonic Cleaning Simulator

This script simulates the ultrasonic cleaning process for industrial parts.
It identifies the contaminants that can be effectively removed using this process.
"""

class UltrasonicCleaning:
    def __init__(self, frequency, power, temperature):
        """
        Initializes the ultrasonic cleaning process.

        Args:
            frequency (float): Frequency of the ultrasonic waves in kHz.
            power (float): Power of the ultrasonic waves in watts.
            temperature (float): Temperature of the cleaning solution in Celsius.
        """
        self.frequency = frequency
        self.power = power
        self.temperature = temperature

    def clean(self, contaminants):
        """
        Simulates the ultrasonic cleaning process.

        Args:
            contaminants (list): List of contaminants to be removed.

        Returns:
            list: List of contaminants that can be effectively removed.
        """
        removable_contaminants = {
            "grease": True,
            "oil": True,
            "dirt": True,
            "metal_shavings": True,
            "organic_materials": True,
            "inorganic_materials": False,
            "radioactive_materials": False,
            "highly_adhesive_materials": False
        }

        effective_removal = []
        for contaminant in contaminants:
            if contaminant in removable_contaminants and removable_contaminants[contaminant]:
                effective_removal.append(contaminant)

        return effective_removal


def main():
    try:
        # Initialize the ultrasonic cleaning process
        cleaning_process = UltrasonicCleaning(frequency=40.0, power=1000.0, temperature=50.0)

        # Define the contaminants to be removed
        contaminants = ["grease", "oil", "dirt", "metal_shavings", "organic_materials", "inorganic_materials"]

        # Simulate the ultrasonic cleaning process
        removable_contaminants = cleaning_process.clean(contaminants)

        # Print the results
        print("Removable contaminants:")
        for contaminant in removable_contaminants:
            print(f"- {contaminant}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
