"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Describe how to implement a diagnostic tool for identifying common issues with York chillers, referencing specific error codes and their meanings.
Generated: DETERMINISTIC_d46d1720dbe06c56
Batch ID: 20250612_155349
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
    handlers=[logging.FileHandler("york_chiller_diagnostics.log"), logging.StreamHandler()]
)

class YorkChillerDiagnosticTool:
    """
    A diagnostic tool for identifying common issues with York chillers.
    This tool references specific error codes and their meanings.
    """

    def __init__(self):
        # Dictionary mapping error codes to their meanings and suggested actions
        self.error_codes = {
            "E101": "High discharge pressure. Check condenser water flow and temperature.",
            "E102": "Low suction pressure. Inspect refrigerant levels and evaporator flow.",
            "E103": "Oil pressure failure. Verify oil levels and pump operation.",
            "E104": "Compressor overload. Check motor amperage and mechanical components.",
            "E105": "Sensor failure. Inspect temperature and pressure sensors.",
        }

    def diagnose(self, error_code):
        """
        Diagnose the issue based on the provided error code.

        :param error_code: str - The error code reported by the chiller.
        :return: str - Diagnosis and suggested action.
        """
        try:
            # Check if the error code exists in the dictionary
            if error_code in self.error_codes:
                logging.info(f"Diagnosing error code: {error_code}")
                return f"Error Code {error_code}: {self.error_codes[error_code]}"
            else:
                logging.warning(f"Unknown error code: {error_code}")
                return f"Error Code {error_code}: Unknown error code. Please consult the manual or contact support."
        except Exception as e:
            # Log any unexpected errors
            logging.error(f"An error occurred during diagnosis: {e}")
            return "An unexpected error occurred. Please try again."

    def list_error_codes(self):
        """
        List all known error codes and their meanings.

        :return: str - A formatted list of error codes and their descriptions.
        """
        try:
            logging.info("Listing all known error codes.")
            return "\n".join([f"{code}: {description}" for code, description in self.error_codes.items()])
        except Exception as e:
            # Log any unexpected errors
            logging.error(f"An error occurred while listing error codes: {e}")
            return "An unexpected error occurred. Please try again."


# Main function to demonstrate the diagnostic tool
def main():
    """
    Main function to interact with the YorkChillerDiagnosticTool.
    """
    try:
        # Initialize the diagnostic tool
        diagnostic_tool = YorkChillerDiagnosticTool()

        # Display all known error codes
        print("Known Error Codes:")
        print(diagnostic_tool.list_error_codes())

        # Example: Diagnose a specific error code
        error_code = input("\nEnter an error code to diagnose (e.g., E101): ").strip()
        diagnosis = diagnostic_tool.diagnose(error_code)
        print("\nDiagnosis:")
        print(diagnosis)
    except Exception as e:
        # Log any unexpected errors in the main function
        logging.error(f"An error occurred in the main function: {e}")
        print("An unexpected error occurred. Please restart the tool.")


# Entry point for the script
if __name__ == "__main__":
    main()
```
