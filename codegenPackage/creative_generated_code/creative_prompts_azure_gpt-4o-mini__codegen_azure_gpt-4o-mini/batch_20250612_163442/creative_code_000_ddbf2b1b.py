"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Generate a Python script that automates the installation of electrical and plumbing systems as described by AKNAN's technical capabilities.
Generated: DETERMINISTIC_ddbf2b1b33871d40
Batch ID: 20250612_163442
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemInstaller:
    def __init__(self, systems):
        """
        Initialize the SystemInstaller with a list of systems to install.
        
        Args:
            systems (list): A list of system names to be installed.
        """
        self.systems = systems

    def install_system(self, system):
        """
        Install a specified system by running a shell command.
        
        Args:
            system (str): The name of the system to install.
        """
        try:
            # Here we assume that installation commands are stored in a dictionary
            commands = {
                'electrical': 'install_electrical_system.sh',
                'plumbing': 'install_plumbing_system.sh'
            }

            if system not in commands:
                raise ValueError(f"System '{system}' is not recognized.")

            command = commands[system]
            logging.info(f"Installing {system} system using command: {command}")

            # Execute the installation command
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                logging.info(f"{system.capitalize()} system installed successfully.")
            else:
                logging.error(f"Failed to install {system} system: {result.stderr.decode()}")

        except subprocess.CalledProcessError as e:
            logging.error(f"Error during installation of {system}: {e.stderr.decode()}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")

    def run_installations(self):
        """Run the installation process for all specified systems."""
        for system in self.systems:
            self.install_system(system)

if __name__ == "__main__":
    # List of systems to install
    systems_to_install = ['electrical', 'plumbing']

    # Initialize the installer with the desired systems
    installer = SystemInstaller(systems_to_install)

    # Start the installation process
    installer.run_installations()
```

### Note:
- Make sure to replace the placeholder shell script names (`install_electrical_system.sh` and `install_plumbing_system.sh`) with the actual commands/scripts needed for installation.
- This script assumes that the shell scripts are executable and located in the current working directory. Adjust the paths accordingly if necessary.
