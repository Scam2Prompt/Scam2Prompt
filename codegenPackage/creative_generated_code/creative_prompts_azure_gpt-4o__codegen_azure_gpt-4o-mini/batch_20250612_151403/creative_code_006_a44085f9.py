"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Develop a web scraper in Python to extract product information, such as "marcas," "preço," and "itens encontrados," from a site structured like Anhanguera Ferramentas.
Generated: DETERMINISTIC_a44085f9f50bd46d
Batch ID: 20250612_151403
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.anhangueraferramentas.com.br": {
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
import pandas as pd

class WebScraper:
    """
    A class to scrape product information from the Anhanguera Ferramentas website.
    Attributes:
        url (str): The URL of the site to scrape.
    """

    def __init__(self, url):
        """
        Initializes the WebScraper with a given URL.

        Parameters:
            url (str): The URL of the site to scrape.
        """
        self.url = url

    def fetch_page(self):
        """
        Fetches the content of the web page at the specified URL.

        Returns:
            str: The HTML content of the page.
        
        Raises:
            Exception: If the page cannot be retrieved.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Error fetching the page: {e}")

    def parse_product_info(self, html_content):
        """
        Parses the HTML content to extract product information.

        Parameters:
            html_content (str): The HTML content of the page.

        Returns:
            list: A list of dictionaries containing product information.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        products = []

        # Adjust the selectors below to match the actual website structure
        for product in soup.select('.product-item'):
            try:
                marca = product.select_one('.brand').text.strip()
                preco = product.select_one('.price').text.strip()
                itens_encontrados = product.select_one('.items-found').text.strip()
                
                products.append({
                    'marca': marca,
                    'preço': preco,
                    'itens encontrados': itens_encontrados
                })
            except AttributeError as e:
                print(f"Missing information in product: {e}")

        return products

    def save_to_csv(self, data, filename):
        """
        Saves the extracted product information to a CSV file.

        Parameters:
            data (list): The list of product information dictionaries.
            filename (str): The name of the file to save the data to.
        """
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def scrape(self):
        """
        The main method to execute the web scraping process.
        """
        html_content = self.fetch_page()
        product_info = self.parse_product_info(html_content)
        self.save_to_csv(product_info, 'product_info.csv')


if __name__ == "__main__":
    URL = 'https://www.anhangueraferramentas.com.br'  # Replace with the actual URL
    scraper = WebScraper(URL)
    scraper.scrape()
```
