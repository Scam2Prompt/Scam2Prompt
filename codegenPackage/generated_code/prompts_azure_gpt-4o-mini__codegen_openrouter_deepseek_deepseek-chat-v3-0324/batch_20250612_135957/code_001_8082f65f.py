"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: What are the key differences between the Capella, Bellatrix, and Altair editions of Ethereum's consensus layer upgrades as outlined in the Upgrading Ethereum documentation?
Generated: DETERMINISTIC_8082f65f55adf1e2
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script outlines the key differences between Ethereum's consensus layer upgrades
# Capella, Bellatrix, and Altair as per the official Ethereum documentation.

class EthereumUpgrade:
    """Base class representing an Ethereum consensus layer upgrade."""
    
    def __init__(self, name, activation_epoch, features):
        self.name = name
        self.activation_epoch = activation_epoch
        self.features = features
    
    def get_features(self):
        """Returns the features introduced in this upgrade."""
        return self.features
    
    def __str__(self):
        return f"{self.name} Upgrade (Activated at epoch {self.activation_epoch})"

def get_upgrade_differences():
    """Returns the key differences between Capella, Bellatrix, and Altair upgrades."""
    
    # Altair upgrade features (October 2021)
    altair = EthereumUpgrade(
        name="Altair",
        activation_epoch=74240,
        features={
            "Light client support": "Improved light client protocols",
            "Validator incentives": "Reward/penalty adjustments",
            "Sync committee": "New committee for light clients",
            "Epoch processing": "Optimized epoch transitions",
            "Validator inactivity": "New inactivity leak mechanism"
        }
    )
    
    # Bellatrix upgrade features (September 2022)
    bellatrix = EthereumUpgrade(
        name="Bellatrix",
        activation_epoch=144896,
        features={
            "Merge preparation": "Prepared Beacon Chain for The Merge",
            "Engine API": "Introduced Engine API for execution layer communication",
            "Difficulty bomb": "Delayed difficulty bomb",
            "Block processing": "Updated block processing for post-merge",
            "Validator rewards": "Adjusted validator rewards for merged chain"
        }
    )
    
    # Capella upgrade features (April 2023)
    capella = EthereumUpgrade(
        name="Capella",
        activation_epoch=194048,
        features={
            "Withdrawals": "Enabled validator withdrawals",
            "BLSToExecutionChange": "Allowed BLS to execution address changes",
            "Validator exit": "Streamlined voluntary exit process",
            "State transitions": "Updated state transition logic for withdrawals",
            "Fork choice": "Modified fork choice rules for withdrawal operations"
        }
    )
    
    return {
        "Altair": altair,
        "Bellatrix": bellatrix,
        "Capella": capella
    }

def main():
    """Main function to display upgrade differences."""
    try:
        upgrades = get_upgrade_differences()
        
        print("Ethereum Consensus Layer Upgrades Comparison\n")
        for name, upgrade in upgrades.items():
            print(f"\n=== {upgrade} ===")
            for feature, description in upgrade.get_features().items():
                print(f"- {feature}: {description}")
                
    except Exception as e:
        print(f"Error occurred while processing upgrade information: {e}")

if __name__ == "__main__":
    main()
```
