"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Write a script to parse and analyze historical text entries (e.g., "Thomas Stevens' biography") from a genealogy website and generate summaries for each individual.
Generated: DETERMINISTIC_bd7c3f6d25eabb0d
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/biographies": {
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
from bs4 import BeautifulSoup
import re
import json
from typing import List, Dict

class BiographyParser:
    def __init__(self, url: str):
        """
        Initialize the BiographyParser with a URL to scrape data from.
        
        :param url: URL of the genealogy website to parse
        """
        self.url = url

    def fetch_data(self) -> str:
        """
        Fetch the HTML content from the provided URL.
        
        :return: HTML content as a string
        :raises Exception: If the request to the URL fails
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch data from {self.url}: {e}")

    def parse_biographies(self, html_content: str) -> List[Dict[str, str]]:
        """
        Parse the HTML content to extract individual biographies.
        
        :param html_content: HTML content of the webpage
        :return: A list of dictionaries containing individual summaries
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        biographies = []

        # Assuming biographies are contained in <div class="biography">
        for bio_div in soup.find_all('div', class_='biography'):
            name = bio_div.find('h2').text.strip()
            summary = self.summarize_biography(bio_div.text.strip())

            biographies.append({
                'name': name,
                'summary': summary
            })

        return biographies

    def summarize_biography(self, text: str) -> str:
        """
        Generate a summary from the full biography text.
        
        :param text: Full biography text
        :return: A concise summary of the biography
        """
        # Simple heuristic: Extract the first two sentences for summary
        sentences = re.split(r'(?<=[.!?]) +', text)
        summary = ' '.join(sentences[:2]) if len(sentences) > 1 else text
        return summary

    def save_to_json(self, data: List[Dict[str, str]], filename: str) -> None:
        """
        Save the parsed biographies to a JSON file.
        
        :param data: List of biographies to save
        :param filename: The file name for the output JSON
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise Exception(f"Failed to write data to {filename}: {e}")

    def run(self, output_filename: str) -> None:
        """
        Run the parser to fetch, parse, and save the biographies.
        
        :param output_filename: The output file name for the JSON data
        """
        html_content = self.fetch_data()
        biographies = self.parse_biographies(html_content)
        self.save_to_json(biographies, output_filename)

if __name__ == "__main__":
    url = "http://example.com/biographies"  # Replace with the actual genealogy website URL
    output_file = "biographies.json"

    parser = BiographyParser(url)
    parser.run(output_file)
```
