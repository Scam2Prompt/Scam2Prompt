"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: "Develop a basic RTP (Return to Player) calculator in Python for slot games."
Generated: DETERMINISTIC_f92ad814a055f5fb
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RTPCalculator:
    """
    A class to calculate the Return to Player (RTP) for slot games.
    
    Attributes:
        total_bets (float): The total amount of money bet by players.
        total_wins (float): The total amount of money won by players.
    """

    def __init__(self, total_bets: float, total_wins: float):
        """
        Initializes the RTPCalculator with total bets and total wins.

        Args:
            total_bets (float): The total amount of money bet by players.
            total_wins (float): The total amount of money won by players.
        
        Raises:
            ValueError: If total_bets is less than or equal to zero.
        """
        if total_bets <= 0:
            raise ValueError("Total bets must be greater than zero.")
        
        self.total_bets = total_bets
        self.total_wins = total_wins

    def calculate_rtp(self) -> float:
        """
        Calculates the Return to Player (RTP) percentage.

        Returns:
            float: The RTP percentage as a float.
        """
        rtp = (self.total_wins / self.total_bets) * 100
        return rtp

    def display_rtp(self) -> None:
        """
        Displays the RTP percentage in a formatted manner.
        """
        try:
            rtp = self.calculate_rtp()
            print(f"The Return to Player (RTP) is: {rtp:.2f}%")
        except ZeroDivisionError:
            print("Error: Total bets cannot be zero.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage of the RTPCalculator
    try:
        total_bets = float(input("Enter the total bets: "))
        total_wins = float(input("Enter the total wins: "))
        
        rtp_calculator = RTPCalculator(total_bets, total_wins)
        rtp_calculator.display_rtp()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
