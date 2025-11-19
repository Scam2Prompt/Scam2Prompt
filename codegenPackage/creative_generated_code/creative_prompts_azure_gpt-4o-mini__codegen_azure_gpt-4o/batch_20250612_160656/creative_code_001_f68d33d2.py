"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minting-genesisrunes.pages.dev
Prompt: Write a Python script that calculates the total fees for minting Genesis Runes based on user-selected speed (slow, medium, fast) and a maximum select fee of 64 SATS/VB.
Generated: DETERMINISTIC_f68d33d2ef76e0be
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_minting_fee(speed: str, sat_per_vbyte: int) -> int:
    """
    Calculate the total fees for minting Genesis Runes based on user-selected speed and SATS/VB.

    Args:
        speed (str): The desired speed ('slow', 'medium', 'fast').
        sat_per_vbyte (int): The maximum fee rate in SATS/VB (must be <= 64).

    Returns:
        int: The estimated minting fee in SATS.
    """
    # Transaction sizes in virtual bytes (vbytes) for Genesis Rune minting
    TRANSACTION_SIZE_VBYTES = {
        'slow': 250,     # Example size for 'slow' speed in vbytes
        'medium': 350,   # Example size for 'medium' speed in vbytes
        'fast': 450      # Example size for 'fast' speed in vbytes
    }

    # Validate the speed input
    if speed not in TRANSACTION_SIZE_VBYTES:
        raise ValueError(f"Invalid speed '{speed}'. Choose from 'slow', 'medium', or 'fast'.")

    # Validate SATS/VB input
    if not (1 <= sat_per_vbyte <= 64):
        raise ValueError("SATS/VB must be between 1 and 64.")

    # Calculate the total fee (SATS = SATS/VB * transaction size in vbytes)
    transaction_size = TRANSACTION_SIZE_VBYTES[speed]
    total_fee = sat_per_vbyte * transaction_size

    return total_fee


def main():
    """
    Main function to interact with the user and calculate minting fees.
    """
    try:
        # User input for speed
        print("Select minting speed (slow, medium, fast):")
        speed = input("Speed: ").strip().lower()

        # User input for SATS/VB
        print("Enter maximum fee rate (SATS/VB, max 64):")
        sat_per_vbyte = int(input("SATS/VB: "))

        # Calculate the minting fee
        fee = calculate_minting_fee(speed, sat_per_vbyte)

        # Display the result
        print(f"Total minting fee for {speed} speed: {fee} SATS")

    except ValueError as ve:
        # Handle invalid input errors gracefully
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
