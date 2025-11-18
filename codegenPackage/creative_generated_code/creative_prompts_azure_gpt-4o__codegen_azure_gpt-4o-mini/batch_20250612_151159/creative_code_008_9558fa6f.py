"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibarmypr.pages.dev
Prompt: Write a Python function to calculate rewards for staking SHIB, LEASH, and BONE tokens on ShibaSwap, factoring in WOOF Returns.
Generated: DETERMINISTIC_9558fa6fb7e83339
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for better traceability and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingRewardsCalculator:
    def __init__(self):
        # Constants for reward calculation
        self.WOOF_RETURN_PERCENTAGE = 0.05  # Example WOOF return percentage

    def calculate_rewards(self, token_amounts):
        """
        Calculate rewards for staking SHIB, LEASH, and BONE tokens on ShibaSwap.
        
        Parameters:
        token_amounts (dict): A dictionary containing token amounts with keys 'SHIB', 'LEASH', and 'BONE'.
        
        Returns:
        dict: A dictionary containing the calculated rewards for each token.
        """
        # Validate input
        if not isinstance(token_amounts, dict):
            logging.error("Invalid input: token_amounts must be a dictionary.")
            raise ValueError("token_amounts must be a dictionary.")
        
        required_keys = {'SHIB', 'LEASH', 'BONE'}
        if not required_keys.issubset(token_amounts.keys()):
            logging.error(f"Invalid input: token_amounts must contain keys {required_keys}.")
            raise ValueError(f"token_amounts must contain keys {required_keys}.")

        rewards = {}
        try:
            for token, amount in token_amounts.items():
                if amount < 0:
                    logging.error(f"Invalid token amount: {amount} for token {token}. Must be non-negative.")
                    raise ValueError(f"Token amount for {token} must be non-negative.")
                
                # Calculate the reward based on the token amount and WOOF return percentage
                rewards[token] = amount * self.WOOF_RETURN_PERCENTAGE
                logging.info(f"Calculated reward for {token}: {rewards[token]} based on amount: {amount}")
        
        except Exception as e:
            logging.exception("An error occurred while calculating rewards.")
            raise
        
        return rewards

# Example usage
if __name__ == "__main__":
    calculator = StakingRewardsCalculator()
    
    # Define the amounts of tokens staked
    staked_tokens = {
        'SHIB': 1000,
        'LEASH': 500,
        'BONE': 200
    }
    
    try:
        rewards = calculator.calculate_rewards(staked_tokens)
        print("Calculated rewards:", rewards)
    except Exception as e:
        print(f"Error calculating rewards: {e}")
```
