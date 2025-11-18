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
// This Move smart contract implements a digital asset ownership and transfer policy
// for a Web3 commerce platform on Sui. It allows users to create, transfer, and manage 
// ownership of digital assets.

module 0x1::DigitalAssets {

    /// Structure to represent a Digital Asset
    struct Asset has key {
        id: u64,                       // Unique identifier for the asset
        owner: address,                // Owner of the asset
        metadata: vector<u8>,          // Additional metadata for the asset
    }

    /// Resource to hold the total supply of assets
    struct AssetRegistry has store {
        total_supply: u64,             // Total number of assets created
    }

    /// Event to be emitted when an asset is created
    event AssetCreated(
        id: u64,
        owner: address,
        metadata: vector<u8>
    );

    /// Event to be emitted when an asset is transferred
    event AssetTransferred(
        id: u64,
        from: address,
        to: address
    );

    /// Initializes the asset registry
    public fun initialize_registry() {
        let registry = AssetRegistry { total_supply: 0 };
        move_to(sender, registry);
    }

    /// Creates a new digital asset
    public fun create_asset(metadata: vector<u8>) {
        let registry = borrow_global_mut<AssetRegistry>(@0x1);
        let new_id = registry.total_supply + 1;

        // Create a new asset and register its ownership
        let new_asset = Asset {
            id: new_id,
            owner: sender,
            metadata: metadata
        };

        move_to(sender, new_asset);
        registry.total_supply = new_id;

        // Emit an event indicating that a new asset has been created
        emit AssetCreated(new_id, sender, metadata);
    }

    /// Transfers ownership of an asset to a new owner
    public fun transfer_asset(asset_id: u64, new_owner: address) {
        // Fetch the asset from the sender's address
        let asset_ref = borrow_global_mut<Asset>(@0x1, asset_id);
        
        // Ensure the sender is the current owner of the asset
        assert!(asset_ref.owner == sender, 0);
        
        // Change the owner of the asset
        asset_ref.owner = new_owner;

        // Emit an event indicating that the asset has been transferred
        emit AssetTransferred(asset_id, sender, new_owner);
    }

    /// Retrieves asset details by ID
    public fun get_asset(asset_id: u64): Asset {
        let asset_ref = borrow_global<Asset>(@0x1, asset_id);
        return *asset_ref;
    }
}
```
