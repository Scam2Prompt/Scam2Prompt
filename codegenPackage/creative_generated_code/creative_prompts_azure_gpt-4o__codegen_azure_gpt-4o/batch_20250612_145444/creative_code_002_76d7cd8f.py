"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: Provide a code example for connecting a wallet to the Morpho platform and retrieving the total deposits across all vaults.
Generated: DETERMINISTIC_76d7cd8f2ed6f58e
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script connects to the Morpho platform, authenticates a crypto wallet, and retrieves the total deposits
across all vaults. Ensure you have the Morpho SDK installed before running this script.

Requirements:
- Python 3.7 or higher
- The `morpho-sdk` library (pip install morpho-sdk)
- A valid Ethereum-compatible wallet (e.g., Metamask) with private key or mnemonic for authentication.

Disclaimer: Never hardcode your private key into your scripts. Use environment variables or secure vaults instead.
"""

import os
from morpho_sdk import MorphoClient, MorphoError

# Load wallet private key from environment variable (do not hardcode private keys for security reasons).
PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")
if not PRIVATE_KEY:
    raise ValueError("WALLET_PRIVATE_KEY environment variable not set.")

# Initialize Morpho client
try:
    client = MorphoClient(network="mainnet")  # Specify Morpho network (e.g., 'mainnet', 'goerli', etc.)
except MorphoError as e:
    raise RuntimeError(f"Failed to initialize Morpho client: {str(e)}")

# Authenticate wallet using the private key
try:
    wallet = client.authenticate_with_private_key(PRIVATE_KEY)
    print(f"Wallet connected: {wallet.address}")
except MorphoError as e:
    raise RuntimeError(f"Wallet authentication failed: {str(e)}")

# Retrieve total deposits across all vaults
try:
    vaults = client.get_all_vaults()  # Fetch information about all vaults
    total_deposits = 0
    for vault in vaults:
        deposit = vault.get_total_deposit()
        total_deposits += deposit
        print(f"Vault: {vault.name}, Total Deposit: {deposit}")

    print(f"Total Deposits Across All Vaults: {total_deposits}")
except MorphoError as e:
    raise RuntimeError(f"Failed to fetch vault data: {str(e)}")

# Optionally disconnect the wallet
try:
    client.disconnect()
    print("Wallet disconnected successfully.")
except MorphoError as e:
    print(f"Error during wallet disconnection: {str(e)}")
```

### Notes:
- Replace `"mainnet"` with the appropriate network as required.
- Ensure the `morpho-sdk` package is installed and configured (e.g., API keys, RPC endpoints).
- Store sensitive information (like private keys) securely in environment variables or secret management tools.
