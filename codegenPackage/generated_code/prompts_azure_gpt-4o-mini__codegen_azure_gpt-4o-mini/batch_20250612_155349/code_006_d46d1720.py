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
import json
import logging

# Configure logging for the diagnostic tool
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YorkChillerDiagnosticTool:
    """
    A diagnostic tool for identifying common issues with York chillers.
    This tool references specific error codes and their meanings.
    """

    def __init__(self):
        # Load error codes and their meanings from a JSON file
        self.error_codes = self.load_error_codes("error_codes.json")

    def load_error_codes(self, file_path):
        """
        Load error codes from a JSON file.

        :param file_path: Path to the JSON file containing error codes.
        :return: Dictionary of error codes and their meanings.
        """
        try:
            with open(file_path, 'r') as file:
                error_codes = json.load(file)
                logging.info("Error codes loaded successfully.")
                return error_codes
        except FileNotFoundError:
            logging.error(f"Error codes file not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the error codes file.")
            raise

    def diagnose(self, error_code):
        """
        Diagnose the issue based on the provided error code.

        :param error_code: The error code to diagnose.
        :return: A string describing the issue or an error message.
        """
        try:
            if error_code in self.error_codes:
                return f"Error Code {error_code}: {self.error_codes[error_code]}"
            else:
                return f"Error Code {error_code} not recognized."
        except Exception as e:
            logging.error(f"An error occurred during diagnosis: {e}")
            return "An error occurred during diagnosis."

def main():
    """
    Main function to run the diagnostic tool.
    """
    diagnostic_tool = YorkChillerDiagnosticTool()
    
    # Example error codes to diagnose
    test_error_codes = ["E01", "E02", "E99"]

    for code in test_error_codes:
        result = diagnostic_tool.diagnose(code)
        print(result)

if __name__ == "__main__":
    main()
```

**Note:** The `error_codes.json` file should be structured as follows for the code to work correctly:

```json
{
    "E01": "Low refrigerant pressure",
    "E02": "High refrigerant pressure",
    "E03": "Compressor failure",
    "E04": "Thermostat malfunction"
}
```
