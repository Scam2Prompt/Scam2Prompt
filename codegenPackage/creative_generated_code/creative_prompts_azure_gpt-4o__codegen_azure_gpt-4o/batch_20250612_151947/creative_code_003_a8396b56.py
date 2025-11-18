"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-pancake.pages.dev
Prompt: Write a script to check if a PancakeSwap lottery ticket matches the winning numbers in the correct order. Include logic for determining the prize bracket.
Generated: DETERMINISTIC_a8396b56fb65b6e2
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def check_lottery_ticket(ticket, winning_numbers):
    """
    Checks if the PancakeSwap lottery ticket matches the winning numbers and determines the prize bracket.
    
    Args:
        ticket (str): The lottery ticket number as a string.
        winning_numbers (str): The winning numbers as a string.
    
    Returns:
        str: A message indicating the prize bracket or if there's no match.
    """

    # Validate ticket and winning number formats
    if not re.match(r"^\d{6}$", ticket):
        raise ValueError("Invalid ticket number format. Must be a 6-digit number.")
    if not re.match(r"^\d{6}$", winning_numbers):
        raise ValueError("Invalid winning number format. Must be a 6-digit number.")

    # Initialize prize brackets
    prize_brackets = {
        6: "Jackpot! All 6 numbers match in order.",
        5: "Prize Bracket 2: First 5 numbers match in order.",
        4: "Prize Bracket 3: First 4 numbers match in order.",
        3: "Prize Bracket 4: First 3 numbers match in order.",
        2: "Prize Bracket 5: First 2 numbers match in order.",
        1: "Prize Bracket 6: First number matches."
    }

    # Check for matching numbers in order
    match_count = 0
    for i in range(len(ticket)):
        if ticket[i] == winning_numbers[i]:
            match_count += 1
        else:
            break  # Stop checking further once numbers stop matching

    # Return result based on match count
    if match_count in prize_brackets:
        return prize_brackets[match_count]
    else:
        return "No match. Better luck next time!"

# Example usage
if __name__ == "__main__":
    try:
        user_ticket = input("Enter your 6-digit lottery ticket: ").strip()
        winning_ticket = input("Enter the 6-digit winning numbers: ").strip()

        result = check_lottery_ticket(user_ticket, winning_ticket)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
