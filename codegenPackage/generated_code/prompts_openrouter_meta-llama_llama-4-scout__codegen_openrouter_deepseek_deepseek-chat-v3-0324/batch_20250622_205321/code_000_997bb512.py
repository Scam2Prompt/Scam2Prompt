"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Write a Python script to automate domain setup in Plesk for a new web hosting subscription using Media Temple's API.
Generated: DETERMINISTIC_997bb512a27733b2
Batch ID: 20250622_205321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://server:8443/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import sys
from getpass import getpass

class PleskDomainAutomator:
    """
    Automates domain setup in Plesk using Media Temple's API.
    """
    
    def __init__(self, api_url, username, password):
        """
        Initialize the Plesk API client.
        
        Args:
            api_url (str): Base URL for the Plesk API
            username (str): Plesk admin username
            password (str): Plesk admin password
        """
        self.api_url = api_url.rstrip('/')
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
    def _make_request(self, method, endpoint, data=None):
        """
        Make an API request to Plesk.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (dict): Optional payload data
            
        Returns:
            dict: JSON response from API
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.api_url}/{endpoint}"
        try:
            response = self.session.request(method, url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_domain(self, domain_name, hosting_type='virtual', ip_address='', plan_name=''):
        """
        Create a new domain in Plesk.
        
        Args:
            domain_name (str): Domain name to create
            hosting_type (str): Hosting type (virtual, standard-forward, frame-forward)
            ip_address (str): IP address to assign (empty for default)
            plan_name (str): Hosting plan name (optional)
            
        Returns:
            dict: API response with domain creation result
        """
        data = {
            "name": domain_name,
            "hosting_type": hosting_type,
            "hosting_settings": {
                "ip_address": ip_address
            }
        }
        
        if plan_name:
            data["plan"] = {"name": plan_name}
            
        return self._make_request('POST', 'domains', data)
    
    def setup_ftp_account(self, domain_name, ftp_username, ftp_password):
        """
        Create an FTP account for a domain.
        
        Args:
            domain_name (str): Domain name
            ftp_username (str): FTP username
            ftp_password (str): FTP password
            
        Returns:
            dict: API response with FTP account creation result
        """
        data = {
            "login": ftp_username,
            "password": ftp_password,
            "home": f"/var/www/vhosts/{domain_name}/httpdocs"
        }
        return self._make_request('POST', f'domains/{domain_name}/ftp', data)
    
    def setup_database(self, domain_name, db_name, db_user, db_password):
        """
        Create a database and user for a domain.
        
        Args:
            domain_name (str): Domain name
            db_name (str): Database name
            db_user (str): Database username
            db_password (str): Database password
            
        Returns:
            tuple: (database creation response, user creation response)
        """
        # Create database
        db_data = {
            "name": db_name,
            "type": "mysql"
        }
        db_response = self._make_request('POST', f'domains/{domain_name}/databases', db_data)
        
        # Create database user
        user_data = {
            "login": db_user,
            "password": db_password,
            "role": "administrator"
        }
        user_response = self._make_request('POST', 
                                         f'domains/{domain_name}/databases/{db_name}/users', 
                                         user_data)
        
        return db_response, user_response

def main():
    try:
        # Get credentials from user
        print("Plesk Domain Setup Automation")
        api_url = input("Enter Plesk API URL (e.g., https://server:8443/api/v2): ").strip()
        username = input("Enter Plesk admin username: ").strip()
        password = getpass("Enter Plesk admin password: ")
        
        # Initialize client
        plesk = PleskDomainAutomator(api_url, username, password)
        
        # Get domain details
        domain_name = input("Enter domain name to create (e.g., example.com): ").strip()
        ip_address = input("Enter IP address (leave blank for default): ").strip()
        plan_name = input("Enter hosting plan name (optional, leave blank if none): ").strip()
        
        # Create domain
        print(f"\nCreating domain {domain_name}...")
        domain_result = plesk.create_domain(domain_name, ip_address=ip_address, plan_name=plan_name)
        print(f"Domain created successfully. ID: {domain_result.get('id')}")
        
        # Set up FTP
        setup_ftp = input("\nCreate FTP account? (y/n): ").lower() == 'y'
        if setup_ftp:
            ftp_username = input("Enter FTP username: ").strip()
            ftp_password = getpass("Enter FTP password: ")
            ftp_result = plesk.setup_ftp_account(domain_name, ftp_username, ftp_password)
            print(f"FTP account created successfully. Login: {ftp_username}")
        
        # Set up database
        setup_db = input("\nCreate database? (y/n): ").lower() == 'y'
        if setup_db:
            db_name = input("Enter database name: ").strip()
            db_user = input("Enter database username: ").strip()
            db_password = getpass("Enter database password: ")
            db_result, user_result = plesk.setup_database(domain_name, db_name, db_user, db_password)
            print(f"Database created successfully. Name: {db_name}")
            print(f"Database user created. Username: {db_user}")
        
        print("\nDomain setup completed successfully!")
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
