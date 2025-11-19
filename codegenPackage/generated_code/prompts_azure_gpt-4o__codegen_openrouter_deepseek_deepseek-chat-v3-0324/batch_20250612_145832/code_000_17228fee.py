"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Write a smart contract using the Move programming language to create customizable trade and transfer policies for in-game assets on the Sui blockchain.
Generated: DETERMINISTIC_17228fee3a6fe5f8
Batch ID: 20250612_145832
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

module game_assets::policy {
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use sui::dynamic_field;
    use sui::event;
    use std::option::{Self, Option};
    use std::string::{Self, String};
    use std::vector;

    // Error codes
    const ENotOwner: u64 = 0;
    const EPolicyExists: u64 = 1;
    const EPolicyNotFound: u64 = 2;
    const EInvalidPolicy: u64 = 3;
    const ETransferNotAllowed: u64 = 4;
    const ETradeNotAllowed: u64 = 5;

    // Event types
    struct PolicyCreated has copy, drop {
        asset_id: ID,
        policy_id: ID
    }

    struct PolicyUpdated has copy, drop {
        policy_id: ID,
        field: String,
        new_value: String
    }

    struct PolicyRemoved has copy, drop {
        policy_id: ID
    }

    struct TransferEvent has copy, drop {
        asset_id: ID,
        from: address,
        to: address,
        policy_id: ID
    }

    struct TradeEvent has copy, drop {
        asset_id: ID,
        from: address,
        to: address,
        policy_id: ID
    }

    // Policy structure
    struct Policy has key, store {
        id: UID,
        asset_id: ID,
        owner: address,
        allow_transfer: bool,
        allow_trade: bool,
        transfer_fee: Option<u64>,
        trade_fee: Option<u64>,
        whitelist: vector<address>,
        blacklist: vector<address>,
        expiration: Option<u64>
    }

    // Creates a new policy for an asset
    public entry fun create_policy(
        asset: &mut UID,
        owner: address,
        allow_transfer: bool,
        allow_trade: bool,
        transfer_fee: Option<u64>,
        trade_fee: Option<u64>,
        whitelist: vector<address>,
        blacklist: vector<address>,
        expiration: Option<u64>,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == owner, ENotOwner);

        let policy_id = object::new(ctx);
        let policy = Policy {
            id: policy_id,
            asset_id: object::id(asset),
            owner,
            allow_transfer,
            allow_trade,
            transfer_fee,
            trade_fee,
            whitelist,
            blacklist,
            expiration
        };

        dynamic_field::add(&mut policy_id, object::id(asset), policy);
        
        event::emit(PolicyCreated {
            asset_id: object::id(asset),
            policy_id: object::id_to_address(&policy_id)
        });
    }

    // Updates a policy field
    public entry fun update_policy(
        policy: &mut Policy,
        field: String,
        new_value: String,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);

        if (string::utf8(&field) == b"allow_transfer") {
            policy.allow_transfer = string::utf8(&new_value) == b"true";
        } else if (string::utf8(&field) == b"allow_trade") {
            policy.allow_trade = string::utf8(&new_value) == b"true";
        } else if (string::utf8(&field) == b"transfer_fee") {
            policy.transfer_fee = option::some(string::parse_u64(&new_value));
        } else if (string::utf8(&field) == b"trade_fee") {
            policy.trade_fee = option::some(string::parse_u64(&new_value));
        } else if (string::utf8(&field) == b"expiration") {
            policy.expiration = option::some(string::parse_u64(&new_value));
        } else {
            abort EInvalidPolicy
        };

        event::emit(PolicyUpdated {
            policy_id: object::id_to_address(&policy.id),
            field,
            new_value
        });
    }

    // Removes a policy
    public entry fun remove_policy(
        policy: Policy,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);
        let Policy { id, asset_id: _, owner: _, allow_transfer: _, allow_trade: _, transfer_fee: _, trade_fee: _, whitelist: _, blacklist: _, expiration: _ } = policy;
        object::delete(id);
        
        event::emit(PolicyRemoved {
            policy_id: object::id_to_address(&id)
        });
    }

    // Transfers an asset with policy enforcement
    public entry fun transfer_with_policy(
        asset: &mut UID,
        policy: &Policy,
        recipient: address,
        ctx: &mut TxContext
    ) {
        assert!(policy.allow_transfer, ETransferNotAllowed);
        assert!(!vector::contains(&policy.blacklist, &recipient), ETransferNotAllowed);
        
        if (option::is_some(&policy.whitelist)) {
            assert!(vector::contains(&policy.whitelist, &recipient), ETransferNotAllowed);
        };

        if (option::is_some(&policy.expiration)) {
            assert!(tx_context::epoch(ctx) <= option::destroy_some(policy.expiration), ETransferNotAllowed);
        };

        transfer::public_transfer(asset, recipient);
        
        event::emit(TransferEvent {
            asset_id: object::id(asset),
            from: tx_context::sender(ctx),
            to: recipient,
            policy_id: object::id_to_address(&policy.id)
        });
    }

    // Trades an asset with policy enforcement
    public entry fun trade_with_policy(
        asset: &mut UID,
        policy: &Policy,
        recipient: address,
        ctx: &mut TxContext
    ) {
        assert!(policy.allow_trade, ETradeNotAllowed);
        assert!(!vector::contains(&policy.blacklist, &recipient), ETradeNotAllowed);
        
        if (option::is_some(&policy.whitelist)) {
            assert!(vector::contains(&policy.whitelist, &recipient), ETradeNotAllowed);
        };

        if (option::is_some(&policy.expiration)) {
            assert!(tx_context::epoch(ctx) <= option::destroy_some(policy.expiration), ETradeNotAllowed);
        };

        transfer::public_transfer(asset, recipient);
        
        event::emit(TradeEvent {
            asset_id: object::id(asset),
            from: tx_context::sender(ctx),
            to: recipient,
            policy_id: object::id_to_address(&policy.id)
        });
    }

    // Adds address to whitelist
    public entry fun add_to_whitelist(
        policy: &mut Policy,
        addr: address,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);
        assert!(!vector::contains(&policy.whitelist, &addr), EPolicyExists);
        vector::push_back(&mut policy.whitelist, addr);
    }

    // Removes address from whitelist
    public entry fun remove_from_whitelist(
        policy: &mut Policy,
        addr: address,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);
        let (found, index) = vector::index_of(&policy.whitelist, &addr);
        assert!(found, EPolicyNotFound);
        vector::remove(&mut policy.whitelist, index);
    }

    // Adds address to blacklist
    public entry fun add_to_blacklist(
        policy: &mut Policy,
        addr: address,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);
        assert!(!vector::contains(&policy.blacklist, &addr), EPolicyExists);
        vector::push_back(&mut policy.blacklist, addr);
    }

    // Removes address from blacklist
    public entry fun remove_from_blacklist(
        policy: &mut Policy,
        addr: address,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == policy.owner, ENotOwner);
        let (found, index) = vector::index_of(&policy.blacklist, &addr);
        assert!(found, EPolicyNotFound);
        vector::remove(&mut policy.blacklist, index);
    }

    // Gets policy for an asset
    public fun get_policy(policy_id: ID): &Policy {
        dynamic_field::borrow<ID, Policy>(&policy_id, &policy_id)
    }
}
```
