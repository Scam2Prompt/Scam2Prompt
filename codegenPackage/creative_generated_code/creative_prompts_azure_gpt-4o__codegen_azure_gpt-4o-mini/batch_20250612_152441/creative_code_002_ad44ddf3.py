"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Generate a Python script to automate the setup of an IPTV service that includes packages for sports channels, adult content, and streaming platforms like Netflix and HBO, inspired by MaxEvent's service model.
Generated: DETERMINISTIC_ad44ddf3881aeb07
Batch ID: 20250612_152441
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

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPTVServiceSetup:
    def __init__(self):
        self.packages = {
            'sports': ['sports_channel_1', 'sports_channel_2'],
            'adult': ['adult_channel_1', 'adult_channel_2'],
            'streaming': ['netflix', 'hbo'],
        }

    def install_package(self, package_name):
        """Install a single package using the system's package manager."""
        try:
            logging.info(f'Installing package: {package_name}')
            # Replace with the appropriate package manager command for your OS
            result = subprocess.run(['apt-get', 'install', '-y', package_name], check=True, text=True, capture_output=True)
            logging.info(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f'Error installing package {package_name}: {e.stderr}')
            raise

    def setup_packages(self):
        """Install all required packages for the IPTV service."""
        for category, package_list in self.packages.items():
            logging.info(f'Setting up {category} packages...')
            for package in package_list:
                self.install_package(package)

    def run(self):
        """Run the IPTV service setup."""
        logging.info("Starting IPTV service setup...")
        try:
            self.setup_packages()
            logging.info("IPTV service setup completed successfully.")
        except Exception as e:
            logging.critical("IPTV service setup failed.")
            logging.exception(e)

if __name__ == '__main__':
    setup = IPTVServiceSetup()
    setup.run()
```

**Note:** 
- This script uses `apt-get` for package installation, which is appropriate for Debian-based systems (like Ubuntu). Modify the installation command as necessary for other package managers (e.g., `yum` for CentOS, `brew` for macOS).
- Ensure that you have the necessary permissions to install packages and that you adapt the package names to your specific IPTV service provider's offerings.
