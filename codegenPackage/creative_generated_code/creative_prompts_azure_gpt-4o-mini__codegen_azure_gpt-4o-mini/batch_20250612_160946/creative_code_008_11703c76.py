"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimscapesmaniabonus.pages.dev
Prompt: Describe how to set up a whitelist feature for trusted payment sources in a decentralized application.
Generated: DETERMINISTIC_11703c764a42e2a5
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

class PaymentWhitelist:
    def __init__(self):
        """Initialize an empty whitelist for storing trusted payment sources."""
        self.whitelist: Dict[str, bool] = {}

    def add_source(self, source: str) -> None:
        """Add a payment source to the whitelist.

        Args:
            source (str): The payment source to be added.

        Raises:
            ValueError: If the source is already in the whitelist.
        """
        if source in self.whitelist:
            raise ValueError(f"Source '{source}' is already whitelisted.")
        
        self.whitelist[source] = True
        print(f"Source '{source}' has been added to the whitelist.")

    def remove_source(self, source: str) -> None:
        """Remove a payment source from the whitelist.

        Args:
            source (str): The payment source to be removed.

        Raises:
            KeyError: If the source is not found in the whitelist.
        """
        if source not in self.whitelist:
            raise KeyError(f"Source '{source}' not found in the whitelist.")
        
        del self.whitelist[source]
        print(f"Source '{source}' has been removed from the whitelist.")

    def is_whitelisted(self, source: str) -> bool:
        """Check if a payment source is whitelisted.

        Args:
            source (str): The payment source to check.

        Returns:
            bool: True if the source is whitelisted, False otherwise.
        """
        return self.whitelist.get(source, False)

    def list_sources(self) -> List[str]:
        """List all whitelisted payment sources.

        Returns:
            List[str]: A list of all whitelisted payment sources.
        """
        return list(self.whitelist.keys())

# Example usage
if __name__ == "__main__":
    try:
        whitelist = PaymentWhitelist()

        # Adding sources
        whitelist.add_source("paypal@example.com")
        whitelist.add_source("stripe@example.com")

        # Checking if a source is whitelisted
        print(f"Is 'paypal@example.com' whitelisted? {whitelist.is_whitelisted('paypal@example.com')}")

        # Listing all whitelisted sources
        print("Current whitelist:", whitelist.list_sources())

        # Removing a source
        whitelist.remove_source("stripe@example.com")

        # Attempting to remove a non-existing source
        whitelist.remove_source("nonexistent@example.com")  # This will raise a KeyError

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
