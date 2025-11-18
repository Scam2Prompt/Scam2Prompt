"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-pepe.xyz
Prompt: Write a script to calculate the cumulative gain of $BPEP tokens based on the presale stage price increments provided in Bitcoin Pepe's roadmap.
Generated: DETERMINISTIC_1b24a54ede6074f5
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BPEPTokenInvestment:
    def __init__(self, initial_investment_usd, token_price_increments):
        """
        Initialize the investment tracker.

        :param initial_investment_usd: Initial investment amount in USD.
        :param token_price_increments: A list of price increments for each presale stage.
        """
        self.initial_investment_usd = initial_investment_usd
        self.token_price_increments = token_price_increments
        self.total_tokens_acquired = 0.0
        self.cumulative_gain = 0.0

    def calculate_tokens_acquired(self):
        """
        Calculate the total number of tokens acquired based on the price increments.
        This method also calculates the cumulative gain after each price increment.
        """
        for price in self.token_price_increments:
            try:
                # Calculate the number of tokens acquired at the current price point
                tokens_acquired = self.initial_investment_usd / price
                self.total_tokens_acquired += tokens_acquired

                # Calculate the cumulative gain based on the total tokens and current price
                current_value = self.total_tokens_acquired * price
                self.cumulative_gain = current_value - self.initial_investment_usd

                # Log the results
                print(f"Acquired {tokens_acquired:.4f} tokens at ${price:.4f} each.")
                print(f"Current total tokens: {self.total_tokens_acquired:.4f}, "
                      f"Current value: ${current_value:.2f}, "
                      f"Cumulative Gain: ${self.cumulative_gain:.2f}\n")

            except ZeroDivisionError:
                print("Error: Token price cannot be zero.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def get_cumulative_gain(self):
        """
        Get the final cumulative gain from the investment.

        :return: The cumulative gain in USD.
        """
        return self.cumulative_gain


# Example usage
if __name__ == "__main__":
    # Initial investment and token price increments (example values)
    initial_investment = 1000.0  # $1000 investment
    price_increments = [0.1, 0.2, 0.3, 0.5]  # Example presale stage prices in USD

    # Create an investment instance
    investment = BPEPTokenInvestment(initial_investment, price_increments)

    # Calculate tokens acquired and cumulative gain
    investment.calculate_tokens_acquired()

    # Retrieve the final cumulative gain
    final_gain = investment.get_cumulative_gain()
    print(f"Final Cumulative Gain: ${final_gain:.2f}")
```
