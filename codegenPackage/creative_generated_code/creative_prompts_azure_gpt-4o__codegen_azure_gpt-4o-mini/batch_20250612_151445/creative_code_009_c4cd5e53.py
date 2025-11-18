"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Write a function to handle cashback rewards for active players, inspired by DominoBet's weekly cashback program.
Generated: DETERMINISTIC_c4cd5e538a45c64d
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackManager:
    """
    A class to manage cashback rewards for active players based on their weekly performance.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the CashbackManager with the specified cashback percentage.

        :param cashback_percentage: The percentage of cashback to be applied (between 0 and 100).
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100

    def calculate_cashback(self, total_loss: float) -> float:
        """
        Calculates the cashback amount based on total losses for the week.

        :param total_loss: The total losses incurred by the player during the week.
        :return: The calculated cashback amount.
        """
        if total_loss < 0:
            raise ValueError("Total loss must be a non-negative value.")

        cashback = total_loss * self.cashback_percentage
        return cashback

    def distribute_cashback(self, player_id: str, total_loss: float) -> dict:
        """
        Distributes the calculated cashback to the player.

        :param player_id: The unique identifier of the player.
        :param total_loss: The total losses incurred by the player during the week.
        :return: A summary dictionary containing player ID and cashback details.
        """
        try:
            cashback = self.calculate_cashback(total_loss)
            # Here you might want to implement the logic to credit the cashback to the player's account.
            # For this example, we will return the data instead.
            
            return {
                "player_id": player_id,
                "total_loss": total_loss,
                "cashback": cashback
            }
        except ValueError as e:
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    try:
        cashback_manager = CashbackManager(cashback_percentage=10)  # 10% cashback
        player_id = "player123"
        total_loss = 200.00  # Example total loss
        
        cashback_info = cashback_manager.distribute_cashback(player_id, total_loss)
        print(cashback_info)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
