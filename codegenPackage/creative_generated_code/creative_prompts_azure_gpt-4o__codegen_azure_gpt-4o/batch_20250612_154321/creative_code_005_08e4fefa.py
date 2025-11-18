"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethmining.info
Prompt: Write a program to simulate Ethereum mining rewards based on network difficulty and block reward parameters.
Generated: DETERMINISTIC_08e4fefa0aeec5d6
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mining_reward(hash_rate, network_difficulty, block_reward):
    """
    Calculate Ethereum mining rewards based on hash rate, network difficulty, and block reward.

    Args:
        hash_rate (float): The hash rate of the miner in hashes per second (H/s).
        network_difficulty (float): The network difficulty (measured in hashes).
        block_reward (float): The block reward in ETH.

    Returns:
        float: Estimated ETH rewards per second.
    """
    try:
        # Ensure inputs are positive numbers
        if hash_rate <= 0 or network_difficulty <= 0 or block_reward <= 0:
            raise ValueError("Inputs must be positive numbers.")

        # Calculate the rewards
        reward_per_second = (hash_rate / network_difficulty) * block_reward

        return reward_per_second
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to simulate Ethereum mining rewards.

    Prompts the user for hash rate, network difficulty, and block reward,
    and calculates the estimated mining rewards.
    """
    try:
        print("Ethereum Mining Reward Simulator")
        print("Please provide the following inputs:")

        # Get user inputs
        hash_rate = float(input("Enter your hash rate (in H/s): "))
        network_difficulty = float(input("Enter the network difficulty (in hashes): "))
        block_reward = float(input("Enter the block reward (in ETH): "))

        # Calculate mining rewards
        reward = calculate_mining_reward(hash_rate, network_difficulty, block_reward)

        # Display the result
        print(f"\nEstimated Mining Reward: {reward:.8f} ETH per second")
    
    except ValueError:
        print("Invalid input. Please provide numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the program
    main()
```
