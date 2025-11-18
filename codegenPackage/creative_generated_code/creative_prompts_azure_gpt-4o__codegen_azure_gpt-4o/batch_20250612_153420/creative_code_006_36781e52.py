"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Write code to calculate and display the mining power generated from burning BTCMTX mining credits in a decentralized cloud mining platform.
Generated: DETERMINISTIC_36781e520cebbd42
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mining_power(burned_credits):
    """
    Function to calculate mining power generated from BTCMTX mining credits.
    
    Parameters:
    burned_credits (float): Number of BTCMTX mining credits burned.

    Returns:
    float: The mining power generated in TH/s.
    """
    # Conversion rate: 1 BTCMTX credit generates 0.5 TH/s mining power
    MINING_POWER_RATE = 0.5  # TH/s per BTCMTX credit

    # Validate the input
    if burned_credits < 0:
        raise ValueError("Burned credits must be a non-negative value.")

    # Calculate mining power
    mining_power = burned_credits * MINING_POWER_RATE
    return mining_power


def main():
    """
    Main function to handle user input and display mining power.
    """
    try:
        print("Welcome to the BTCMTX Mining Power Calculator.")
        # Prompt the user for the number of BTCMTX credits burned
        burned_credits = float(input("Enter the number of BTCMTX mining credits burned: "))

        # Calculate the mining power
        mining_power = calculate_mining_power(burned_credits)

        # Display the result
        print(f"Burning {burned_credits} BTCMTX mining credits generates {mining_power:.2f} TH/s mining power.")
    except ValueError as ve:
        # Handle value errors (e.g., invalid or negative input)
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
