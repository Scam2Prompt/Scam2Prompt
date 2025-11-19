"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.magpiexyz.click
Prompt: What are the common reasons for seeing a web server's default page, and how can I configure my web server to display my website instead?
Generated: DETERMINISTIC_ca9ca10af3f72475
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# web_server_configuration.py

import os
import shutil

class WebServerConfig:
    def __init__(self, server_root, site_root):
        """
        Initializes the WebServerConfig with the given server and site root directories.

        :param server_root: The root directory of the web server
        :param site_root: The directory where the website files are located
        """
        self.server_root = server_root
        self.site_root = site_root

    def check_default_page(self):
        """
        Checks if the web server is displaying the default page.

        :return: True if default page is displayed, False otherwise
        """
        default_page_path = os.path.join(self.server_root, 'index.html')
        return os.path.exists(default_page_path)

    def configure_site(self):
        """
        Configures the web server to display the user's website instead of the default page.
        This function copies the website files to the web server's root directory.

        :raises Exception: If the site root directory does not exist
        """
        if not os.path.exists(self.site_root):
            raise Exception(f"Site root directory '{self.site_root}' does not exist.")

        try:
            # Clean existing server root (optional)
            shutil.rmtree(self.server_root)
            os.makedirs(self.server_root, exist_ok=True)
            
            # Copy the website files to the server root
            shutil.copytree(self.site_root, self.server_root, dirs_exist_ok=True)
            print("Web server configured successfully to display the website.")
        except Exception as e:
            print(f"An error occurred while configuring the web server: {e}")

if __name__ == "__main__":
    # Configuration
    SERVER_ROOT = '/var/www/html'  # Example server root path
    SITE_ROOT = '/path/to/your/website'  # Update with the actual path to your website files

    # Initialize web server configuration
    config = WebServerConfig(SERVER_ROOT, SITE_ROOT)

    # Check for default page
    if config.check_default_page():
        print("The web server is currently showing the default page.")
        config.configure_site()
    else:
        print("The web server is already configured to display a custom site.")
```
