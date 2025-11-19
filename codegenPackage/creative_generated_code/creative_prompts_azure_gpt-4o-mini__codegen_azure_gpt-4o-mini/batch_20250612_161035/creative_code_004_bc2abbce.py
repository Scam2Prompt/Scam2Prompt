"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lista-rewards.pages.dev
Prompt: Create a function that calculates potential rewards from locking LISTA tokens in the LISTADAO protocol.
Generated: DETERMINISTIC_bc2abbce277fc855
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ListaDao:
    """
    A class to represent the LISTADAO protocol for calculating rewards from locked LISTA tokens.
    """

    def __init__(self, annual_reward_rate: float, total_tokens: float):
        """
        Initializes the ListaDao instance.

        Parameters:
        annual_reward_rate (float): The annual reward rate as a percentage (e.g., 5 for 5%).
        total_tokens (float): The total number of LISTA tokens locked.
        """
        if annual_reward_rate < 0 or total_tokens < 0:
            raise ValueError("Annual reward rate and total tokens must be non-negative.")

        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal
        self.total_tokens = total_tokens

    def calculate_rewards(self, lock_duration_years: float) -> float:
        """
        Calculates potential rewards from locking LISTA tokens over a specified duration.

        Parameters:
        lock_duration_years (float): The duration in years for which the tokens are locked.

        Returns:
        float: The potential rewards earned by locking the LISTA tokens.
        """
        if lock_duration_years < 0:
            raise ValueError("Lock duration must be non-negative.")

        # Calculate potential rewards
        rewards = self.total_tokens * self.annual_reward_rate * lock_duration_years
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the LISTADAO with a 5% annual reward rate and 1000 tokens locked
        lista_dao = ListaDao(annual_reward_rate=5.0, total_tokens=1000.0)
        
        # Calculate potential rewards for locking tokens for 2 years
        duration = 2.0  # Years
        potential_rewards = lista_dao.calculate_rewards(lock_duration_years=duration)
        
        print(f"Potential rewards from locking LISTA tokens for {duration} years: {potential_rewards:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
```
