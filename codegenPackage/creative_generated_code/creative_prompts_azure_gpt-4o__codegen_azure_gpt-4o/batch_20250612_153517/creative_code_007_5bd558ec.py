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
import logging

# Configure logging to capture errors and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FlamingoAirdrop:
    def __init__(self, total_tokens, num_recipients, rounds):
        """
        Initialize the airdrop simulation.

        :param total_tokens: Total number of $FLM tokens available for distribution.
        :param num_recipients: Number of participants eligible for the airdrop.
        :param rounds: Number of rounds for token distribution (between 5 to 10).
        """
        if rounds < 5 or rounds > 10:
            raise ValueError("Rounds must be between 5 and 10.")
        self.total_tokens = total_tokens
        self.num_recipients = num_recipients
        self.rounds = rounds
        self.recipients = {f"recipient_{i}": 0 for i in range(1, num_recipients + 1)}

    def distribute_tokens(self):
        """
        Perform the token allocation across multiple rounds.
        """
        tokens_remaining = self.total_tokens

        for round_num in range(1, self.rounds + 1):
            logging.info(f"Starting round {round_num} of token distribution.")
            round_allocation = self._calculate_round_allocation(tokens_remaining)
            tokens_remaining -= round_allocation

            for recipient in self.recipients.keys():
                # Allocate tokens to recipient proportional to random distribution.
                allocation = round_allocation * random.uniform(0.01, 0.1)  # Allocate between 1% and 10% of round's tokens
                allocation = min(allocation, tokens_remaining)  # Ensure allocation doesn't exceed remaining tokens
                if allocation <= 0:
                    break  # Stop allocation if no tokens are left
                self.recipients[recipient] += allocation
                tokens_remaining -= allocation

                if tokens_remaining <= 0:
                    logging.info("All tokens have been allocated.")
                    break

            logging.info(f"Completed round {round_num}. Tokens remaining: {tokens_remaining}")

        if tokens_remaining > 0:
            self._allocate_remaining(tokens_remaining)

        logging.info("Token distribution complete.")

    def _calculate_round_allocation(self, tokens_remaining):
        """
        Calculate the number of tokens to be distributed in the current round.
        :param tokens_remaining: Tokens left for allocation.
        :return: Tokens allocated for the round.
        """
        # Allocate 10-20% of remaining tokens per round
        percentage = random.uniform(0.1, 0.2)
        return int(tokens_remaining * percentage)

    def _allocate_remaining(self, tokens_remaining):
        """
        Distribute any remaining tokens after all rounds are complete.

        :param tokens_remaining: Tokens left after rounds.
        """
        logging.info("Distributing remaining tokens.")
        for recipient in self.recipients.keys():
            allocation = min(tokens_remaining, random.randint(1, 10))  # Distribute small batches
            self.recipients[recipient] += allocation
            tokens_remaining -= allocation
            if tokens_remaining <= 0:
                break
        logging.info("Remaining tokens distributed.")

    def get_results(self):
        """
        Retrieve the final token allocation results.

        :return: Dictionary containing recipients and their respective allocations.
        """
        return self.recipients


def main():
    """
    Entry point for the script. Simulates the Flamingo Finance multichain airdrop.
    """
    try:
        total_tokens = 1000000  # Example total tokens for the simulation
        num_recipients = 100  # Example number of recipients
        rounds = random.randint(5, 10)  # Randomly choose the number of rounds within the allowed range

        # Create a FlamingoAirdrop instance
        airdrop = FlamingoAirdrop(total_tokens, num_recipients, rounds)

        # Perform token distribution
        airdrop.distribute_tokens()

        # Display final results
        results = airdrop.get_results()
        for recipient, tokens in results.items():
            logging.info(f"{recipient}: {tokens:.2f} $FLM")

    except Exception as e:
        logging.error(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    main()
```
