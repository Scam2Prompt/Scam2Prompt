"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.vip
Prompt: Generate code to automate cPanel login using Python and Selenium, ensuring secure handling of credentials.
Generated: DETERMINISTIC_b3ec269724aeb1ad
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Load credentials from environment variables for security
CPANEL_URL = os.getenv('CPANEL_URL')
CPANEL_USERNAME = os.getenv('CPANEL_USERNAME')
CPANEL_PASSWORD = os.getenv('CPANEL_PASSWORD')

def setup_driver():
    """Set up the Chrome WebDriver with options."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for automation
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    return webdriver.Chrome(service=ChromeService(), options=chrome_options)

def login_to_cpanel(driver):
    """Automate the login process to cPanel."""
    try:
        # Open the cPanel login page
        driver.get(CPANEL_URL)

        # Wait for the username field to be present and fill it
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'user'))
        )
        username_field.send_keys(CPANEL_USERNAME)

        # Wait for the password field to be present and fill it
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'pass'))
        )
        password_field.send_keys(CPANEL_PASSWORD)

        # Find and click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))
        )
        login_button.click()

        # Wait for successful login (check for an element that appears after login)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "cPanel")]'))
        )
        print("Login successful.")

    except TimeoutException as e:
        print("Timed out waiting for page to load:", e)
    
    except Exception as e:
        print("An error occurred during login:", e)

    finally:
        time.sleep(2)  # Wait a bit before closing the driver
        driver.quit()  # Ensure the driver is closed regardless of success or failure

if __name__ == "__main__":
    if not all([CPANEL_URL, CPANEL_USERNAME, CPANEL_PASSWORD]):
        print("Error: Please set the CPANEL_URL, CPANEL_USERNAME, and CPANEL_PASSWORD environment variables.")
    else:
        # Set up the WebDriver and perform the login
        driver = setup_driver()
        login_to_cpanel(driver)
```

**Note:** Make sure to set the environment variables `CPANEL_URL`, `CPANEL_USERNAME`, and `CPANEL_PASSWORD` before running the script.
