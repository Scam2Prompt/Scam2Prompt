"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bittensor-ecosystem.vercel.app
Prompt: Provide a Python script to fetch network statistics from the Bittensor ecosystem and display the current staking status.
Generated: DETERMINISTIC_8406dda57c69a604
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import bittensor
import sys

def fetch_network_statistics():
    """
    Fetch and display network statistics from the Bittensor ecosystem.
    This includes staking information for active network participants.
    """
    try:
        # Load the default wallet
        wallet = bittensor.wallet(name='default')
        
        # Connect to the Bittensor network
        subtensor = bittensor.subtensor(network=bittensor.defaults.network)
        
        # Fetch list of all network hotkeys (active participants)
        active_hotkeys = subtensor.get_hotkeys()
        if not active_hotkeys:
            print("No active participants found on the Bittensor network.")
            return
        
        print(f"Total active participants: {len(active_hotkeys)}")
        print("Staking Status:")
        print("-" * 50)
        
        # Fetch detailed staking information for each participant
        for hotkey in active_hotkeys:
            try:
                staking_info = subtensor.get_stake(hotkey=hotkey)
                total_stake = staking_info.total_stake if staking_info else 0.0
                print(f"Hotkey: {hotkey}\nTotal Stake: {total_stake:.6f} TAO\n")
            except Exception as e:
                print(f"Error fetching staking information for hotkey {hotkey}: {str(e)}")
                
        print("-" * 50)
        print("Staking information retrieval complete.")
    except Exception as e:
        print(f"An error occurred while fetching network statistics: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    """
    Entry point for the script. Fetches and displays staking information
    from the Bittensor ecosystem.
    """
    print("Fetching Bittensor network statistics...")
    fetch_network_statistics()
```
