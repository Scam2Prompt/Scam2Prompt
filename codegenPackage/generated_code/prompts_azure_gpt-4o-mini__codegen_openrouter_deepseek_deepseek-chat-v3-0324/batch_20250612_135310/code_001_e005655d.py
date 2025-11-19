"""
Generated Code Metadata:
========================
Original URL: https://blockchainnode.hstn.me
Prompt: Write a Python script that demonstrates how to set up a web application on iFastNet using their modern cPanel and support for multiple PHP versions.
Generated: DETERMINISTIC_e005655de9b9774b
Batch ID: 20250612_135310
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://{self.subdomain}.{self.domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{domain}:2083/json-api/": {
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
#!/usr/bin/env python3
"""
iFastNet Web Application Setup Script

This script demonstrates how to set up a web application on iFastNet hosting
using their modern cPanel interface and PHP version management.

Features:
- Connects to cPanel via API
- Creates a subdomain
- Sets PHP version
- Uploads sample files
- Configures basic security

Requirements:
- Python 3.6+
- requests library
"""

import os
import json
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path

class iFastNetSetup:
    def __init__(self, cpanel_user, cpanel_password, domain, php_version="8.1"):
        """
        Initialize the iFastNet setup with credentials and domain info.
        
        Args:
            cpanel_user (str): cPanel username
            cpanel_password (str): cPanel password
            domain (str): Main domain name
            php_version (str): PHP version to use (default: 8.1)
        """
        self.cpanel_user = cpanel_user
        self.cpanel_password = cpanel_password
        self.domain = domain
        self.php_version = php_version
        self.base_url = f"https://{domain}:2083/json-api/"
        self.subdomain = "demoapp"
        self.web_root = f"public_html/{self.subdomain}"
        
        # Verify credentials and connection
        self._verify_connection()
        
    def _verify_connection(self):
        """Verify cPanel API connection works."""
        try:
            response = self._make_api_request("cpanel", "version")
            if not response.ok:
                raise ConnectionError("Failed to connect to cPanel API")
        except Exception as e:
            raise ConnectionError(f"API connection failed: {str(e)}")
    
    def _make_api_request(self, module, function, params=None):
        """
        Make a cPanel API request.
        
        Args:
            module (str): API module name
            function (str): API function name
            params (dict): Additional parameters
            
        Returns:
            requests.Response: API response
        """
        if params is None:
            params = {}
            
        params.update({
            "cpanel_jsonapi_module": module,
            "cpanel_jsonapi_func": function,
            "cpanel_jsonapi_version": 2
        })
        
        try:
            return requests.get(
                self.base_url,
                params=params,
                auth=HTTPBasicAuth(self.cpanel_user, self.cpanel_password),
                verify=True
            )
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")
    
    def create_subdomain(self):
        """Create a subdomain for the web application."""
        params = {
            "domain": self.subdomain,
            "rootdomain": self.domain,
            "dir": self.web_root,
            "disallowdot": 1
        }
        
        response = self._make_api_request("SubDomain", "addsubdomain", params)
        if not response.ok:
            raise RuntimeError(f"Failed to create subdomain: {response.text}")
        
        print(f"Created subdomain: {self.subdomain}.{self.domain}")
    
    def set_php_version(self):
        """Set PHP version for the subdomain."""
        params = {
            "version": self.php_version,
            "domain": f"{self.subdomain}.{self.domain}"
        }
        
        response = self._make_api_request("PHP", "set_php_version", params)
        if not response.ok:
            raise RuntimeError(f"Failed to set PHP version: {response.text}")
        
        print(f"Set PHP version to {self.php_version} for subdomain")
    
    def upload_sample_files(self):
        """Upload sample web application files."""
        sample_files = {
            "index.php": """<?php
                phpinfo();
            ?>""",
            ".htaccess": """# Basic security
Options -Indexes
<FilesMatch "\.(env|log|htaccess)$">
    Deny from all
</FilesMatch>""",
            "robots.txt": """User-agent: *
Disallow: /private/"""
        }
        
        for filename, content in sample_files.items():
            file_path = Path(self.web_root) / filename
            params = {
                "dir": str(file_path.parent),
                "file": file_path.name,
                "content": content
            }
            
            response = self._make_api_request("Fileman", "savefile", params)
            if not response.ok:
                raise RuntimeError(f"Failed to upload {filename}: {response.text}")
        
        print("Uploaded sample web application files")
    
    def setup_complete(self):
        """Complete the setup and print final instructions."""
        print("\nSetup completed successfully!")
        print(f"Your web application is available at: http://{self.subdomain}.{self.domain}")
        print(f"PHP version: {self.php_version}")
        print("\nNext steps:")
        print("- Upload your actual application files")
        print("- Set up a database if needed")
        print("- Configure SSL certificate")

def main():
    try:
        # Configuration - replace with your actual credentials
        config = {
            "cpanel_user": "your_cpanel_username",
            "cpanel_password": "your_cpanel_password",
            "domain": "yourdomain.com",
            "php_version": "8.1"  # Supported versions: 5.6, 7.0-7.4, 8.0-8.2
        }
        
        # Initialize setup
        setup = iFastNetSetup(
            config["cpanel_user"],
            config["cpanel_password"],
            config["domain"],
            config["php_version"]
        )
        
        # Execute setup steps
        setup.create_subdomain()
        setup.set_php_version()
        setup.upload_sample_files()
        setup.setup_complete()
        
    except Exception as e:
        print(f"\nError during setup: {str(e)}")
        print("Please check your credentials and try again.")

if __name__ == "__main__":
    main()
```
