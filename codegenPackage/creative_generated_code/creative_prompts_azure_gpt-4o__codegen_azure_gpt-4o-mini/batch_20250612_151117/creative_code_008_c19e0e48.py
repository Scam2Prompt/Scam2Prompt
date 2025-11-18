"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-coin.web.app
Prompt: Write a program to simulate the distribution of 10,000,000 $WLD tokens among 50,000 users, ensuring fairness and equal allocation.
Generated: DETERMINISTIC_c19e0e482b99c678
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def distribute_tokens(total_tokens, num_users):
    """
    Distributes a specified number of tokens equally among users.
    
    Parameters:
        total_tokens (int): The total number of tokens to distribute.
        num_users (int): The number of users to distribute tokens to.
    
    Returns:
        dict: A dictionary where keys are user IDs and values are the number of tokens each user receives.
    """
    if total_tokens < 0:
        raise ValueError("Total tokens must be a non-negative integer.")
    if num_users <= 0:
        raise ValueError("Number of users must be a positive integer.")

    # Calculate the number of tokens per user
    tokens_per_user = total_tokens // num_users
    remainder_tokens = total_tokens % num_users

    # Create a distribution dictionary
    distribution = {user_id: tokens_per_user for user_id in range(1, num_users + 1)}

    # Distribute the remainder tokens randomly
    for _ in range(remainder_tokens):
        random_user = random.randint(1, num_users)
        distribution[random_user] += 1

    return distribution

def main():
    # Constants for token distribution
    TOTAL_TOKENS = 10_000_000
    NUM_USERS = 50_000

    try:
        # Distribute tokens among users
        token_distribution = distribute_tokens(TOTAL_TOKENS, NUM_USERS)
        
        # Output sample distribution for verification
        print("Sample Token Distribution:")
        for user_id in list(token_distribution.keys())[:10]:  # Displaying first 10 users
            print(f"User {user_id}: {token_distribution[user_id]} tokens")

        # Optionally: display total distributed tokens to verify correctness
        total_distributed = sum(token_distribution.values())
        print(f"\nTotal Tokens Distributed: {total_distributed} out of {TOTAL_TOKENS}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
