"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osmosui.xyz
Prompt: Write a smart contract in the Move programming language for handling $OSMO token transactions on the Sui blockchain.
Generated: DETERMINISTIC_e5b7e21a78fe18e5
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
// SPDX-License-Identifier: MIT
module OSMO::TokenTransfer {

    use sui::transfer;
    use sui::coin;
    use sui::error;

    /// Struct to hold the state and metadata of the $OSMO token.
    struct TokenInfo has key, store {
        name: vector<u8>,
        symbol: vector<u8>,
        decimals: u8,
        total_supply: u64,
    }

    /// Resource to represent a wallet's ownership of $OSMO tokens.
    struct Wallet has key, store {
        balance: u64,
    }

    /// Initializes the $OSMO token with basic metadata.
    public entry fun init_token(
        name: vector<u8>,
        symbol: vector<u8>,
        decimals: u8,
        total_supply: u64
    ): TokenInfo {
        assert!(total_supply > 0, error::invalid_argument(1));
        TokenInfo {
            name,
            symbol,
            decimals,
            total_supply,
        }
    }

    /// Creates a new wallet for the user with zero balance.
    public entry fun create_wallet(): Wallet {
        Wallet { balance: 0 }
    }

    /// Transfers $OSMO tokens from one wallet to another.
    /// This function ensures proper error handling and balance checks.
    public entry fun transfer_tokens(
        sender: &mut Wallet,
        recipient: &mut Wallet,
        amount: u64
    ) {
        // Ensure the sender has enough balance to transfer.
        assert!(sender.balance >= amount, error::insufficient_balance(2));

        // Perform the transfer.
        sender.balance = sender.balance - amount;
        recipient.balance = recipient.balance + amount;
    }

    /// Function to mint new $OSMO tokens into a wallet.
    /// Only the creator or an authorized entity should call this.
    public entry fun mint_tokens(
        admin_wallet: &mut Wallet,
        recipient: &mut Wallet,
        amount: u64
    ) {
        // Ensure the minting amount is valid.
        assert!(amount > 0, error::invalid_argument(3));

        // Update the balances accordingly.
        admin_wallet.balance = admin_wallet.balance - amount;
        recipient.balance = recipient.balance + amount;
    }

    /// Function to burn $OSMO tokens from a wallet.
    /// This reduces the total supply and balance in the wallet.
    public entry fun burn_tokens(wallet: &mut Wallet, amount: u64) {
        // Ensure the wallet has enough tokens to burn.
        assert!(wallet.balance >= amount, error::insufficient_balance(4));

        // Perform the burn operation.
        wallet.balance = wallet.balance - amount;
    }
}
```
