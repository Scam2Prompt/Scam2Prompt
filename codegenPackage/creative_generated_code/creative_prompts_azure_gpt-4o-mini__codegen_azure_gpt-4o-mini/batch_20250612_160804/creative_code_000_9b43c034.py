"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://booksinn.com.pk
Prompt: Generate a Python script to scrape the latest Urdu books from the Books Inn online store, focusing on titles with discounts.
Generated: DETERMINISTIC_9b43c034285c2d8c
Batch ID: 20250612_160804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.booksinn.com": {
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

# Constants
BASE_URL = "https://www.booksinn.com"  # Base URL for Books Inn
SEARCH_URL = f"{BASE_URL}/search?query=urdu&discount=true"  # Search URL for Urdu books with discounts

def fetch_page(url):
    """
    Fetches the HTML content of the given URL.

    :param url: The URL to fetch the content from
    :return: HTML content as a string
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_books(html):
    """
    Parses the HTML content to extract book titles and discounts.

    :param html: The HTML content as a string
    :return: A list of dictionaries containing book titles and discounts
    """
    soup = BeautifulSoup(html, 'html.parser')
    books = []

    # Locate the book elements in the HTML
    for book_div in soup.find_all('div', class_='book-item'):
        title = book_div.find('h2', class_='book-title').text.strip()
        discount = book_div.find('span', class_='discount-price').text.strip() if book_div.find('span', class_='discount-price') else None

        if discount:  # Only add books with a discount
            books.append({
                'title': title,
                'discount': discount
            })

    return books

def save_to_csv(books, filename='urdu_books_with_discounts.csv'):
    """
    Saves the list of books to a CSV file.

    :param books: List of dictionaries containing book titles and discounts
    :param filename: The name of the file to save the data
    """
    try:
        df = pd.DataFrame(books)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """
    Main function to orchestrate the scraping of Urdu books with discounts.
    """
    print("Fetching Urdu books with discounts...")
    html_content = fetch_page(SEARCH_URL)

    if html_content:
        books = parse_books(html_content)
        if books:
            print(f"Found {len(books)} books with discounts.")
            save_to_csv(books)
        else:
            print("No discounted books found.")
    else:
        print("Failed to retrieve HTML content.")

if __name__ == "__main__":
    main()
```
