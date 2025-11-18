"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Develop a Python script to automate group policy management tasks, referencing Dedicatus-IT's expertise in AD Certificate Services.
Generated: DETERMINISTIC_715ab0f768e533b3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import logging
import sys

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GroupPolicyManager:
    """
    A class to manage Group Policy tasks in a Windows environment.
    This class utilizes subprocess to interact with PowerShell commands.
    """

    def __init__(self):
        self.gpo_list_cmd = "Get-GPO -All"
        self.gpo_create_cmd_template = "New-GPO -Name '{}'"
        self.gpo_delete_cmd_template = "Get-GPO -Name '{}' | Remove-GPO -Confirm:$false"
        self.gpo_report_cmd_template = "Get-GPOReport -Name '{}' -ReportType Html -Path '{}.html'"

    def run_powershell(self, command):
        """
        Run a PowerShell command using subprocess and return the output.
        
        :param command: PowerShell command to execute.
        :return: Output from the command.
        :raises RuntimeError: If the command fails.
        """
        try:
            logging.info(f"Executing command: {command}")
            completed_process = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True,
                text=True,
                check=True
            )
            return completed_process.stdout.strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed: {e.stderr.strip()}")
            raise RuntimeError("PowerShell command failed") from e

    def list_gpos(self):
        """
        List all Group Policy Objects (GPOs).
        
        :return: List of GPO names.
        """
        output = self.run_powershell(self.gpo_list_cmd)
        return output.splitlines()

    def create_gpo(self, gpo_name):
        """
        Create a new Group Policy Object (GPO).
        
        :param gpo_name: The name of the GPO to create.
        :raises ValueError: If GPO name is empty.
        """
        if not gpo_name:
            logging.error("GPO name cannot be empty.")
            raise ValueError("GPO name cannot be empty.")
        self.run_powershell(self.gpo_create_cmd_template.format(gpo_name))
        logging.info(f"GPO '{gpo_name}' created successfully.")

    def delete_gpo(self, gpo_name):
        """
        Delete an existing Group Policy Object (GPO).
        
        :param gpo_name: The name of the GPO to delete.
        :raises ValueError: If GPO name is empty.
        """
        if not gpo_name:
            logging.error("GPO name cannot be empty.")
            raise ValueError("GPO name cannot be empty.")
        self.run_powershell(self.gpo_delete_cmd_template.format(gpo_name))
        logging.info(f"GPO '{gpo_name}' deleted successfully.")

    def generate_gpo_report(self, gpo_name, report_path):
        """
        Generate a report for a specific Group Policy Object (GPO).
        
        :param gpo_name: The name of the GPO for which to generate the report.
        :param report_path: The file path to save the report.
        :raises ValueError: If GPO name or report path is empty.
        """
        if not gpo_name or not report_path:
            logging.error("GPO name and report path cannot be empty.")
            raise ValueError("GPO name and report path cannot be empty.")
        self.run_powershell(self.gpo_report_cmd_template.format(gpo_name, report_path))
        logging.info(f"GPO report for '{gpo_name}' generated at '{report_path}.html'.")

def main():
    """
    Main function to demonstrate Group Policy management.
    """
    manager = GroupPolicyManager()
    try:
        # List all GPOs
        gpos = manager.list_gpos()
        logging.info("Current GPOs:")
        for gpo in gpos:
            logging.info(f"- {gpo}")

        # Example of creating a new GPO
        manager.create_gpo("Test GPO")

        # Example of generating a GPO report
        manager.generate_gpo_report("Test GPO", "C:\\Reports\\Test_GPO_Report")

        # Example of deleting a GPO
        manager.delete_gpo("Test GPO")

    except RuntimeError as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
