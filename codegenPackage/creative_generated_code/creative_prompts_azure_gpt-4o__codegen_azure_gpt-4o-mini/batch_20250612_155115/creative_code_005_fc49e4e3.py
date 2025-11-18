"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymixer.xyz
Prompt: Create a program that checks the SSL Labs Grade A rating for a website and ensures no HTTP traffic or CDN usage, as emphasized on Anonymixer's site.
Generated: DETERMINISTIC_fc49e4e3747b29a0
Batch ID: 20250612_155115
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.ssllabs.com/api/v3/analyze?host={self.website": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://{self.website": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{self.website": {
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

class SSLGradeChecker:
    """
    A class to check the SSL Labs Grade of a given website.
    It also checks for HTTP traffic and CDN usage.
    """

    def __init__(self, website):
        """
        Initializes the SSLGradeChecker with the given website.

        Args:
            website (str): The website URL to check.
        """
        self.website = website

    def check_ssl_grade(self):
        """
        Checks the SSL Labs grade for the website.

        Returns:
            str: The SSL grade of the website.
        """
        url = f"https://api.ssllabs.com/api/v3/analyze?host={self.website}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            
            # Check if the analysis has completed
            if 'endpoints' in data and isinstance(data['endpoints'], list) and len(data['endpoints']) > 0:
                grade = data['endpoints'][0].get('grade', 'Not Available')
                return grade
            else:
                return "Grade not available, analysis might be in progress."
        except requests.RequestException as e:
            return f"Error while checking SSL grade: {e}"

    def check_http_and_cdn(self):
        """
        Checks if the website uses HTTP or CDN.

        Returns:
            bool: True if HTTP or CDN is detected, otherwise False.
        """
        try:
            # Check if the website is reachable via HTTP
            http_response = requests.get(f"http://{self.website}", timeout=5)
            if http_response.ok:
                return True  # HTTP traffic detected

            # Check headers for CDN usage
            https_response = requests.get(f"https://{self.website}", timeout=5)
            cdn_headers = ['via', 'x-cache', 'xcdn']
            for header in cdn_headers:
                if header in https_response.headers:
                    return True  # CDN usage detected

            return False  # No HTTP traffic or CDN detected
        except requests.RequestException:
            return False  # Treat any error as no HTTP or CDN usage

    def run_checks(self):
        """
        Runs the SSL grade check and HTTP/CDN checks, printing results.
        """
        ssl_grade = self.check_ssl_grade()
        is_http_or_cdn = self.check_http_and_cdn()

        print(f"SSL Grade for {self.website}: {ssl_grade}")
        if is_http_or_cdn:
            print("Warning: HTTP traffic or CDN usage detected.")
        else:
            print("No HTTP traffic or CDN usage detected.")


if __name__ == "__main__":
    # Sample usage; replace 'example.com' with your target domain
    website_to_check = "example.com"  # Change this to the desired website
    checker = SSLGradeChecker(website_to_check)
    checker.run_checks()
```
