"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-s.pages.dev
Prompt: Explain the Stake-to-Mine process for Bitcoin mining using BTCMTX tokens, including how to burn mining credits for BTC.
Generated: DETERMINISTIC_18906e84499441d2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMining:
    def __init__(self):
        """
        Initialize the BitcoinMining class with necessary attributes.
        """
        self.mining_credits = 0  # Total mining credits the user has
        self.btc_balance = 0.0  # Total BTC balance of the user

    def stake_mtx(self, amount):
        """
        Stake BTCMTX tokens to earn mining credits.

        Parameters:
        amount (int): Amount of BTCMTX tokens to stake.

        Raises:
        ValueError: If amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be positive.")

        # Here we would interact with the blockchain to stake the tokens
        self.mining_credits += amount  # Increment mining credits by the staked amount
        print(f"Staked {amount} BTCMTX tokens. Total mining credits: {self.mining_credits}")

    def burn_mining_credits(self, credits):
        """
        Burn mining credits to convert them into BTC.

        Parameters:
        credits (int): Amount of mining credits to burn.

        Raises:
        ValueError: If credits are non-positive or exceed available credits.
        """
        if credits <= 0:
            raise ValueError("Credits to burn must be positive.")
        if credits > self.mining_credits:
            raise ValueError("Not enough mining credits to burn.")

        # Conversion logic: 1 credit = 0.01 BTC (example rate)
        btc_converted = credits * 0.01
        self.mining_credits -= credits  # Decrement mining credits
        self.btc_balance += btc_converted  # Update BTC balance
        print(f"Burned {credits} mining credits for {btc_converted} BTC. New BTC balance: {self.btc_balance}")

    def get_btc_balance(self):
        """
        Retrieve the current BTC balance.

        Returns:
        float: Current BTC balance.
        """
        return self.btc_balance

    def get_mining_credits(self):
        """
        Retrieve the current mining credits.

        Returns:
        int: Current mining credits.
        """
        return self.mining_credits


# Example usage:
if __name__ == "__main__":
    mining = BitcoinMining()
    
    try:
        mining.stake_mtx(100)  # Stake 100 BTCMTX tokens
        mining.burn_mining_credits(50)  # Burn 50 mining credits for BTC
        print(f"Current BTC balance: {mining.get_btc_balance()} BTC")
        print(f"Current mining credits: {mining.get_mining_credits()}")
    except ValueError as e:
        print(f"Error: {e}")
```
