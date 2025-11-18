"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Write code to calculate and display the mining power generated from burning BTCMTX mining credits in a decentralized cloud mining platform.
Generated: DETERMINISTIC_36781e520cebbd42
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CloudMiningPlatform:
    def __init__(self, conversion_rate: float):
        """
        Initialize the CloudMiningPlatform with the specified BTCMTX to mining power conversion rate.
        
        Args:
            conversion_rate (float): The amount of mining power generated per BTCMTX burned.
        """
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be a positive number.")
        self.conversion_rate = conversion_rate

    def calculate_mining_power(self, btcmtx_amount: float) -> float:
        """
        Calculate the mining power generated from burning BTCMTX mining credits.
        
        Args:
            btcmtx_amount (float): The amount of BTCMTX to burn.
        
        Returns:
            float: The amount of mining power generated.
        
        Raises:
            ValueError: If btcmtx_amount is negative or zero.
        """
        if btcmtx_amount <= 0:
            raise ValueError("BTCMTX amount must be a positive number.")
        
        mining_power = btcmtx_amount * self.conversion_rate
        return mining_power

    def display_mining_power(self, btcmtx_amount: float) -> None:
        """
        Display the mining power generated from burning the specified amount of BTCMTX.
        
        Args:
            btcmtx_amount (float): The amount of BTCMTX to burn.
        """
        try:
            mining_power = self.calculate_mining_power(btcmtx_amount)
            print(f"Burned {btcmtx_amount} BTCMTX generates {mining_power:.2f} units of mining power.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage of the CloudMiningPlatform
    try:
        # Initialize the platform with a conversion rate (e.g., 10 units of mining power per BTCMTX)
        platform = CloudMiningPlatform(conversion_rate=10.0)
        
        # Specify the amount of BTCMTX to burn
        btcmtx_amount = 5.0
        
        # Display the mining power generated
        platform.display_mining_power(btcmtx_amount)
    except ValueError as e:
        print(f"Initialization error: {e}")
```
