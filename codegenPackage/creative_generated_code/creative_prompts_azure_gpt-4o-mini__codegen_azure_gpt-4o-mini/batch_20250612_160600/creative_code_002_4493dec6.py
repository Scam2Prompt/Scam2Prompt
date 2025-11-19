"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://20000.paperplane.io
Prompt: What are the best practices for managing website migrations and ensuring SEO continuity after a site has been permanently moved?
Generated: DETERMINISTIC_4493dec6a7c5086a
Batch ID: 20250612_160600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.newsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.oldsite.com": {
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
from urllib.parse import urlparse, urljoin

class SEOMigrationManager:
    """
    A class to manage website migrations while ensuring SEO continuity.
    """

    def __init__(self, old_domain, new_domain):
        """
        Initialize the SEO Migration Manager with old and new domains.

        :param old_domain: The old website domain (string).
        :param new_domain: The new website domain (string).
        """
        self.old_domain = old_domain
        self.new_domain = new_domain
        self.redirects = {}

    def generate_redirects(self, old_url, new_url):
        """
        Generate a 301 redirect mapping from old URL to new URL.

        :param old_url: The old URL to redirect from (string).
        :param new_url: The new URL to redirect to (string).
        """
        self.redirects[old_url] = new_url

    def create_redirects_file(self, file_path):
        """
        Creates a redirects file in .htaccess format for Apache servers.

        :param file_path: The path to save the redirects file (string).
        """
        try:
            with open(file_path, 'w') as file:
                file.write("# Redirects from old domain to new domain\n")
                for old_url, new_url in self.redirects.items():
                    file.write(f"Redirect 301 {old_url} {new_url}\n")
            print(f"Redirects file created successfully at: {file_path}")
        except IOError as e:
            print(f"Error creating redirects file: {e}")

    def check_redirects(self):
        """
        Check the redirects to ensure they are working as expected.
        """
        for old_url, new_url in self.redirects.items():
            try:
                response = requests.get(urljoin(self.old_domain, old_url), allow_redirects=False)
                if response.status_code == 301 and response.headers['Location'] == urljoin(self.new_domain, new_url):
                    print(f"Redirect from {old_url} to {new_url} is working.")
                else:
                    print(f"Redirect from {old_url} to {new_url} is not working.")
            except requests.RequestException as e:
                print(f"Error checking redirect for {old_url}: {e}")

    def notify_search_engines(self):
        """
        Notify search engines about the domain change.
        """
        # This is a placeholder for notifying search engines through their respective APIs.
        print(f"Notifying search engines about the migration from {self.old_domain} to {self.new_domain}...")

    def run_migration(self, redirects, redirects_file_path):
        """
        Run the entire migration process.

        :param redirects: A dictionary of old URL to new URL mappings (dict).
        :param redirects_file_path: The path to save the redirects file (string).
        """
        for old_url, new_url in redirects.items():
            self.generate_redirects(old_url, new_url)
        
        self.create_redirects_file(redirects_file_path)
        self.check_redirects()
        self.notify_search_engines()

# Example usage:
if __name__ == "__main__":
    OLD_DOMAIN = "https://www.oldsite.com"
    NEW_DOMAIN = "https://www.newsite.com"
    
    # Define the redirects (old URL: new URL)
    redirects = {
        "/old-page": "/new-page",
        "/old-about": "/new-about",
        # Add more redirects as necessary
    }

    # Create an instance of SEOMigrationManager
    migration_manager = SEOMigrationManager(OLD_DOMAIN, NEW_DOMAIN)
    
    # Run the migration
    migration_manager.run_migration(redirects, "redirects.htaccess")
```
