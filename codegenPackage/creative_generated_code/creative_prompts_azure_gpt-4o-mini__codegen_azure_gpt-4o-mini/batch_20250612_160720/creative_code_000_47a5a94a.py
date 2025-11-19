"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zagoranews.com
Prompt: Generate a news summary about the recent events in Zagora, including the celebration of top students at the secondary school Amzrou and the concerns raised by the Moroccan Association for Human Rights regarding water issues in Takouinet.
Generated: DETERMINISTIC_47a5a94a67176f25
Batch ID: 20250612_160720
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example-news-website.com": {
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

class NewsScraper:
    def __init__(self):
        self.base_url = "https://www.example-news-website.com"  # Replace with the actual news website

    def fetch_news(self):
        """
        Fetches the news from the specified URL.
        
        Returns:
            str: The raw HTML content of the news page.
        """
        try:
            response = requests.get(self.base_url + "/zagora-news")
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
            return None

    def parse_news(self, html_content):
        """
        Parses the HTML content and extracts relevant news summaries.
        
        Args:
            html_content (str): The raw HTML content of the news page.
        
        Returns:
            dict: A dictionary containing news summaries.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        news_summary = {}

        # Extract celebration event details
        celebration_section = soup.find('section', {'id': 'celebration'})
        if celebration_section:
            students = celebration_section.find_all('li')
            news_summary['celebration'] = {
                'event': 'Celebration of Top Students',
                'students': [student.get_text() for student in students]
            }

        # Extract human rights concerns
        concerns_section = soup.find('section', {'id': 'human-rights'})
        if concerns_section:
            concerns = concerns_section.get_text()
            news_summary['human_rights_concerns'] = {
                'organization': 'Moroccan Association for Human Rights',
                'issues': concerns
            }

        return news_summary

    def generate_summary(self):
        """
        Generates a news summary and prints it to the console.
        """
        html_content = self.fetch_news()
        if html_content:
            summary = self.parse_news(html_content)
            self.print_summary(summary)

    def print_summary(self, summary):
        """
        Prints the news summary in a readable format.
        
        Args:
            summary (dict): The news summary to print.
        """
        print("News Summary:")
        print("\nCelebration of Top Students:")
        if 'celebration' in summary:
            print(f"Event: {summary['celebration']['event']}")
            print("Students:")
            for student in summary['celebration']['students']:
                print(f"- {student}")

        print("\nHuman Rights Concerns:")
        if 'human_rights_concerns' in summary:
            print(f"Organization: {summary['human_rights_concerns']['organization']}")
            print(f"Issues: {summary['human_rights_concerns']['issues']}")

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.generate_summary()
```
