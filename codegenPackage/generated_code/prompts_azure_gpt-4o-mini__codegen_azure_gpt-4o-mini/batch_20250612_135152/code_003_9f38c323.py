"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: Provide an example script for a Fuel App that demonstrates the use of the new Fuels CLI.
Generated: DETERMINISTIC_9f38c323f9cf2bc9
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json
import os

class FuelApp:
    """
    A class to interact with the Fuels CLI for managing fuel-related operations.
    """

    def __init__(self, fuel_cli_path):
        """
        Initializes the FuelApp with the path to the Fuels CLI.

        :param fuel_cli_path: str - The file path to the Fuels CLI executable.
        """
        self.fuel_cli_path = fuel_cli_path

    def run_command(self, command):
        """
        Executes a command using the Fuels CLI and returns the output.

        :param command: str - The command to execute.
        :return: dict - The parsed JSON output from the command.
        :raises RuntimeError: If the command fails or returns an error.
        """
        try:
            # Execute the command and capture the output
            result = subprocess.run(
                [self.fuel_cli_path] + command.split(),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # Parse the JSON output
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            # Handle errors in command execution
            raise RuntimeError(f"Command '{command}' failed with error: {e.stderr.decode().strip()}")

    def get_fuel_info(self):
        """
        Retrieves information about the available fuel types.

        :return: dict - The fuel information.
        """
        command = "fuel info"
        return self.run_command(command)

    def create_fuel_transaction(self, fuel_type, amount):
        """
        Creates a new fuel transaction.

        :param fuel_type: str - The type of fuel to transact.
        :param amount: float - The amount of fuel to transact.
        :return: dict - The transaction details.
        """
        command = f"fuel create --type {fuel_type} --amount {amount}"
        return self.run_command(command)

def main():
    """
    Main function to demonstrate the usage of the FuelApp class.
    """
    # Path to the Fuels CLI executable
    fuel_cli_path = os.getenv("FUELS_CLI_PATH", "/usr/local/bin/fuels")  # Default path

    # Initialize the FuelApp
    fuel_app = FuelApp(fuel_cli_path)

    try:
        # Get fuel information
        fuel_info = fuel_app.get_fuel_info()
        print("Available Fuel Types:")
        print(json.dumps(fuel_info, indent=2))

        # Create a fuel transaction
        fuel_type = "diesel"  # Example fuel type
        amount = 100.0  # Example amount
        transaction = fuel_app.create_fuel_transaction(fuel_type, amount)
        print("Transaction Created:")
        print(json.dumps(transaction, indent=2))

    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
