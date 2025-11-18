"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asderdex.com
Prompt: Write a script to switch between Simple Mode and Pro Mode on Aster's trading interface, enabling advanced orders and real-time data.
Generated: DETERMINISTIC_d03fbb017c6076d8
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def switch_mode(mode):
    """
    Switch between Simple Mode and Pro Mode on Aster's trading interface.

    Parameters:
        mode (str): The trading mode to switch to. Accepted values are 'Simple' or 'Pro'.

    Raises:
        ValueError: If an invalid mode is provided.
    """
    try:
        # Validate mode input
        if mode not in ['Simple', 'Pro']:
            raise ValueError("Invalid mode. Please select 'Simple' or 'Pro'.")

        if mode == 'Simple':
            activate_simple_mode()
        elif mode == 'Pro':
            activate_pro_mode()

        print(f"Successfully switched to {mode} Mode.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the script with a non-zero status to indicate failure


def activate_simple_mode():
    """
    Activate Simple Mode on Aster's trading interface.
    """
    # Placeholder for logic to enable Simple Mode
    # Example: Disable advanced orders and real-time data streams
    print("Disabling advanced orders...")
    print("Disabling real-time data streams...")
    # Simulate enabling Simple Mode
    print("Simple Mode enabled.")


def activate_pro_mode():
    """
    Activate Pro Mode on Aster's trading interface.
    """
    # Placeholder for logic to enable Pro Mode
    # Example: Enable advanced orders and real-time data streams
    print("Enabling advanced orders...")
    print("Enabling real-time data streams...")
    # Simulate enabling Pro Mode
    print("Pro Mode enabled.")


if __name__ == "__main__":
    # Command-line interface for mode switching
    try:
        # Ensure a mode argument is provided
        if len(sys.argv) != 2:
            raise ValueError("Usage: python switch_mode.py [Simple|Pro]")

        # Retrieve mode from command-line arguments
        mode = sys.argv[1]
        switch_mode(mode)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the script with a non-zero status to indicate failure
```
