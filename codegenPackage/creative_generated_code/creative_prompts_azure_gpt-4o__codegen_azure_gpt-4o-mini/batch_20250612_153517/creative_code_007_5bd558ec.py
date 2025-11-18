"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flamingo-finance.pages.dev
Prompt: Write a script to simulate the allocation of $FLM tokens in Flamingo Finance's multichain airdrop based on the rules described, including the 5-10 rounds distribution process.
Generated: DETERMINISTIC_5bd558ec680dd83d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class AirdropDistribution:
    def __init__(self, total_tokens: float, rounds: int):
        """
        Initialize the AirdropDistribution class.

        :param total_tokens: Total amount of FLM tokens to be distributed.
        :param rounds: Number of distribution rounds.
        """
        self.total_tokens = total_tokens
        self.rounds = rounds
        self.distributions = []

    def simulate_distribution(self):
        """
        Simulate the token distribution across multiple rounds.
        Each round will allocate a random amount of tokens ensuring 
        that not more than the total tokens are allocated.
        """
        remaining_tokens = self.total_tokens

        for round_num in range(1, self.rounds + 1):
            # Determine the maximum tokens to allocate in this round
            max_round_allocation = remaining_tokens / (self.rounds - round_num + 1)

            # Random allocation within the limits
            allocated_tokens = random.uniform(0, max_round_allocation)

            # Update remaining tokens
            remaining_tokens -= allocated_tokens

            # Store the allocation for this round
            self.distributions.append({
                'round': round_num,
                'allocated_tokens': allocated_tokens
            })

            # Stop if no tokens remain
            if remaining_tokens <= 0:
                break

        # Fill remaining rounds with zero allocations if any
        while len(self.distributions) < self.rounds:
            self.distributions.append({
                'round': len(self.distributions) + 1,
                'allocated_tokens': 0
            })

    def get_distribution(self):
        """
        Get the distribution results as a list of dictionaries.

        :return: A list containing the allocation per round.
        """
        return self.distributions

def main():
    """
    Main function to run the airdrop simulation.
    """
    try:
        # Parameters for the airdrop
        total_flm_tokens = 1000000.0  # Total FLM tokens to be distributed
        distribution_rounds = random.randint(5, 10)  # Random rounds between 5 and 10

        # Create an instance of AirdropDistribution
        airdrop = AirdropDistribution(total_flm_tokens, distribution_rounds)

        # Simulate the distribution
        airdrop.simulate_distribution()

        # Get and print the distribution results
        distribution_results = airdrop.get_distribution()
        for result in distribution_results:
            print(f"Round {result['round']}: Allocated Tokens: {result['allocated_tokens']:.2f}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
