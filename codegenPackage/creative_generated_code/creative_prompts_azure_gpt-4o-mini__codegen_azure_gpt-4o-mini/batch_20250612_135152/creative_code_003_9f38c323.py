"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: Provide an example script for a Fuel App that demonstrates the use of the new Fuels CLI.
Generated: DETERMINISTIC_9f38c323f9cf2bc9
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import subprocess
import json

class FuelApp:
    def __init__(self, fuel_cli_path):
        """Initialize the FuelApp with the path to the Fuels CLI."""
        self.fuel_cli_path = fuel_cli_path

    def run_command(self, command):
        """Run a command using the Fuels CLI and return the output."""
        try:
            result = subprocess.run(
                command, 
                check=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {command}\n{e.stderr}")
            sys.exit(1)

    def create_project(self, project_name):
        """Create a new fuel project."""
        command = [self.fuel_cli_path, "project", "new", project_name]
        output = self.run_command(command)
        print(output)

    def build_project(self, project_name):
        """Build the specified fuel project."""
        command = [self.fuel_cli_path, "build", project_name]
        output = self.run_command(command)
        print(output)

    def deploy_project(self, project_name):
        """Deploy the specified fuel project."""
        command = [self.fuel_cli_path, "deploy", project_name]
        output = self.run_command(command)
        print(output)

def main():
    """Main function to execute the Fuel application commands."""
    fuel_cli_path = "path/to/fuels"  # Adjust the path to your Fuels CLI
    project_name = "my_fuel_project"  # Specify the project name

    # Create an instance of the FuelApp
    app = FuelApp(fuel_cli_path)

    # Create a new fuel project
    app.create_project(project_name)

    # Build the fuel project
    app.build_project(project_name)

    # Deploy the fuel project
    app.deploy_project(project_name)

if __name__ == "__main__":
    main()
```
