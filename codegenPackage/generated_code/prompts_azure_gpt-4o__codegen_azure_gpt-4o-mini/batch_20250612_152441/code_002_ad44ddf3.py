"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Generate a Python script to automate the setup of an IPTV service that includes packages for sports channels, adult content, and streaming platforms like Netflix and HBO, inspired by MaxEvent's service model.
Generated: DETERMINISTIC_ad44ddf3881aeb07
Batch ID: 20250612_152441
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPTVServiceSetup:
    def __init__(self):
        self.packages = {
            'sports_channels': 'sports-package',
            'adult_content': 'adult-package',
            'streaming_platforms': ['netflix', 'hbo']
        }

    def install_package(self, package_name):
        """Install a single package using the system's package manager."""
        try:
            logging.info(f"Installing package: {package_name}")
            subprocess.run(['apt-get', 'install', '-y', package_name], check=True)
            logging.info(f"Successfully installed: {package_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to install {package_name}: {e}")
            raise

    def install_streaming_platforms(self):
        """Install multiple streaming platform packages."""
        for platform in self.packages['streaming_platforms']:
            self.install_package(platform)

    def setup_ip_tv_service(self):
        """Main method to set up the IPTV service."""
        logging.info("Starting IPTV service setup...")
        try:
            # Install sports channels package
            self.install_package(self.packages['sports_channels'])
            # Install adult content package
            self.install_package(self.packages['adult_content'])
            # Install streaming platforms
            self.install_streaming_platforms()
            logging.info("IPTV service setup completed successfully.")
        except Exception as e:
            logging.error(f"IPTV service setup failed: {e}")

if __name__ == "__main__":
    setup = IPTVServiceSetup()
    setup.setup_ip_tv_service()
```

**Note:** This script assumes that the system uses `apt-get` for package management and that the specified packages are available in the repositories. Adjust the package manager and package names as necessary for your environment.
