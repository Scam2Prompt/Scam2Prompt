"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: Write a technical overview of Ethereum's proof of stake transition, including the different editions of the Eth2 protocol, such as Capella, Bellatrix, and Altair.
Generated: DETERMINISTIC_897cfab24d3357a2
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Ethereum Proof of Stake Transition Overview

class EthereumPoSTransition:
    """
    A class to represent Ethereum's transition from Proof of Work (PoW) to Proof of Stake (PoS).
    Includes details about different Eth2 protocol upgrades.
    """
    
    def __init__(self):
        self.phases = {
            "Phase 0": {
                "name": "Beacon Chain",
                "launch_date": "December 1, 2020",
                "description": "Launched the Beacon Chain, introducing PoS consensus",
                "features": [
                    "Validator registration",
                    "Attestations",
                    "Finality gadget"
                ]
            },
            "Phase 1": {
                "name": "Shard Chains",
                "launch_date": "Postponed (merged with Phase 1.5)",
                "description": "Originally planned for shard chains implementation",
                "features": []
            },
            "Phase 1.5": {
                "name": "The Merge",
                "launch_date": "September 15, 2022",
                "description": "Ethereum Mainnet merged with Beacon Chain",
                "features": [
                    "Transition from PoW to PoS",
                    "Execution layer + consensus layer merge"
                ]
            },
            "Phase 2": {
                "name": "Shard Chains Execution",
                "launch_date": "Future",
                "description": "Will enable shard chains to process transactions",
                "features": []
            }
        }
        
        self.upgrades = {
            "Altair": {
                "launch_date": "October 27, 2021",
                "description": "First Beacon Chain upgrade",
                "features": [
                    "Light client support",
                    "Validator incentives overhaul",
                    "Sync committee for light clients"
                ]
            },
            "Bellatrix": {
                "launch_date": "September 6, 2022",
                "description": "Pre-Merge upgrade preparing for The Merge",
                "features": [
                    "Triggered Merge transition",
                    "Updated fork choice rules",
                    "Engine API for execution layer"
                ]
            },
            "Capella": {
                "launch_date": "April 12, 2023",
                "description": "Post-Merge upgrade enabling withdrawals",
                "features": [
                    "Validator withdrawals",
                    "BLSToExecutionChange messages",
                    "Updated state transition logic"
                ]
            }
        }
    
    def get_phases(self):
        """Returns all phases of Ethereum's PoS transition"""
        return self.phases
    
    def get_upgrades(self):
        """Returns all Eth2 protocol upgrades"""
        return self.upgrades
    
    def get_phase_details(self, phase_name):
        """Returns details for a specific phase"""
        try:
            return self.phases[phase_name]
        except KeyError:
            raise ValueError(f"Unknown phase: {phase_name}")
    
    def get_upgrade_details(self, upgrade_name):
        """Returns details for a specific upgrade"""
        try:
            return self.upgrades[upgrade_name]
        except KeyError:
            raise ValueError(f"Unknown upgrade: {upgrade_name}")


# Example usage
if __name__ == "__main__":
    eth_pos = EthereumPoSTransition()
    
    try:
        # Get all phases
        print("Ethereum PoS Transition Phases:")
        for phase, details in eth_pos.get_phases().items():
            print(f"{phase}: {details['name']} - {details['launch_date']}")
        
        # Get all upgrades
        print("\nEth2 Protocol Upgrades:")
        for upgrade, details in eth_pos.get_upgrades().items():
            print(f"{upgrade}: {details['description']} - {details['launch_date']}")
        
        # Get specific details
        print("\nDetails for 'The Merge':")
        print(eth_pos.get_phase_details("Phase 1.5"))
        
        print("\nDetails for 'Capella' upgrade:")
        print(eth_pos.get_upgrade_details("Capella"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
