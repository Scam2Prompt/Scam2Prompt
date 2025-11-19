"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Write a Move smart contract to implement digital asset ownership and transfer policies for a Web3 commerce platform on Sui.
Generated: DETERMINISTIC_ddf7223ed7dfe274
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// DigitalAsset.move

// Module for digital asset ownership and transfer policies
module DigitalAsset {
    use sui::object::{Object, UID};
    use sui::transfer;
    use sui::tx_context::TxContext;

    // Struct to represent a digital asset
    struct DigitalAsset has key, store {
        id: UID,
        owner: address,
        name: string,
        description: string,
    }

    // Public function to create a new digital asset
    public fun create_asset(
        name: string,
        description: string,
        ctx: &mut TxContext
    ): DigitalAsset {
        // Create a new digital asset
        let asset = DigitalAsset {
            id: UID::new(ctx),
            owner: ctx.sender(),
            name,
            description,
        };

        // Transfer the asset to the creator
        transfer::transfer_object(asset, ctx.sender());

        asset
    }

    // Public function to transfer a digital asset
    public fun transfer_asset(
        asset: DigitalAsset,
        new_owner: address,
        ctx: &mut TxContext
    ) {
        // Check if the sender is the current owner
        assert!(asset.owner == ctx.sender(), 1);

        // Update the owner
        asset.owner = new_owner;

        // Transfer the asset to the new owner
        transfer::transfer_object(asset, new_owner);
    }

    // Public function to update a digital asset's metadata
    public fun update_asset(
        asset: &mut DigitalAsset,
        name: string,
        description: string,
        ctx: &mut TxContext
    ) {
        // Check if the sender is the current owner
        assert!(asset.owner == ctx.sender(), 1);

        // Update the metadata
        asset.name = name;
        asset.description = description;
    }
}

// EntryPoint.move

// Module for entry points
module EntryPoint {
    use DigitalAsset;

    // Entry point for creating a new digital asset
    entry create_asset(
        name: string,
        description: string,
        ctx: &mut TxContext
    ) {
        let asset = DigitalAsset::create_asset(name, description, ctx);
        // Return the created asset
        return asset;
    }

    // Entry point for transferring a digital asset
    entry transfer_asset(
        asset: DigitalAsset,
        new_owner: address,
        ctx: &mut TxContext
    ) {
        DigitalAsset::transfer_asset(asset, new_owner, ctx);
    }

    // Entry point for updating a digital asset's metadata
    entry update_asset(
        asset: &mut DigitalAsset,
        name: string,
        description: string,
        ctx: &mut TxContext
    ) {
        DigitalAsset::update_asset(asset, name, description, ctx);
    }
}
```
