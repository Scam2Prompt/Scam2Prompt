"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Generate a Python script to calculate the number of SHROOM tokens a user can buy based on the amount of ETH they spend, given the presale rates (e.g., 0.1 ETH ~ 99,500 SHROOM).
Generated: DETERMINISTIC_243dafa5faf8fef7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shroom_token_calculator.py

def calculate_shroom_tokens(eth_spent: float, presale_rate: float) -> int:
    """
    Calculate the number of SHROOM tokens a user can buy based on the amount of ETH they spend.

    Args:
    - eth_spent (float): The amount of ETH the user spends.
    - presale_rate (float): The presale rate of SHROOM tokens per ETH.

    Returns:
    - int: The number of SHROOM tokens the user can buy.

    Raises:
    - ValueError: If eth_spent or presale_rate is negative.
    """

    # Check for negative inputs
    if eth_spent < 0 or presale_rate <= 0:
        raise ValueError("ETH spent must be non-negative and presale rate must be positive.")

    # Calculate SHROOM tokens
    shroom_tokens = int(eth_spent * presale_rate)

    return shroom_tokens


def main():
    try:
        # Define presale rates (e.g., 0.1 ETH ~ 99,500 SHROOM)
        presale_rates = {
            0.1: 99500,  # 0.1 ETH ~ 99,500 SHROOM
            # Add more presale rates as needed
        }

        # Get user input
        eth_spent = float(input("Enter the amount of ETH you want to spend: "))

        # Display available presale rates
        print("Available presale rates:")
        for i, (eth, shroom) in enumerate(presale_rates.items()):
            print(f"{i+1}. {eth} ETH ~ {shroom} SHROOM")

        # Get user's presale rate choice
        while True:
            choice = input("Enter the number of your chosen presale rate: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(presale_rates):
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get chosen presale rate
        chosen_rate = list(presale_rates.items())[choice - 1][1] / list(presale_rates.items())[choice - 1][0]

        # Calculate SHROOM tokens
        shroom_tokens = calculate_shroom_tokens(eth_spent, chosen_rate)

        # Display result
        print(f"You can buy {shroom_tokens} SHROOM tokens with {eth_spent} ETH at the chosen presale rate.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
