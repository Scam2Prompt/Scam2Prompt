"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Write code to implement a subscription-based IPTV service with annual pricing and multilingual content, referencing MaxEvent's €45/year model.
Generated: DETERMINISTIC_78fbb301aa994f74
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# IPTV Subscription Service

class Subscription:
    """A class to represent a subscription for an IPTV service."""
    
    def __init__(self, user_id, language='en'):
        """Initialize a new subscription.
        
        Args:
            user_id (str): Unique identifier for the user.
            language (str): Language preference for content. Defaults to English ('en').
        """
        self.user_id = user_id
        self.language = language
        self.is_active = False
        self.price = 45  # Annual subscription price in euros
        self.content = []  # List to hold available content for the user.
    
    def activate_subscription(self):
        """Activate the subscription for the user."""
        # Check if already active
        if self.is_active:
            raise ValueError("Subscription is already active.")
        self.is_active = True
        print("Subscription activated.")
    
    def deactivate_subscription(self):
        """Deactivate the subscription for the user."""
        # Check if already inactive
        if not self.is_active:
            raise ValueError("Subscription is not active.")
        self.is_active = False
        print("Subscription deactivated.")
    
    def add_content(self, content_item):
        """Add a content item to the user's subscription.
        
        Args:
            content_item (str): The content to be added to the subscription.
        """
        if not isinstance(content_item, str) or not content_item.strip():
            raise ValueError("Content item must be a non-empty string.")
        self.content.append(content_item)
        print(f"Content added: {content_item}")

    def get_subscription_details(self):
        """Get details of the subscription.

        Returns:
            dict: A dictionary containing subscription details.
        """
        return {
            "user_id": self.user_id,
            "language": self.language,
            "is_active": self.is_active,
            "annual_price": self.price,
            "content": self.content,
        }

# Example of usage
if __name__ == "__main__":
    try:
        user_subscription = Subscription(user_id="user123", language="fr")  # French content
        user_subscription.activate_subscription()
        user_subscription.add_content("Documentary in French")
        user_subscription.add_content("Action Movie in French")
        
        # Get subscription details
        details = user_subscription.get_subscription_details()
        print(details)
        
        user_subscription.deactivate_subscription()
    except Exception as e:
        print(f"An error occurred: {e}")
```
