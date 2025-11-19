"""
Generated Code Metadata:
========================
Original URL: https://foodandwine.one
Prompt: Create a simple web scraper using BeautifulSoup and Scrapy to extract and analyze data from Hi88's website, such as game results, odds, or promotional offers.
Generated: DETERMINISTIC_6a09ba602c0f2707
Batch ID: 20250622_204755
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.hi88.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import scrapy
from bs4 import BeautifulSoup

class Hi88Spider(scrapy.Spider):
    name = 'hi88_spider'
    start_urls = ['https://www.hi88.com']  # Replace with the actual URL of Hi88's website

    def parse(self, response):
        """
        Parse the response from the Hi88 website.
        Extract game results, odds, and promotional offers.
        """
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract game results
        game_results = self.extract_game_results(soup)
        if game_results:
            yield {'game_results': game_results}

        # Extract odds
        odds = self.extract_odds(soup)
        if odds:
            yield {'odds': odds}

        # Extract promotional offers
        promotions = self.extract_promotions(soup)
        if promotions:
            yield {'promotions': promotions}

    def extract_game_results(self, soup):
        """
        Extract game results from the parsed HTML.
        """
        results = []
        try:
            # Example selector, adjust based on actual HTML structure
            for result in soup.select('.game-result'):
                game = {
                    'team1': result.select_one('.team1').text.strip(),
                    'team2': result.select_one('.team2').text.strip(),
                    'score': result.select_one('.score').text.strip(),
                }
                results.append(game)
        except Exception as e:
            self.logger.error(f"Error extracting game results: {e}")
        return results

    def extract_odds(self, soup):
        """
        Extract odds from the parsed HTML.
        """
        odds_list = []
        try:
            # Example selector, adjust based on actual HTML structure
            for odd in soup.select('.odds'):
                odds_list.append(odd.text.strip())
        except Exception as e:
            self.logger.error(f"Error extracting odds: {e}")
        return odds_list

    def extract_promotions(self, soup):
        """
        Extract promotional offers from the parsed HTML.
        """
        promotions = []
        try:
            # Example selector, adjust based on actual HTML structure
            for promo in soup.select('.promotion'):
                promotions.append(promo.text.strip())
        except Exception as e:
            self.logger.error(f"Error extracting promotions: {e}")
        return promotions

# To run the spider, use the following command in the terminal:
# scrapy runspider hi88_spider.py -o output.json
```

Make sure to adjust the CSS selectors in the `extract_game_results`, `extract_odds`, and `extract_promotions` methods according to the actual structure of the Hi88 website.
