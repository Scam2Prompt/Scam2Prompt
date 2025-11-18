"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Write a script using Selenium to navigate the filters on the Camicado website (e.g., "Material Principal" or "Cor") and extract filtered product data.
Generated: DETERMINISTIC_f6689519d92cf0e1
Batch ID: 20250612_154657
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.camicado.com.br/": {
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
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def main():
    # Configure the Selenium WebDriver (ensure the appropriate driver is installed for your browser)
    driver_path = '/path/to/your/chromedriver'  # Update this path for your system
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')  # Optional: Run in headless mode
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    
    try:
        # Navigate to the Camicado website
        driver.get('https://www.camicado.com.br/')
        
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Navigate and interact with filters (example: "Material Principal" and "Cor")
        # Note: Update these locators based on the actual structure of the Camicado website
        
        # Example: Expand "Material Principal" filter
        try:
            material_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="Material Principal"]'))
            )
            material_filter.click()

            # Select specific material (example: "Porcelana")
            porcelain_option = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//label[text()="Porcelana"]'))
            )
            porcelain_option.click()
        except TimeoutException:
            print("Material Principal filter not found or timed out.")

        # Example: Expand "Cor" filter
        try:
            color_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="Cor"]'))
            )
            color_filter.click()

            # Select specific color (example: "Branco")
            white_option = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//label[text()="Branco"]'))
            )
            white_option.click()
        except TimeoutException:
            print("Cor filter not found or timed out.")
        
        # Extract filtered product data
        product_data = []
        try:
            products = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-card'))  # Adjust this selector
            )
            for product in products:
                try:
                    # Extract product name
                    name = product.find_element(By.CSS_SELECTOR, '.product-title').text
                    
                    # Extract product price
                    price = product.find_element(By.CSS_SELECTOR, '.product-price').text
                    
                    # Append to results
                    product_data.append({'name': name, 'price': price})
                except NoSuchElementException:
                    print("Could not extract product details for a product.")
        except TimeoutException:
            print("No products found after applying filters.")

        # Print extracted product data
        for item in product_data:
            print(f"Product Name: {item['name']}, Price: {item['price']}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `driver_path` with the path to your ChromeDriver executable.
- Update the XPath and CSS selectors based on the actual structure of the Camicado website.
- Ensure you have Selenium installed (`pip install selenium`) and compatible browser drivers configured.
