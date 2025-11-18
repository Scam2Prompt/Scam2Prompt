"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiio.vercel.app
Prompt: Write a Move smart contract to implement digital asset ownership and transfer policies for a Web3 commerce platform on Sui.
Generated: DETERMINISTIC_ddf7223ed7dfe274
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module Commerce::AssetOwnership {

    use sui::object::{Self, UID};
    use sui::tx_context::TxContext;
    use sui::error::Error;

    /// Struct representing an asset owned by an address
    struct Asset has key, store {
        id: UID,
        owner: address,
        metadata: vector<u8>, // Metadata for the asset (e.g., name, description, etc.)
    }

    /// Event emitted when an asset is transferred
    struct TransferEvent has drop {
        asset_id: UID,
        from: address,
        to: address,
    }

    /// Create a new asset
    public entry fun create_asset(
        owner: address,
        metadata: vector<u8>,
        ctx: &mut TxContext
    ): Asset {
        // Generate a unique ID for the asset
        let id = UID::new(ctx);

        // Return the new asset instance
        Asset {
            id,
            owner,
            metadata,
        }
    }

    /// Transfer an asset to a new owner
    public entry fun transfer_asset(
        asset: Asset,
        new_owner: address,
        ctx: &mut TxContext
    ): Asset acquires Asset {
        // Ensure the caller is the current owner of the asset
        let caller = ctx.sender();
        assert!(caller == asset.owner, Error::new(1, "Caller is not the owner of the asset"));

        // Emit a transfer event
        emit TransferEvent {
            asset_id: asset.id,
            from: asset.owner,
            to: new_owner,
        };

        // Update ownership and return the updated asset
        Asset {
            id: asset.id,
            owner: new_owner,
            metadata: asset.metadata,
        }
    }

    /// View asset details
    public fun view_asset(asset: &Asset): (UID, address, vector<u8>) {
        (asset.id, asset.owner, asset.metadata)
    }

    /// Validate asset ownership
    public fun is_owner(asset: &Asset, addr: address): bool {
        asset.owner == addr
    }
}
```
