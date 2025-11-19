"""
Generated Code Metadata:
========================
Original URL: https://remote-job.org
Prompt: Generate a Python code example for an Automation Quality Engineer II task, using popular libraries and frameworks for automation testing.
Generated: DETERMINISTIC_7b0fbbcfa1e58d59
Batch ID: 20250622_210027
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

# Generated Code:
# ===============

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestLoginFunctionality(unittest.TestCase):
    """
    Test suite for verifying login functionality of a web application.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        This method is called once before all tests.
        """
        # Initialize the WebDriver using ChromeDriverManager
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.base_url = "https://example.com"  # Replace with the target URL

    def setUp(self):
        """
        Set up before each test case.
        """
        self.driver.get(self.base_url)

    def test_valid_login(self):
        """
        Test case for valid login credentials.
        """
        try:
            # Locate and interact with the username field
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("valid_user")

            # Locate and interact with the password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("valid_password")

            # Submit the login form
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Wait for the page to load
            time.sleep(3)

            # Verify successful login by checking the presence of a dashboard element
            dashboard_element = self.driver.find_element(By.ID, "dashboard")
            self.assertTrue(dashboard_element.is_displayed(), "Dashboard is not displayed after login.")

        except Exception as e:
            self.fail(f"Valid login test failed due to an exception: {e}")

    def test_invalid_login(self):
        """
        Test case for invalid login credentials.
        """
        try:
            # Locate and interact with the username field
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("invalid_user")

            # Locate and interact with the password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("invalid_password")

            # Submit the login form
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Wait for the page to load
            time.sleep(3)

            # Verify error message is displayed
            error_message = self.driver.find_element(By.ID, "error-message")
            self.assertTrue(error_message.is_displayed(), "Error message is not displayed for invalid login.")

        except Exception as e:
            self.fail(f"Invalid login test failed due to an exception: {e}")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment.
        This method is called once after all tests.
        """
        cls.driver.quit()


if __name__ == "__main__":
    # Run the test suite
    unittest.main()
```
