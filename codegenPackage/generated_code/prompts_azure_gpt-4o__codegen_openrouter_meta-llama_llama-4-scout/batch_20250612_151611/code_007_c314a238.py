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
# fuel_injector_diagnostic_tool.py

class FuelInjectorDiagnosticTool:
    """
    A diagnostic tool to identify contamination in fuel injectors and suggest cleaning methods.
    """

    def __init__(self):
        # Contaminants and their corresponding cleaning methods
        self.contaminants = {
            "varnish": "Use a varnish removal solvent and soak the injector for 30 minutes.",
            "gum": "Use a gum removal solvent and soak the injector for 30 minutes.",
            "dirt": "Use compressed air to blow out the debris.",
            "water": "Use a water removal solvent and dry the injector thoroughly.",
            "rust": "Use a rust removal solvent and replace the injector if necessary.",
        }

    def diagnose_contamination(self, symptoms):
        """
        Diagnose contamination based on user-provided symptoms.

        Args:
            symptoms (list): A list of symptoms observed.

        Returns:
            dict: A dictionary containing the suspected contaminants and recommended cleaning methods.
        """
        suspected_contaminants = {}

        if "poor engine performance" in symptoms or "rough idling" in symptoms:
            suspected_contaminants["varnish"] = self.contaminants["varnish"]
            suspected_contaminants["gum"] = self.contaminants["gum"]

        if "clogged injector" in symptoms or "reduced fuel flow" in symptoms:
            suspected_contaminants["dirt"] = self.contaminants["dirt"]

        if "water in fuel" in symptoms or "corrosion" in symptoms:
            suspected_contaminants["water"] = self.contaminants["water"]
            suspected_contaminants["rust"] = self.contaminants["rust"]

        return suspected_contaminants

    def suggest_cleaning_methods(self, suspected_contaminants):
        """
        Suggest cleaning methods for the suspected contaminants.

        Args:
            suspected_contaminants (dict): A dictionary containing the suspected contaminants and recommended cleaning methods.

        Returns:
            list: A list of recommended cleaning methods.
        """
        cleaning_methods = list(suspected_contaminants.values())

        return cleaning_methods


def main():
    try:
        diagnostic_tool = FuelInjectorDiagnosticTool()

        print("Fuel Injector Diagnostic Tool")
        print("--------------------------------")

        symptoms = input("Enter symptoms (comma-separated): ").split(",")

        symptoms = [symptom.strip().lower() for symptom in symptoms]

        suspected_contaminants = diagnostic_tool.diagnose_contamination(symptoms)

        if suspected_contaminants:
            print("\nSuspected Contaminants and Recommended Cleaning Methods:")
            for contaminant, method in suspected_contaminants.items():
                print(f"- {contaminant.capitalize()}: {method}")

            cleaning_methods = diagnostic_tool.suggest_cleaning_methods(suspected_contaminants)

            print("\nRecommended Cleaning Methods:")
            for i, method in enumerate(cleaning_methods, start=1):
                print(f"{i}. {method}")
        else:
            print("\nNo suspected contaminants found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
