"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Create a Move-based smart contract for a gaming application that allows players to trade dynamic assets securely on the Sui blockchain.
Generated: DETERMINISTIC_18d1cd2df23b56a0
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
/// Module: game_assets
/// A Move smart contract for trading dynamic game assets on Sui
module game_assets::trading {
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{TxContext};
    use sui::dynamic_field;
    use sui::event;
    use std::option::{Self, Option};
    use std::string::{String};

    /// Error codes
    const E_NOT_OWNER: u64 = 0;
    const E_ASSET_NOT_FOUND: u64 = 1;
    const E_TRADE_NOT_FOUND: u64 = 2;
    const E_TRADE_EXISTS: u64 = 3;
    const E_INVALID_OFFER: u64 = 4;

    /// Asset type representing a game item
    struct GameAsset has key, store {
        id: UID,
        name: String,
        description: String,
        value: u64,
        metadata: vector<u8>
    }

    /// Trade offer between two players
    struct TradeOffer has key, store {
        id: UID,
        initiator: address,
        recipient: address,
        offered_assets: vector<ID>,
        requested_assets: vector<ID>,
        status: String,
        expiration: u64
    }

    /// Event emitted when a new trade is created
    struct TradeCreated has copy, drop {
        trade_id: ID,
        initiator: address,
        recipient: address,
        timestamp: u64
    }

    /// Event emitted when a trade is completed
    struct TradeCompleted has copy, drop {
        trade_id: ID,
        timestamp: u64
    }

    /// Event emitted when a trade is canceled
    struct TradeCanceled has copy, drop {
        trade_id: ID,
        timestamp: u64
    }

    /// Create a new game asset
    public entry fun create_asset(
        name: String,
        description: String,
        value: u64,
        metadata: vector<u8>,
        ctx: &mut TxContext
    ): GameAsset {
        GameAsset {
            id: object::new(ctx),
            name,
            description,
            value,
            metadata
        }
    }

    /// Create a new trade offer
    public entry fun create_trade(
        initiator: &mut GameAsset,
        recipient: address,
        offered_assets: vector<ID>,
        requested_assets: vector<ID>,
        expiration: u64,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == initiator.owner, E_NOT_OWNER);
        assert!(expiration > tx_context::epoch(ctx), E_INVALID_OFFER);

        let trade_id = object::new(ctx);
        let trade = TradeOffer {
            id: trade_id,
            initiator: tx_context::sender(ctx),
            recipient,
            offered_assets,
            requested_assets,
            status: string::utf8(b"pending"),
            expiration
        };

        // Store the trade in dynamic fields
        dynamic_field::add(&mut trade_id, b"trade", trade);

        // Emit trade created event
        event::emit(TradeCreated {
            trade_id: object::uid_to_inner(&trade_id),
            initiator: tx_context::sender(ctx),
            recipient,
            timestamp: tx_context::epoch(ctx)
        });
    }

    /// Accept a trade offer
    public entry fun accept_trade(
        recipient: &mut GameAsset,
        trade_id: ID,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == recipient.owner, E_NOT_OWNER);

        let trade: &mut TradeOffer = dynamic_field::borrow_mut(&trade_id, b"trade");
        assert!(trade.recipient == tx_context::sender(ctx), E_NOT_OWNER);
        assert!(trade.status == string::utf8(b"pending"), E_INVALID_OFFER);
        assert!(trade.expiration > tx_context::epoch(ctx), E_INVALID_OFFER);

        // Transfer assets
        transfer_assets(trade.initiator, trade.recipient, trade.offered_assets);
        transfer_assets(trade.recipient, trade.initiator, trade.requested_assets);

        // Update trade status
        trade.status = string::utf8(b"completed");

        // Emit trade completed event
        event::emit(TradeCompleted {
            trade_id: object::uid_to_inner(&trade_id),
            timestamp: tx_context::epoch(ctx)
        });
    }

    /// Cancel a trade offer
    public entry fun cancel_trade(
        initiator: &mut GameAsset,
        trade_id: ID,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == initiator.owner, E_NOT_OWNER);

        let trade: &mut TradeOffer = dynamic_field::borrow_mut(&trade_id, b"trade");
        assert!(trade.initiator == tx_context::sender(ctx), E_NOT_OWNER);
        assert!(trade.status == string::utf8(b"pending"), E_INVALID_OFFER);

        // Update trade status
        trade.status = string::utf8(b"canceled");

        // Emit trade canceled event
        event::emit(TradeCanceled {
            trade_id: object::uid_to_inner(&trade_id),
            timestamp: tx_context::epoch(ctx)
        });
    }

    /// Helper function to transfer multiple assets
    fun transfer_assets(
        from: address,
        to: address,
        asset_ids: vector<ID>
    ) {
        let i = 0;
        let len = vector::length(&asset_ids);
        while (i < len) {
            let asset_id = *vector::borrow(&asset_ids, i);
            transfer::transfer(object::id_to_address(asset_id), to);
            i = i + 1;
        }
    }

    /// Get trade details
    public fun get_trade(trade_id: ID): &TradeOffer {
        dynamic_field::borrow(&trade_id, b"trade")
    }

    /// Check if a trade exists
    public fun trade_exists(trade_id: ID): bool {
        dynamic_field::exists_(trade_id, b"trade")
    }
}
```
