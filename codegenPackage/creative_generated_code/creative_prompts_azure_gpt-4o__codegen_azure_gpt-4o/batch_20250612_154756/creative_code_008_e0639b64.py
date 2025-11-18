"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a Python script to simulate the lottery prize draw for consórcio participants, ensuring compliance with the rules and tax deductions outlined on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_e0639b6472d47204
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

def calculate_tax_deduction(prize_amount):
    """
    Calculate the tax deduction based on the prize amount.
    Assuming a flat tax rate of 30% (as an example, adjust as per actual rules).
    
    Args:
        prize_amount (float): The total prize amount.
    
    Returns:
        float: The net prize amount after tax deduction.
    """
    tax_rate = 0.30  # 30% tax rate
    deducted_amount = prize_amount * tax_rate
    return prize_amount - deducted_amount


def simulate_lottery_draw(participants, prize_amount):
    """
    Simulate the lottery draw for consórcio participants.
    
    Args:
        participants (list of str): List of participant names.
        prize_amount (float): The total prize amount.
    
    Returns:
        dict: A dictionary containing the winner and their net prize amount.
    """
    if not participants:
        raise ValueError("Participants list cannot be empty.")
    if prize_amount <= 0:
        raise ValueError("Prize amount must be greater than zero.")
    
    # Randomly select a winner
    winner = random.choice(participants)
    
    # Calculate the net prize after tax deduction
    net_prize = calculate_tax_deduction(prize_amount)
    
    return {"winner": winner, "net_prize": net_prize}


def main():
    """
    Main function to execute the lottery simulation.
    Includes input handling and result output.
    """
    try:
        # Input participants and prize amount
        participants = input("Enter participant names (comma-separated): ").strip().split(",")
        participants = [p.strip() for p in participants if p.strip()]  # Clean up participant names
        
        if not participants:
            raise ValueError("You must provide at least one participant.")

        prize_amount = float(input("Enter the prize amount: "))
        if prize_amount <= 0:
            raise ValueError("Prize amount must be a positive number.")

        # Simulate the lottery draw
        result = simulate_lottery_draw(participants, prize_amount)

        # Output the result
        print(f"Winner: {result['winner']}")
        print(f"Net Prize Amount (after tax deduction): ${result['net_prize']:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
