"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qubeticstoken-live.web.app
Prompt: Can you explain the token claiming process after purchasing TICS tokens during the presale on Qubetics?
Generated: DETERMINISTIC_5ced0f6caa79cb58
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TICSClaimProcess:
    """
    A class to manage the claiming process of TICS tokens after purchase during the presale period.

    Attributes:
        purchaser_address (str): The address of the purchaser.
        tokens_purchased (int): The number of TICS tokens purchased.
        presale_duration (int): Duration of the presale in days.
        claimable (bool): Status of whether the tokens can be claimed.
    """

    def __init__(self, purchaser_address: str, tokens_purchased: int, presale_duration: int):
        """
        Initializes the claim process with purchaser details and presale information.

        Args:
            purchaser_address (str): The address of the purchaser.
            tokens_purchased (int): The number of TICS tokens purchased.
            presale_duration (int): Duration of the presale in days.

        Raises:
            ValueError: If tokens_purchased is negative or if presale_duration is non-positive.
        """
        if tokens_purchased < 0:
            raise ValueError("The number of tokens purchased cannot be negative.")
        if presale_duration <= 0:
            raise ValueError("Presale duration must be greater than zero.")

        self.purchaser_address = purchaser_address
        self.tokens_purchased = tokens_purchased
        self.presale_duration = presale_duration
        self.claimable = False  # Initially, tokens are not claimable.

    def end_presale(self):
        """
        Ends the presale and makes tokens claimable.

        This method should be called after the presale duration has elapsed.
        """
        self.claimable = True  # Update the claimable status to true.

    def claim_tokens(self):
        """
        Allows the purchaser to claim their TICS tokens.

        Returns:
            str: A confirmation message if tokens are successfully claimed.

        Raises:
            RuntimeError: If tokens are not claimable at the time of claiming.
        """
        if not self.claimable:
            raise RuntimeError("Tokens cannot be claimed yet. Please wait until the presale ends.")

        # Process of transferring tokens to the purchaser
        self._transfer_tokens()

        return f"{self.tokens_purchased} TICS tokens have been successfully claimed by {self.purchaser_address}."

    def _transfer_tokens(self):
        """
        Simulates the transfer of tokens to the purchaser's address.

        This is a placeholder method that would contain logic to interact with the blockchain.
        """
        # Placeholder for actual token transfer logic
        print(f"Transferring {self.tokens_purchased} TICS tokens to {self.purchaser_address}...")

# Example Usage
if __name__ == "__main__":
    try:
        # Create a new TICS claim process instance
        claim_process = TICSClaimProcess("0x123456789abcdef", 100, 30)

        # Simulate the end of presale after 30 days
        claim_process.end_presale()

        # Claim the tokens
        confirmation_message = claim_process.claim_tokens()
        print(confirmation_message)

    except Exception as e:
        print(f"An error occurred: {e}")
```
