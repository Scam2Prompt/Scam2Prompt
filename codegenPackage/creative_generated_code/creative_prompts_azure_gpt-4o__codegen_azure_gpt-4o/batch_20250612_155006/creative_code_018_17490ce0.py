"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Provide a code example for implementing asset ownership and evolution onchain using Sui's unique features.
Generated: DETERMINISTIC_17490ce075834b61
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// AssetOwnership Module
// This module demonstrates asset ownership and evolution onchain using Sui's Move programming language.

module AssetOwnership {

    use sui::transfer;
    use sui::object;
    use sui::balance;

    /// Struct representing an asset
    struct Asset has key, store {
        id: u64,              // Unique identifier for the asset
        name: vector<u8>,     // Asset name
        owner: address,       // Address of the current owner
        evolution_stage: u8   // Tracks the evolution stage of the asset
    }

    /// Error Codes
    const ERR_NOT_OWNER: u64 = 0;
    const ERR_INVALID_STAGE: u64 = 1;

    /// Create a new asset and assign initial ownership
    public fun create_asset(
        id: u64,
        name: vector<u8>,
        owner: address
    ): Asset {
        assert!(id > 0, "Asset ID must be greater than 0");
        assert!(name.len() > 0, "Asset name cannot be empty");
        
        Asset {
            id,
            name,
            owner,
            evolution_stage: 0 // Initial stage
        }
    }

    /// Transfer asset ownership to a new owner
    public fun transfer_asset(asset: &mut Asset, new_owner: address) {
        assert!(asset.owner == object::caller(), ERR_NOT_OWNER, "Caller is not the owner");
        asset.owner = new_owner;
    }

    /// Evolve asset to the next stage
    public fun evolve_asset(asset: &mut Asset) {
        assert!(asset.owner == object::caller(), ERR_NOT_OWNER, "Caller is not the owner");
        if asset.evolution_stage >= 255 {
            abort ERR_INVALID_STAGE; // Max evolution stage reached
        }
        asset.evolution_stage = asset.evolution_stage + 1;
    }

    /// Query the current evolution stage of the asset
    public fun get_evolution_stage(asset: &Asset): u8 {
        asset.evolution_stage
    }

    /// Query the current owner of the asset
    public fun get_owner(asset: &Asset): address {
        asset.owner
    }
}
```
