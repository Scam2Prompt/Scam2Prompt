"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Generate code to calculate a user's final tier based on their wallet score and allocation criteria, including multipliers for consistency and 2023 transactions.
Generated: DETERMINISTIC_0acb8aaa6378a96d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UserTierCalculator:
    """
    A class to calculate a user's final tier based on their wallet score and allocation criteria.
    
    Attributes:
        wallet_score (float): The user's wallet score.
        consistency_multiplier (float): Multiplier based on user's consistency.
        transaction_multiplier (float): Multiplier based on the number of transactions in 2023.
    """
    
    def __init__(self, wallet_score: float, consistency_multiplier: float, transaction_multiplier: float):
        """
        Initializes the UserTierCalculator with wallet score and multipliers.
        
        Args:
            wallet_score (float): User's wallet score. Must be a non-negative value.
            consistency_multiplier (float): Multiplier for consistency, should be >= 1.
            transaction_multiplier (float): Multiplier for transactions, should be >= 1.
        
        Raises:
            ValueError: If any of the input values are invalid.
        """
        if wallet_score < 0:
            raise ValueError("Wallet score must be a non-negative value.")
        if consistency_multiplier < 1:
            raise ValueError("Consistency multiplier must be >= 1.")
        if transaction_multiplier < 1:
            raise ValueError("Transaction multiplier must be >= 1.")
        
        self.wallet_score = wallet_score
        self.consistency_multiplier = consistency_multiplier
        self.transaction_multiplier = transaction_multiplier

    def calculate_final_tier(self) -> str:
        """
        Calculates the final tier based on the wallet score and multipliers.
        
        Returns:
            str: The final tier of the user.
        """
        final_score = self.wallet_score * self.consistency_multiplier * self.transaction_multiplier
        
        # Define tier thresholds
        if final_score >= 1000:
            return "Gold"
        elif final_score >= 500:
            return "Silver"
        elif final_score >= 100:
            return "Bronze"
        else:
            return "Basic"

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of UserTierCalculator with sample data
        user_tier_calculator = UserTierCalculator(wallet_score=750, consistency_multiplier=1.2, transaction_multiplier=1.1)
        
        # Calculate the final tier
        final_tier = user_tier_calculator.calculate_final_tier()
        
        print(f"The user's final tier is: {final_tier}")
    except ValueError as e:
        print(f"Error: {e}")
```
