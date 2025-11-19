"""
Generated Code Metadata:
========================
Original URL: https://dogleonidas.pages.dev
Prompt: Generate a Python script to calculate the number of $DOG tokens received for a given ETH deposit, based on the presale rates provided on the webpage.
Generated: DETERMINISTIC_072db069099f15a9
Batch ID: 20250622_204748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Presale Token Calculator

Calculates the number of $DOG tokens received for a given ETH deposit based on presale rates.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_dog_tokens(eth_deposit: float, presale_rate: float) -> float:
    """
    Calculates the number of $DOG tokens received for a given ETH deposit.

    Args:
    - eth_deposit (float): The amount of ETH deposited.
    - presale_rate (float): The presale rate of $DOG tokens per ETH.

    Returns:
    - float: The number of $DOG tokens received.

    Raises:
    - ValueError: If eth_deposit or presale_rate is negative.
    """
    if eth_deposit < 0 or presale_rate <= 0:
        raise ValueError("ETH deposit must be non-negative and presale rate must be positive.")

    # Calculate $DOG tokens received
    dog_tokens = eth_deposit * presale_rate
    return dog_tokens


def main():
    try:
        # Presale rates (example rates, replace with actual rates)
        presale_rates = {
            "tier1": 1000,  # 1 ETH = 1000 $DOG
            "tier2": 800,   # 1 ETH = 800 $DOG
            # Add more tiers as needed
        }

        # Get ETH deposit from user
        while True:
            try:
                eth_deposit = float(input("Enter the amount of ETH deposited: "))
                if eth_deposit < 0:
                    print("Please enter a non-negative ETH deposit.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid ETH deposit.")

        # Display available presale tiers
        print("Available presale tiers:")
        for tier, rate in presale_rates.items():
            print(f"{tier}: 1 ETH = {rate} $DOG")

        # Get presale tier from user
        while True:
            tier_choice = input("Enter the presale tier (e.g., 'tier1'): ")
            if tier_choice in presale_rates:
                presale_rate = presale_rates[tier_choice]
                break
            else:
                print("Invalid tier. Please choose a valid presale tier.")

        # Calculate $DOG tokens received
        dog_tokens = calculate_dog_tokens(eth_deposit, presale_rate)

        # Display result
        print(f"For an ETH deposit of {eth_deposit} ETH at a rate of 1 ETH = {presale_rate} $DOG, you receive {dog_tokens} $DOG tokens.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
