"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Generate code to calculate points earned from crypto transactions, including multipliers, based on the HAGGIS Hunt reward system.
Generated: DETERMINISTIC_04a2ab5733eb5832
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HaggisHuntRewardSystem:
    """
    A class to calculate points earned from crypto transactions based on 
    the HAGGIS Hunt reward system with multipliers.
    """

    def __init__(self):
        self.base_points = 0  # Base points for each transaction
        self.multiplier = 1    # Multiplier for the points

    def set_base_points(self, points: int):
        """
        Set the base points for each transaction.
        
        Args:
            points (int): The base points to be set.
        """
        if points < 0:
            raise ValueError("Base points cannot be negative.")
        self.base_points = points

    def set_multiplier(self, multiplier: float):
        """
        Set the multiplier for the points.
        
        Args:
            multiplier (float): The multiplier value to be set.
        """
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative.")
        self.multiplier = multiplier

    def calculate_points(self, transaction_amount: float) -> float:
        """
        Calculate the total points earned from a crypto transaction.
        
        Args:
            transaction_amount (float): The amount of the transaction.
        
        Returns:
            float: The total points earned.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        # Calculate points based on transaction amount and multipliers
        earned_points = self.base_points * self.multiplier * transaction_amount
        return earned_points

    def reset(self):
        """
        Reset the points calculation parameters to default values.
        """
        self.base_points = 0
        self.multiplier = 1

if __name__ == "__main__":
    try:
        reward_system = HaggisHuntRewardSystem()
        
        # Example: Set base points and multiplier
        reward_system.set_base_points(10)  # Base points for each transaction
        reward_system.set_multiplier(1.5)   # 1.5x multiplier for the transaction
        
        # Calculate points for a transaction
        transaction_amount = 100.0  # Example transaction amount
        points_earned = reward_system.calculate_points(transaction_amount)
        
        print(f"Points earned from the transaction: {points_earned:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
