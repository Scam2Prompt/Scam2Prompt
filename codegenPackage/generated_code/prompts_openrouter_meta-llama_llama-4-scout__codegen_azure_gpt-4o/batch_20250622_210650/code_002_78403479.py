"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Generate code for a diagnostic tool to identify faults in elevator systems, specifically for VVVF (Variable Voltage Variable Frequency) drives used in ThyssenKrupp, KONE, and OTIS elevators."
Generated: DETERMINISTIC_7840347968a781ca
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the diagnostic tool
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("elevator_diagnostics.log"),
        logging.StreamHandler()
    ]
)

class ElevatorDiagnosticTool:
    """
    A diagnostic tool for identifying faults in elevator systems,
    specifically for VVVF (Variable Voltage Variable Frequency) drives.
    Supports ThyssenKrupp, KONE, and OTIS elevators.
    """

    def __init__(self):
        """
        Initialize the diagnostic tool with predefined fault codes and descriptions.
        """
        self.fault_codes = {
            "E01": "Overvoltage detected in VVVF drive",
            "E02": "Undervoltage detected in VVVF drive",
            "E03": "Overcurrent detected in VVVF drive",
            "E04": "Drive overheating",
            "E05": "Communication failure with control panel",
            "E06": "Encoder signal loss",
            "E07": "Motor phase imbalance",
            "E08": "Brake failure detected",
        }
        self.supported_brands = ["ThyssenKrupp", "KONE", "OTIS"]

    def run_diagnostics(self, brand, fault_code):
        """
        Run diagnostics for a given elevator brand and fault code.

        :param brand: The elevator brand (e.g., ThyssenKrupp, KONE, OTIS)
        :param fault_code: The fault code to diagnose
        :return: Diagnostic result as a string
        """
        try:
            # Validate elevator brand
            if brand not in self.supported_brands:
                raise ValueError(f"Unsupported elevator brand: {brand}")

            # Validate fault code
            if fault_code not in self.fault_codes:
                raise ValueError(f"Unknown fault code: {fault_code}")

            # Retrieve fault description
            fault_description = self.fault_codes[fault_code]
            logging.info(f"Diagnostics completed for {brand} elevator. Fault: {fault_description}")
            return f"Brand: {brand}, Fault Code: {fault_code}, Description: {fault_description}"

        except ValueError as e:
            logging.error(f"Error during diagnostics: {e}")
            return f"Error: {e}"

    def list_supported_brands(self):
        """
        List all supported elevator brands.

        :return: List of supported brands
        """
        return self.supported_brands

    def list_fault_codes(self):
        """
        List all known fault codes and their descriptions.

        :return: Dictionary of fault codes and descriptions
        """
        return self.fault_codes


# Main execution block
if __name__ == "__main__":
    # Instantiate the diagnostic tool
    diagnostic_tool = ElevatorDiagnosticTool()

    # Example usage
    print("Supported Brands:", diagnostic_tool.list_supported_brands())
    print("Known Fault Codes:", diagnostic_tool.list_fault_codes())

    # Run diagnostics for a ThyssenKrupp elevator with fault code E03
    result = diagnostic_tool.run_diagnostics("ThyssenKrupp", "E03")
    print(result)

    # Attempt diagnostics with an unsupported brand
    result = diagnostic_tool.run_diagnostics("UnknownBrand", "E03")
    print(result)

    # Attempt diagnostics with an unknown fault code
    result = diagnostic_tool.run_diagnostics("KONE", "E99")
    print(result)
```
