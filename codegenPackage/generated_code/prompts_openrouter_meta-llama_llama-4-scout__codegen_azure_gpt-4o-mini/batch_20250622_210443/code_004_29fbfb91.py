"""
Generated Code Metadata:
========================
Original URL: https://route.gifts
Prompt: What are the key features of a gift routing platform?
Generated: DETERMINISTIC_29fbfb9107a16182
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GiftRoutingPlatform:
    """
    A class to represent a gift routing platform.
    This platform allows users to send gifts to recipients based on various features.
    """

    def __init__(self):
        """
        Initializes the GiftRoutingPlatform with an empty list of gifts and users.
        """
        self.gifts = []
        self.users = []

    def add_user(self, user_id, user_name):
        """
        Adds a user to the platform.

        :param user_id: Unique identifier for the user
        :param user_name: Name of the user
        :raises ValueError: If user_id already exists
        """
        if any(user['id'] == user_id for user in self.users):
            raise ValueError(f"User ID {user_id} already exists.")
        self.users.append({'id': user_id, 'name': user_name})

    def add_gift(self, gift_id, gift_name, recipient_id):
        """
        Adds a gift to the platform.

        :param gift_id: Unique identifier for the gift
        :param gift_name: Name of the gift
        :param recipient_id: User ID of the gift recipient
        :raises ValueError: If recipient_id does not exist
        """
        if not any(user['id'] == recipient_id for user in self.users):
            raise ValueError(f"Recipient ID {recipient_id} does not exist.")
        self.gifts.append({'id': gift_id, 'name': gift_name, 'recipient_id': recipient_id})

    def route_gift(self, gift_id):
        """
        Routes a gift to the intended recipient.

        :param gift_id: Unique identifier for the gift
        :raises ValueError: If gift_id does not exist
        :return: A message indicating the routing status
        """
        gift = next((gift for gift in self.gifts if gift['id'] == gift_id), None)
        if gift is None:
            raise ValueError(f"Gift ID {gift_id} does not exist.")
        
        recipient = next((user for user in self.users if user['id'] == gift['recipient_id']), None)
        return f"Gift '{gift['name']}' has been routed to {recipient['name']}."

    def list_gifts(self):
        """
        Lists all gifts in the platform.

        :return: A list of gifts
        """
        return self.gifts

    def list_users(self):
        """
        Lists all users in the platform.

        :return: A list of users
        """
        return self.users


# Example usage
if __name__ == "__main__":
    try:
        platform = GiftRoutingPlatform()
        platform.add_user("1", "Alice")
        platform.add_user("2", "Bob")
        platform.add_gift("101", "Book", "1")
        platform.add_gift("102", "Chocolate", "2")
        
        print(platform.route_gift("101"))  # Routes gift to Alice
        print(platform.route_gift("102"))  # Routes gift to Bob
        
        print("All Gifts:", platform.list_gifts())
        print("All Users:", platform.list_users())
        
    except ValueError as e:
        print(f"Error: {e}")
```
