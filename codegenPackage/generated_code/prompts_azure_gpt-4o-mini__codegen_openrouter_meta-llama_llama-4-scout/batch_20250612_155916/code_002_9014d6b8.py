"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: What are the unique features of the GiftGo app that help simplify the gift-giving process?
Generated: DETERMINISTIC_9014d6b8828719e2
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# giftgo_app.py

class Gift:
    """Represents a gift with its name, price, and recipient."""
    
    def __init__(self, name, price, recipient):
        """
        Initializes a Gift object.

        Args:
            name (str): The name of the gift.
            price (float): The price of the gift.
            recipient (str): The recipient of the gift.
        """
        self.name = name
        self.price = price
        self.recipient = recipient


class GiftGoApp:
    """Simulates the GiftGo app, helping users manage gifts."""

    def __init__(self):
        """Initializes the GiftGo app with an empty list of gifts."""
        self.gifts = []

    def add_gift(self, gift):
        """
        Adds a gift to the list of gifts.

        Args:
            gift (Gift): The gift to add.

        Raises:
            TypeError: If the gift is not a Gift object.
        """
        if not isinstance(gift, Gift):
            raise TypeError("Only Gift objects can be added.")
        self.gifts.append(gift)

    def get_unique_recipients(self):
        """
        Returns a set of unique recipients.

        Returns:
            set: A set of unique recipient names.
        """
        return set(gift.recipient for gift in self.gifts)

    def get_gift_by_recipient(self, recipient):
        """
        Returns a list of gifts for a specific recipient.

        Args:
            recipient (str): The recipient's name.

        Returns:
            list: A list of Gift objects for the recipient.
        """
        return [gift for gift in self.gifts if gift.recipient == recipient]

    def get_total_spent(self):
        """
        Calculates the total amount spent on gifts.

        Returns:
            float: The total amount spent.
        """
        return sum(gift.price for gift in self.gifts)


def main():
    try:
        app = GiftGoApp()

        # Adding gifts
        gift1 = Gift("Book", 15.99, "John")
        gift2 = Gift("Toy", 24.99, "Jane")
        gift3 = Gift("Game", 49.99, "John")

        app.add_gift(gift1)
        app.add_gift(gift2)
        app.add_gift(gift3)

        # Getting unique recipients
        unique_recipients = app.get_unique_recipients()
        print("Unique Recipients:", unique_recipients)

        # Getting gifts by recipient
        johns_gifts = app.get_gift_by_recipient("John")
        print("John's Gifts:")
        for gift in johns_gifts:
            print(f"- {gift.name}: ${gift.price:.2f}")

        # Calculating total spent
        total_spent = app.get_total_spent()
        print(f"Total Spent: ${total_spent:.2f}")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
