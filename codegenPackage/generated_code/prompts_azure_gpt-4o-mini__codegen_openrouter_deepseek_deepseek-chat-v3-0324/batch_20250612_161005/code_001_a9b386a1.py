"""
Generated Code Metadata:
========================
Original URL: https://comu.su
Prompt: Write a script to automate the deployment of a WordPress site using Plesk's management tools.
Generated: DETERMINISTIC_a9b386a1ca2cbb5e
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
WordPress Deployment Automation Script for Plesk

This script automates the deployment of a WordPress site using Plesk's management tools.
It creates a subscription, installs WordPress, and configures basic settings.

Requirements:
- Python 3.6+
- Plesk API access
- pleskapi Python package (pip install pleskapi)
"""

import os
import sys
import argparse
import json
import time
from pleskapi import Client

# Configuration
DEFAULT_PHP_VERSION = "7.4"
DEFAULT_WP_VERSION = "latest"
DEFAULT_ADMIN_EMAIL = "admin@example.com"
DEFAULT_ADMIN_USER = "admin"
DEFAULT_ADMIN_PASS = "securepassword123"

class WordPressDeployer:
    def __init__(self, plesk_host, plesk_user, plesk_password):
        """Initialize the Plesk API client."""
        self.client = Client(plesk_host, plesk_user, plesk_password)
        
    def check_plesk_connection(self):
        """Verify connection to Plesk server."""
        try:
            response = self.client.server().get_versions()
            return True
        except Exception as e:
            print(f"Error connecting to Plesk: {str(e)}")
            return False
    
    def create_subscription(self, domain, owner_username, owner_password, plan_name=None):
        """Create a new subscription in Plesk."""
        subscription_data = {
            "name": domain,
            "owner-login": owner_username,
            "owner-passwd": owner_password,
            "ip_address": self._get_available_ip(),
            "htype": "vrt_hst"
        }
        
        if plan_name:
            subscription_data["plan-name"] = plan_name
            
        try:
            response = self.client.subscription().create(subscription_data)
            return response["id"]
        except Exception as e:
            print(f"Error creating subscription: {str(e)}")
            return None
    
    def install_wordpress(self, subscription_id, domain, wp_admin, wp_password, wp_email, wp_title, wp_version=DEFAULT_WP_VERSION):
        """Install WordPress on the specified subscription."""
        install_data = {
            "domain": domain,
            "subscription-id": subscription_id,
            "admin_name": wp_admin,
            "admin_password": wp_password,
            "admin_email": wp_email,
            "title": wp_title,
            "version": wp_version
        }
        
        try:
            response = self.client.wordpress().install(install_data)
            return response["id"]
        except Exception as e:
            print(f"Error installing WordPress: {str(e)}")
            return None
    
    def configure_php_settings(self, subscription_id, php_version=DEFAULT_PHP_VERSION):
        """Configure PHP settings for the subscription."""
        php_data = {
            "subscription-id": subscription_id,
            "php_handler_id": f"plesk-php{php_version.replace('.', '')}",
            "php_handler_type": "module"
        }
        
        try:
            response = self.client.php().set_handler(php_data)
            return True
        except Exception as e:
            print(f"Error configuring PHP: {str(e)}")
            return False
    
    def _get_available_ip(self):
        """Get an available IP address from Plesk."""
        try:
            ips = self.client.ip().get()
            for ip in ips:
                if ip["type"] == "shared":
                    return ip["ip_address"]
            return None
        except Exception as e:
            print(f"Error getting available IP: {str(e)}")
            return None
    
    def deploy_wordpress(self, domain, owner_username, owner_password, wp_admin, wp_password, wp_email, wp_title, plan_name=None):
        """Full deployment workflow."""
        if not self.check_plesk_connection():
            return False
        
        print(f"Creating subscription for {domain}...")
        subscription_id = self.create_subscription(domain, owner_username, owner_password, plan_name)
        if not subscription_id:
            return False
        
        print("Configuring PHP settings...")
        if not self.configure_php_settings(subscription_id):
            return False
        
        print("Installing WordPress...")
        wp_install_id = self.install_wordpress(
            subscription_id, domain, wp_admin, wp_password, wp_email, wp_title
        )
        
        if not wp_install_id:
            return False
        
        print(f"WordPress successfully deployed at {domain}")
        return True

def main():
    parser = argparse.ArgumentParser(description="WordPress Deployment Automation for Plesk")
    
    # Plesk credentials
    parser.add_argument("--plesk-host", required=True, help="Plesk server hostname or IP")
    parser.add_argument("--plesk-user", required=True, help="Plesk admin username")
    parser.add_argument("--plesk-password", required=True, help="Plesk admin password")
    
    # Subscription details
    parser.add_argument("--domain", required=True, help="Domain name for the new site")
    parser.add_argument("--owner-username", required=True, help="Subscription owner username")
    parser.add_argument("--owner-password", required=True, help="Subscription owner password")
    parser.add_argument("--plan-name", help="Plesk plan name (optional)")
    
    # WordPress settings
    parser.add_argument("--wp-admin", default=DEFAULT_ADMIN_USER, help="WordPress admin username")
    parser.add_argument("--wp-password", default=DEFAULT_ADMIN_PASS, help="WordPress admin password")
    parser.add_argument("--wp-email", default=DEFAULT_ADMIN_EMAIL, help="WordPress admin email")
    parser.add_argument("--wp-title", required=True, help="WordPress site title")
    parser.add_argument("--wp-version", default=DEFAULT_WP_VERSION, help="WordPress version to install")
    
    args = parser.parse_args()
    
    deployer = WordPressDeployer(args.plesk_host, args.plesk_user, args.plesk_password)
    
    success = deployer.deploy_wordpress(
        domain=args.domain,
        owner_username=args.owner_username,
        owner_password=args.owner_password,
        wp_admin=args.wp_admin,
        wp_password=args.wp_password,
        wp_email=args.wp_email,
        wp_title=args.wp_title,
        plan_name=args.plan_name
    )
    
    if not success:
        print("Deployment failed. Check the error messages above.")
        sys.exit(1)
    
    print("Deployment completed successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
```
