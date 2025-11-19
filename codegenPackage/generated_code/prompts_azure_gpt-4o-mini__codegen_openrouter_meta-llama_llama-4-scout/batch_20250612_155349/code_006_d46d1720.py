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
# york_chiller_diagnostic_tool.py

class YorkChillerError(Exception):
    """Base class for York chiller errors."""
    pass

class YorkChillerDiagnosticTool:
    """Diagnostic tool for identifying common issues with York chillers."""

    def __init__(self):
        # Dictionary of common York chiller error codes and their meanings
        self.error_codes = {
            "A1": "Low refrigerant pressure",
            "A2": "High refrigerant pressure",
            "A3": "Low oil pressure",
            "A4": "High oil temperature",
            "E1": "Communication error between modules",
            "E2": "Invalid configuration",
            "E3": "Sensor fault",
        }

    def diagnose(self, error_code):
        """
        Diagnose the issue based on the provided error code.

        Args:
            error_code (str): The error code to diagnose.

        Returns:
            str: A description of the issue and recommended action.

        Raises:
            YorkChillerError: If the error code is not recognized.
        """
        try:
            error_meaning = self.error_codes[error_code]
            return f"Error {error_code}: {error_meaning}. Recommended action: Check the relevant system component and refer to the user manual for troubleshooting steps."
        except KeyError:
            raise YorkChillerError(f"Unrecognized error code: {error_code}")

    def run_diagnostic(self):
        """
        Run the diagnostic tool.

        Returns:
            None
        """
        print("York Chiller Diagnostic Tool")
        print("--------------------------------")

        while True:
            error_code = input("Enter the error code (or 'q' to quit): ")
            if error_code.lower() == 'q':
                break

            try:
                diagnosis = self.diagnose(error_code)
                print(diagnosis)
            except YorkChillerError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    diagnostic_tool = YorkChillerDiagnosticTool()
    diagnostic_tool.run_diagnostic()
```
