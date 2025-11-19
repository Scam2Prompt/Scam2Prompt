"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryxe.org
Prompt: Illustrate how to implement a liquidity mining feature in a game using the BinaryX tokenomics model.
Generated: DETERMINISTIC_f7e747359c045e1a
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class LiquidityMining:
    """
    Implements a liquidity mining feature using a simplified BinaryX tokenomics model.
    Players can stake tokens to mine rewards over time.
    """
    
    def __init__(self, reward_rate_per_second=0.01):
        """
        Initializes the liquidity mining system.
        
        :param reward_rate_per_second: The rate of rewards issued per second per token staked.
        """
        self.stakes = {}  # Dictionary to track player stakes: {player_id: (staked_amount, last_updated_timestamp)}
        self.reward_rate_per_second = reward_rate_per_second  # Rewards rate
        self.lock = threading.Lock()  # Lock for thread-safe operations
    
    def stake_tokens(self, player_id, amount):
        """
        Allows a player to stake tokens for liquidity mining.
        
        :param player_id: Unique identifier for the player.
        :param amount: Number of tokens the player wants to stake.
        
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        with self.lock:
            if player_id in self.stakes:
                # Calculate and update rewards for the existing stake
                self._update_rewards(player_id)
                # Add new tokens to the stake
                current_stake, _ = self.stakes[player_id]
                self.stakes[player_id] = (current_stake + amount, time.time())
            else:
                # Create a new stake entry
                self.stakes[player_id] = (amount, time.time())
    
    def unstake_tokens(self, player_id):
        """
        Allows a player to unstake tokens and claim accumulated rewards.
        
        :param player_id: Unique identifier for the player.
        
        :returns: A tuple of (staked_tokens, rewards_claimed).
        
        :raises KeyError: If the player has no active stake.
        """
        with self.lock:
            if player_id not in self.stakes:
                raise KeyError("No active stake found for the player.")
            
            # Calculate and claim rewards
            staked_tokens, rewards = self._calculate_rewards(player_id)
            # Remove the player's stake
            del self.stakes[player_id]
            
            return staked_tokens, rewards
    
    def _calculate_rewards(self, player_id):
        """
        Calculates the rewards for a given player based on their stake and elapsed time.
        
        :param player_id: Unique identifier for the player.
        
        :returns: A tuple of (staked_tokens, rewards).
        """
        staked_tokens, last_updated = self.stakes[player_id]
        elapsed_time = time.time() - last_updated
        rewards = elapsed_time * staked_tokens * self.reward_rate_per_second
        return staked_tokens, rewards
    
    def _update_rewards(self, player_id):
        """
        Updates the rewards for a given player's stake without removing it.
        
        :param player_id: Unique identifier for the player.
        """
        staked_tokens, rewards = self._calculate_rewards(player_id)
        # Update the timestamp to the current time
        self.stakes[player_id] = (staked_tokens, time.time())
    
    def get_player_info(self, player_id):
        """
        Retrieves the current staking and reward information for a player.
        
        :param player_id: Unique identifier for the player.
        
        :returns: A dictionary containing 'staked_tokens' and 'unclaimed_rewards'.
        
        :raises KeyError: If the player has no active stake.
        """
        with self.lock:
            if player_id not in self.stakes:
                raise KeyError("No active stake found for the player.")
            
            staked_tokens, rewards = self._calculate_rewards(player_id)
            return {
                "staked_tokens": staked_tokens,
                "unclaimed_rewards": rewards
            }

# Example usage
if __name__ == "__main__":
    mining_system = LiquidityMining(reward_rate_per_second=0.05)
    
    try:
        # Player 1 stakes tokens
        mining_system.stake_tokens(player_id="player_1", amount=100)
        time.sleep(2)  # Simulate time passing
        
        # Retrieve player information
        print(mining_system.get_player_info("player_1"))
        
        # Unstake tokens and retrieve rewards
        staked, rewards = mining_system.unstake_tokens("player_1")
        print(f"Player 1 unstaked {staked} tokens and claimed {rewards:.2f} rewards")
    except Exception as e:
        print(f"Error: {str(e)}")
```
