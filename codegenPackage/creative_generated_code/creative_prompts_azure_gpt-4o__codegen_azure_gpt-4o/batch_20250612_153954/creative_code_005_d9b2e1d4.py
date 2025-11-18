"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-stacks.com
Prompt: Develop a program to calculate the percentage of ILV tokens released versus the estimated total supply, using the data provided on the Illuvium staking page.
Generated: DETERMINISTIC_d9b2e1d4dc495a0e
Batch ID: 20250612_153954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/illuvium/staking": {
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
# Program to calculate the percentage of ILV tokens released versus the estimated total supply

# Import necessary libraries
import requests

def get_ilv_data(api_url):
    """
    Fetch ILV staking data from the provided API URL.

    Parameters:
    api_url (str): The URL to fetch ILV staking data.

    Returns:
    dict: A dictionary containing the staking data if successful, None otherwise.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ILV data: {e}")
        return None

def calculate_percentage(tokens_released, total_supply):
    """
    Calculate the percentage of tokens released against the total estimated supply.

    Parameters:
    tokens_released (float): The number of ILV tokens released.
    total_supply (float): The estimated total supply of ILV tokens.

    Returns:
    float: The percentage of released tokens.
    """
    try:
        # Ensure inputs are valid
        if tokens_released < 0 or total_supply <= 0:
            raise ValueError("Invalid input values: tokens_released must be >= 0 and total_supply must be > 0")
        
        # Calculate the percentage
        percentage = (tokens_released / total_supply) * 100
        return percentage
    except ValueError as ve:
        print(f"Error in calculation: {ve}")
        return None

def main():
    """
    Main function to fetch staking data, calculate percentages, and display the results.
    """
    # Replace this URL with the actual Illuvium staking API endpoint
    api_url = "https://api.example.com/illuvium/staking"  # Example URL, update as needed

    # Fetch ILV staking data
    staking_data = get_ilv_data(api_url)
    if not staking_data:
        print("Failed to fetch staking data. Exiting...")
        return

    # Extract relevant data
    try:
        tokens_released = float(staking_data.get("tokensReleased", 0))
        total_supply = float(staking_data.get("totalSupply", 0))
    except (TypeError, ValueError) as e:
        print(f"Error parsing staking data: {e}")
        return

    # Calculate the percentage of tokens released
    percentage = calculate_percentage(tokens_released, total_supply)
    if percentage is not None:
        print(f"Percentage of ILV tokens released: {percentage:.2f}%")

# Entry point for the program
if __name__ == "__main__":
    main()
```
