"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.polkadotstaker.com
Prompt: Generate code to query the Polkadot network for validator statistics and identify validators like Polkadot Staker for staking DOT tokens.
Generated: DETERMINISTIC_496178b3f5b6c43e
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# polkadot_validator_stats.py

import asyncio
from substrateinterface import SubstrateInterface, SubstrateRequestException

# Function to query validator statistics
async def fetch_validator_stats():
    """
    Connects to the Polkadot network, retrieves validator statistics, and identifies
    validators suitable for staking DOT tokens.
    """
    try:
        # Establish connection with the Polkadot network
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",  # Public Polkadot RPC endpoint
            ss58_format=0,               # Address format for Polkadot
            type_registry_preset='polkadot'
        )

        print("Connected to Polkadot network.")

        # Query the active validators set
        active_validators = substrate.query(
            module='Staking',
            storage_function='Validators'
        )

        # Print the total number of validators retrieved
        print(f"Total active validators: {len(active_validators)}")

        # List to store validator statistics
        validators_stats = []

        # Loop through each validator and retrieve relevant statistics
        for validator, metadata in active_validators.items():
            # Extract commission rate and other metadata
            commission_rate = metadata['commission'] / 10**7  # Adjust for precision
            blocked = metadata['blocked']

            # Check if validator is suitable for staking (custom criteria can be added)
            is_suitable_for_staking = (
                commission_rate < 10.0 and  # Commission less than 10%
                not blocked                 # Validator is not blocked
            )

            validator_info = {
                "address": validator,
                "commission_rate": commission_rate,
                "blocked": blocked,
                "suitable_for_staking": is_suitable_for_staking
            }

            validators_stats.append(validator_info)

        # Filter validators suitable for staking
        suitable_validators = [v for v in validators_stats if v['suitable_for_staking']]

        print(f"Total suitable validators for staking: {len(suitable_validators)}")

        # Display suitable validators (can be replaced with saving to a file or database)
        for validator in suitable_validators:
            print(f"Validator: {validator['address']}, Commission: {validator['commission_rate']}%")

    except SubstrateRequestException as e:
        print(f"Error querying Polkadot network: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        await substrate.close()
        print("Disconnected from Polkadot network.")

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(fetch_validator_stats())
```

### Notes:
- Ensure the `substrate-interface` package is installed: `pip install substrate-interface`.
- This script connects to the Polkadot network via the official RPC endpoint and retrieves validator statistics.
- Replace criteria for staking suitability (`commission_rate < 10.0`, `not blocked`) with your own logic as needed.
