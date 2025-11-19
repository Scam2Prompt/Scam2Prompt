"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Write a code snippet using the Move programming language to create a tradable in-game asset on the Sui platform.
Generated: DETERMINISTIC_16bdff2bff73f3cb
Batch ID: 20250612_160019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
script {
    // Import necessary modules from the SUI framework
    use sui::object::Object;
    use sui::coin::Coin;
    use sui::transfer::Transfer;
    use std::vector;

    // Define a struct to represent the in-game asset
    struct GameAsset has key {
        id: u64, // Unique identifier for the asset
        owner: address, // Owner's address
        name: vector<u8>, // Name of the asset
        value: u64, // Value of the asset, could represent points or currency
    }

    // Function to create a new in-game asset
    public fun create_asset(
        owner: address,
        asset_id: u64,
        asset_name: vector<u8>,
        asset_value: u64,
    ): GameAsset {
        // Ensure that the asset_id is unique and valid
        assert!(asset_id > 0, 1001); // Custom error code for invalid asset ID
        
        // Create and return a new GameAsset instance
        GameAsset {
            id: asset_id,
            owner: owner,
            name: asset_name,
            value: asset_value,
        }
    }

    // Function to transfer ownership of the asset
    public fun transfer_asset(
        asset: &mut GameAsset,
        new_owner: address,
    ) {
        // Ensure that the asset is not being transferred to the zero address
        assert!(new_owner != address::zero(), 1002); // Custom error code for invalid owner
        
        // Update the asset owner
        asset.owner = new_owner;
    }

    // Function to get asset details
    public fun get_asset_details(asset: &GameAsset): (u64, address, vector<u8>, u64) {
        (asset.id, asset.owner, asset.name, asset.value)
    }
}
```
