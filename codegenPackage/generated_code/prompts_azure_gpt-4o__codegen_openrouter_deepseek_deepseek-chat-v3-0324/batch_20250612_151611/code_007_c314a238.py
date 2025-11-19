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
import sys
from enum import Enum
from typing import Dict, List, Optional

class ContaminantType(Enum):
    """Enumeration of possible fuel injector contaminants."""
    CARBON = "Carbon deposits"
    VARNISH = "Varnish"
    GUM = "Gum"
    RUST = "Rust"
    WATER = "Water"
    DIRT = "Dirt and debris"
    SULFUR = "Sulfur deposits"

class CleaningMethod(Enum):
    """Enumeration of possible cleaning methods."""
    ULTRASONIC = "Ultrasonic cleaning"
    CHEMICAL = "Chemical cleaning"
    MANUAL = "Manual cleaning"
    FLUSHING = "Fuel system flushing"
    REPLACEMENT = "Replacement of parts"

class DiagnosticResult:
    """Class to store diagnostic results and recommended actions."""
    def __init__(self, contaminants: List[ContaminantType], methods: List[CleaningMethod]):
        self.contaminants = contaminants
        self.methods = methods

    def __str__(self) -> str:
        return (f"Detected contaminants: {', '.join([c.value for c in self.contaminants])}\n"
                f"Recommended cleaning methods: {', '.join([m.value for m in self.methods])}")

class FuelInjectorDiagnosticTool:
    """Main diagnostic tool class."""
    def __init__(self):
        self._contaminant_methods: Dict[ContaminantType, List[CleaningMethod]] = {
            ContaminantType.CARBON: [CleaningMethod.ULTRASONIC, CleaningMethod.CHEMICAL],
            ContaminantType.VARNISH: [CleaningMethod.CHEMICAL, CleaningMethod.FLUSHING],
            ContaminantType.GUM: [CleaningMethod.CHEMICAL, CleaningMethod.FLUSHING],
            ContaminantType.RUST: [CleaningMethod.ULTRASONIC, CleaningMethod.MANUAL],
            ContaminantType.WATER: [CleaningMethod.FLUSHING],
            ContaminantType.DIRT: [CleaningMethod.MANUAL, CleaningMethod.ULTRASONIC],
            ContaminantType.SULFUR: [CleaningMethod.CHEMICAL, CleaningMethod.REPLACEMENT]
        }

    def _get_user_input(self, prompt: str, options: List[str]) -> Optional[int]:
        """Helper method to get validated user input."""
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                choice = input("Enter your choice (or 'q' to quit): ").strip()
                if choice.lower() == 'q':
                    return None
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice_num - 1
                print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _identify_contaminants(self) -> Optional[List[ContaminantType]]:
        """Identify contaminants based on user input."""
        symptoms = [
            "Poor fuel economy",
            "Engine misfires",
            "Rough idle",
            "Loss of power",
            "Engine stalling",
            "Fuel odor",
            "Black smoke from exhaust"
        ]
        
        contaminant_options = [
            "Carbon deposits (black, sooty deposits)",
            "Varnish (sticky, brown deposits)",
            "Gum (thick, sticky deposits)",
            "Rust (reddish-brown particles)",
            "Water (milky fuel or phase separation)",
            "Dirt and debris (visible particles)",
            "Sulfur deposits (yellowish deposits)"
        ]
        
        print("\nSelect symptoms observed (multiple can be selected):")
        selected_symptoms = []
        for i, symptom in enumerate(symptoms, 1):
            choice = input(f"{i}. {symptom} (y/n): ").strip().lower()
            if choice == 'y':
                selected_symptoms.append(symptom)
        
        if not selected_symptoms:
            print("No symptoms selected. Cannot proceed with diagnosis.")
            return None
        
        print("\nBased on your symptoms, possible contaminants are:")
        selected_contaminants = []
        for i, contaminant in enumerate(contaminant_options, 1):
            choice = input(f"{i}. {contaminant} (y/n): ").strip().lower()
            if choice == 'y':
                selected_contaminants.append(list(ContaminantType)[i-1])
        
        return selected_contaminants if selected_contaminants else None

    def _determine_cleaning_methods(self, contaminants: List[ContaminantType]) -> List[CleaningMethod]:
        """Determine appropriate cleaning methods for identified contaminants."""
        methods = set()
        for contaminant in contaminants:
            if contaminant in self._contaminant_methods:
                methods.update(self._contaminant_methods[contaminant])
        return list(methods)

    def run_diagnostic(self) -> Optional[DiagnosticResult]:
        """Run the diagnostic process."""
        print("=== Fuel Injector Diagnostic Tool ===")
        print("This tool helps identify contaminants in fuel injectors and suggests cleaning methods.\n")
        
        contaminants = self._identify_contaminants()
        if not contaminants:
            return None
        
        methods = self._determine_cleaning_methods(contaminants)
        return DiagnosticResult(contaminants, methods)

def main():
    """Main function to run the diagnostic tool."""
    tool = FuelInjectorDiagnosticTool()
    try:
        result = tool.run_diagnostic()
        if result:
            print("\n=== Diagnostic Results ===")
            print(result)
        else:
            print("Diagnostic could not be completed.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
