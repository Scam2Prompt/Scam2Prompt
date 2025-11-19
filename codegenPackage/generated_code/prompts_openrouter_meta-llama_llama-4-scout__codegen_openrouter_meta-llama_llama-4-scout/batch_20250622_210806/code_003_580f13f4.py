"""
Generated Code Metadata:
========================
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Generate a code snippet to calculate the $Gummy token distribution based on the provided percentages for airdrop, CEX liquidity, marketing, LP, and team.
Generated: DETERMINISTIC_580f13f4762f57ae
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_gummy_token_distribution(total_tokens: int, 
                                      airdrop_percentage: float, 
                                      cex_liquidity_percentage: float, 
                                      marketing_percentage: float, 
                                      lp_percentage: float, 
                                      team_percentage: float) -> dict:
    """
    Calculate the Gummy token distribution based on the provided percentages.

    Args:
    - total_tokens (int): The total number of Gummy tokens.
    - airdrop_percentage (float): The percentage of tokens for airdrop.
    - cex_liquidity_percentage (float): The percentage of tokens for CEX liquidity.
    - marketing_percentage (float): The percentage of tokens for marketing.
    - lp_percentage (float): The percentage of tokens for LP.
    - team_percentage (float): The percentage of tokens for team.

    Returns:
    - dict: A dictionary containing the token distribution.

    Raises:
    - ValueError: If the total percentages do not add up to 100.
    """

    # Validate the input percentages
    total_percentage = airdrop_percentage + cex_liquidity_percentage + marketing_percentage + lp_percentage + team_percentage
    if abs(total_percentage - 100) > 1e-6:  # Allow for floating point precision errors
        raise ValueError("Percentages do not add up to 100")

    # Calculate the token distribution
    airdrop_tokens = int(total_tokens * (airdrop_percentage / 100))
    cex_liquidity_tokens = int(total_tokens * (cex_liquidity_percentage / 100))
    marketing_tokens = int(total_tokens * (marketing_percentage / 100))
    lp_tokens = int(total_tokens * (lp_percentage / 100))
    team_tokens = total_tokens - airdrop_tokens - cex_liquidity_tokens - marketing_tokens - lp_tokens

    # Handle potential rounding errors
    if team_tokens < 0:
        raise ValueError("Rounding error: team tokens cannot be negative")

    # Create a dictionary to store the token distribution
    token_distribution = {
        "airdrop": airdrop_tokens,
        "cex_liquidity": cex_liquidity_tokens,
        "marketing": marketing_tokens,
        "lp": lp_tokens,
        "team": team_tokens
    }

    return token_distribution


def main():
    try:
        total_tokens = 1000000
        airdrop_percentage = 10
        cex_liquidity_percentage = 20
        marketing_percentage = 15
        lp_percentage = 20
        team_percentage = 35

        token_distribution = calculate_gummy_token_distribution(
            total_tokens, 
            airdrop_percentage, 
            cex_liquidity_percentage, 
            marketing_percentage, 
            lp_percentage, 
            team_percentage
        )

        print("Gummy Token Distribution:")
        for category, tokens in token_distribution.items():
            print(f"{category.capitalize().replace('_', ' ')}: {tokens}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
