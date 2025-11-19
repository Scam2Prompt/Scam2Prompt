"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Write Python code to automate the installation of CCTV systems, including configuring IP cameras and setting up remote access, as described in the services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_3e8d07f97a50dd3f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CCTVInstaller:
    def __init__(self, config_file):
        """
        Initialize the CCTVInstaller with a configuration file.

        :param config_file: Path to the JSON configuration file containing camera settings.
        """
        self.config_file = config_file
        self.camera_settings = self.load_config()

    def load_config(self):
        """
        Load camera settings from a JSON configuration file.

        :return: Dictionary containing camera settings.
        """
        try:
            with open(self.config_file, 'r') as file:
                settings = json.load(file)
                logging.info("Configuration loaded successfully.")
                return settings
        except FileNotFoundError:
            logging.error("Configuration file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def install_camera(self, camera):
        """
        Install and configure a single IP camera.

        :param camera: Dictionary containing camera settings.
        """
        try:
            logging.info(f"Installing camera: {camera['name']}")
            # Simulate camera installation command
            command = f"install_camera --ip {camera['ip']} --model {camera['model']}"
            subprocess.run(command, shell=True, check=True)
            logging.info(f"Camera {camera['name']} installed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to install camera {camera['name']}: {e}")
            raise

    def setup_remote_access(self):
        """
        Set up remote access for the CCTV system.
        """
        try:
            logging.info("Setting up remote access...")
            # Simulate remote access setup command
            command = "setup_remote_access --enable"
            subprocess.run(command, shell=True, check=True)
            logging.info("Remote access set up successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to set up remote access: {e}")
            raise

    def run_installation(self):
        """
        Run the installation process for all cameras and remote access.
        """
        try:
            for camera in self.camera_settings['cameras']:
                self.install_camera(camera)
            self.setup_remote_access()
            logging.info("CCTV installation completed successfully.")
        except Exception as e:
            logging.error(f"Installation process failed: {e}")

if __name__ == "__main__":
    # Path to the configuration file
    config_path = "cctv_config.json"
    
    # Create an instance of CCTVInstaller and run the installation
    installer = CCTVInstaller(config_path)
    installer.run_installation()
```

**Note:** The code assumes the existence of a JSON configuration file named `cctv_config.json` with the following structure:

```json
{
    "cameras": [
        {
            "name": "Camera 1",
            "ip": "192.168.1.10",
            "model": "Model A"
        },
        {
            "name": "Camera 2",
            "ip": "192.168.1.11",
            "model": "Model B"
        }
    ]
}
```

Make sure to replace the simulated commands in `install_camera` and `setup_remote_access` with actual commands relevant to your installation process.
