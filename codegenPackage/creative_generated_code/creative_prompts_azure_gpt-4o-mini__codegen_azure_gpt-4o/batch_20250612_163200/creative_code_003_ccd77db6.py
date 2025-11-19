"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-8wr.pages.dev
Prompt: Generate a function that allows users to select the sync type for their wallets in the MultiChainsFI system.
Generated: DETERMINISTIC_ccd77db6fbc86c5e
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from enum import Enum

class SyncType(Enum):
    """Enumeration for wallet sync types."""
    FULL_SYNC = "Full Sync"  # Complete sync of all wallet data
    LIGHT_SYNC = "Light Sync"  # Partial sync requiring less resources
    CUSTOM_SYNC = "Custom Sync"  # User-defined sync parameters

def select_wallet_sync_type():
    """
    Allows users to select the sync type for their wallets in the MultiChainsFI system.
    
    Returns:
        str: The selected sync type.
    """
    # Display the available sync options to the user
    print("Select the wallet sync type:")
    for index, sync_type in enumerate(SyncType, start=1):
        print(f"{index}. {sync_type.value}")

    try:
        # Prompt the user to select an option
        user_choice = int(input("Enter the number corresponding to your choice: "))
        
        # Validate the user's choice and return the selected sync type
        if user_choice < 1 or user_choice > len(SyncType):
            raise ValueError("Invalid choice. Please select a valid option.")

        selected_sync_type = list(SyncType)[user_choice - 1]
        print(f"You selected: {selected_sync_type.value}")
        return selected_sync_type.value

    except ValueError as ve:
        # Handle invalid input or invalid choice
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    selected_sync = select_wallet_sync_type()
    if selected_sync:
        print(f"Proceeding with {selected_sync}...")
    else:
        print("Wallet sync type selection failed.")
```
