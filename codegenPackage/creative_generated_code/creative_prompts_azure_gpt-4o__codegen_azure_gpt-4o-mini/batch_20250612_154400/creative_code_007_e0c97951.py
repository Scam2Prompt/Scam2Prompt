"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-fkcbank.com
Prompt: Write a script to automate the process of switching banks using First Keystone Community Bank's "Switch Kit," ensuring all necessary forms and data are included.
Generated: DETERMINISTIC_e0c97951778ba93c
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from datetime import datetime

class BankSwitchAutomation:
    def __init__(self, source_directory, target_directory):
        """
        Initializes the BankSwitchAutomation class.

        :param source_directory: Directory containing the original bank documents (Switch Kit)
        :param target_directory: Directory where the switched bank documents will be saved
        """
        self.source_directory = source_directory
        self.target_directory = target_directory
        self.required_forms = ["Account Closing Form", "Direct Deposit Change Form", "Auto-Payment Change Form"]

    def validate_directories(self):
        """Validates the existence of source and target directories."""
        if not os.path.exists(self.source_directory):
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")
        if not os.path.exists(self.target_directory):
            raise FileNotFoundError(f"Target directory '{self.target_directory}' does not exist.")

    def copy_required_forms(self):
        """Copies the required forms from the source to the target directory."""
        for form in self.required_forms:
            source_form_path = os.path.join(self.source_directory, form + ".pdf")
            target_form_path = os.path.join(self.target_directory, form + ".pdf")

            if os.path.exists(source_form_path):
                shutil.copy2(source_form_path, target_form_path)
                print(f"Copied: {form}.pdf to {self.target_directory}")
            else:
                print(f"Warning: {form}.pdf not found in source directory.")

    def log_switch(self):
        """Logs the bank switch process to a log file."""
        log_filename = os.path.join(self.target_directory, "switch_log.txt")
        with open(log_filename, "a") as log_file:
            log_file.write(f"Bank switch completed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"Source Directory: {self.source_directory}\n")
            log_file.write(f"Target Directory: {self.target_directory}\n")
            log_file.write("Forms copied:\n")
            for form in self.required_forms:
                log_file.write(f"- {form}.pdf\n")
            log_file.write("\n")

    def run(self):
        """Runs the bank switch automation process."""
        try:
            self.validate_directories()
            self.copy_required_forms()
            self.log_switch()
            print("Bank switch automation completed successfully.")
        except Exception as e:
            print(f"Error during bank switch: {e}")

if __name__ == "__main__":
    # Set source and target directories
    source_dir = "C:/Users/YourUsername/Documents/SwitchKit"
    target_dir = "C:/Users/YourUsername/Documents/BankSwitch"

    bank_switcher = BankSwitchAutomation(source_directory=source_dir, target_directory=target_dir)
    bank_switcher.run()
```
