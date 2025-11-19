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
  "https://booksinn.pk/": {
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

def fetch_books_inn_discounted_urdu_books():
    """
    Scrapes the Books Inn website for the latest Urdu books with discounts.
    
    Returns:
        list[dict]: A list of dictionaries containing book information.
    """
    # URL to Books Inn's Urdu books section (adjust as per the real URL)
    base_url = "https://booksinn.pk/"
    urdu_books_url = f"{base_url}product-category/urdu-books/"

    try:
        # Fetch the webpage content
        response = requests.get(urdu_books_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the webpage: {e}")
        return []

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize the list to store book information
    discounted_books = []

    # Find the book elements (adjust the selectors as per the website's structure)
    book_items = soup.find_all('div', class_='product-grid-item')  # Example class name
    
    for book in book_items:
        try:
            # Extract book title
            title_element = book.find('h3', class_='product-title')  # Example class name
            title = title_element.text.strip() if title_element else "Unknown Title"
            
            # Extract discount availability
            discount_element = book.find('span', class_='onsale')  # Example class name for discounts
            discount_text = discount_element.text.strip() if discount_element else None

            # Extract book price
            price_element = book.find('span', class_='price')  # Example class name
            price = price_element.text.strip() if price_element else "Price Not Available"

            # Add to the list if the book has a discount
            if discount_text:
                discounted_books.append({
                    "title": title,
                    "discount": discount_text,
                    "price": price,
                })

        except Exception as e:
            print(f"Error while processing a book entry: {e}")
            continue

    return discounted_books


if __name__ == "__main__":
    # Fetch the discounted Urdu books
    books = fetch_books_inn_discounted_urdu_books()

    # Display the results
    if books:
        print("Latest Discounted Urdu Books:")
        for book in books:
            print(f"Title: {book['title']}")
            print(f"Discount: {book['discount']}")
            print(f"Price: {book['price']}")
            print("-" * 40)
    else:
        print("No discounted Urdu books found or an error occurred.")
```

Note: The class names and selectors in the example (`'product-grid-item'`, `'product-title'`, `'onsale'`, `'price'`) are placeholders and may need adjustments based on the actual structure of the Books Inn website. You should inspect the website's HTML structure to find the correct selectors.
