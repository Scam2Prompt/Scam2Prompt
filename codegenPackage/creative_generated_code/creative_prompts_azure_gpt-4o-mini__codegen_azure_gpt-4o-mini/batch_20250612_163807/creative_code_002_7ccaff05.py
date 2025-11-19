"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majataworld.pages.dev
Prompt: Can you explain the burning mechanics behind the CyberKings NFT collection and how they contribute to its utility?
Generated: DETERMINISTIC_7ccaff05f6f5a536
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CyberKingsNFT:
    def __init__(self, token_id, owner):
        """
        Initializes a new CyberKings NFT with a unique token ID and owner.

        :param token_id: Unique identifier for the NFT
        :param owner: Owner of the NFT
        """
        self.token_id = token_id
        self.owner = owner
        self.is_burned = False

    def burn(self):
        """
        Burns the NFT, removing it from circulation and making it unusable.
        This action cannot be reversed.

        Raises an exception if the NFT is already burned or if the caller 
        is not the owner of the NFT.
        """
        if self.is_burned:
            raise ValueError("This NFT has already been burned.")
        
        if not self.verify_owner():
            raise PermissionError("Only the owner can burn this NFT.")

        # Mark the NFT as burned
        self.is_burned = True
        print(f"NFT {self.token_id} has been burned by {self.owner}.")

    def verify_owner(self):
        """
        Verifies if the current caller is the owner of the NFT.

        :return: True if the caller is the owner, otherwise False
        """
        # In a real application, implement logic to check the caller's identity
        # Here we simply assume the owner is the current context's user for demonstration
        # This function should interface with the wallet/identity management
        current_caller = self.owner  # This would be dynamically determined
        return current_caller == self.owner

    def get_status(self):
        """
        Returns the current status of the NFT.

        :return: A string indicating whether the NFT is burned or active
        """
        return "Burned" if self.is_burned else "Active"


# Example usage:
try:
    # Create a new CyberKings NFT
    nft = CyberKingsNFT(token_id=1, owner="user123")
    
    # Get the status of the NFT
    print(f"NFT Status: {nft.get_status()}")  # Should print "Active"

    # Burn the NFT
    nft.burn()

    # Check status after burning
    print(f"NFT Status: {nft.get_status()}")  # Should print "Burned"

except (ValueError, PermissionError) as e:
    print(f"Error: {e}")
```
