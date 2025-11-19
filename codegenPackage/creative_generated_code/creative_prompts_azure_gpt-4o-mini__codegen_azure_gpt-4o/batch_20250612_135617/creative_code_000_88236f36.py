"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collaborativesolutions.com
Prompt: How can I use Workday to transform finance and HR programs in my organization?
Generated: DETERMINISTIC_88236f36fb58c79a
Batch ID: 20250612_135617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.workday.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is production-ready Python code that demonstrates the use of Workday's API to integrate finance and HR functionalities in your organization. This code assumes you're using Workday's RESTful API and have valid API credentials.

```python
import requests
import json
from requests.auth import HTTPBasicAuth

# Constants for Workday API
WORKDAY_BASE_URL = "https://api.workday.com"
FINANCE_ENDPOINT = "/finance/v1/accounts"
HR_ENDPOINT = "/hr/v1/workers"
API_USERNAME = "your_api_username"  # Replace with your Workday API username
API_PASSWORD = "your_api_password"  # Replace with your Workday API password

def get_finance_data():
    """
    Fetch finance data from Workday API.
    
    Returns:
        dict: Parsed finance data.
    Raises:
        Exception: If the API call fails.
    """
    try:
        url = f"{WORKDAY_BASE_URL}{FINANCE_ENDPOINT}"
        response = requests.get(url, auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))

        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        finance_data = response.json()
        return finance_data
    except requests.exceptions.RequestException as e:
        # Log and raise API errors
        print(f"Error fetching finance data: {e}")
        raise

def get_hr_data():
    """
    Fetch HR data from Workday API.
    
    Returns:
        dict: Parsed HR data.
    Raises:
        Exception: If the API call fails.
    """
    try:
        url = f"{WORKDAY_BASE_URL}{HR_ENDPOINT}"
        response = requests.get(url, auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))

        # Check for HTTP errors
        response.raise_for_status()

        # Parse JSON response
        hr_data = response.json()
        return hr_data
    except requests.exceptions.RequestException as e:
        # Log and raise API errors
        print(f"Error fetching HR data: {e}")
        raise

def transform_data(hr_data, finance_data):
    """
    Transform HR and finance data for organizational purposes.

    Args:
        hr_data (dict): HR data from Workday API.
        finance_data (dict): Finance data from Workday API.
    
    Returns:
        dict: Transformed data combining HR and finance insights.
    """
    # Example transformation: Combine HR and finance data
    transformed_data = {
        "employee_count": len(hr_data.get("workers", [])),
        "total_finance_accounts": len(finance_data.get("accounts", [])),
        "details": {
            "hr_data": hr_data,
            "finance_data": finance_data
        }
    }
    return transformed_data

def main():
    """
    Main function to integrate Workday finance and HR programs.
    """
    try:
        print("Fetching finance data...")
        finance_data = get_finance_data()
        
        print("Fetching HR data...")
        hr_data = get_hr_data()
        
        print("Transforming data...")
        transformed_data = transform_data(hr_data, finance_data)
        
        print(json.dumps(transformed_data, indent=4))
        print("Data integration successful!")
    except Exception as e:
        print(f"Error during integration: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `API_USERNAME` and `API_PASSWORD` with your Workday API credentials.
2. Ensure the `WORKDAY_BASE_URL` and API endpoints (`FINANCE_ENDPOINT`, `HR_ENDPOINT`) are correct and correspond to your organization's Workday API configuration.
3. This code includes robust error handling and adheres to Python programming best practices.
4. You may need to adjust the transformation logic (`transform_data`) to suit your organization's specific requirements.
