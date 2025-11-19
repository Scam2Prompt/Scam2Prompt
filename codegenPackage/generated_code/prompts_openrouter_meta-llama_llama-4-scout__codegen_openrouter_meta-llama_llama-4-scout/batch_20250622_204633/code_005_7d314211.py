"""
Generated Code Metadata:
========================
Original URL: https://shibarmypr.pages.dev
Prompt: Summarize the differences between SHIB, LEASH, and BONE tokens, focusing on their supply and utility within the Shiba ecosystem.
Generated: DETERMINISTIC_7d314211ba27203e
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Token Information Class
class TokenInfo:
    def __init__(self, name, total_supply, circulating_supply, utility):
        """
        Initialize a TokenInfo object.

        Args:
        - name (str): The name of the token.
        - total_supply (int): The total supply of the token.
        - circulating_supply (int): The circulating supply of the token.
        - utility (str): The utility of the token within the Shiba ecosystem.
        """
        self.name = name
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.utility = utility

# Shiba Ecosystem Token Summarizer
class ShibaTokenSummarizer:
    def __init__(self):
        """
        Initialize a ShibaTokenSummarizer object.
        """
        self.tokens = {}

    def add_token(self, token_info):
        """
        Add a token to the summarizer.

        Args:
        - token_info (TokenInfo): The token information to add.
        """
        self.tokens[token_info.name] = token_info

    def summarize_tokens(self):
        """
        Summarize the differences between SHIB, LEASH, and BONE tokens.

        Returns:
        - A dictionary with token names as keys and their information as values.
        """
        summary = {}
        for token_name, token_info in self.tokens.items():
            summary[token_name] = {
                "Total Supply": token_info.total_supply,
                "Circulating Supply": token_info.circulating_supply,
                "Utility": token_info.utility
            }
        return summary

    def print_summary(self):
        """
        Print the summary of the tokens in a readable format.
        """
        summary = self.summarize_tokens()
        for token_name, token_info in summary.items():
            print(f"**{token_name} Token Information:**")
            for key, value in token_info.items():
                print(f"- {key}: {value}")
            print()

def main():
    try:
        # Create a ShibaTokenSummarizer object
        summarizer = ShibaTokenSummarizer()

        # Create token information objects
        shib_info = TokenInfo(
            "SHIB",
            1000000000000,  # Total supply
            500000000000,   # Circulating supply (approximate)
            "The primary token used for transactions and community engagement within the Shiba ecosystem."
        )

        leash_info = TokenInfo(
            "LEASH",
            10725,          # Total supply
            3500,           # Circulating supply (approximate)
            "An ERC-20 token that rebalances and stabilizes the ShibaSwap ecosystem."
        )

        bone_info = TokenInfo(
            "BONE",
            250000000,      # Total supply
            0,              # Circulating supply (initially 0)
            "The governance token for the Shiba Inu ecosystem, used for voting on proposals."
        )

        # Add tokens to the summarizer
        summarizer.add_token(shib_info)
        summarizer.add_token(leash_info)
        summarizer.add_token(bone_info)

        # Print the summary
        summarizer.print_summary()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
