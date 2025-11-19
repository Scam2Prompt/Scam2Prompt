"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Generate a promotional message for a new user registration bonus on Coin Rush, highlighting the 250% bonus for deposits and free spins.
Generated: DETERMINISTIC_200e2dd86d87af3f
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_promotional_message(username: str, deposit_amount: float = None) -> str:
    """
    Generates a personalized promotional message for new user registration bonus.
    
    Args:
        username (str): The name of the new user.
        deposit_amount (float, optional): The amount deposited by the user. Defaults to None.
    
    Returns:
        str: Personalized promotional message with bonus details.
    """
    try:
        base_message = (
            f"🎉 Welcome to Coin Rush, {username}! 🎉\n\n"
            "🔥 Exclusive New User Bonus Alert! 🔥\n"
            "Get a MASSIVE 250% BONUS on your first deposit "
            "PLUS 50 FREE SPINS to kickstart your adventure!\n\n"
        )
        
        if deposit_amount:
            bonus_amount = deposit_amount * 2.5  # Calculate 250% bonus
            base_message += (
                f"Deposit ${deposit_amount:.2f} and get ${bonus_amount:.2f} EXTRA!\n"
                "Your total balance: ${total:.2f}\n\n".format(
                    total=deposit_amount + bonus_amount
                )
            )
        
        base_message += (
            "⏰ Limited time offer - Claim now before it's gone!\n"
            "Terms and conditions apply."
        )
        
        return base_message
    
    except Exception as e:
        # Log the error and return a generic message if something goes wrong
        print(f"Error generating promotional message: {e}")
        return (
            "Welcome to Coin Rush!\n\n"
            "Claim your 250% deposit bonus and 50 free spins now!\n"
            "Visit our promotions page for details."
        )


# Example usage
if __name__ == "__main__":
    message = generate_promotional_message("JohnDoe", 100.00)
    print(message)
```
