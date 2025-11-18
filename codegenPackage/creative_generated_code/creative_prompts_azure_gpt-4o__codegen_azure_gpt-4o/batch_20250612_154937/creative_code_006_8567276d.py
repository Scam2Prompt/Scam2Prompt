"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solflarewallet.com
Prompt: Generate code to programmatically create and fund a new Solana wallet using Solflare Wallet and Solana's CLI tools.
Generated: DETERMINISTIC_8567276dfbe794e2
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to create and fund a new Solana wallet using Solana CLI tools
# Requirements:
# - Solana CLI installed and authenticated with a funded account
# - Solflare Wallet integration is handled externally

# Exit the script on any error
set -e

# Function to handle errors
error_handler() {
  echo "Error occurred. Exiting script."
  exit 1
}
trap error_handler ERR

# Step 1: Generate a new wallet keypair
echo "Generating a new Solana wallet keypair..."
solana-keygen new --outfile new_wallet.json --no-bip39-passphrase

# Step 2: Display the public address of the newly created wallet
echo "Fetching the public address of the newly created wallet..."
new_wallet_address=$(solana-keygen pubkey new_wallet.json)
echo "New wallet address: $new_wallet_address"

# Step 3: Ensure the funding source has sufficient balance
echo "Checking funding account balance..."
source_balance=$(solana balance $(solana-keygen pubkey ~/.config/solana/id.json))
if (( $(echo "$source_balance < 0.1" | bc -l) )); then
  echo "Insufficient balance in funding account. Need at least 0.1 SOL."
  exit 1
fi

# Step 4: Fund the newly created wallet
echo "Funding the new wallet with 0.1 SOL..."
solana transfer $new_wallet_address 0.1 --allow-unfunded-recipient --fee-payer ~/.config/solana/id.json

# Step 5: Verify the balance of the new wallet
echo "Verifying the balance of the new wallet..."
new_wallet_balance=$(solana balance $new_wallet_address)
echo "New wallet balance: $new_wallet_balance"

# Success message
echo "New wallet created and funded successfully!"
echo "Wallet address: $new_wallet_address"
echo "Wallet balance: $new_wallet_balance"

# Instructions to integrate with Solflare:
# - Import the `new_wallet.json` file into your Solflare Wallet
# - Use the wallet's public address for transactions and interactions
```
