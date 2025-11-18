"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Write a script to automate the generation of monthly current affairs tests using data from national and international sources, similar to Shield IAS's approach.
Generated: DETERMINISTIC_f45e0d39172cc4a3
Batch ID: 20250612_154422
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/international-current-affairs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/national-current-affairs": {
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
from datetime import datetime
import json
import random
import os

# Define constants for the sources of current affairs
SOURCE_URLS = {
    "national": "https://example.com/national-current-affairs",
    "international": "https://example.com/international-current-affairs"
}

# Define a class to handle current affairs test generation
class CurrentAffairsTestGenerator:
    def __init__(self, source_urls):
        self.source_urls = source_urls
        self.current_affairs_data = []

    def fetch_current_affairs(self):
        """Fetch current affairs data from the specified sources."""
        for category, url in self.source_urls.items():
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract current affairs data from the HTML
                articles = soup.find_all('article')
                for article in articles:
                    title = article.find('h2').text
                    summary = article.find('p').text
                    self.current_affairs_data.append({
                        'title': title,
                        'summary': summary,
                        'category': category
                    })
            except requests.RequestException as e:
                print(f"Error fetching data from {url}: {e}")

    def generate_test(self, num_questions=10):
        """Generate a test from the fetched current affairs data."""
        if not self.current_affairs_data:
            print("No current affairs data available to generate a test.")
            return []

        # Randomly select questions from the current affairs data
        selected_questions = random.sample(self.current_affairs_data, min(num_questions, len(self.current_affairs_data)))
        return selected_questions

    def save_test_to_file(self, test_data, filename):
        """Save the generated test to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(test_data, f, indent=4)
            print(f"Test saved to {filename}")
        except IOError as e:
            print(f"Error saving test to file: {e}")

def main():
    """Main function to automate current affairs test generation."""
    test_generator = CurrentAffairsTestGenerator(SOURCE_URLS)

    # Fetch the current affairs data
    test_generator.fetch_current_affairs()

    # Generate a test with 10 questions
    test_data = test_generator.generate_test(num_questions=10)

    # Create a filename based on the current date
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"current_affairs_test_{today}.json"

    # Save the test to a file
    if test_data:
        test_generator.save_test_to_file(test_data, filename)

if __name__ == '__main__':
    main()
```
