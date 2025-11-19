"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artistichive.io
Prompt: What are the advantages of using blockchain technology for art ownership on ArtisticHive?
Generated: DETERMINISTIC_dcf9640b51afa407
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blockchain_art_ownership.py

class ArtOwnership:
    """
    A class to represent the ownership of art using blockchain technology.
    
    Attributes
    ----------
    art_id : str
        Unique identifier for the art piece.
    owner : str
        Current owner's information (e.g., wallet address).
    provenance : list
        A list to store the history of ownership for the art piece.

    Methods
    -------
    transfer_ownership(new_owner):
        Transfers ownership of the art to a new owner.
    
    get_provenance():
        Returns the history of ownership for the art piece.
    """

    def __init__(self, art_id: str, owner: str):
        """
        Initializes the ArtOwnership instance with an art id and an owner.

        Parameters
        ----------
        art_id : str
            Unique identifier for the art piece.
        owner : str
            Initial owner's information.
        """
        self.art_id = art_id
        self.owner = owner
        self.provenance = [(owner, 'Created')]

    def transfer_ownership(self, new_owner: str):
        """
        Transfers ownership of the art to a new owner and records the transaction.

        Parameters
        ----------
        new_owner : str
            The wallet address of the new owner.

        Raises
        ------
        ValueError
            If the new owner is the same as the current owner.
        """
        if new_owner == self.owner:
            raise ValueError("The new owner must be different from the current owner.")
        
        # Record the ownership transfer
        self.provenance.append((new_owner, 'Transferred'))
        self.owner = new_owner

    def get_provenance(self):
        """
        Returns the history of ownership for the art piece.

        Returns
        -------
        list
            A list of tuples containing the owner and the action (e.g., 'Created', 'Transferred').
        """
        return self.provenance


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of ArtOwnership
        art_piece = ArtOwnership(art_id="ART001", owner="owner_wallet_1")
        
        # Transfer ownership
        art_piece.transfer_ownership("owner_wallet_2")
        
        # Get and print provenance
        provenance_history = art_piece.get_provenance()
        print("Provenance History:", provenance_history)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
