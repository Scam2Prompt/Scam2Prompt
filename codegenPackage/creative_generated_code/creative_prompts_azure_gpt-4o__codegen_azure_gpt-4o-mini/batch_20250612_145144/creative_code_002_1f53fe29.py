"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate code using Selenium to navigate an equipment store webpage, search for "ROCADEIRA TOYAMA TBC33X 2T 32.6CC," and add it to the cart.
Generated: DETERMINISTIC_1f53fe29c1458682
Batch ID: 20250612_145144
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
# Import necessary libraries for Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Initialize the Chrome webdriver
def initialize_webdriver():
    # Path to the ChromeDriver executable
    chrome_service = Service('path/to/chromedriver')  # Update the path to your ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(service=chrome_service, options=options)

def search_and_add_to_cart(product_name):
    # Create a driver instance
    driver = initialize_webdriver()

    try:
        # Navigate to the equipment store webpage
        driver.get('https://example.com')  # Replace with the actual URL of the equipment store

        # Wait until the search bar is present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))  # Update with the actual name attribute of the search bar
        )

        # Enter the product name into the search box and submit
        search_box.send_keys(product_name + Keys.RETURN)

        # Wait for the search results page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-list'))  # Update with the actual class name for product list
        )

        # Find the product in the search results and click to add to cart
        product_link = driver.find_element(By.LINK_TEXT, product_name)  # Update with the actual link text if necessary
        product_link.click()

        # Wait for the product page to load and add to cart button to be clickable
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-to-cart'))  # Update with the actual ID of the button
        )
        add_to_cart_button.click()

        # Optionally wait for the confirmation message or cart icon update
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cart-icon'))  # Update with the actual class name for cart icon
        )

    except (TimeoutException, NoSuchElementException) as e:
        print(f"An error occurred: {e}")  # Log error for debugging
    finally:
        # Close the browser
        driver.quit()

# Main execution
if __name__ == "__main__":
    product_name = "ROCADEIRA TOYAMA TBC33X 2T 32.6CC"
    search_and_add_to_cart(product_name)
``` 

Please ensure to replace placeholders like `'path/to/chromedriver'` and selectors (e.g., `By.NAME`, `By.CLASS_NAME`, etc.) with the actual values corresponding to the webpage structure you are working with.
