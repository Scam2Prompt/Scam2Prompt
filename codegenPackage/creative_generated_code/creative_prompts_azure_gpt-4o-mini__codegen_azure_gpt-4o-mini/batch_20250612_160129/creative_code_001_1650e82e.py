"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woo-finance.com
Prompt: Write a Python script that utilizes the SEO综合查询 feature to analyze the SEO performance of a given website.
Generated: DETERMINISTIC_1650e82e1e1a7d9b
Batch ID: 20250612_160129
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.seo.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
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

class SEOAnalyzer:
    """
    A class to analyze the SEO performance of a given website using the SEO综合查询 feature.
    """

    def __init__(self, base_url):
        """
        Initializes the SEOAnalyzer with the base URL of the API.

        :param base_url: str - The base URL for the SEO analysis API.
        """
        self.base_url = base_url

    def fetch_seo_data(self, website):
        """
        Fetches SEO data for the specified website.

        :param website: str - The website URL to analyze.
        :return: dict - The SEO data response from the API.
        :raises ValueError: If the website URL is invalid.
        :raises Exception: If an error occurs during the API request.
        """
        if not self.is_valid_url(website):
            raise ValueError("Invalid website URL provided.")

        try:
            response = requests.get(f"{self.base_url}/analyze?url={website}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching SEO data: {e}")

    @staticmethod
    def is_valid_url(url):
        """
        Validates the URL format.

        :param url: str - The URL to validate.
        :return: bool - True if the URL is valid, False otherwise.
        """
        return url.startswith("http://") or url.startswith("https://")

    def analyze(self, website):
        """
        Analyzes the SEO performance of the given website.

        :param website: str - The website URL to analyze.
        """
        try:
            seo_data = self.fetch_seo_data(website)
            self.display_results(seo_data)
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def display_results(seo_data):
        """
        Displays the SEO analysis results.

        :param seo_data: dict - The SEO data received from the API.
        """
        print("SEO Analysis Results:")
        for key, value in seo_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    BASE_URL = "https://api.seo.com"  # Replace with the actual API base URL
    website_to_analyze = input("Enter the website URL to analyze: ")

    # Create an instance of the SEOAnalyzer
    analyzer = SEOAnalyzer(BASE_URL)

    # Perform the analysis
    analyzer.analyze(website_to_analyze)
```

Make sure to replace `"https://api.seo.com"` with the actual base URL of the SEO综合查询 API you intend to use.
