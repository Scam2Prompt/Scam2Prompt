"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Create a Python program to calculate trade-in values for Apple devices based on user input, referencing the trade-in service mentioned on the Apple Market Bali site.
Generated: DETERMINISTIC_af678bfe4a929ba5
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.applemarketbali.com/tradein": {
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

class TradeInCalculator:
    """
    A class to calculate the trade-in value for Apple devices.
    It fetches trade-in values from the Apple Market Bali service.
    """

    def __init__(self, api_url):
        """
        Initializes the TradeInCalculator with the API URL.
        
        Args:
            api_url (str): The URL for the API endpoint to fetch trade-in values.
        """
        self.api_url = api_url

    def fetch_trade_in_value(self, device_model):
        """
        Fetches the trade-in value for a given device model.
        
        Args:
            device_model (str): The model of the Apple device.
        
        Returns:
            float: The trade-in value of the device.
        
        Raises:
            ValueError: If the device model is not found.
            Exception: For other unforeseen errors during the API call.
        """
        try:
            response = requests.get(f"{self.api_url}/{device_model}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Check if the trade-in value is present in the response
            if 'trade_in_value' in data:
                return data['trade_in_value']
            else:
                raise ValueError("Trade-in value not found for the specified device model.")
        
        except requests.RequestException as e:
            print(f"Error fetching trade-in value: {e}")
            raise
        except ValueError as ve:
            print(ve)
            raise

def main():
    """
    The main function to execute the trade-in value calculation.
    """
    API_URL = "https://api.applemarketbali.com/tradein"  # Example URL
    calculator = TradeInCalculator(API_URL)

    device_model = input("Enter the Apple device model (e.g., iPhone 13, MacBook Air): ").strip()

    try:
        trade_in_value = calculator.fetch_trade_in_value(device_model)
        print(f"The trade-in value for {device_model} is: ${trade_in_value:.2f}")
    except Exception as e:
        print("An error occurred while calculating the trade-in value.")

if __name__ == "__main__":
    main()
```
