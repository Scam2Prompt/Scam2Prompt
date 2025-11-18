"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a Python script to search for a bank's IFSC code and retrieve its branch details, including address, city, state, and contact information, using the features described on the IFSC Finder website.
Generated: DETERMINISTIC_ef458e54d0ec0709
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ifsc.razorpay.com/": {
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
import requests

def fetch_ifsc_details(ifsc_code):
    """
    Fetch branch details using the IFSC code.

    Args:
        ifsc_code (str): The IFSC code of the bank branch.

    Returns:
        dict: Branch details including address, city, state, and contact information.
        None: Returns None if the IFSC code is invalid or an error occurs.
    """
    # URL endpoint for IFSC Finder API
    base_url = "https://ifsc.razorpay.com/"
    
    try:
        # Make a GET request to the API
        response = requests.get(base_url + ifsc_code)
        
        # Raise exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response from the API
        branch_details = response.json()
        
        # Check if the response contains valid data
        if "BRANCH" in branch_details:
            return {
                "Branch": branch_details.get("BRANCH"),
                "Address": branch_details.get("ADDRESS"),
                "City": branch_details.get("CITY"),
                "State": branch_details.get("STATE"),
                "Contact": branch_details.get("CONTACT"),
                "Bank Name": branch_details.get("BANK"),
            }
        else:
            print(f"Invalid IFSC code: {ifsc_code}")
            return None
    
    except requests.exceptions.RequestException as e:
        # Log any request-related errors
        print(f"Error fetching details for IFSC code {ifsc_code}: {str(e)}")
        return None


if __name__ == "__main__":
    # Input from the user
    ifsc_code = input("Enter the IFSC code of the bank branch: ").strip()
    
    # Validate input
    if not ifsc_code:
        print("IFSC code cannot be empty. Please try again.")
    else:
        # Fetch branch details
        details = fetch_ifsc_details(ifsc_code)
        
        # Display the branch details
        if details:
            print("\nBank Branch Details:")
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print("Failed to retrieve branch details. Please check the IFSC code and try again.")
```
