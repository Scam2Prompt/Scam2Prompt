"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnelapp.com
Prompt: What are the steps to create a gift using Tonnel's platform?
Generated: DETERMINISTIC_66c3ced82aa1b7cc
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GiftCreationError(Exception):
    """Custom exception for errors encountered during gift creation."""
    pass


class TonnelPlatform:
    def __init__(self):
        self.gifts = []  # List to store created gifts

    def create_gift(self, gift_name, recipient, message, value):
        """
        Creates a gift with the specified details.

        Parameters:
        gift_name (str): The name of the gift.
        recipient (str): The recipient of the gift.
        message (str): A personalized message for the recipient.
        value (float): The monetary value of the gift.

        Raises:
        GiftCreationError: If the gift creation fails due to invalid parameters.
        """
        # Validate inputs
        if not isinstance(gift_name, str) or not gift_name:
            raise GiftCreationError("Invalid gift name provided.")
        if not isinstance(recipient, str) or not recipient:
            raise GiftCreationError("Invalid recipient name provided.")
        if not isinstance(message, str):
            raise GiftCreationError("Message must be a string.")
        if not isinstance(value, (int, float)) or value <= 0:
            raise GiftCreationError("Value must be a positive number.")

        # Create the gift dictionary
        gift = {
            "gift_name": gift_name,
            "recipient": recipient,
            "message": message,
            "value": value
        }

        # Simulate saving the gift (e.g., to a database)
        self.gifts.append(gift)

        print(f"Gift created successfully: {gift}")
        return gift


if __name__ == "__main__":
    # Example usage of TonnelPlatform
    tonnel = TonnelPlatform()

    try:
        # Creating a gift with valid details
        tonnel.create_gift("Book", "Alice", "Happy Birthday!", 29.99)

        # Uncomment the following line to see error handling in action
        # tonnel.create_gift("", "Bob", "Congrats!", 19.99)  # Invalid gift name

    except GiftCreationError as e:
        print(f"Error creating gift: {e}")
```
