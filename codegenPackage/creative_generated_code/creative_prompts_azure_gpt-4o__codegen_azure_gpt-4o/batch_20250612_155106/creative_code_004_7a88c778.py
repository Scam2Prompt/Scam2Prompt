"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-faq.io
Prompt: Create a script to evaluate user reviews and performance metrics for Web3 wallets, referencing Rabby Wallet's 4.8 user rating and reliability features.
Generated: DETERMINISTIC_7a88c778f0ba69f5
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import statistics

# Class to model a Web3 wallet
class Web3Wallet:
    def __init__(self, name, user_rating, reliability_score):
        """
        Initialize a Web3Wallet instance.

        :param name: Name of the wallet
        :param user_rating: User rating (0-5 scale)
        :param reliability_score: Reliability score (0-10 scale)
        """
        self.name = name
        self.user_rating = user_rating
        self.reliability_score = reliability_score

    def performance_metric(self):
        """
        Calculate an overall performance metric combining user rating and reliability score.

        :return: Combined performance metric (weighted average)
        """
        # Weighted average: user_rating contributes 60%, reliability_score contributes 40%
        return round(self.user_rating * 0.6 + (self.reliability_score / 10) * 0.4, 2)


# Function to load reviews from a JSON file
def load_reviews(file_path):
    """
    Load user reviews from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of reviews
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File at '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return []


# Function to evaluate wallets
def evaluate_wallets(wallets, reviews):
    """
    Evaluate wallets based on user reviews and performance metrics.

    :param wallets: List of Web3Wallet instances
    :param reviews: List of user reviews
    :return: None
    """
    print(f"{'Wallet Name':<15} {'User Rating':<12} {'Reliability':<12} {'Performance':<12}")
    print("-" * 50)

    for wallet in wallets:
        # Calculate performance metric
        performance = wallet.performance_metric()
        print(f"{wallet.name:<15} {wallet.user_rating:<12} {wallet.reliability_score:<12} {performance:<12}")

    print("\nUser Review Insights:")
    all_ratings = [review.get('rating', 0) for review in reviews if isinstance(review.get('rating', None), (int, float))]
    if all_ratings:
        print(f"Average User Rating: {statistics.mean(all_ratings):.2f}")
        print(f"Highest User Rating: {max(all_ratings):.1f}")
        print(f"Lowest User Rating: {min(all_ratings):.1f}")
    else:
        print("No valid ratings found in reviews.")


# Main execution
def main():
    """
    Main function to run the evaluation script.
    """
    # Reference wallet (Rabby Wallet with known attributes)
    rabby_wallet = Web3Wallet(name="Rabby Wallet", user_rating=4.8, reliability_score=9.5)

    # Additional wallet examples
    wallet_2 = Web3Wallet(name="MetaMask", user_rating=4.5, reliability_score=8.0)
    wallet_3 = Web3Wallet(name="Trust Wallet", user_rating=4.2, reliability_score=7.5)

    wallets = [rabby_wallet, wallet_2, wallet_3]

    # Load reviews from a JSON file (example file path)
    reviews = load_reviews("user_reviews.json")

    # Evaluate wallets and reviews
    evaluate_wallets(wallets, reviews)


# Entry point
if __name__ == "__main__":
    main()
```
