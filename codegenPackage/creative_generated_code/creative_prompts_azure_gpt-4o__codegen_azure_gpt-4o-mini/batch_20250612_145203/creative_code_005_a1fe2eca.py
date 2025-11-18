"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Create a step-by-step guide in code for swapping ETH, BNB, MATIC, or USDT for $WAI tokens using the widget provided on the WienerAI website.
Generated: DETERMINISTIC_a1fe2eca1f93db9c
Batch ID: 20250612_145203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wienerai.com/widget": {
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

class TokenSwap:
    def __init__(self, base_url):
        """
        Initialize the TokenSwap class with the provided base URL for the WienerAI widget API.
        
        :param base_url: The base URL for the WienerAI widget API.
        """
        self.base_url = base_url

    def get_token_price(self, from_token, to_token):
        """
        Get the current price for swapping from one token to another.
        
        :param from_token: The token to swap from (e.g., 'ETH', 'BNB', 'MATIC', 'USDT').
        :param to_token: The token to swap to (e.g., '$WAI').
        :return: Current price for the swap.
        :raises Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(f"{self.base_url}/price", params={'from': from_token, 'to': to_token})
            response.raise_for_status()
            data = response.json()
            return data['price']
        except requests.RequestException as e:
            raise Exception(f"Error fetching token price: {e}")

    def swap_tokens(self, from_token, to_token, amount):
        """
        Execute the token swap by calling the WienerAI widget API.
        
        :param from_token: The token to swap from (e.g., 'ETH', 'BNB', 'MATIC', 'USDT').
        :param to_token: The token to swap to (e.g., '$WAI').
        :param amount: The amount of the from_token to swap.
        :return: Transaction details.
        :raises Exception: If the API request fails or if the swap fails.
        """
        try:
            payload = {
                'from': from_token,
                'to': to_token,
                'amount': amount
            }
            response = requests.post(f"{self.base_url}/swap", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error executing token swap: {e}")

def main():
    """
    Main function to run the token swap process.
    """
    base_url = "https://api.wienerai.com/widget"  # Replace with actual WienerAI API URL
    swap = TokenSwap(base_url)

    from_token = input("Enter the token to swap from (ETH, BNB, MATIC, USDT): ").strip()
    to_token = "$WAI"
    amount = float(input(f"Enter the amount of {from_token} to swap for {to_token}: "))

    # Get the current price for the swap
    try:
        price = swap.get_token_price(from_token, to_token)
        print(f"The current price for swapping {from_token} to {to_token} is {price}.")

        # Confirm and execute the token swap
        confirm = input(f"Do you want to proceed with the swap of {amount} {from_token} for {to_token}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            transaction_details = swap.swap_tokens(from_token, to_token, amount)
            print("Swap successful! Transaction details:", transaction_details)
        else:
            print("Swap cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
