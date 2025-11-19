"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a Python script that calculates the number of DOG tokens received for a given ETH amount during the pre-sale, based on the conversion rate of 0.1 ETH to 99,500 DOG.
Generated: DETERMINISTIC_84e8fcb04b9fa86c
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to calculate the number of DOG tokens received for a given ETH amount.

def calculate_dog_tokens(eth_amount):
    """
    Function to calculate the DOG tokens received for a given ETH amount during the pre-sale.

    Conversion rate:
    0.1 ETH = 99,500 DOG
    
    :param eth_amount: float, Amount of ETH provided by the user.
    :return: float, Number of DOG tokens received.
    """
    try:
        # Check if the provided ETH amount is valid
        if eth_amount <= 0:
            raise ValueError("ETH amount must be greater than zero.")
        
        # Conversion rate: 0.1 ETH gives 99,500 DOG. Calculate the rate per ETH.
        conversion_rate = 99_500 / 0.1
        
        # Calculate DOG tokens received
        dog_tokens = eth_amount * conversion_rate
        return dog_tokens
    
    except Exception as e:
        # Handle any unexpected error and return a meaningful message
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to interact with the user and perform the calculation.
    """
    print("Welcome to the DOG Token Pre-sale Calculator!")
    
    try:
        # Prompt the user to enter the ETH amount
        eth_amount = float(input("Enter the amount of ETH you want to exchange for DOG tokens: "))
        
        # Calculate the DOG tokens
        dog_tokens = calculate_dog_tokens(eth_amount)
        
        if dog_tokens is not None:
            # Display the result to the user
            print(f"For {eth_amount:.4f} ETH, you will receive {dog_tokens:,.2f} DOG tokens.")
        else:
            print("Failed to calculate DOG tokens. Please try again.")
    
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for ETH amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
