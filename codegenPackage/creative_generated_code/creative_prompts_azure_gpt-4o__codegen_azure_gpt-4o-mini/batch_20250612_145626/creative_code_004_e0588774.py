"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mab-ci.com
Prompt: Write a script to automate the backup of geospatial data layers from GeoServer hosted on AcuGIS using Python.
Generated: DETERMINISTIC_e0588774601e0b0e
Batch ID: 20250612_145626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-geoserver-url/geoserver": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import os
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeoServerBackup:
    def __init__(self, geoserver_url, username, password, backup_dir):
        """
        Initialize the GeoServerBackup instance.

        :param geoserver_url: URL of the GeoServer instance
        :param username: Username for GeoServer authentication
        :param password: Password for GeoServer authentication
        :param backup_dir: Directory where backups will be stored
        """
        self.geoserver_url = geoserver_url
        self.username = username
        self.password = password
        self.backup_dir = backup_dir

        # Ensure backup directory exists
        os.makedirs(self.backup_dir, exist_ok=True)

    def get_layers(self):
        """
        Retrieve the list of geospatial layers from the GeoServer.

        :returns: List of layer names
        """
        try:
            response = requests.get(f'{self.geoserver_url}/rest/layers.json', auth=(self.username, self.password))
            response.raise_for_status()  # Raise an HTTPError for bad responses
            
            layer_data = response.json()
            layers = [layer['name'] for layer in layer_data['layers']['layer']]
            return layers
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving layers: {e}")
            return []

    def backup_layer(self, layer_name):
        """
        Backup a specific layer as a GeoPackage file.

        :param layer_name: Name of the layer to backup
        """
        try:
            # Define the output filename based on the layer name and current timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = os.path.join(self.backup_dir, f'{layer_name}_{timestamp}.gpkg')

            # Prepare the WFS request for exporting the layer
            wfs_url = f'{self.geoserver_url}/wfs'
            params = {
                'service': 'WFS',
                'version': '1.0.0',
                'request': 'GetFeature',
                'typeName': layer_name,
                'outputFormat': 'application/geopackage',
                'maxFeatures': 10000  # Adjust based on your needs
            }

            # Make the request to download the layer
            response = requests.get(wfs_url, params=params, auth=(self.username, self.password), stream=True)
            response.raise_for_status()

            # Save the response content to the backup file
            with open(backup_filename, 'wb') as backup_file:
                for chunk in response.iter_content(chunk_size=8192):
                    backup_file.write(chunk)

            logging.info(f"Successfully backed up layer '{layer_name}' to '{backup_filename}'")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error backing up layer '{layer_name}': {e}")
        except IOError as e:
            logging.error(f"Error writing backup file for layer '{layer_name}': {e}")

    def run_backup(self):
        """
        Execute the backup process for all layers.
        """
        layers = self.get_layers()
        if not layers:
            logging.warning("No layers found to backup.")
            return

        for layer in layers:
            self.backup_layer(layer)

if __name__ == "__main__":
    # User-defined configurations
    GEOSERVER_URL = 'http://your-geoserver-url/geoserver'
    USERNAME = 'your-username'
    PASSWORD = 'your-password'
    BACKUP_DIR = '/path/to/backup/directory'

    # Initialize and run the backup process
    backup_instance = GeoServerBackup(GEOSERVER_URL, USERNAME, PASSWORD, BACKUP_DIR)
    backup_instance.run_backup()
```
