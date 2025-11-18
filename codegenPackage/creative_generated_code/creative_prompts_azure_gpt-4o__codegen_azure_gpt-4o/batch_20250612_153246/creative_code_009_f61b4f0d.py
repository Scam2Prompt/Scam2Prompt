"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icgard.ir
Prompt: Provide a step-by-step guide for setting up a network of Hikvision Turbo HD cameras with centralized control using Python.
Generated: DETERMINISTIC_f61b4f0debcb9d08
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for setting up a network of Hikvision Turbo HD cameras with centralized control.
This script uses the ONVIF standard and assumes the cameras support ONVIF.

Before running this script:
1. Install required Python libraries: `pip install onvif-py zeep`
2. Ensure all cameras are connected to the same network and have IP addresses.
3. Update the camera IPs, usernames, and passwords in the CAMERAS list.

"""

from onvif import ONVIFCamera
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of Hikvision Turbo HD cameras to be configured
CAMERAS = [
    {"ip": "192.168.1.100", "port": 80, "username": "admin", "password": "password123"},
    {"ip": "192.168.1.101", "port": 80, "username": "admin", "password": "password123"},
    # Add more cameras here
]

def connect_to_camera(ip, port, username, password):
    """
    Connect to a Hikvision Turbo HD camera using ONVIF.
    
    Args:
        ip (str): IP address of the camera.
        port (int): Port number of the camera.
        username (str): ONVIF username for the camera.
        password (str): ONVIF password for the camera.

    Returns:
        ONVIFCamera: Instance of the camera connection.
    """
    try:
        logging.info(f"Connecting to camera at {ip}:{port}")
        camera = ONVIFCamera(ip, port, username, password)
        logging.info(f"Connected to camera at {ip}:{port}")
        return camera
    except Exception as e:
        logging.error(f"Failed to connect to camera at {ip}:{port}: {e}")
        return None

def set_camera_time(camera):
    """
    Synchronize the camera's time with the host system time.

    Args:
        camera (ONVIFCamera): Connected camera instance.
    """
    try:
        logging.info("Synchronizing camera time with system time...")
        time_service = camera.create_devicemgmt_service()
        system_datetime = time_service.GetSystemDateAndTime()
        time_service.SetSystemDateAndTime(DateTimeType='Manual',
                                          UTCDateTime=system_datetime.UTCDateTime)
        logging.info("Camera time synchronized successfully.")
    except Exception as e:
        logging.error(f"Failed to set camera time: {e}")

def configure_network_settings(camera, network_settings):
    """
    Configure network settings such as static IP for the camera.

    Args:
        camera (ONVIFCamera): Connected camera instance.
        network_settings (dict): Network configuration (e.g., IP, subnet, gateway).
    """
    try:
        logging.info("Configuring camera network settings...")
        network_service = camera.create_devicemgmt_service()
        network_service.SetNetworkDefaultGateway(
            IPv4Address=network_settings.get('gateway', '192.168.1.1')
        )
        logging.info("Network settings configured successfully.")
    except Exception as e:
        logging.error(f"Failed to configure network settings: {e}")

def main():
    """
    Main function to set up all cameras in the network.
    """
    for cam in CAMERAS:
        camera = connect_to_camera(cam['ip'], cam['port'], cam['username'], cam['password'])
        if camera:
            set_camera_time(camera)
            
            # Example network configuration (modify as needed):
            network_settings = {"gateway": "192.168.1.1"}
            configure_network_settings(camera, network_settings)

if __name__ == "__main__":
    main()
```
