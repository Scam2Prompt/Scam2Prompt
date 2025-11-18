"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Create a code example for implementing tradable in-game assets on the Sui blockchain, leveraging its dynamic asset functionality.
Generated: DETERMINISTIC_9b0adc6d0c299245
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// File: tradable_asset.move

// This Move module implements tradable in-game assets on the Sui blockchain using dynamic assets.
// It allows creation, transfer, and querying of asset data.

module tradable_asset::assets {

    use sui::object::{Self, UID};
    use sui::transfer::{Self, transfer};
    use sui::errors::{Self, error};
    use sui::tx_context::{Self, TxContext};

    // Asset struct representing an in-game tradable item
    struct Asset has key, store {
        id: UID,               // Unique identifier for the asset
        name: vector<u8>,      // Name of the asset
        description: vector<u8>, // Description of the asset
        value: u64,            // Value of the asset (e.g., in-game currency)
    }

    /// Public function to create a new Asset
    public fun create_asset(
        name: vector<u8>,
        description: vector<u8>,
        value: u64,
        ctx: &mut TxContext
    ): Asset {
        let asset = Asset {
            id: UID::new(ctx),
            name,
            description,
            value,
        };
        asset
    }

    /// Public function to transfer an Asset to another address
    public entry fun transfer_asset(
        asset: Asset,
        recipient: address,
        ctx: &mut TxContext
    ) {
        transfer(asset, recipient, ctx);
    }

    /// Public function to query details of an asset
    public fun get_asset_details(asset: &Asset): (vector<u8>, vector<u8>, u64) {
        (asset.name, asset.description, asset.value)
    }

    /// Error handling: Ensure asset value is non-negative
    public fun validate_asset_value(value: u64): bool {
        if (value < 0) {
            error("Asset value cannot be negative");
            return false;
        }
        true
    }
}
```
