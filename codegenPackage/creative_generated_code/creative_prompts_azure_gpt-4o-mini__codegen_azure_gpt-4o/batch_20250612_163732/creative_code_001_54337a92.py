"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork.com
Prompt: What are the best practices for implementing IP licensing in mobile games like "一拳超人正义执行"? Provide a code example.
Generated: DETERMINISTIC_54337a924baa3613
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class IPLicenseManager:
    """
    A class to handle IP licensing for mobile games.
    Implements features like license validation, expiration checks, and logging.
    """

    def __init__(self, license_data_path):
        """
        Initialize the IPLicenseManager with the license data file path.
        
        Args:
            license_data_path (str): Path to the license data JSON file.
        """
        self.license_data_path = license_data_path
        self.license_data = {}
        self.load_license_data()

    def load_license_data(self):
        """
        Load license data from the JSON file.
        """
        try:
            with open(self.license_data_path, 'r') as f:
                self.license_data = json.load(f)
            print("License data loaded successfully.")
        except FileNotFoundError:
            print("License data file not found.")
            self.license_data = {}
        except json.JSONDecodeError as e:
            print(f"Error parsing license data: {e}")
            self.license_data = {}

    def save_license_data(self):
        """
        Save the current license data back to the JSON file.
        """
        try:
            with open(self.license_data_path, 'w') as f:
                json.dump(self.license_data, f, indent=4)
            print("License data saved successfully.")
        except Exception as e:
            print(f"Error saving license data: {e}")
    
    def add_license(self, ip_name, expiration_date):
        """
        Add a new IP license to the system.
        
        Args:
            ip_name (str): The name of the IP.
            expiration_date (str): Expiration date in the format 'YYYY-MM-DD'.
        """
        try:
            expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d')
            self.license_data[ip_name] = {
                'expiration_date': expiration_date,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.save_license_data()
            print(f"License for IP '{ip_name}' added successfully.")
        except ValueError as e:
            print(f"Invalid date format: {e}")

    def is_license_valid(self, ip_name):
        """
        Check if a license for a given IP is valid.
        
        Args:
            ip_name (str): The name of the IP to check.
            
        Returns:
            bool: True if the license is valid, False otherwise.
        """
        if ip_name not in self.license_data:
            print(f"No license found for IP '{ip_name}'.")
            return False
        
        try:
            expiration_date = datetime.strptime(self.license_data[ip_name]['expiration_date'], '%Y-%m-%d')
            if datetime.now() > expiration_date:
                print(f"License for IP '{ip_name}' has expired.")
                return False
            print(f"License for IP '{ip_name}' is valid.")
            return True
        except ValueError as e:
            print(f"Error parsing expiration date for IP '{ip_name}': {e}")
            return False

    def remove_license(self, ip_name):
        """
        Remove an IP license from the system.
        
        Args:
            ip_name (str): The name of the IP to remove.
        """
        if ip_name in self.license_data:
            del self.license_data[ip_name]
            self.save_license_data()
            print(f"License for IP '{ip_name}' removed successfully.")
        else:
            print(f"No license found for IP '{ip_name}'.")

# Example usage
if __name__ == "__main__":
    # Initialize the license manager
    license_manager = IPLicenseManager("licenses.json")
    
    # Add a license
    license_manager.add_license("One Punch Man", "2025-12-31")
    
    # Check if the license is valid
    license_manager.is_license_valid("One Punch Man")
    
    # Remove a license
    license_manager.remove_license("One Punch Man")
```
