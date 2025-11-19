"""
Generated Code Metadata:
========================
Original URL: https://presales-monprotocolapp.pages.dev
Prompt: What are the key considerations for implementing a presale allocation system for NFTs, and how does MON Protocol's system address these considerations?
Generated: DETERMINISTIC_2eefb5ac789f561c
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTPresaleAllocation:
    """
    A class to manage the presale allocation of NFTs.
    
    Attributes:
        total_supply (int): Total number of NFTs available for presale.
        allocated (dict): A dictionary to track allocated NFTs per user.
        presale_start (datetime): Start time of the presale.
        presale_end (datetime): End time of the presale.
    """

    def __init__(self, total_supply, presale_start, presale_end):
        """
        Initializes the NFT presale allocation system.

        Args:
            total_supply (int): Total number of NFTs available for presale.
            presale_start (datetime): Start time of the presale.
            presale_end (datetime): End time of the presale.
        """
        self.total_supply = total_supply
        self.allocated = {}
        self.presale_start = presale_start
        self.presale_end = presale_end

    def is_presale_active(self):
        """Check if the presale is currently active."""
        from datetime import datetime
        now = datetime.now()
        return self.presale_start <= now <= self.presale_end

    def allocate_nft(self, user_id, quantity):
        """
        Allocates NFTs to a user during the presale.

        Args:
            user_id (str): The ID of the user requesting allocation.
            quantity (int): The number of NFTs to allocate.

        Raises:
            ValueError: If the presale is not active or if allocation exceeds available supply.
        """
        if not self.is_presale_active():
            raise ValueError("Presale is not active.")
        
        if user_id in self.allocated:
            current_allocation = self.allocated[user_id]
        else:
            current_allocation = 0

        if current_allocation + quantity > self.total_supply:
            raise ValueError("Allocation exceeds available supply.")

        self.allocated[user_id] = current_allocation + quantity
        self.total_supply -= quantity

    def get_allocation(self, user_id):
        """
        Retrieves the current NFT allocation for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The number of NFTs allocated to the user.
        """
        return self.allocated.get(user_id, 0)

    def finalize_presale(self):
        """Finalizes the presale and resets the allocation system."""
        if not self.is_presale_active():
            self.allocated.clear()
            self.total_supply = 0
        else:
            raise ValueError("Presale is still active. Cannot finalize.")

# Example usage
if __name__ == "__main__":
    from datetime import datetime, timedelta

    # Define presale period
    start_time = datetime.now()
    end_time = start_time + timedelta(days=1)  # Presale lasts for 1 day

    # Initialize presale allocation system
    presale = NFTPresaleAllocation(total_supply=1000, presale_start=start_time, presale_end=end_time)

    # Allocate NFTs to users
    try:
        presale.allocate_nft(user_id="user1", quantity=5)
        print(f"User1 allocation: {presale.get_allocation('user1')} NFTs")
    except ValueError as e:
        print(f"Error: {e}")

    # Finalize presale
    try:
        presale.finalize_presale()
    except ValueError as e:
        print(f"Error: {e}")
```
