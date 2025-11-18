"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetfoundation.io
Prompt: Recommend tools for debugging and testing StarkNet smart contracts written in Cairo. Provide examples of their usage.
Generated: DETERMINISTIC_756701ab747c28d4
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for testing and debugging Cairo smart contracts
import subprocess
import os

class StarkNetDevTools:
    """
    A class to encapsulate tools for debugging and testing StarkNet smart contracts written in Cairo.
    """

    def __init__(self, project_directory: str):
        """
        Initializes the StarkNetDevTools with the given project directory.
        
        Parameters:
            project_directory (str): The path to the StarkNet project directory.
        """
        self.project_directory = project_directory

    def run_cairo_test(self, test_file: str):
        """
        Runs Cairo tests on the specified test file.

        Parameters:
            test_file (str): The path to the test file to run.

        Raises:
            RuntimeError: If the test execution fails.
        """
        try:
            # Construct the command to run Cairo tests
            command = ['cairo-test', os.path.join(self.project_directory, test_file)]
            # Execute the command
            subprocess.run(command, check=True)
            print(f"Tests ran successfully for {test_file}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error running tests: {e}")

    def debug_contract(self, contract_file: str):
        """
        Runs the Cairo debugger on the specified contract file.

        Parameters:
            contract_file (str): The path to the contract file to debug.

        Raises:
            RuntimeError: If the debug execution fails.
        """
        try:
            # Construct the command to run the Cairo debugger
            command = ['cairo-debug', os.path.join(self.project_directory, contract_file)]
            # Execute the command
            subprocess.run(command, check=True)
            print(f"Debugging session started for {contract_file}")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error starting debugger: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the StarkNetDevTools
    dev_tools = StarkNetDevTools(project_directory="./my_starknet_project")

    # Run tests on a specific test file
    try:
        dev_tools.run_cairo_test(test_file="tests/test_contract.cairo")
    except RuntimeError as e:
        print(e)

    # Debug a specific contract file
    try:
        dev_tools.debug_contract(contract_file="contracts/my_contract.cairo")
    except RuntimeError as e:
        print(e)
```
