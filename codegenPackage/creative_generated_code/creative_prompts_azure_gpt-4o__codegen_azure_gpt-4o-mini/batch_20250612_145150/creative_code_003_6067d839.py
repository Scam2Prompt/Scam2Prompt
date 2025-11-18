"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Generate a Python script that interacts with a hypothetical banking API to change a card PIN, ensuring compliance with the steps mentioned on the Heritage Bank website (e.g., PIN Change Number, OTP, and PIN confirmation).
Generated: DETERMINISTIC_6067d8397a6868af
Batch ID: 20250612_145150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.heritagebank.com": {
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

class BankingAPIClient:
    """A client to interact with Heritage Bank's hypothetical API to manage card operations."""

    BASE_URL = "https://api.heritagebank.com"  # Hypothetical base URL for the API

    def __init__(self, api_key):
        """
        Initialize the BankingAPIClient with the provided API key.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def change_card_pin(self, card_number, current_pin, new_pin, pin_change_number):
        """
        Change the card PIN using the provided details.

        :param card_number: str - The card number for which the PIN is to be changed.
        :param current_pin: str - The current PIN of the card.
        :param new_pin: str - The new desired PIN for the card.
        :param pin_change_number: str - The PIN Change Number provided by the bank.
        
        :return: response JSON if successful, raises an exception otherwise.
        """
        try:
            # Step 1: Request an OTP for security validation
            otp = self.request_otp(card_number)
            
            # Step 2: Validate the OTP
            self.validate_otp(card_number, otp)

            # Step 3: Make the API call to change the PIN
            response = requests.post(
                f"{self.BASE_URL}/change_pin",
                json={
                    "card_number": card_number,
                    "current_pin": current_pin,
                    "new_pin": new_pin,
                    "pin_change_number": pin_change_number,
                    "otp": otp
                },
                headers={"Authorization": f"Bearer {self.api_key}"}
            )

            # Check response status
            response.raise_for_status()  # Will raise an error for 4xx/5xx responses
            return response.json()  # Return the successful response as JSON

        except requests.RequestException as e:
            # Log the error and re-raise for higher-level handling
            print(f"An error occurred while changing the card PIN: {e}")
            raise

    def request_otp(self, card_number):
        """
        Request an OTP for the card PIN change process.

        :param card_number: str - The card number to send the OTP to.
        
        :return: str - The OTP received (simulated for this example).
        """
        # Simulated OTP request (In a real world scenario, this would involve an API call)
        print(f"Requesting OTP for card number ending in {card_number[-4:]}")
        return "123456"  # Simulated OTP

    def validate_otp(self, card_number, otp):
        """
        Validate the OTP received for the card number.

        :param card_number: str - The card number for which the OTP is validated.
        :param otp: str - The OTP to validate.
        
        :raises ValueError: if the OTP does not meet expected criteria (in this case, a fixed OTP).
        """
        # Simulated OTP validation
        print(f"Validating OTP for card number ending in {card_number[-4:]}")
        if otp != "123456":  # Replace with actual OTP validation
            raise ValueError("Invalid OTP provided.")

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    client = BankingAPIClient(api_key)

    # Sample values for demonstration (to be replaced with real values)
    card_number = "1234567812345678"
    current_pin = "1234"
    new_pin = "5678"
    pin_change_number = "PIN_CHANGE_123"

    try:
        response = client.change_card_pin(card_number, current_pin, new_pin, pin_change_number)
        print("PIN change successful:", response)
    except Exception as e:
        print("Failed to change PIN:", e)
```
