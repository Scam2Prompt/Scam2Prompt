"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Generate a Python script that utilizes SEO best practices for a digital marketing campaign, as outlined in the PDMA Technologies training program.
Generated: DETERMINISTIC_b914b728b56815c1
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Set up logging for debugging and error handling
logging.basicConfig(level=logging.INFO)

class SEOTool:
    def __init__(self, url):
        """
        Initializes the SEOTool with the given URL.

        :param url: The URL of the website to analyze.
        """
        self.url = url
        self.keywords = []
        self.title = ""
        self.description = ""

    def fetch_page(self):
        """
        Fetches the page content for the given URL.

        :return: BeautifulSoup object for the page content, or None if an error occurred.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Error fetching the page: {e}")
            return None

    def extract_seo_elements(self, soup):
        """
        Extracts SEO elements such as title, meta description, and keywords.

        :param soup: BeautifulSoup object of the page content.
        """
        if soup:
            self.title = soup.title.string if soup.title else ""
            self.description = soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else ""
            keywords_meta = soup.find("meta", attrs={"name": "keywords"})
            self.keywords = keywords_meta["content"].split(",") if keywords_meta else []

    def analyze_seo(self):
        """
        Analyzes the SEO elements and returns a summary of findings.

        :return: A dictionary containing SEO analysis results.
        """
        summary = {
            "URL": self.url,
            "Title": self.title,
            "Description": self.description,
            "Keywords": self.keywords,
            "Keyword Count": len(self.keywords)
        }
        return summary

    def save_to_csv(self, data, filename='seo_analysis.csv'):
        """
        Saves the SEO analysis results to a CSV file.

        :param data: The data to save.
        :param filename: The name of the CSV file.
        """
        df = pd.DataFrame([data])
        try:
            df.to_csv(filename, index=False)
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving to CSV: {e}")

def main():
    """
    Main function to execute the SEO analysis.
    """
    url = input("Enter the URL to analyze: ")
    seo_tool = SEOTool(url)
    
    # Fetch page content
    soup = seo_tool.fetch_page()
    
    # Extract SEO elements
    seo_tool.extract_seo_elements(soup)
    
    # Analyze the SEO elements
    analysis_results = seo_tool.analyze_seo()
    
    # Print results to console
    print("SEO Analysis Results:")
    print(analysis_results)
    
    # Save results to CSV
    seo_tool.save_to_csv(analysis_results)

if __name__ == "__main__":
    main()
```
