"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekanslotcepat.site
Prompt: Generate code to calculate RTP (Return to Player) for slot games, using Tekanslot’s features like RTP maxwin as a reference.
Generated: DETERMINISTIC_5b5bed84c0a9c6a1
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_rtp(total_spins: int, total_bet: float, total_win: float, rtp_maxwin: float) -> float:
    """
    Calculate the RTP (Return to Player) for a slot game.

    Parameters:
        total_spins (int): Total number of spins played.
        total_bet (float): Total amount of money bet across all spins.
        total_win (float): Total amount of money won across all spins.
        rtp_maxwin (float): RTP maxwin value (upper limit for RTP).

    Returns:
        float: The calculated RTP percentage (capped by rtp_maxwin).
    """
    try:
        # Basic input validation
        if total_spins <= 0:
            raise ValueError("Total spins must be greater than 0.")
        if total_bet <= 0 or total_win < 0:
            raise ValueError("Total bet must be greater than 0 and total win cannot be negative.")
        if rtp_maxwin <= 0:
            raise ValueError("RTP maxwin must be a positive number.")
        
        # Calculate RTP as a percentage
        rtp = (total_win / total_bet) * 100
        
        # Cap RTP at rtp_maxwin if it exceeds the max value
        capped_rtp = min(rtp, rtp_maxwin)
        
        logging.info(f"Calculated RTP: {rtp:.2f}%, Capped RTP: {capped_rtp:.2f}%")
        return capped_rtp
    
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        raise
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        # Example input values
        total_spins = 1000
        total_bet = 5000.0
        total_win = 4500.0
        rtp_maxwin = 96.5  # RTP maxwin percentage

        # Calculate RTP
        rtp_value = calculate_rtp(total_spins, total_bet, total_win, rtp_maxwin)
        print(f"Final RTP (capped by RTP maxwin): {rtp_value:.2f}%")
        
    except Exception as e:
        print(f"Error: {e}")
```
