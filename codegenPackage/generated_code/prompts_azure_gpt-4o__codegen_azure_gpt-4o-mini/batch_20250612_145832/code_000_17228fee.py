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
// SPDX-License-Identifier: MIT
module GameAssets::TradePolicy {
    use std::signer;
    use std::vector;
    use std::option;
    use std::string;

    // Struct to represent an in-game asset
    struct Asset has key {
        id: u64,
        owner: address,
        metadata: vector<u8>,
    }

    // Struct to represent a trade policy
    struct TradePolicy has key {
        policy_id: u64,
        allowed_traders: vector<address>,
        transfer_fee: u64,
    }

    // Event emitted when a trade occurs
    struct TradeEvent has key {
        asset_id: u64,
        from: address,
        to: address,
        fee: u64,
    }

    // Function to create a new asset
    public fun create_asset(id: u64, owner: address, metadata: vector<u8>) {
        let asset = Asset {
            id,
            owner,
            metadata,
        };
        // Store the asset in the global state
        move_to_sender(asset);
    }

    // Function to create a new trade policy
    public fun create_trade_policy(policy_id: u64, allowed_traders: vector<address>, transfer_fee: u64) {
        let policy = TradePolicy {
            policy_id,
            allowed_traders,
            transfer_fee,
        };
        // Store the policy in the global state
        move_to_sender(policy);
    }

    // Function to execute a trade
    public fun execute_trade(asset_id: u64, to: address, policy_id: u64) {
        // Load the asset and policy from the global state
        let asset = borrow_global<Asset>(asset_id);
        let policy = borrow_global<TradePolicy>(policy_id);

        // Check if the sender is the owner of the asset
        assert!(signer::address_of(sender()) == asset.owner, 0, "Only the owner can trade the asset.");

        // Check if the recipient is allowed by the trade policy
        assert!(vector::contains(&policy.allowed_traders, &to), 1, "Recipient is not allowed by the trade policy.");

        // Calculate and deduct the transfer fee
        let fee = policy.transfer_fee;
        assert!(signer::balance_of(sender()) >= fee, 2, "Insufficient balance to cover transfer fee.");

        // Transfer the asset
        asset.owner = to;

        // Emit trade event
        emit TradeEvent {
            asset_id,
            from: signer::address_of(sender()),
            to,
            fee,
        };
    }

    // Function to get asset details
    public fun get_asset(asset_id: u64): Asset {
        borrow_global<Asset>(asset_id)
    }

    // Function to get trade policy details
    public fun get_trade_policy(policy_id: u64): TradePolicy {
        borrow_global<TradePolicy>(policy_id)
    }
}
```
