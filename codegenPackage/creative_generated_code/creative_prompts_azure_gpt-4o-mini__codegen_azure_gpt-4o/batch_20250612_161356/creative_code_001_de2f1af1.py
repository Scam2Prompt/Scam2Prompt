"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: What are the key features of the Gitcoin Round Manager application?
Generated: DETERMINISTIC_de2f1af1a1fb5eea
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gitcoin Round Manager Application - Key Features

This script outlines the key features of the Gitcoin Round Manager application.
The application is responsible for managing funding rounds, handling contributions,
calculating matching funds, and providing transparency into grant funding processes.
"""

# Import necessary modules
import json
from datetime import datetime


class RoundManager:
    """
    A class to manage rounds in the Gitcoin Round Manager Application.
    Responsible for creating and managing funding rounds, handling contributions,
    calculating matching funds, and providing transparency.
    """

    def __init__(self):
        """
        Initialize the RoundManager with an empty list of rounds.
        """
        self.rounds = []

    def create_round(self, name, start_date, end_date, total_funding):
        """
        Creates a new funding round.

        :param name: Name of the funding round.
        :param start_date: Start date of the round in YYYY-MM-DD format.
        :param end_date: End date of the round in YYYY-MM-DD format.
        :param total_funding: Total funding available for this round.
        :return: Details of the created round.
        """
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj <= start_date_obj:
                raise ValueError("End date must be after the start date.")

            round_data = {
                "name": name,
                "start_date": start_date_obj,
                "end_date": end_date_obj,
                "total_funding": total_funding,
                "contributions": []
            }
            self.rounds.append(round_data)

            return round_data
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error creating round: {e}")

    def add_contribution(self, round_name, contributor, amount):
        """
        Adds a contribution to a specific funding round.

        :param round_name: Name of the funding round.
        :param contributor: Name of the contributor.
        :param amount: Contribution amount.
        :return: Updated round details, or None if an error occurs.
        """
        try:
            for round_data in self.rounds:
                if round_data["name"] == round_name:
                    if amount <= 0:
                        raise ValueError("Contribution amount must be greater than zero.")
                    contribution = {
                        "contributor": contributor,
                        "amount": amount
                    }
                    round_data["contributions"].append(contribution)
                    return round_data

            raise ValueError(f"Round '{round_name}' not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error adding contribution: {e}")

    def calculate_matching_funds(self, round_name):
        """
        Calculates matching funds for a given round based on contributions.

        :param round_name: Name of the funding round.
        :return: Total matching funds calculated, or None if an error occurs.
        """
        try:
            for round_data in self.rounds:
                if round_data["name"] == round_name:
                    total_contributions = sum(c["amount"] for c in round_data["contributions"])
                    matching_funds = min(total_contributions, round_data["total_funding"])
                    return matching_funds

            raise ValueError(f"Round '{round_name}' not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error calculating matching funds: {e}")

    def get_round_summary(self, round_name):
        """
        Retrieves a summary of a specific funding round.

        :param round_name: Name of the funding round.
        :return: Round summary in JSON format, or None if an error occurs.
        """
        try:
            for round_data in self.rounds:
                if round_data["name"] == round_name:
                    summary = {
                        "name": round_data["name"],
                        "start_date": round_data["start_date"].strftime("%Y-%m-%d"),
                        "end_date": round_data["end_date"].strftime("%Y-%m-%d"),
                        "total_funding": round_data["total_funding"],
                        "contributions": round_data["contributions"],
                        "matching_funds": self.calculate_matching_funds(round_name)
                    }
                    return json.dumps(summary, indent=4)

            raise ValueError(f"Round '{round_name}' not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error retrieving round summary: {e}")


# Example usage
if __name__ == "__main__":
    manager = RoundManager()

    # Create a new funding round
    round_1 = manager.create_round("Round A", "2023-10-01", "2023-10-31", 10000)

    # Add contributions
    manager.add_contribution("Round A", "Alice", 500)
    manager.add_contribution("Round A", "Bob", 1500)

    # Get round summary
    summary = manager.get_round_summary("Round A")
    if summary:
        print(summary)

    # Calculate matching funds
    matching_funds = manager.calculate_matching_funds("Round A")
    if matching_funds is not None:
        print(f"Calculated Matching Funds: {matching_funds}")
```
