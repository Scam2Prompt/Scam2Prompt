"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Write a Python function that calculates the potential winnings based on the RTP percentages of games available on ANGKA805.
Generated: DETERMINISTIC_a5fcb912ed041e53
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_winnings(bet_amount: float, rtp_percentage: float) -> float:
    """
    Calculate potential winnings based on the bet amount and the Return to Player (RTP) percentage.
    
    Parameters:
    bet_amount (float): The amount of money wagered.
    rtp_percentage (float): The Return to Player percentage (0 to 100).
    
    Returns:
    float: The potential winnings based on the RTP.
    
    Raises:
    ValueError: If the bet amount is negative or RTP percentage is not between 0 and 100.
    """
    
    # Validate the input parameters
    if bet_amount < 0:
        raise ValueError("Bet amount cannot be negative.")
    if rtp_percentage < 0 or rtp_percentage > 100:
        raise ValueError("RTP percentage must be between 0 and 100.")
    
    # Calculate potential winnings
    potential_winnings = (rtp_percentage / 100) * bet_amount
    
    return potential_winnings

# Example usage
if __name__ == "__main__":
    try:
        bet = 100.0  # Example bet amount
        rtp = 95.0   # Example RTP percentage
        
        winnings = calculate_potential_winnings(bet, rtp)
        print(f"Potential winnings for a bet of ${bet} with RTP of {rtp}%: ${winnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
