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
// Import necessary modules
use sui::object::{Object, UID};
use sui::transfer;
use sui::tx_context::TxContext;

// Define a struct for in-game assets
struct Asset {
    id: UID,
    name: String,
    description: String,
    owner: address,
}

// Define a struct for trade policies
struct TradePolicy {
    id: UID,
    asset_id: ID<Asset>,
    allowed_traders: vector<address>,
    expiration_time: u64,
}

// Define a struct for transfer policies
struct TransferPolicy {
    id: UID,
    asset_id: ID<Asset>,
    allowed_transfers: vector<address>,
    transfer_cap: u64,
}

// Define the main contract
module GameAssets {
    use sui::object::{Self, Object, UID};
    use sui::transfer;
    use sui::tx_context::TxContext;

    // Define a table to store all assets
    public table Assets: Table<ID<Asset>, Asset>;

    // Define a table to store all trade policies
    public table TradePolicies: Table<ID<TradePolicy>, TradePolicy>;

    // Define a table to store all transfer policies
    public table TransferPolicies: Table<ID<TransferPolicy>, TransferPolicy>;

    // Function to create a new asset
    public fun create_asset(
        ctx: &mut TxContext,
        name: String,
        description: String,
    ): ID<Asset> {
        let asset = Asset {
            id: UID::new(ctx),
            name,
            description,
            owner: ctx.sender(),
        };
        table::add(&mut Assets, asset.id, asset);
        asset.id
    }

    // Function to create a new trade policy
    public fun create_trade_policy(
        ctx: &mut TxContext,
        asset_id: ID<Asset>,
        allowed_traders: vector<address>,
        expiration_time: u64,
    ): ID<TradePolicy> {
        let policy = TradePolicy {
            id: UID::new(ctx),
            asset_id,
            allowed_traders,
            expiration_time,
        };
        table::add(&mut TradePolicies, policy.id, policy);
        policy.id
    }

    // Function to create a new transfer policy
    public fun create_transfer_policy(
        ctx: &mut TxContext,
        asset_id: ID<Asset>,
        allowed_transfers: vector<address>,
        transfer_cap: u64,
    ): ID<TransferPolicy> {
        let policy = TransferPolicy {
            id: UID::new(ctx),
            asset_id,
            allowed_transfers,
            transfer_cap,
        };
        table::add(&mut TransferPolicies, policy.id, policy);
        policy.id
    }

    // Function to trade an asset
    public fun trade_asset(
        ctx: &mut TxContext,
        asset_id: ID<Asset>,
        trader: address,
        new_owner: address,
    ) {
        // Get the asset and trade policy
        let asset = table::borrow_mut(&mut Assets, asset_id);
        let policy = table::borrow(&TradePolicies, asset_id);

        // Check if the trader is allowed
        if !vector::contains(&policy.allowed_traders, &trader) {
            abort(1);
        }

        // Check if the policy has expired
        if policy.expiration_time < ctx.block_timestamp() {
            abort(2);
        }

        // Transfer the asset
        asset.owner = new_owner;
        transfer::transfer_object(asset_id, new_owner, ctx);
    }

    // Function to transfer an asset
    public fun transfer_asset(
        ctx: &mut TxContext,
        asset_id: ID<Asset>,
        new_owner: address,
    ) {
        // Get the asset and transfer policy
        let asset = table::borrow_mut(&mut Assets, asset_id);
        let policy = table::borrow(&TransferPolicies, asset_id);

        // Check if the transfer is allowed
        if !vector::contains(&policy.allowed_transfers, &ctx.sender()) {
            abort(3);
        }

        // Check if the transfer cap is reached
        if policy.transfer_cap == 0 {
            abort(4);
        }

        // Transfer the asset
        asset.owner = new_owner;
        transfer::transfer_object(asset_id, new_owner, ctx);
        policy.transfer_cap = policy.transfer_cap - 1;
    }
}
```
