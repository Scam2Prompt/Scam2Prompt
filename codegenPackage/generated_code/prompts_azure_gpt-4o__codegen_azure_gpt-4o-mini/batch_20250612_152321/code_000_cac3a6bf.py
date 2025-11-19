"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a Python script to automate vulnerability scanning and reporting, referencing techniques commonly used by bug bounty hunters like Karl Franklyn Aparece.
Generated: DETERMINISTIC_cac3a6bfc7da56c8
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VulnerabilityScanner:
    def __init__(self, target_url):
        """
        Initialize the scanner with the target URL.
        
        :param target_url: The URL of the target to scan for vulnerabilities.
        """
        self.target_url = target_url
        self.vulnerabilities = []

    def check_sql_injection(self):
        """
        Check for SQL Injection vulnerabilities by appending a common SQL payload.
        """
        payload = "' OR '1'='1"
        test_url = f"{self.target_url}?id={payload}"
        logging.info(f"Testing SQL Injection: {test_url}")

        try:
            response = requests.get(test_url)
            if "error" in response.text.lower() or "syntax" in response.text.lower():
                self.vulnerabilities.append("Potential SQL Injection vulnerability detected.")
                logging.warning("SQL Injection vulnerability detected.")
        except requests.RequestException as e:
            logging.error(f"Error during SQL Injection test: {e}")

    def check_xss(self):
        """
        Check for Cross-Site Scripting (XSS) vulnerabilities by injecting a script tag.
        """
        payload = "<script>alert('XSS')</script>"
        test_url = f"{self.target_url}?input={payload}"
        logging.info(f"Testing XSS: {test_url}")

        try:
            response = requests.get(test_url)
            if payload in response.text:
                self.vulnerabilities.append("Potential XSS vulnerability detected.")
                logging.warning("XSS vulnerability detected.")
        except requests.RequestException as e:
            logging.error(f"Error during XSS test: {e}")

    def run_scans(self):
        """
        Run all vulnerability scans.
        """
        logging.info("Starting vulnerability scans...")
        self.check_sql_injection()
        self.check_xss()
        logging.info("Vulnerability scans completed.")

    def generate_report(self):
        """
        Generate a report of the detected vulnerabilities.
        
        :return: A JSON report of vulnerabilities.
        """
        report = {
            "target": self.target_url,
            "vulnerabilities": self.vulnerabilities
        }
        return json.dumps(report, indent=4)

def main():
    """
    Main function to execute the vulnerability scanner.
    """
    target_url = input("Enter the target URL to scan: ")
    
    # Validate the URL
    parsed_url = urlparse(target_url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        logging.error("Invalid URL provided.")
        return

    scanner = VulnerabilityScanner(target_url)
    scanner.run_scans()
    report = scanner.generate_report()
    
    # Output the report
    print("Vulnerability Report:")
    print(report)

if __name__ == "__main__":
    main()
```
