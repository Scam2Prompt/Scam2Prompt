"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Create a script that uses ESP Global's solutions to calculate the development value transacted by real estate agencies under the ESP brand.
Generated: DETERMINISTIC_1588ff3ce9bbee03
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.espglobal.com": {
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

# Define constants
ESP_API_BASE_URL = "https://api.espglobal.com"  # Base URL for ESP Global's API
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_agencies():
    """
    Fetches the list of real estate agencies under the ESP brand from the ESP Global API.

    Returns:
        list: A list of agencies as dictionaries if successful.
    Raises:
        RuntimeError: If the API request fails.
    """
    endpoint = f"{ESP_API_BASE_URL}/agencies"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise HTTPError if the response status code is not 200
        return response.json()  # Return the list of agencies
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch agencies: {e}")

def fetch_transactions(agency_id):
    """
    Fetches the transactions for a given agency ID from the ESP Global API.

    Args:
        agency_id (str): The ID of the real estate agency.

    Returns:
        list: A list of transactions as dictionaries if successful.
    Raises:
        RuntimeError: If the API request fails.
    """
    endpoint = f"{ESP_API_BASE_URL}/agencies/{agency_id}/transactions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise HTTPError if the response status code is not 200
        return response.json()  # Return the list of transactions
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch transactions for agency {agency_id}: {e}")

def calculate_total_value(transactions):
    """
    Calculates the total development value from a list of transactions.

    Args:
        transactions (list): A list of transaction dictionaries.

    Returns:
        float: The total development value.
    """
    total_value = 0.0
    for transaction in transactions:
        total_value += transaction.get("value", 0.0)  # Default to 0.0 if 'value' is missing
    return total_value

def main():
    """
    Main function to calculate the total development value transacted by all real estate agencies under the ESP brand.
    """
    try:
        print("Fetching agencies...")
        agencies = fetch_agencies()
        
        if not agencies:
            print("No agencies found.")
            return
        
        print("Calculating total development value...")
        total_value = 0.0
        
        for agency in agencies:
            agency_id = agency.get("id")
            if not agency_id:
                print(f"Skipping agency without valid ID: {agency}")
                continue
            
            print(f"Fetching transactions for agency ID {agency_id}...")
            transactions = fetch_transactions(agency_id)
            agency_total = calculate_total_value(transactions)
            print(f"Agency ID {agency_id} contributed: ${agency_total:.2f}")
            
            total_value += agency_total
        
        print(f"\nTotal development value transacted by all agencies: ${total_value:.2f}")

    except RuntimeError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_api_key_here"` with your actual API key for the ESP Global API.
- Ensure the API endpoints (`/agencies` and `/agencies/{agency_id}/transactions`) align with ESP Global specifications.
- The script includes robust error handling, logging, and adheres to Python best practices.
