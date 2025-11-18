"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a diagnostic tool using Python to identify contamination in fuel injectors and suggest cleaning methods, incorporating the contaminants mentioned on the Fuel Injector Services webpage.
Generated: DETERMINISTIC_c314a2385207ed43
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FuelInjectorDiagnosticTool:
    """
    A tool to diagnose contamination in fuel injectors and suggest cleaning methods.
    """

    def __init__(self):
        self.contaminants = {
            "Carbon Deposits": "Use a professional-grade fuel injector cleaner to dissolve carbon buildup.",
            "Rust Particles": "Flush the fuel injector with a specialized cleaning solution to remove rust debris.",
            "Dirt or Debris": "Perform ultrasonic cleaning to dislodge dirt and debris.",
            "Water Contamination": "Use isopropyl alcohol-based cleaning agents to remove water contamination.",
            "Fuel Additive Residue": "Run the system with high-quality fuel to flush out residues and additives."
        }

    def diagnose_contamination(self):
        """
        Diagnose contaminant type in the fuel injector.

        Returns:
            str: Name of the contaminant detected.
        """
        # Randomly simulate detected contaminant for demonstration purposes
        contaminant = random.choice(list(self.contaminants.keys()))
        return contaminant

    def suggest_cleaning_method(self, contaminant):
        """
        Suggest cleaning methods based on the detected contaminant.

        Args:
            contaminant (str): Name of the contaminant.

        Returns:
            str: Cleaning method suggestion.
        """
        # Retrieve cleaning method for the given contaminant
        return self.contaminants.get(contaminant, "Contaminant not recognized. Consult a professional.")

    def run_diagnostic(self):
        """
        Perform the diagnostic and provide a cleaning method suggestion.
        """
        try:
            print("Running diagnostic...")
            # Diagnose the contaminant
            contaminant = self.diagnose_contamination()
            print(f"Contaminant Detected: {contaminant}")
            
            # Suggest cleaning method
            cleaning_method = self.suggest_cleaning_method(contaminant)
            print(f"Cleaning Suggestion: {cleaning_method}")

        except Exception as e:
            # Handle any unexpected errors gracefully
            print(f"An error occurred during diagnostic: {str(e)}")


if __name__ == "__main__":
    # Create an instance of the diagnostic tool
    diagnostic_tool = FuelInjectorDiagnosticTool()
    
    # Run the diagnostic
    diagnostic_tool.run_diagnostic()
```
