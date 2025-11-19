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
module GameAssets::TradableAsset {

    use sui::object::UID;
    use sui::transfer;
    
    /// Struct representing the tradable in-game asset
    struct Asset has key, store {
        id: UID,              // Unique identifier for the asset
        name: vector<u8>,     // Name of the asset
        value: u64            // Numeric value representing the asset's worth
    }

    /// Public function to create a new asset
    /// Only the creator can invoke this function
    public entry fun create_asset(
        name: vector<u8>,     // Name of the asset
        value: u64            // Initial value of the asset
    ): Asset {
        let id = UID::new();  // Generate a new unique ID for the asset
        Asset { id, name, value }
    }

    /// Public function to transfer ownership of an asset
    public entry fun transfer_asset(
        asset: Asset,         // Asset to be transferred
        recipient: address    // Address of the recipient
    ) {
        transfer::transfer(asset, recipient); // Transfer the asset's ownership
    }

    /// Public function to update the asset's value
    /// Only the owner of the asset can update its value
    public entry fun update_value(
        asset: &mut Asset,    // Mutable reference to the asset
        new_value: u64        // New value to be set
    ) {
        assert!(new_value > 0, "Asset value must be greater than zero");
        asset.value = new_value;
    }
}
```
