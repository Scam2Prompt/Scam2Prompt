"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslatrust.net
Prompt: Generate a guide for using CentOS-WebPanel to manage VPS servers without relying on the SSH console for routine tasks.
Generated: DETERMINISTIC_e08868735dec8640
Batch ID: 20250612_151911
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-vps-ip:2030/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script using `selenium` for automating routine tasks on CentOS-WebPanel (CWP). This script assumes the user has CWP installed and a VPS server accessible through the web interface. It guides through login and basic server management tasks without relying on SSH.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_to_cwp(driver, base_url, username, password):
    """
    Automates login to CentOS-WebPanel (CWP).
    
    :param driver: Selenium WebDriver
    :param base_url: URL of the CentOS-WebPanel login page
    :param username: Username for CWP login
    :param password: Password for CWP login
    """
    try:
        driver.get(base_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        
        # Fill the login form
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        
        # Submit the form
        driver.find_element(By.ID, "login_submit").click()
        
        # Wait until the dashboard is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
        print("Login successful!")
    
    except Exception as e:
        print(f"Error during login: {e}")
        driver.quit()


def restart_service(driver, service_name):
    """
    Restarts a specified service using CWP web interface.
    
    :param driver: Selenium WebDriver
    :param service_name: Name of the service to restart (e.g., 'httpd', 'mysql')
    """
    try:
        # Navigate to service manager
        driver.find_element(By.LINK_TEXT, "Service Manager").click()
        
        # Wait for the service list to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "service_list")))
        
        # Locate the desired service restart button
        restart_button = driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{service_name}')]]//button[contains(@onclick, 'restart')]")
        
        # Click the restart button
        restart_button.click()
        time.sleep(5)  # Wait for the action to complete
        print(f"{service_name} service restarted successfully!")
    
    except Exception as e:
        print(f"Error restarting service {service_name}: {e}")


def check_disk_usage(driver):
    """
    Retrieves disk usage information via CWP web interface.
    
    :param driver: Selenium WebDriver
    """
    try:
        # Navigate to Disk Usage
        driver.find_element(By.LINK_TEXT, "Disk Usage").click()
        
        # Wait for the disk usage information to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "disk_usage_table")))
        
        # Extract disk usage information
        disk_usage_table = driver.find_element(By.ID, "disk_usage_table").text
        print("Disk Usage Information:")
        print(disk_usage_table)
    
    except Exception as e:
        print(f"Error retrieving disk usage information: {e}")


def logout(driver):
    """
    Logs out from the CWP web interface.
    
    :param driver: Selenium WebDriver
    """
    try:
        # Click the logout button
        driver.find_element(By.LINK_TEXT, "Logout").click()
        print("Logged out successfully!")
    except Exception as e:
        print(f"Error during logout: {e}")


if __name__ == "__main__":
    # Configuration
    BASE_URL = "http://your-vps-ip:2030/login"  # Replace with your CWP login URL
    USERNAME = "your_username"  # Replace with your CWP username
    PASSWORD = "your_password"  # Replace with your CWP password
    
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # Replace with the browser driver you are using
    driver.maximize_window()
    
    try:
        # Login to CWP
        login_to_cwp(driver, BASE_URL, USERNAME, PASSWORD)
        
        # Perform routine tasks
        restart_service(driver, "httpd")  # Example: Restart Apache
        check_disk_usage(driver)
        
        # Logout
        logout(driver)
    
    except Exception as main_exception:
        print(f"An unexpected error occurred: {main_exception}")
    
    finally:
        # Close the browser
        driver.quit()
```

### Notes:
- This script uses Selenium WebDriver; ensure it is installed with `pip install selenium`.
- Replace placeholders (`BASE_URL`, `USERNAME`, `PASSWORD`) with actual values.
- You must have the appropriate browser driver installed (e.g., ChromeDriver for Google Chrome).

This example demonstrates basic server management (logging in, restarting services, checking disk usage, and logging out) without an SSH console. Extend functions for more actions (e.g., managing users/databases).
