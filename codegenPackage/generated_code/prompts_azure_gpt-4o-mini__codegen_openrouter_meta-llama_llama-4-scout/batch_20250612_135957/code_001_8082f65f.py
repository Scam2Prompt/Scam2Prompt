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
from enum import Enum

class EthereumUpgrade(Enum):
    CAPELLA = "Capella"
    BELLATRIX = "Bellatrix"
    ALTAIR = "Altair"

class EthereumUpgradeDocumentation:
    def __init__(self):
        self.upgrades = {
            EthereumUpgrade.CAPELLA: {
                "description": "The Capella upgrade, also known as Shapella, is a consensus layer upgrade that enables partial withdrawals and full EIP-4894 support.",
                "key_features": ["Partial withdrawals", "EIP-4894 support"]
            },
            EthereumUpgrade.BELLATRIX = {
                "description": "The Bellatrix upgrade is a consensus layer upgrade that prepares the network for the Merge and introduces the concept of 'execution layer' and 'consensus layer'.",
                "key_features": ["Preparation for the Merge", "Execution layer and consensus layer separation"]
            },
            EthereumUpgrade.ALTAIR = {
                "description": "The Altair upgrade is a consensus layer upgrade that introduces light clients and improves validator rewards and penalties.",
                "key_features": ["Light client support", "Validator rewards and penalties improvements"]
            }
        }

    def get_upgrade_info(self, upgrade: EthereumUpgrade):
        try:
            return self.upgrades[upgrade]
        except KeyError:
            raise ValueError(f"Invalid Ethereum upgrade: {upgrade}")

    def compare_upgrades(self, upgrades: list[EthereumUpgrade]):
        try:
            upgrade_info = {upgrade: self.get_upgrade_info(upgrade) for upgrade in upgrades}
            return upgrade_info
        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    documentation = EthereumUpgradeDocumentation()
    upgrades_to_compare = [EthereumUpgrade.CAPELLA, EthereumUpgrade.BELLATRIX, EthereumUpgrade.ALTAIR]

    upgrade_comparison = documentation.compare_upgrades(upgrades_to_compare)

    if upgrade_comparison:
        for upgrade, info in upgrade_comparison.items():
            print(f"Upgrade: {upgrade.value}")
            print(f"Description: {info['description']}")
            print(f"Key Features: {', '.join(info['key_features'])}")
            print("------------------------")

if __name__ == "__main__":
    main()
```
