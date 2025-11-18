"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://downtownspokanehotels.com
Prompt: Write a script to simulate a lottery number generator based on the betting combinations (e.g., 2D, 3D, 4D) mentioned on the Holyslots88 website.
Generated: DETERMINISTIC_72f43dd3768d1077
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_lottery_numbers(bet_type):
    """
    Generates lottery numbers based on the bet type.
    
    Parameters:
        bet_type (str): Type of betting combination (e.g., '2D', '3D', '4D').
        
    Returns:
        list: List of randomly generated lottery numbers based on the bet type.
    
    Raises:
        ValueError: If an unsupported bet type is provided.
    """
    # Define valid betting types and their corresponding digit counts
    bet_types = {
        '2D': 2,  # 2-digit lottery
        '3D': 3,  # 3-digit lottery
        '4D': 4   # 4-digit lottery
    }
    
    if bet_type not in bet_types:
        raise ValueError(f"Unsupported bet type: {bet_type}. Supported bet types are: {', '.join(bet_types.keys())}")
    
    digit_count = bet_types[bet_type]
    return [random.randint(0, 9) for _ in range(digit_count)]

def main():
    """
    Main function to simulate the lottery number generator.
    
    Prompts the user for a bet type, generates the lottery numbers, and displays them.
    """
    print("Welcome to the Lottery Number Generator!")
    print("Supported bet types: 2D, 3D, 4D")
    
    try:
        # Get user input for bet type
        bet_type = input("Enter your bet type (e.g., '2D', '3D', '4D'): ").strip().upper()
        
        # Generate lottery numbers
        lottery_numbers = generate_lottery_numbers(bet_type)
        
        # Display the generated lottery numbers
        print(f"Generated lottery numbers for {bet_type}: {' '.join(map(str, lottery_numbers))}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
