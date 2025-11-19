"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gosonicsolutions.com
Prompt: What are the key factors to consider when selecting a cleaning process for different contaminants, according to the guidelines from Sonic Solutions?
Generated: DETERMINISTIC_92e76f91e445d9b4
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningProcessSelector:
    """
    A class to select the appropriate cleaning process based on the type of contaminant.
    """

    def __init__(self):
        # Define a dictionary that maps contaminants to their key factors
        self.contaminant_factors = {
            "oil": {
                "solvent_type": "organic solvents",
                "temperature": "ambient",
                "time": "15-30 minutes"
            },
            "dust": {
                "solvent_type": "water-based cleaners",
                "temperature": "ambient",
                "time": "5-10 minutes"
            },
            "biological": {
                "solvent_type": "bleach solution",
                "temperature": "hot",
                "time": "10-20 minutes"
            },
            "chemical": {
                "solvent_type": "neutral cleaners",
                "temperature": "room temperature",
                "time": "5-15 minutes"
            }
        }

    def get_cleaning_process(self, contaminant):
        """
        Retrieves the cleaning process based on the given contaminant.

        :param contaminant: str - The type of contaminant to clean
        :return: dict - A dictionary containing the cleaning parameters
        :raises ValueError: If the contaminant is not recognized
        """
        try:
            # Normalize contaminant string to lower case for consistent lookup
            contaminant = contaminant.lower()
            if contaminant not in self.contaminant_factors:
                raise ValueError(f"Unrecognized contaminant: {contaminant}")

            # Return the cleaning factors for the identified contaminant
            return self.contaminant_factors[contaminant]

        except ValueError as e:
            # Handle the error gracefully and inform the user
            print(e)
            return None


# Example usage
if __name__ == "__main__":
    selector = CleaningProcessSelector()
    
    # Example contaminant
    contaminant = "oil"
    
    # Fetch and display the cleaning process
    process = selector.get_cleaning_process(contaminant)
    
    if process:
        print(f"Cleaning process for '{contaminant}':")
        for key, value in process.items():
            print(f"{key.capitalize()}: {value}")
```
