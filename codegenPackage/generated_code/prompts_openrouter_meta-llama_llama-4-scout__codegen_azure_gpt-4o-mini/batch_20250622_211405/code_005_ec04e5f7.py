"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Propose a tokenomics model for PrivateAI (PGPT) incorporating revenue streams from DAO operations, staking, AI queries, and data marketplace transactions.
Generated: DETERMINISTIC_ec04e5f7f28b973b
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsModel:
    """
    A class to represent the tokenomics model for PrivateAI (PGPT).
    
    Attributes:
        total_supply (float): Total supply of PGPT tokens.
        circulating_supply (float): Circulating supply of PGPT tokens.
        revenue_streams (dict): A dictionary to hold different revenue streams.
    """

    def __init__(self, total_supply: float, circulating_supply: float):
        """
        Initializes the TokenomicsModel with total and circulating supply.
        
        Args:
            total_supply (float): Total supply of PGPT tokens.
            circulating_supply (float): Circulating supply of PGPT tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if circulating_supply < 0 or circulating_supply > total_supply:
            raise ValueError("Circulating supply must be between 0 and total supply.")

        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.revenue_streams = {
            "dao_operations": 0.0,
            "staking": 0.0,
            "ai_queries": 0.0,
            "data_marketplace": 0.0
        }

    def update_revenue_stream(self, stream_name: str, amount: float):
        """
        Updates the revenue for a specific stream.
        
        Args:
            stream_name (str): The name of the revenue stream to update.
            amount (float): The amount to add to the revenue stream.
        
        Raises:
            ValueError: If the stream name is invalid or amount is negative.
        """
        if stream_name not in self.revenue_streams:
            raise ValueError(f"Invalid revenue stream: {stream_name}.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.revenue_streams[stream_name] += amount

    def calculate_total_revenue(self) -> float:
        """
        Calculates the total revenue from all streams.
        
        Returns:
            float: The total revenue from all revenue streams.
        """
        return sum(self.revenue_streams.values())

    def get_revenue_distribution(self) -> dict:
        """
        Returns the distribution of revenue across all streams.
        
        Returns:
            dict: A dictionary containing the revenue distribution.
        """
        total_revenue = self.calculate_total_revenue()
        if total_revenue == 0:
            return {stream: 0 for stream in self.revenue_streams}

        return {stream: (amount / total_revenue) * 100 for stream, amount in self.revenue_streams.items()}

    def __str__(self):
        """
        Returns a string representation of the TokenomicsModel.
        
        Returns:
            str: A string summarizing the tokenomics model.
        """
        return (f"Tokenomics Model:\n"
                f"Total Supply: {self.total_supply}\n"
                f"Circulating Supply: {self.circulating_supply}\n"
                f"Revenue Streams: {self.revenue_streams}\n"
                f"Total Revenue: {self.calculate_total_revenue()}\n"
                f"Revenue Distribution: {self.get_revenue_distribution()}")

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = TokenomicsModel(total_supply=1000000, circulating_supply=500000)
        tokenomics.update_revenue_stream("dao_operations", 10000)
        tokenomics.update_revenue_stream("staking", 5000)
        tokenomics.update_revenue_stream("ai_queries", 20000)
        tokenomics.update_revenue_stream("data_marketplace", 15000)

        print(tokenomics)
    except ValueError as e:
        print(f"Error: {e}")
```
