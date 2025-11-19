"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Create a guide for deploying a scalable gaming application on Sui, focusing on dynamic asset management and royalty distribution using Move.
Generated: DETERMINISTIC_8d606708d6848120
Batch ID: 20250612_153915
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

/// Module for managing game assets and royalties on Sui
module game::asset_manager {
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use sui::coin::{Self, Coin};
    use sui::balance::{Self, Balance};
    use sui::url::{Self, Url};
    use sui::dynamic_field::{Self, DynamicField};
    use sui::event;

    // Error codes
    const ENotOwner: u64 = 0;
    const EAssetNotFound: u64 = 1;
    const EInvalidRoyalty: u64 = 2;
    const EInsufficientBalance: u64 = 3;

    // Event types
    struct AssetCreated<phantom T> has copy, drop {
        id: ID,
        creator: address,
        metadata: Url
    }

    struct RoyaltyPaid has copy, drop {
        asset_id: ID,
        recipient: address,
        amount: u64
    }

    /// Game asset that can be traded and has royalties
    struct GameAsset<phantom T> has key, store {
        id: UID,
        creator: address,
        metadata: Url,
        royalty_percentage: u8,
        supply: u64
    }

    /// Collection of assets owned by a user
    struct AssetCollection<phantom T> has key {
        id: UID,
        assets: vector<ID>
    }

    /// Royalty balance for creators
    struct RoyaltyBalance has key {
        id: UID,
        balance: Balance<SUI>
    }

    /// Initialize a new asset collection for a user
    public fun init_collection<T: store>(user: &signer, ctx: &mut TxContext) {
        let collection = AssetCollection<T> {
            id: object::new(ctx),
            assets: vector::empty()
        };
        transfer::transfer(collection, tx_context::sender(ctx));
    }

    /// Create a new game asset with metadata and royalty percentage
    public entry fun create_asset<T: store>(
        creator: &signer,
        metadata: Url,
        royalty_percentage: u8,
        initial_supply: u64,
        ctx: &mut TxContext
    ) {
        assert!(royalty_percentage <= 100, EInvalidRoyalty);
        
        let asset = GameAsset<T> {
            id: object::new(ctx),
            creator: tx_context::sender(creator),
            metadata,
            royalty_percentage,
            supply: initial_supply
        };

        let asset_id = object::id_to_address(&asset.id);
        event::emit(AssetCreated<T> {
            id: asset_id,
            creator: tx_context::sender(creator),
            metadata: metadata
        });

        // Add to creator's collection
        add_to_collection<T>(creator, asset_id, ctx);
        transfer::transfer(asset, tx_context::sender(ctx));
    }

    /// Internal function to add asset to user's collection
    fun add_to_collection<T: store>(
        user: &signer,
        asset_id: ID,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(user);
        let collection = get_or_create_collection<T>(sender, ctx);
        vector::push_back(&mut collection.assets, asset_id);
    }

    /// Get or create collection for user
    fun get_or_create_collection<T: store>(
        user: address,
        ctx: &mut TxContext
    ): AssetCollection<T> {
        if (!exists<AssetCollection<T>>(user)) {
            let collection = AssetCollection<T> {
                id: object::new(ctx),
                assets: vector::empty()
            };
            transfer::transfer(collection, user);
        };
        borrow_global_mut<AssetCollection<T>>(user)
    }

    /// Transfer asset between users with royalty payment
    public entry fun transfer_asset<T: store>(
        sender: &signer,
        receiver: address,
        asset_id: ID,
        payment: Coin<SUI>,
        ctx: &mut TxContext
    ) {
        let asset: GameAsset<T> = transfer_from_sender<T>(sender, asset_id);
        let royalty_amount = (coin::value(&payment) * (asset.royalty_percentage as u64)) / 100;
        let remaining_amount = coin::value(&payment) - royalty_amount;

        // Pay royalty to creator
        if (royalty_amount > 0) {
            pay_royalty<T>(&asset, royalty_amount, ctx);
        }

        // Transfer remaining amount to seller
        if (remaining_amount > 0) {
            let seller_coin = coin::split(&mut payment, remaining_amount, ctx);
            transfer::public_transfer(seller_coin, tx_context::sender(sender));
        }

        // Transfer asset to receiver
        transfer::public_transfer(asset, receiver);
        add_to_collection<T>(receiver, asset_id, ctx);
    }

    /// Internal function to pay royalty to creator
    fun pay_royalty<T: store>(
        asset: &GameAsset<T>,
        amount: u64,
        ctx: &mut TxContext
    ) {
        let creator = asset.creator;
        if (!exists<RoyaltyBalance>(creator)) {
            let balance = RoyaltyBalance {
                id: object::new(ctx),
                balance: balance::zero()
            };
            transfer::transfer(balance, creator);
        };

        let royalty_balance = borrow_global_mut<RoyaltyBalance>(creator);
        let coin = coin::take(&mut royalty_balance.balance, amount, ctx);
        transfer::public_transfer(coin, creator);

        event::emit(RoyaltyPaid {
            asset_id: object::id_to_address(&asset.id),
            recipient: creator,
            amount
        });
    }

    /// Withdraw accumulated royalties
    public entry fun withdraw_royalties(
        creator: &signer,
        amount: u64,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(creator);
        assert!(exists<RoyaltyBalance>(sender), EInsufficientBalance);
        
        let royalty_balance = borrow_global_mut<RoyaltyBalance>(sender);
        assert!(balance::value(&royalty_balance.balance) >= amount, EInsufficientBalance);
        
        let coin = coin::take(&mut royalty_balance.balance, amount, ctx);
        transfer::public_transfer(coin, sender);
    }

    /// Internal function to transfer asset from sender with checks
    fun transfer_from_sender<T: store>(
        sender: &signer,
        asset_id: ID
    ): GameAsset<T> {
        let sender_addr = tx_context::sender(sender);
        assert!(exists<GameAsset<T>>(asset_id), EAssetNotFound);
        
        let asset = move_from<GameAsset<T>>(asset_id);
        assert!(object::uid_to_address(&asset.id) == sender_addr, ENotOwner);
        
        asset
    }

    /// Update asset metadata (only creator can update)
    public entry fun update_metadata<T: store>(
        creator: &signer,
        asset_id: ID,
        new_metadata: Url,
        ctx: &mut TxContext
    ) {
        let asset: GameAsset<T> = transfer_from_sender<T>(creator, asset_id);
        assert!(asset.creator == tx_context::sender(creator), ENotOwner);
        
        asset.metadata = new_metadata;
        transfer::public_transfer(asset, tx_context::sender(ctx));
    }

    /// Get the royalty balance for a creator
    public fun get_royalty_balance(creator: address): u64 {
        if (exists<RoyaltyBalance>(creator)) {
            balance::value(&borrow_global<RoyaltyBalance>(creator).balance)
        } else {
            0
        }
    }
}
```
