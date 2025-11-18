"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-ondo.org
Prompt: Generate code using Selenium to simulate a user navigating the "스타배송" section of https://rewards-ondo.org and extracting shipping details for products.
Generated: DETERMINISTIC_11a7707aafc70f9e
Batch ID: 20250612_152658
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rewards-ondo.org": {
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration for Selenium WebDriver
driver_path = 'path/to/chromedriver'  # Replace with the path to your ChromeDriver
url = 'https://rewards-ondo.org'

def initialize_driver():
    """Initialize the WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for efficiency
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver

def navigate_to_star_delivery(driver):
    """Navigate to the '스타배송' section."""
    try:
        driver.get(url)
        # Wait for the page to load and display the '스타배송' section
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, '스타배송')))
        
        # Click on the '스타배송' link
        star_delivery_link = driver.find_element(By.LINK_TEXT, '스타배송')
        star_delivery_link.click()
        
        # Wait for the products to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list')))
    except Exception as e:
        print(f"Error navigating to '스타배송': {e}")
        driver.quit()

def extract_shipping_details(driver):
    """Extract shipping details for products in the '스타배송' section."""
    try:
        # Locate all products in the product list
        products = driver.find_elements(By.CSS_SELECTOR, '.product-list .product-item')
        shipping_details = []

        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, '.product-name').text
            shipping_info = product.find_element(By.CSS_SELECTOR, '.shipping-info').text
            
            # Append extracted details to the list
            shipping_details.append({
                'product_name': product_name,
                'shipping_info': shipping_info
            })
        
        return shipping_details
    except Exception as e:
        print(f"Error extracting shipping details: {e}")
        return []

def main():
    """Main function to execute the web scraping."""
    driver = initialize_driver()
    try:
        navigate_to_star_delivery(driver)
        shipping_details = extract_shipping_details(driver)

        # Output the extracted shipping details
        for detail in shipping_details:
            print(detail)
    finally:
        driver.quit()  # Ensure the driver is closed regardless of success or failure

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/chromedriver'` with the actual path to your ChromeDriver executable. Additionally, ensure that you have the required libraries installed (`selenium`), and that the appropriate WebDriver for your browser is available.
