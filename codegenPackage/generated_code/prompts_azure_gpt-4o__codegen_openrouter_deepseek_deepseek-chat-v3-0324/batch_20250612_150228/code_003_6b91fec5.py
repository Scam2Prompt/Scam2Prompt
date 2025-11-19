"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Write a smart contract in Move language to utilize NAVI Protocol's shared liquidity pool system for lending and borrowing assets on the Sui blockchain.
Generated: DETERMINISTIC_6b91fec58aee588e
Batch ID: 20250612_150228
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

module navi::lending {
    use sui::coin::{Self, Coin};
    use sui::balance::{Self, Balance};
    use sui::object::{Self, ID, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use sui::dynamic_field;
    use sui::event;
    use sui::sui::SUI;
    use navi::protocol::{Self, LendingPool, BorrowReceipt, DepositReceipt};

    // Error codes
    const EINSUFFICIENT_BALANCE: u64 = 0;
    const EINVALID_POOL: u64 = 1;
    const EINVALID_COIN_TYPE: u64 = 2;
    const ELOAN_EXCEEDS_LIMIT: u64 = 3;
    const EREPAYMENT_FAILED: u64 = 4;
    const EWITHDRAWAL_FAILED: u64 = 5;
    const EINVALID_RECEIPT: u64 = 6;

    // Events
    struct DepositEvent has copy, drop {
        pool_id: ID,
        amount: u64,
        user: address,
    }

    struct BorrowEvent has copy, drop {
        pool_id: ID,
        amount: u64,
        user: address,
    }

    struct RepayEvent has copy, drop {
        pool_id: ID,
        amount: u64,
        user: address,
    }

    struct WithdrawEvent has copy, drop {
        pool_id: ID,
        amount: u64,
        user: address,
    }

    // Main lending contract
    public entry fun deposit<T>(
        pool: &mut LendingPool<T>,
        coin: Coin<T>,
        ctx: &mut TxContext
    ) {
        let amount = coin::value(&coin);
        let sender = tx_context::sender(ctx);

        // Verify pool is valid
        assert!(protocol::is_valid_pool(pool), EINVALID_POOL);

        // Deposit into pool
        let receipt = protocol::deposit(pool, coin);

        // Emit deposit event
        event::emit(DepositEvent {
            pool_id: object::id(pool),
            amount,
            user: sender,
        });

        // Transfer receipt to user
        transfer::public_transfer(receipt, sender);
    }

    public entry fun borrow<T>(
        pool: &mut LendingPool<T>,
        amount: u64,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);

        // Verify pool is valid
        assert!(protocol::is_valid_pool(pool), EINVALID_POOL);

        // Borrow from pool
        let (coin, receipt) = protocol::borrow(pool, amount, ctx);

        // Emit borrow event
        event::emit(BorrowEvent {
            pool_id: object::id(pool),
            amount,
            user: sender,
        });

        // Transfer assets to user
        transfer::public_transfer(coin, sender);
        transfer::public_transfer(receipt, sender);
    }

    public entry fun repay<T>(
        pool: &mut LendingPool<T>,
        receipt: BorrowReceipt<T>,
        coin: Coin<T>,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        let amount = coin::value(&coin);

        // Verify pool is valid
        assert!(protocol::is_valid_pool(pool), EINVALID_POOL);

        // Repay loan
        protocol::repay(pool, receipt, coin);

        // Emit repay event
        event::emit(RepayEvent {
            pool_id: object::id(pool),
            amount,
            user: sender,
        });
    }

    public entry fun withdraw<T>(
        pool: &mut LendingPool<T>,
        receipt: DepositReceipt<T>,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);

        // Verify pool is valid
        assert!(protocol::is_valid_pool(pool), EINVALID_POOL);

        // Withdraw from pool
        let (coin, interest) = protocol::withdraw(pool, receipt, ctx);

        let amount = coin::value(&coin) + coin::value(&interest);

        // Emit withdraw event
        event::emit(WithdrawEvent {
            pool_id: object::id(pool),
            amount,
            user: sender,
        });

        // Transfer assets to user
        transfer::public_transfer(coin, sender);
        transfer::public_transfer(interest, sender);
    }

    // Helper functions
    public fun get_pool_balance<T>(pool: &LendingPool<T>): u64 {
        protocol::get_pool_balance(pool)
    }

    public fun get_borrow_balance<T>(pool: &LendingPool<T>): u64 {
        protocol::get_borrow_balance(pool)
    }

    public fun get_interest_rate<T>(pool: &LendingPool<T>): u64 {
        protocol::get_interest_rate(pool)
    }

    public fun get_utilization_rate<T>(pool: &LendingPool<T>): u64 {
        protocol::get_utilization_rate(pool)
    }
}
```
