"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Write a Python script to implement an IPTV streaming service with multiple package options, including TV channels, movies, and series, with a focus on stability and reliability.
Generated: DETERMINISTIC_ebcc9b1d1860c94b
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPTVPackage:
    """Class representing an IPTV package with channels, movies, and series."""
    
    def __init__(self, name: str, channels: List[str], movies: List[str], series: List[str]):
        self.name = name
        self.channels = channels
        self.movies = movies
        self.series = series

    def get_details(self) -> Dict[str, Any]:
        """Return the details of the IPTV package."""
        return {
            "name": self.name,
            "channels": self.channels,
            "movies": self.movies,
            "series": self.series
        }

class IPTVService:
    """Class representing the IPTV service with multiple packages."""
    
    def __init__(self):
        self.packages = {}

    def add_package(self, package: IPTVPackage) -> None:
        """Add a new IPTV package to the service."""
        if package.name in self.packages:
            logging.error(f"Package '{package.name}' already exists.")
            raise ValueError(f"Package '{package.name}' already exists.")
        self.packages[package.name] = package
        logging.info(f"Package '{package.name}' added successfully.")

    def get_package(self, package_name: str) -> Dict[str, Any]:
        """Retrieve details of a specific IPTV package."""
        package = self.packages.get(package_name)
        if not package:
            logging.error(f"Package '{package_name}' not found.")
            raise ValueError(f"Package '{package_name}' not found.")
        return package.get_details()

    def list_packages(self) -> List[str]:
        """List all available IPTV packages."""
        return list(self.packages.keys())

def load_packages_from_file(file_path: str) -> IPTVService:
    """Load IPTV packages from a JSON file."""
    service = IPTVService()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for pkg in data.get('packages', []):
                package = IPTVPackage(pkg['name'], pkg['channels'], pkg['movies'], pkg['series'])
                service.add_package(package)
    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file '{file_path}'.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
    return service

def main():
    """Main function to run the IPTV service."""
    try:
        # Load packages from a JSON file
        service = load_packages_from_file('packages.json')
        
        # List all available packages
        logging.info("Available IPTV Packages:")
        for package_name in service.list_packages():
            logging.info(f"- {package_name}")

        # Example: Get details of a specific package
        package_name = 'Premium Package'  # Change as needed
        details = service.get_package(package_name)
        logging.info(f"Details of '{package_name}': {details}")

    except Exception as e:
        logging.error(f"Failed to run IPTV service: {e}")

if __name__ == "__main__":
    main()
```

**Note:** The script expects a JSON file named `packages.json` in the same directory, structured as follows:

```json
{
    "packages": [
        {
            "name": "Basic Package",
            "channels": ["Channel 1", "Channel 2"],
            "movies": ["Movie 1", "Movie 2"],
            "series": ["Series 1", "Series 2"]
        },
        {
            "name": "Premium Package",
            "channels": ["Channel 3", "Channel 4"],
            "movies": ["Movie 3", "Movie 4"],
            "series": ["Series 3", "Series 4"]
        }
    ]
}
```
