"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Illustrate how to implement a voting mechanism for selecting exchanges for the $SRIZE token listing, based on the features highlighted on the Solnarize webpage.
Generated: DETERMINISTIC_7dc83ab48b95856f
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VotingSystem:
    """
    Voting Mechanism for selecting exchanges for $SRIZE token listing.
    """

    def __init__(self):
        """
        Initializes the voting system with an empty exchange list and vote counts.
        """
        self.exchanges = {}
        self.total_votes = 0

    def add_exchange(self, exchange_name):
        """
        Adds a new exchange to the voting system.

        :param exchange_name: Name of the exchange to be added.
        """
        if exchange_name in self.exchanges:
            print(f"Exchange '{exchange_name}' is already added.")
        else:
            self.exchanges[exchange_name] = 0
            print(f"Exchange '{exchange_name}' added successfully.")

    def vote(self, exchange_name):
        """
        Casts a vote for a specific exchange.

        :param exchange_name: Name of the exchange to vote for.
        """
        if exchange_name not in self.exchanges:
            print(f"Exchange '{exchange_name}' does not exist.")
            return

        self.exchanges[exchange_name] += 1
        self.total_votes += 1
        print(f"Vote cast for exchange '{exchange_name}'.")

    def get_results(self):
        """
        Gets the current voting results.

        :return: A dictionary containing exchange names and their respective votes.
        """
        return self.exchanges

    def display_results(self):
        """
        Displays the current voting results in a formatted way.
        """
        print("\nVoting Results:")
        for exchange, votes in self.exchanges.items():
            vote_percentage = (votes / self.total_votes * 100) if self.total_votes > 0 else 0
            print(f"{exchange}: {votes} vote(s) | {vote_percentage:.2f}% of total votes")

    def save_results_to_file(self, filepath):
        """
        Saves the voting results to a JSON file.

        :param filepath: File path to save the results.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.exchanges, file, indent=4)
            print(f"Results saved to '{filepath}'")
        except Exception as e:
            print(f"Error saving results: {e}")

    def load_results_from_file(self, filepath):
        """
        Loads voting results from a JSON file.

        :param filepath: File path to load the results from.
        """
        try:
            with open(filepath, 'r') as file:
                self.exchanges = json.load(file)
            self.total_votes = sum(self.exchanges.values())
            print(f"Results loaded from '{filepath}'")
        except Exception as e:
            print(f"Error loading results: {e}")


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Add exchanges
    voting_system.add_exchange("Binance")
    voting_system.add_exchange("Coinbase")
    voting_system.add_exchange("Kraken")

    # Cast votes
    voting_system.vote("Binance")
    voting_system.vote("Coinbase")
    voting_system.vote("Binance")
    voting_system.vote("Kraken")
    voting_system.vote("Kraken")
    voting_system.vote("Binance")

    # Display results
    voting_system.display_results()

    # Save results to a file
    voting_system.save_results_to_file("voting_results.json")

    # Load results from a file
    new_voting_system = VotingSystem()
    new_voting_system.load_results_from_file("voting_results.json")
    new_voting_system.display_results()
```
