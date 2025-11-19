"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a diagnostic tool using Python to identify contamination in fuel injectors and suggest cleaning methods, incorporating the contaminants mentioned on the Fuel Injector Services webpage.
Generated: DETERMINISTIC_c314a2385207ed43
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FuelInjectorDiagnosticTool:
    """
    A diagnostic tool to identify contamination in fuel injectors and suggest cleaning methods.
    """

    CONTAMINANTS = {
        "carbon": {
            "description": "Carbon deposits can accumulate in fuel injectors, affecting performance.",
            "cleaning_method": "Use a fuel injector cleaner or ultrasonic cleaning."
        },
        "rust": {
            "description": "Rust can form due to moisture in the fuel system.",
            "cleaning_method": "Replace the affected injectors and clean the fuel system."
        },
        "dirt": {
            "description": "Dirt and debris can clog fuel injectors.",
            "cleaning_method": "Use a fuel filter and clean the injectors with a specialized cleaner."
        },
        "gunk": {
            "description": "Gunk can build up from old fuel or additives.",
            "cleaning_method": "Perform a thorough cleaning with a professional service."
        }
    }

    def __init__(self):
        """
        Initializes the diagnostic tool.
        """
        self.diagnosis_results = {}

    def diagnose(self, symptoms):
        """
        Diagnoses the fuel injector contamination based on provided symptoms.

        :param symptoms: List of symptoms indicating potential contamination.
        :return: Dictionary with contamination diagnosis and suggested cleaning methods.
        """
        try:
            for symptom in symptoms:
                if symptom in self.CONTAMINANTS:
                    self.diagnosis_results[symptom] = self.CONTAMINANTS[symptom]
                else:
                    raise ValueError(f"Unknown symptom: {symptom}")

            return self.diagnosis_results

        except ValueError as e:
            print(f"Error: {e}")
            return {}

    def display_results(self):
        """
        Displays the diagnosis results in a user-friendly format.
        """
        if not self.diagnosis_results:
            print("No contamination detected or no symptoms provided.")
            return

        print("Diagnosis Results:")
        for contaminant, details in self.diagnosis_results.items():
            print(f"\nContaminant: {contaminant.capitalize()}")
            print(f"Description: {details['description']}")
            print(f"Suggested Cleaning Method: {details['cleaning_method']}")

def main():
    """
    Main function to run the diagnostic tool.
    """
    tool = FuelInjectorDiagnosticTool()
    
    # Example symptoms input (this could be replaced with user input)
    symptoms = ["carbon", "dirt", "rust"]

    # Diagnose the symptoms
    results = tool.diagnose(symptoms)

    # Display the results
    tool.display_results()

if __name__ == "__main__":
    main()
```
