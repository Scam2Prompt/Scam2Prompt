"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write code to calculate RTP (Return to Player) for a scatter game on the Pelangi189 platform, ensuring accurate payout percentages.
Generated: DETERMINISTIC_fc53dfa37cb86289
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScatterGameRTP:
    """
    A class to calculate the Return to Player (RTP) for a scatter game on the Pelangi189 platform.

    Attributes:
        total_bets (float): The total amount of bets placed by players.
        total_payouts (float): The total amount of payouts made to players.
    """

    def __init__(self, total_bets: float, total_payouts: float):
        """
        Initializes the ScatterGameRTP class with total bets and total payouts.

        Args:
            total_bets (float): The total amount of bets placed.
            total_payouts (float): The total amount of payouts made.

        Raises:
            ValueError: If total_bets is less than or equal to zero.
        """
        if total_bets <= 0:
            raise ValueError("Total bets must be greater than zero.")

        self.total_bets = total_bets
        self.total_payouts = total_payouts

    def calculate_rtp(self) -> float:
        """
        Calculate the RTP (Return to Player) percentage.

        Returns:
            float: The RTP percentage.

        Raises:
            ZeroDivisionError: If total_bets is zero.
        """
        try:
            rtp = (self.total_payouts / self.total_bets) * 100
            return rtp
        except ZeroDivisionError:
            raise ZeroDivisionError("Total bets cannot be zero when calculating RTP.")

    def get_rtp_summary(self) -> str:
        """
        Generate a summary of the RTP calculation.

        Returns:
            str: A summary statement of the RTP.
        """
        rtp = self.calculate_rtp()
        return f"The RTP for the scatter game is {rtp:.2f}%."

# Example usage
if __name__ == "__main__":
    try:
        # Sample values for total bets and total payouts
        total_bets = 10000.0  # Total amount of bets
        total_payouts = 9500.0  # Total amount paid out

        # Create an instance of ScatterGameRTP
        rtp_calculator = ScatterGameRTP(total_bets, total_payouts)

        # Print the RTP summary
        print(rtp_calculator.get_rtp_summary())

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Calculation Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
