"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Develop a Python script that automates the purchase of tickets for educational events using IQRA Tokens. Include functionality to verify the transaction and store the ticket details.
Generated: DETERMINISTIC_aedb78db2534ec55
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.iqr_tokens.com": {
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
import json

class TicketPurchaseError(Exception):
    """Custom exception for ticket purchase errors."""
    pass

class IQRAToken:
    """Class to handle IQRA Token transactions."""
    
    def __init__(self, token_api_url, user_id):
        """
        Initializes the IQRA Token handler.

        Args:
            token_api_url (str): The API URL for token transactions.
            user_id (str): The ID of the user purchasing tickets.
        """
        self.token_api_url = token_api_url
        self.user_id = user_id

    def purchase_ticket(self, event_id, amount):
        """
        Purchases a ticket for a specified event.

        Args:
            event_id (str): The ID of the event to purchase a ticket for.
            amount (float): The amount of IQRA Tokens to spend.

        Returns:
            dict: Response from the token purchase API.

        Raises:
            TicketPurchaseError: If the purchase fails.
        """
        try:
            response = requests.post(
                f"{self.token_api_url}/purchase",
                json={"user_id": self.user_id, "event_id": event_id, "amount": amount}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise TicketPurchaseError(f"Failed to purchase ticket: {e}")

class TicketManager:
    """Class to manage ticket purchases and storage."""
    
    def __init__(self, storage_file):
        """
        Initializes the TicketManager.

        Args:
            storage_file (str): Path to the file where ticket details will be stored.
        """
        self.storage_file = storage_file

    def store_ticket_details(self, ticket_details):
        """
        Stores ticket details in a file.

        Args:
            ticket_details (dict): Details of the purchased ticket.
        """
        try:
            with open(self.storage_file, 'a') as file:
                json.dump(ticket_details, file)
                file.write('\n')  # Newline for separation of entries
        except IOError as e:
            raise Exception(f"Failed to write ticket details to file: {e}")

def main():
    """Main function to automate the ticket purchase process."""
    token_api_url = "https://api.iqr_tokens.com"  # Replace with the actual API URL
    user_id = "your_user_id_here"  # Replace with actual user ID
    storage_file = "tickets.json"
    event_id = "event123"  # Replace with the actual event ID
    token_amount = 1.0  # Replace with the actual amount of IQRA Tokens to spend

    iqra_token = IQRAToken(token_api_url, user_id)
    ticket_manager = TicketManager(storage_file)

    try:
        # Purchase a ticket
        purchase_response = iqra_token.purchase_ticket(event_id, token_amount)
        print("Ticket purchased successfully:", purchase_response)

        # Store ticket details
        ticket_manager.store_ticket_details(purchase_response)
        print("Ticket details stored successfully.")
    except TicketPurchaseError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
