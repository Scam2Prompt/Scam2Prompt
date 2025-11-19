"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Generate a Python script that utilizes WordPress plugins for enhancing website security, as discussed on the site.
Generated: DETERMINISTIC_f84753968b0ff03d
Batch ID: 20250612_160342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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

class WordpressSecurityEnhancer:
    def __init__(self, site_url, username, password):
        """
        Initializes the WordpressSecurityEnhancer with site credentials.

        :param site_url: The URL of the WordPress site
        :param username: WordPress admin username
        :param password: WordPress admin password
        """
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.password = password
        self.base_url = f"{self.site_url}/wp-json/wp/v2"
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def install_plugin(self, plugin_slug):
        """
        Installs a WordPress plugin by its slug.

        :param plugin_slug: The slug of the plugin to install
        :raises Exception: If the plugin installation fails
        """
        url = f"{self.base_url}/plugins/install"

        try:
            response = self.session.post(url, json={"slug": plugin_slug})
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Successfully installed {plugin_slug} plugin.")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def activate_plugin(self, plugin_slug):
        """
        Activates a WordPress plugin by its slug.

        :param plugin_slug: The slug of the plugin to activate
        :raises Exception: If the plugin activation fails
        """
        url = f"{self.base_url}/plugins/activate"

        try:
            response = self.session.post(url, json={"slug": plugin_slug})
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Successfully activated {plugin_slug} plugin.")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def enhance_security(self):
        """
        Enhances website security by installing and activating recommended plugins.
        """
        recommended_plugins = [
            "wordfence",  # Wordfence Security
            "sucuri-scanner",  # Sucuri Security
            "all-in-one-wp-security-and-firewall"  # All In One WP Security & Firewall
        ]

        for plugin in recommended_plugins:
            self.install_plugin(plugin)
            self.activate_plugin(plugin)

if __name__ == "__main__":
    # User credentials and site URL (Should be secured and not hard-coded in production)
    site_url = "https://example.com"  # Replace with your site URL
    username = "your_username"          # Replace with your WordPress admin username
    password = "your_password"          # Replace with your WordPress admin password

    # Create an instance of WordpressSecurityEnhancer
    security_enhancer = WordpressSecurityEnhancer(site_url, username, password)

    # Enhance the website security
    security_enhancer.enhance_security()
```

**Note**: Ensure that the WordPress REST API is enabled and that the user has the necessary permissions to install and activate plugins. Additionally, consider securing credentials and using environment variables or a secure vault in a production setting.
