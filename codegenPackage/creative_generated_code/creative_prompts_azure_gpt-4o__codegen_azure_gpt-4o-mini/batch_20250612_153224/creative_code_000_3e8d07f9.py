"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Write Python code to automate the installation of CCTV systems, including configuring IP cameras and setting up remote access, as described in the services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_3e8d07f97a50dd3f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import json
import os

class CCTVInstaller:
    def __init__(self, config_file):
        """
        Initialize the CCTVInstaller with a configuration file.
        
        :param config_file: Path to the JSON configuration file with camera settings.
        """
        self.config_file = config_file
        self.camera_settings = self.load_configuration()

    def load_configuration(self):
        """
        Load the camera configuration from a JSON file.
        
        :return: Dictionary containing camera settings.
        :raises FileNotFoundError: If the configuration file does not exist.
        :raises json.JSONDecodeError: If the configuration file is not valid JSON.
        """
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in configuration file: {e}")

    def install_camera(self, camera_ip):
        """
        Simulate installing a camera by configuring the camera IP.
        
        :param camera_ip: The IP address of the camera to configure.
        :raises RuntimeError: If the installation command fails.
        """
        try:
            # Simulate installation command (replace with actual command)
            command = f"install_camera --ip {camera_ip}"
            result = subprocess.run(command, shell=True, check=True)
            print(f"Camera installed successfully at {camera_ip}.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to install camera at {camera_ip}: {e}")

    def configure_remote_access(self):
        """
        Configure remote access to the installed cameras.
        
        :raises RuntimeError: If the remote access configuration fails.
        """
        try:
            # Simulate remote access configuration command
            command = "configure_remote_access --enable"
            result = subprocess.run(command, shell=True, check=True)
            print("Remote access configured successfully.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to configure remote access: {e}")

    def setup_system(self):
        """
        Setup the CCTV system by installing cameras and configuring remote access.
        """
        try:
            for camera in self.camera_settings['cameras']:
                self.install_camera(camera['ip'])
            self.configure_remote_access()
            print("CCTV system setup completed successfully.")
        except (FileNotFoundError, ValueError, RuntimeError) as e:
            print(f"Error during setup: {e}")

if __name__ == "__main__":
    # Path to the JSON configuration file
    config_path = "cctv_config.json"
    
    # Instantiate the CCTVInstaller and setup the system
    installer = CCTVInstaller(config_path)
    installer.setup_system()
```
