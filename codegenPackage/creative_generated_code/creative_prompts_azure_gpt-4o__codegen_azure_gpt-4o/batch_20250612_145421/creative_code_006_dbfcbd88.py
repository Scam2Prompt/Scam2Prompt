"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate a Python script to automate the selection process for ventilators and exhaustors using updated software like Ventowin, as described by BerlinerLuft.
Generated: DETERMINISTIC_dbfcbd883662afaa
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys


class VentilationSelectionAutomation:
    """
    Automates the selection process for ventilators and exhaustors using Ventowin software.
    """

    def __init__(self, ventowin_path, input_file, output_file):
        """
        Initializes the automation script with required parameters.

        :param ventowin_path: Path to the Ventowin executable file.
        :param input_file: Path to the input file containing selection criteria.
        :param output_file: Path to the output file where results will be saved.
        """
        self.ventowin_path = ventowin_path
        self.input_file = input_file
        self.output_file = output_file

    def validate_paths(self):
        """
        Validates if the required files and paths exist.
        """
        if not os.path.isfile(self.ventowin_path):
            raise FileNotFoundError(f"Ventowin executable not found at: {self.ventowin_path}")
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"Input file not found at: {self.input_file}")
        if not os.access(os.path.dirname(self.output_file) or ".", os.W_OK):
            raise PermissionError(f"Cannot write to the specified output directory: {os.path.dirname(self.output_file)}")

    def run_ventowin(self):
        """
        Executes the Ventowin software with the provided input and output files.

        :raises RuntimeError: If the Ventowin execution fails.
        """
        try:
            # Construct the command to run Ventowin
            command = [self.ventowin_path, "-input", self.input_file, "-output", self.output_file]

            # Run the command using subprocess
            result = subprocess.run(command, capture_output=True, text=True)

            # Check for errors in execution
            if result.returncode != 0:
                raise RuntimeError(f"Ventowin execution failed: {result.stderr}")

            print("Ventowin executed successfully!")
            print(f"Output saved to: {self.output_file}")

        except Exception as e:
            raise RuntimeError(f"An error occurred during Ventowin execution: {str(e)}")

    def automate(self):
        """
        Orchestrates the entire automation process.
        """
        try:
            print("Validating paths...")
            self.validate_paths()

            print("Running Ventowin software...")
            self.run_ventowin()

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


# Main entry point of the script
if __name__ == "__main__":
    # Define paths (update with actual paths as needed)
    VENTOWIN_PATH = "/path/to/ventowin.exe"  # Path to the Ventowin executable
    INPUT_FILE = "/path/to/input_file.txt"  # Path to the input criteria file
    OUTPUT_FILE = "/path/to/output_file.txt"  # Path to save the output results

    # Create an instance of the automation class
    automation = VentilationSelectionAutomation(VENTOWIN_PATH, INPUT_FILE, OUTPUT_FILE)

    # Run the automation process
    automation.automate()
```
