"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Develop a vulnerability scanning tool for web applications, inspired by Icchatva's cyber security solutions for application testing.
Generated: DETERMINISTIC_bd2e4899e40f869e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re

class VulnerabilityScanner:
    """
    A simple vulnerability scanning tool for web applications inspired by Icchatva's cybersecurity solutions.
    Scans for common vulnerabilities such as XSS, open redirects, and forms without CSRF protection.
    """

    def __init__(self, base_url):
        """
        Initializes the scanner with a base URL.

        Args:
            base_url (str): The URL of the web application to scan.
        """
        self.base_url = base_url
        self.scanned_urls = set()
        self.vulnerabilities = []

    def is_valid_url(self, url):
        """
        Checks if a URL belongs to the target domain.

        Args:
            url (str): The URL to validate.

        Returns:
            bool: True if the URL belongs to the base domain, False otherwise.
        """
        parsed_base = urlparse(self.base_url)
        parsed_url = urlparse(url)
        return parsed_base.netloc == parsed_url.netloc

    def get_all_links(self, url):
        """
        Extracts all links from a webpage.

        Args:
            url (str): The target URL.

        Returns:
            list: A list of extracted links.
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            links = [urljoin(url, anchor.get('href')) for anchor in soup.find_all('a', href=True)]
            return filter(self.is_valid_url, links)
        except requests.RequestException as e:
            print(f"Error fetching links from {url}: {str(e)}")
            return []

    def scan_for_xss(self, url):
        """
        Scans a webpage for potential XSS vulnerabilities.

        Args:
            url (str): The target URL.
        """
        try:
            response = requests.get(url)
            if '<script>' in response.text.lower():
                self.vulnerabilities.append({'url': url, 'type': 'Potential XSS vulnerability detected.'})
        except requests.RequestException as e:
            print(f"Error scanning {url} for XSS: {str(e)}")

    def scan_for_open_redirects(self, url):
        """
        Scans a URL for potential open redirect vulnerabilities.

        Args:
            url (str): The target URL.
        """
        try:
            parsed_url = urlparse(url)
            if 'redirect' in parsed_url.query.lower() or 'url' in parsed_url.query.lower():
                self.vulnerabilities.append({'url': url, 'type': 'Potential Open Redirect vulnerability detected.'})
        except Exception as e:
            print(f"Error scanning {url} for redirects: {str(e)}")

    def scan_forms_for_csrf(self, url):
        """
        Scans forms on a webpage for missing CSRF tokens.

        Args:
            url (str): The target URL.
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            forms = soup.find_all('form')
            for form in forms:
                if not any(input_tag.get('name') for input_tag in form.find_all('input') if 'csrf' in input_tag.get('name', '').lower()):
                    self.vulnerabilities.append({'url': url, 'type': 'Form missing CSRF token.'})
        except requests.RequestException as e:
            print(f"Error scanning forms on {url}: {str(e)}")

    def scan_url(self, url):
        """
        Scans a single URL for vulnerabilities.

        Args:
            url (str): The URL to scan.
        """
        if url in self.scanned_urls:
            return

        print(f"Scanning {url}...")
        self.scanned_urls.add(url)

        # Scan for specific vulnerabilities
        self.scan_for_xss(url)
        self.scan_for_open_redirects(url)
        self.scan_forms_for_csrf(url)

        # Recursively scan links found on the page
        for link in self.get_all_links(url):
            self.scan_url(link)

    def run(self):
        """
        Starts the vulnerability scanning process.
        """
        print(f"Starting scan for {self.base_url}...")
        self.scan_url(self.base_url)
        print("Scan complete. Vulnerabilities found:")
        for vulnerability in self.vulnerabilities:
            print(vulnerability)


if __name__ == "__main__":
    # Base URL of the web application to scan
    base_url = input("Enter the base URL of the web application: ").strip()
    
    # Ensure the URL is valid and starts with http or https
    if not re.match(r'^https?://', base_url):
        print("Invalid URL. Please enter a valid URL starting with http:// or https://")
    else:
        scanner = VulnerabilityScanner(base_url)
        scanner.run()
```
