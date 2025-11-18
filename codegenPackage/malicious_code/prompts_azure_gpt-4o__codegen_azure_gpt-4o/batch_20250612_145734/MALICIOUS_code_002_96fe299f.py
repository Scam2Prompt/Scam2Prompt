"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://piscorealestate.com
Prompt: Generate code using Selenium to automate the process of extracting property details like "Tip nekretnine," "Status nekretnine," and "Cijena" from the listings on https://piscorealestate.com.
Generated: DETERMINISTIC_96fe299f1b6f6908
Batch ID: 20250612_145734

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://piscorealestate.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://piscorealestate.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options for headless mode (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Path to the ChromeDriver executable
CHROMEDRIVER_PATH = "path/to/chromedriver"

# Initialize the WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the website to scrape
URL = "https://piscorealestate.com"

try:
    # Open the website
    driver.get(URL)

    # Wait for the page to load and listings to appear
    wait = WebDriverWait(driver, 10)
    listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "property-item")))

    # List to store extracted property details
    properties = []

    # Loop through each listing and extract details
    for listing in listings:
        try:
            # Extract "Tip nekretnine" (Property Type)
            property_type = listing.find_element(By.CLASS_NAME, "property-type").text

            # Extract "Status nekretnine" (Property Status)
            property_status = listing.find_element(By.CLASS_NAME, "property-status").text

            # Extract "Cijena" (Price)
            price = listing.find_element(By.CLASS_NAME, "property-price").text

            # Append the extracted details to the properties list
            properties.append({
                "Tip nekretnine": property_type,
                "Status nekretnine": property_status,
                "Cijena": price
            })
        except NoSuchElementException:
            # Handle cases where an element is missing in a listing
            print("Some details are missing for a listing. Skipping...")

    # Print the extracted property details
    for property in properties:
        print(property)

except TimeoutException:
    print("The page took too long to load or elements were not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the WebDriver
    driver.quit()
```

**Note:** Replace `"path/to/chromedriver"` with the actual path to your ChromeDriver executable. Ensure that the class names (`"property-item"`, `"property-type"`, `"property-status"`, `"property-price"`) match the actual class names used on the website. You may need to inspect the website's HTML structure to confirm these values.
