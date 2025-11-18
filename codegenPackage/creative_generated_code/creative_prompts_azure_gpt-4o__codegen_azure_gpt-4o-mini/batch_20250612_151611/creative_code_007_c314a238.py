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
import sys

class FuelInjectorDiagnosticTool:
    """A diagnostic tool to identify contamination in fuel injectors and suggest cleaning methods based on known contaminants."""

    CONTAMINANTS = {
        'carbon': 'Use a specialized fuel injector cleaning solvent and ultrasonic cleaning.',
        'varnish': 'Perform a chemical cleaning with appropriate solvent and run cleaner through fuel system.',
        'rust': 'Replace affected components and ensure the fuel tank is cleaned to prevent future contamination.',
        'dirt': 'Flush the fuel system with fuel injector cleaner and replace fuel filters.',
        'water': 'Drain contaminated fuel and replace with fresh fuel; consider using a water separator.',
        'gunk': 'Use a fuel system cleaner to dissolve the gunk and flush the system thoroughly.'
    }

    def __init__(self):
        """Initialize the diagnostic tool."""
        self.contamination_report = {}

    def diagnose(self, symptoms):
        """Diagnose the fuel injector contamination based on user symptoms.

        Args:
            symptoms (list of str): A list of symptoms reported by the user.

        Returns:
            dict: A report of identified contaminants and suggested cleaning methods.
        """
        for symptom in symptoms:
            self.contamination_report[symptom] = self.CONTAMINANTS.get(symptom.lower(), 'Unknown contaminant. Further inspection needed.')
        return self.contamination_report

    def display_report(self, report):
        """Display the diagnostic report to the user.

        Args:
            report (dict): The contamination report to display.
        """
        print("\n--- Fuel Injector Contamination Report ---")
        for symptom, suggestion in report.items():
            print(f"Symptom: {symptom.capitalize()}\nSuggestion: {suggestion}\n")

def main():
    """Main function to run the diagnostic tool."""
    print("Welcome to the Fuel Injector Diagnostic Tool.")
    print("Please enter the symptoms of contamination (comma-separated):")
    
    try:
        user_input = input().strip()
        if not user_input:
            raise ValueError("No symptoms provided.")
        
        symptoms = [symptom.strip() for symptom in user_input.split(',')]
        
        diagnostic_tool = FuelInjectorDiagnosticTool()
        report = diagnostic_tool.diagnose(symptoms)
        diagnostic_tool.display_report(report)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
