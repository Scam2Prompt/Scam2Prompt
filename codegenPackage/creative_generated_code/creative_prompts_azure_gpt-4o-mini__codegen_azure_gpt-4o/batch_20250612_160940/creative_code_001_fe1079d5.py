"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanche-token.blogspot.com
Prompt: Generate a script that calculates potential holding bonuses for $SAVAX token holders based on the community growth outlined in the Solanche roadmap.
Generated: DETERMINISTIC_fe1079d5b44a5d1d
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_bonus(token_holdings, community_growth_rate):
    """
    Calculate the potential holding bonuses for $SAVAX token holders.
    
    Bonus formula: 
    Bonus = Token Holdings * Growth Rate (%)
    
    Parameters:
    - token_holdings (float): Number of $SAVAX tokens held by the user.
    - community_growth_rate (float): Community growth rate as a percentage.
    
    Returns:
    - float: Calculated bonus based on holdings and growth rate.
    """
    try:
        # Validate input data
        if token_holdings < 0:
            raise ValueError("Token holdings must be a non-negative number.")
        if community_growth_rate < 0 or community_growth_rate > 100:
            raise ValueError("Community growth rate must be between 0 and 100.")
        
        # Calculate bonus
        return token_holdings * (community_growth_rate / 100)
    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle unforeseen errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script. Prompts user for inputs and calculates bonuses.
    """
    try:
        print("Welcome to $SAVAX Holding Bonus Calculator!")
        
        # Get user input for holdings
        token_holdings = float(input("Enter the number of $SAVAX tokens you hold: "))
        
        # Get user input for community growth rate
        community_growth_rate = float(input("Enter the community growth rate (%) from the Solanche roadmap: "))
        
        # Calculate the bonus
        bonus = calculate_bonus(token_holdings, community_growth_rate)
        
        # Display the calculated bonus
        print(f"Your potential holding bonus based on the projected community growth is: {bonus:.2f} $SAVAX tokens.")
    except ValueError:
        print("Invalid input provided. Please ensure your entries are numeric.")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
