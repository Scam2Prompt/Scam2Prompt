"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: What are the key differences between the EVM chains supported by the Solidus AI Tech platform, and how do they impact the staking experience for AITECH token holders?
Generated: DETERMINISTIC_6aa79cf965e286e9
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Supported EVM chains
from enum import Enum
from typing import Dict

class EVMChain(Enum):
    """Enum representing supported EVM chains."""
    ETHEREUM = "Ethereum"
    POLYGON = "Polygon"
    BINANCE_SMART_CHAIN = "Binance Smart Chain"
    AVALANCHE = "Avalanche"

# Chain properties
CHAIN_PROPERTIES: Dict[EVMChain, Dict[str, str]] = {
    EVMChain.ETHEREUM: {
        "staking_requirement": "10 AITECH",
        "staking_duration": "30 days",
        "reward_rate": "5%",
    },
    EVMChain.POLYGON: {
        "staking_requirement": "5 AITECH",
        "staking_duration": "15 days",
        "reward_rate": "4%",
    },
    EVMChain.BINANCE_SMART_CHAIN: {
        "staking_requirement": "20 AITECH",
        "staking_duration": "60 days",
        "reward_rate": "6%",
    },
    EVMChain.AVALANCHE: {
        "staking_requirement": "15 AITECH",
        "staking_duration": "30 days",
        "reward_rate": "5.5%",
    },
}

def get_chain_properties(chain: EVMChain) -> Dict[str, str]:
    """Retrieve properties for a specific EVM chain."""
    try:
        return CHAIN_PROPERTIES[chain]
    except KeyError:
        raise ValueError(f"Unsupported EVM chain: {chain}")

def compare_chains() -> Dict[str, Dict[EVMChain, str]]:
    """Compare key differences between supported EVM chains."""
    comparison_result = {
        "staking_requirement": {},
        "staking_duration": {},
        "reward_rate": {},
    }
    
    for chain in EVMChain:
        properties = get_chain_properties(chain)
        comparison_result["staking_requirement"][chain] = properties["staking_requirement"]
        comparison_result["staking_duration"][chain] = properties["staking_duration"]
        comparison_result["reward_rate"][chain] = properties["reward_rate"]
    
    return comparison_result

def print_comparison_result(comparison_result: Dict[str, Dict[EVMChain, str]]) -> None:
    """Print comparison result in a readable format."""
    for category, chain_values in comparison_result.items():
        print(f"**{category.capitalize().replace('_', ' ')}**")
        for chain, value in chain_values.items():
            print(f"{chain.value}: {value}")
        print()  # Empty line for better readability

def main() -> None:
    try:
        comparison_result = compare_chains()
        print_comparison_result(comparison_result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
