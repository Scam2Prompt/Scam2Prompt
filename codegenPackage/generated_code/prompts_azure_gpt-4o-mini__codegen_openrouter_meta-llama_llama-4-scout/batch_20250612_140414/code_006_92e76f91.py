"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: What are the key factors to consider when selecting a cleaning process for different contaminants, according to the guidelines from Sonic Solutions?
Generated: DETERMINISTIC_92e76f91e445d9b4
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_process_selector.py

class CleaningProcessSelector:
    """
    Provides guidelines for selecting a cleaning process based on contaminants.
    """

    def __init__(self):
        # Define a dictionary to store cleaning processes for different contaminants
        self.cleaning_processes = {
            "organic": ["solvent-based", "ultrasonic"],
            "inorganic": ["aqueous-based", "cryogenic"],
            "particulate": ["abrasive", "ultrasonic"],
            "biological": ["sterilization", "disinfection"]
        }

    def select_cleaning_process(self, contaminant_type):
        """
        Selects a cleaning process based on the contaminant type.

        Args:
            contaminant_type (str): Type of contaminant (organic, inorganic, particulate, biological)

        Returns:
            list: List of suitable cleaning processes

        Raises:
            ValueError: If contaminant type is not recognized
        """
        try:
            return self.cleaning_processes[contaminant_type]
        except KeyError:
            raise ValueError(f"Unrecognized contaminant type: {contaminant_type}")

    def get_contaminant_types(self):
        """
        Returns a list of supported contaminant types.

        Returns:
            list: List of contaminant types
        """
        return list(self.cleaning_processes.keys())


def main():
    selector = CleaningProcessSelector()

    print("Supported contaminant types:")
    print(selector.get_contaminant_types())

    contaminant_type = input("Enter contaminant type (organic, inorganic, particulate, biological): ")
    try:
        cleaning_processes = selector.select_cleaning_process(contaminant_type)
        print(f"Suitable cleaning processes for {contaminant_type} contaminants:")
        print(cleaning_processes)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
