"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: What steps should I take to reset my cPanel password if I encounter issues with JavaScript being disabled?
Generated: DETERMINISTIC_28a869ae2cf6a267
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example Python script using the `selenium` library to automate resetting a cPanel password. The code assumes that JavaScript is disabled and navigates the HTML structure accordingly.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys

def reset_cpanel_password(cpanel_url, username, email):
    """
    Automates the process of resetting a cPanel password with JavaScript disabled.
    
    Args:
        cpanel_url (str): The URL of the cPanel login page.
        username (str): The cPanel username.
        email (str): The email associated with the cPanel account.

    Returns:
        None
    """
    try:
        # Initialize the Selenium WebDriver with JavaScript disabled
        options = webdriver.FirefoxOptions()
        options.set_preference("javascript.enabled", False)  # Disable JavaScript
        driver = webdriver.Firefox(options=options)

        # Open the cPanel login page
        driver.get(cpanel_url)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        # Locate and click the "Reset Password" link (or equivalent element)
        try:
            reset_link = driver.find_element(By.LINK_TEXT, "Reset Password")
            reset_link.click()
        except NoSuchElementException:
            print("Reset Password link not found.")
            driver.quit()
            return

        # Fill out the username field
        try:
            username_field = driver.find_element(By.NAME, "username")
            username_field.send_keys(username)
        except NoSuchElementException:
            print("Username field not found.")
            driver.quit()
            return

        # Fill out the email field
        try:
            email_field = driver.find_element(By.NAME, "email")
            email_field.send_keys(email)
        except NoSuchElementException:
            print("Email field not found.")
            driver.quit()
            return

        # Submit the form
        try:
            submit_button = driver.find_element(By.NAME, "submit")
            submit_button.click()
        except NoSuchElementException:
            print("Submit button not found.")
            driver.quit()
            return

        # Wait for confirmation message
        try:
            confirmation_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "confirmation"))
            )
            print("Confirmation message:", confirmation_message.text)
        except TimeoutException:
            print("Confirmation message not displayed within the expected time.")

    except Exception as e:
        # Handle unexpected exceptions
        print("An error occurred:", str(e))
    finally:
        # Ensure the browser is closed to free up resources
        driver.quit()


if __name__ == "__main__":
    # Example usage
    if len(sys.argv) != 4:
        print("Usage: python reset_cpanel_password.py <cpanel_url> <username> <email>")
        sys.exit(1)

    cpanel_url = sys.argv[1]
    username = sys.argv[2]
    email = sys.argv[3]

    reset_cpanel_password(cpanel_url, username, email)
```

### Notes:
- Install Selenium if not already done: `pip install selenium`.
- Ensure you have the GeckoDriver executable installed for the Firefox driver.
- This script works in environments where JavaScript is disabled.
- Replace `cpanel_url` with the actual URL of your cPanel login page.
