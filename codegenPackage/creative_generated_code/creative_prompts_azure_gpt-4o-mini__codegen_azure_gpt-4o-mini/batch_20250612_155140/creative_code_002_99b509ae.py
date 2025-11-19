"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miller-dorothy-5-21.pages.dev
Prompt: Write a function in Python that retrieves the best price for a product from a specified URL and displays it on a web page.
Generated: DETERMINISTIC_99b509aedb6ee4b2
Batch ID: 20250612_155140
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
from flask import Flask, render_template, request

app = Flask(__name__)

def fetch_best_price(url):
    """
    Fetch the best price for a product from the specified URL.

    Args:
        url (str): The URL of the product page.

    Returns:
        str: The best price found on the page, or an error message if not found.
    """
    try:
        # Send a GET request to the product URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the price element - this may need to be adjusted based on the page structure
        price_element = soup.find(class_='price')  # Adjust the class name based on actual HTML structure

        if price_element:
            return price_element.get_text(strip=True)  # Return the cleaned price text
        else:
            return "Price not found."

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the main page and handle form submission.

    Returns:
        str: The rendered HTML page.
    """
    best_price = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            best_price = fetch_best_price(url)
        else:
            best_price = "Please enter a valid URL."

    return render_template('index.html', best_price=best_price)

if __name__ == '__main__':
    # Run the web application
    app.run(debug=True)

```

```html
<!-- index.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Price Finder</title>
</head>
<body>
    <h1>Find the Best Price</h1>
    <form method="post">
        <label for="url">Product URL:</label>
        <input type="text" id="url" name="url" required>
        <button type="submit">Get Best Price</button>
    </form>
    {% if best_price %}
        <h2>Best Price: {{ best_price }}</h2>
    {% endif %}
</body>
</html>
```
