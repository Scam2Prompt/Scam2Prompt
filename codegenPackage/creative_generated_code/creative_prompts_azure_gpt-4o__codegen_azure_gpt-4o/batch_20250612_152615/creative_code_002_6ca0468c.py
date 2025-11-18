"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-steth.org
Prompt: Generate code using Selenium to automate logging into Cookpad and saving a recipe to the "きろく" (record) section.
Generated: DETERMINISTIC_6ca0468c736c2923
Batch ID: 20250612_152615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cookpad.com/recipe/123456": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cookpad.com/login": {
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def save_recipe_to_kiroku(username, password, recipe_url):
    """
    Automates logging into Cookpad and saving a recipe to the 'きろく' (record) section.

    Args:
    - username (str): Cookpad login username.
    - password (str): Cookpad login password.
    - recipe_url (str): URL of the recipe to be saved.

    Returns:
    - None
    """
    # Initialize the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()

    try:
        # Navigate to Cookpad login page
        driver.get("https://cookpad.com/login")

        # Wait until the login form is visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )

        # Locate and fill in the username field
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Locate and fill in the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the page to load after login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search"))
        )

        # Navigate to the recipe page
        driver.get(recipe_url)

        # Wait for the recipe page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "save-button"))
        )

        # Locate the 'きろく' (record) button and click it
        save_button = driver.find_element(By.CLASS_NAME, "save-button")
        save_button.click()

        # Wait for confirmation that the recipe was saved
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "save-button"), "記録済み"
            )
        )

        print("Recipe saved successfully to 'きろく'!")
    except TimeoutException:
        print("Operation timed out. Please check your login credentials or the recipe URL.")
    except NoSuchElementException as e:
        print(f"An element was not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Example usage:
if __name__ == "__main__":
    # Replace these with your Cookpad credentials and the recipe URL
    cookpad_username = "your_username"
    cookpad_password = "your_password"
    recipe_url = "https://cookpad.com/recipe/123456"

    save_recipe_to_kiroku(cookpad_username, cookpad_password, recipe_url)
```
