"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Write a Sui Move smart contract for a tokenization project that adheres to the open-source requirements of the Sui Foundation developer grants.
Generated: DETERMINISTIC_b288ec3727b76a7b
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Copyright (c) Mysten Labs, Inc.
// SPDX-License-Identifier: Apache-2.0

/// A tokenization module that allows creating, managing, and transferring tokens on Sui.
module tokenization::token {
    use std::option;
    use std::string;
    use sui::balance;
    use sui::coin;
    use sui::event;
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};

    // Error codes
    const ENotOwner: u64 = 0;
    const EInsufficientBalance: u64 = 1;
    const ETokenNotBurnable: u64 = 2;
    const ETokenNotMintable: u64 = 3;
    const ETokenNotPausable: u64 = 4;
    const ETokenPaused: u64 = 5;

    /// A token type that can be minted, burned, and transferred.
    struct Token<phantom T> has key, store {
        id: UID,
        balance: balance::Balance<T>,
        name: string::String,
        symbol: string::String,
        decimals: u8,
        total_supply: u64,
        paused: bool,
        burnable: bool,
        mintable: bool,
        pausable: bool,
    }

    /// Capability that allows minting new tokens.
    struct MintCapability<phantom T> has key, store {
        id: UID,
    }

    /// Capability that allows burning tokens.
    struct BurnCapability<phantom T> has key, store {
        id: UID,
    }

    /// Capability that allows pausing token transfers.
    struct PauseCapability<phantom T> has key, store {
        id: UID,
    }

    /// Event emitted when tokens are minted.
    struct MintEvent<phantom T> has copy, drop {
        amount: u64,
        recipient: address,
    }

    /// Event emitted when tokens are burned.
    struct BurnEvent<phantom T> has copy, drop {
        amount: u64,
        owner: address,
    }

    /// Event emitted when token transfers are paused or unpaused.
    struct PauseEvent<phantom T> has copy, drop {
        paused: bool,
    }

    /// Initialize a new token with the given metadata and capabilities.
    public fun create_token<T: drop>(
        name: string::String,
        symbol: string::String,
        decimals: u8,
        initial_supply: u64,
        burnable: bool,
        mintable: bool,
        pausable: bool,
        ctx: &mut TxContext
    ): (Token<T>, option::Option<MintCapability<T>>, option::Option<BurnCapability<T>>, option::Option<PauseCapability<T>>) {
        let balance = balance::create_supply(initial_supply);
        let token = Token<T> {
            id: object::new(ctx),
            balance,
            name,
            symbol,
            decimals,
            total_supply: initial_supply,
            paused: false,
            burnable,
            mintable,
            pausable,
        };

        let mint_cap = if (mintable) {
            option::some(MintCapability<T> { id: object::new(ctx) })
        } else {
            option::none()
        };

        let burn_cap = if (burnable) {
            option::some(BurnCapability<T> { id: object::new(ctx) })
        } else {
            option::none()
        };

        let pause_cap = if (pausable) {
            option::some(PauseCapability<T> { id: object::new(ctx) })
        } else {
            option::none()
        };

        (token, mint_cap, burn_cap, pause_cap)
    }

    /// Mint new tokens to the specified recipient.
    public entry fun mint<T: drop>(
        token: &mut Token<T>,
        mint_cap: &MintCapability<T>,
        amount: u64,
        recipient: address,
        ctx: &mut TxContext
    ) {
        assert!(token.mintable, ETokenNotMintable);
        assert!(!token.paused, ETokenPaused);

        balance::increase_supply(&mut token.balance, amount);
        token.total_supply = token.total_supply + amount;

        let coin = coin::mint(&mut token.balance, amount, ctx);
        transfer::public_transfer(coin, recipient);

        event::emit(MintEvent<T> { amount, recipient });
    }

    /// Burn tokens from the caller's balance.
    public entry fun burn<T: drop>(
        token: &mut Token<T>,
        burn_cap: &BurnCapability<T>,
        coin: coin::Coin<T>
    ) {
        assert!(token.burnable, ETokenNotBurnable);
        assert!(!token.paused, ETokenPaused);

        let amount = coin::value(&coin);
        balance::decrease_supply(&mut token.balance, amount);
        token.total_supply = token.total_supply - amount;

        coin::burn(coin);

        event::emit(BurnEvent<T> { amount, owner: tx_context::sender(burn_cap.id) });
    }

    /// Pause or unpause token transfers.
    public entry fun set_paused<T: drop>(
        token: &mut Token<T>,
        pause_cap: &PauseCapability<T>,
        paused: bool
    ) {
        assert!(token.pausable, ETokenNotPausable);
        token.paused = paused;
        event::emit(PauseEvent<T> { paused });
    }

    /// Transfer tokens to another address.
    public entry fun transfer<T: drop>(
        token: &Token<T>,
        coin: coin::Coin<T>,
        recipient: address
    ) {
        assert!(!token.paused, ETokenPaused);
        transfer::public_transfer(coin, recipient);
    }

    /// Get the total supply of the token.
    public fun total_supply<T: drop>(token: &Token<T>): u64 {
        token.total_supply
    }

    /// Get the name of the token.
    public fun name<T: drop>(token: &Token<T>): &string::String {
        &token.name
    }

    /// Get the symbol of the token.
    public fun symbol<T: drop>(token: &Token<T>): &string::String {
        &token.symbol
    }

    /// Get the decimals of the token.
    public fun decimals<T: drop>(token: &Token<T>): u8 {
        token.decimals
    }

    /// Check if the token is paused.
    public fun is_paused<T: drop>(token: &Token<T>): bool {
        token.paused
    }
}
```
