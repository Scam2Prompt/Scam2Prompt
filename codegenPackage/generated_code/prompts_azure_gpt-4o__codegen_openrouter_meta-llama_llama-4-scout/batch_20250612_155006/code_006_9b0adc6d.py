"""
Generated Code Metadata:
========================
Original URL: https://sui-dapps.vercel.app
Prompt: Create a code example for implementing tradable in-game assets on the Sui blockchain, leveraging its dynamic asset functionality.
Generated: DETERMINISTIC_9b0adc6d0c299245
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary modules from Sui
use sui::types::{SuiAddress, ObjectID};
use sui::MoveModule;
use sui::MoveValue;

// Define a struct for the tradable in-game asset
struct TradableAsset {
    id: ObjectID,
    name: String,
    description: String,
    owner: SuiAddress,
}

// Implement the TradableAsset struct
impl TradableAsset {
    // Create a new TradableAsset
    fn new(id: ObjectID, name: String, description: String, owner: SuiAddress) -> Self {
        TradableAsset { id, name, description, owner }
    }
}

// Define a module for the in-game asset
#[move]
module sui_example::tradable_asset {
    use sui::object::{Self, Object};
    use sui::types::{SuiAddress, ObjectID};

    // Define a struct for the tradable asset
    struct TradableAsset has key, store {
        id: ObjectID,
        name: string,
        description: string,
        owner: SuiAddress,
    }

    // Define a function to create a new tradable asset
    public fun create_tradable_asset(
        ctx: &mut MoveContext,
        name: string,
        description: string,
    ): Object {
        let creator = ctx.signer();
        let asset = TradableAsset {
            id: Object::new(ctx),
            name,
            description,
            owner: creator,
        };
        Object::new(asset)
    }

    // Define a function to transfer ownership of the tradable asset
    public fun transfer_ownership(
        ctx: &mut MoveContext,
        asset: Object,
        new_owner: SuiAddress,
    ) {
        let asset_mut = asset.borrow_mut();
        asset_mut.owner = new_owner;
    }

    // Define a function to get the details of the tradable asset
    public fun get_asset_details(
        ctx: &MoveContext,
        asset: &Object,
    ): (string, string, SuiAddress) {
        let asset_borrow = asset.borrow();
        (asset_borrow.name, asset_borrow.description, asset_borrow.owner)
    }
}

// Define a Sui Move module for interacting with the tradable asset
#[move]
module sui_example::tradable_asset_module {
    use sui_example::tradable_asset;

    // Define a function to create a new tradable asset
    public fun create_asset(
        ctx: &mut MoveContext,
        name: string,
        description: string,
    ): Object {
        tradable_asset::create_tradable_asset(ctx, name, description)
    }

    // Define a function to transfer ownership of the tradable asset
    public fun transfer_asset_ownership(
        ctx: &mut MoveContext,
        asset: Object,
        new_owner: SuiAddress,
    ) {
        tradable_asset::transfer_ownership(ctx, asset, new_owner)
    }

    // Define a function to get the details of the tradable asset
    public fun get_asset_info(
        ctx: &MoveContext,
        asset: &Object,
    ): (string, string, SuiAddress) {
        tradable_asset::get_asset_details(ctx, asset)
    }
}

// Example usage
#[cfg(test)]
mod tests {
    use super::*;
    use sui::test_utils;

    #[test]
    fn test_tradable_asset() {
        let mut ctx = test_utils::new_move_context();
        let asset = create_asset(&mut ctx, "Test Asset".to_string(), "This is a test asset".to_string());
        let (name, description, owner) = get_asset_info(&ctx, &asset);
        assert_eq!(name, "Test Asset");
        assert_eq!(description, "This is a test asset");
        let new_owner = SuiAddress::random();
        transfer_asset_ownership(&mut ctx, asset, new_owner);
        let (name, description, owner) = get_asset_info(&ctx, &asset);
        assert_eq!(owner, new_owner);
    }
}
```
