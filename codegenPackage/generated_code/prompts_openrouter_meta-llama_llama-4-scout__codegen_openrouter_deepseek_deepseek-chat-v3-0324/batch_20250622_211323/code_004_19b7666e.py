"""
Generated Code Metadata:
========================
Original URL: https://suifox.online
Prompt: Develop a simple smart contract in Rust for a meme token on the Sui blockchain, considering fast and secure transactions.
Generated: DETERMINISTIC_19b7666eee247bae
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! MemeToken Smart Contract for Sui Blockchain
//! This contract implements a simple meme token with fast and secure transactions.

use sui::{
    object::{ID, UID},
    sui_types::{
        base_types::{SuiAddress, TxContext},
        error::SuiError,
        gas_coin::GasCoin,
        move_package::MovePackage,
    },
    transfer,
    tx_context::TxContext as SuiTxContext,
};

/// MemeToken struct representing the token with basic metadata.
struct MemeToken {
    id: UID,
    name: String,
    symbol: String,
    total_supply: u64,
    decimals: u8,
}

/// Initializes a new MemeToken with the given parameters.
/// # Arguments
/// * `name` - Name of the token
/// * `symbol` - Symbol of the token
/// * `total_supply` - Total supply of the token
/// * `decimals` - Number of decimal places
/// * `ctx` - Transaction context
public fun init(
    name: vector<u8>,
    symbol: vector<u8>,
    total_supply: u64,
    decimals: u8,
    ctx: &mut TxContext,
): MemeToken {
    MemeToken {
        id: object::new(ctx),
        name: string::utf8(name),
        symbol: string::utf8(symbol),
        total_supply,
        decimals,
    }
}

/// Transfers `amount` of MemeToken from `sender` to `recipient`.
/// # Arguments
/// * `token` - The MemeToken object
/// * `sender` - Address of the sender
/// * `recipient` - Address of the recipient
/// * `amount` - Amount to transfer
/// * `ctx` - Transaction context
public fun transfer(
    token: &mut MemeToken,
    sender: &SuiAddress,
    recipient: &SuiAddress,
    amount: u64,
    ctx: &mut TxContext,
) {
    assert!(amount > 0, SuiError::InvalidAmount);
    assert!(token.total_supply >= amount, SuiError::InsufficientBalance);

    token.total_supply = token.total_supply - amount;
    transfer::transfer(token, recipient, ctx);
}

/// Mints new tokens and adds them to the total supply.
/// # Arguments
/// * `token` - The MemeToken object
/// * `amount` - Amount to mint
public fun mint(
    token: &mut MemeToken,
    amount: u64,
) {
    assert!(amount > 0, SuiError::InvalidAmount);
    token.total_supply = token.total_supply + amount;
}

/// Burns tokens and removes them from the total supply.
/// # Arguments
/// * `token` - The MemeToken object
/// * `amount` - Amount to burn
public fun burn(
    token: &mut MemeToken,
    amount: u64,
) {
    assert!(amount > 0, SuiError::InvalidAmount);
    assert!(token.total_supply >= amount, SuiError::InsufficientBalance);
    token.total_supply = token.total_supply - amount;
}

/// Returns the total supply of the token.
/// # Arguments
/// * `token` - The MemeToken object
public fun total_supply(token: &MemeToken): u64 {
    token.total_supply
}

/// Returns the name of the token.
/// # Arguments
/// * `token` - The MemeToken object
public fun name(token: &MemeToken): String {
    token.name
}

/// Returns the symbol of the token.
/// # Arguments
/// * `token` - The MemeToken object
public fun symbol(token: &MemeToken): String {
    token.symbol
}

/// Returns the decimals of the token.
/// # Arguments
/// * `token` - The MemeToken object
public fun decimals(token: &MemeToken): u8 {
    token.decimals
}
```
