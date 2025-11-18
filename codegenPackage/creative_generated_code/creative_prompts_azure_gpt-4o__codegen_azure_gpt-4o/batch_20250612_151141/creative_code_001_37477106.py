"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjojoexchange.pages.dev
Prompt: Generate a Python script to calculate weekly airdrop points based on trading volume and average margin, following the rules outlined on the JOJO platform.
Generated: DETERMINISTIC_37477106d79b2fb8
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_airdrop_points(trading_volume, average_margin):
    """
    Calculate weekly airdrop points based on trading volume and average margin.

    Rules:
    - Points are proportional to trading volume, scaled by average margin.
    - Trading volume must be positive, and average margin must be between 0 and 100.

    Parameters:
    - trading_volume (float): Total trading volume of the user in USD.
    - average_margin (float): Average margin percentage.

    Returns:
    - float: Weekly airdrop points calculated using the formula.
    """
    try:
        # Validate inputs
        if trading_volume < 0:
            raise ValueError("Trading volume must be positive.")
        if not (0 <= average_margin <= 100):
            raise ValueError("Average margin must be between 0 and 100.")

        # Formula for calculating airdrop points (example logic)
        points = trading_volume * (average_margin / 100)
        return points

    except ValueError as ve:
        logging.error(f"Input validation error: {ve}")
        return 0.0
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return 0.0

def main():
    """
    Main function to handle user input and display weekly airdrop points.
    """
    try:
        # Prompt the user for input
        trading_volume = float(input("Enter your weekly trading volume (USD): "))
        average_margin = float(input("Enter your average margin percentage (0-100): "))

        # Calculate airdrop points
        points = calculate_airdrop_points(trading_volume, average_margin)

        # Display the result
        if points > 0:
            print(f"Your weekly airdrop points: {points:.2f}")
        else:
            print("Failed to calculate airdrop points due to invalid input.")

    except ValueError:
        logging.error("Invalid input. Please enter numeric values.")
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main function: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
