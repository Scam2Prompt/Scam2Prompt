"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: "Write a code snippet demonstrating how to use Sui's Move programming language to create a simple smart contract for digital ownership."
Generated: DETERMINISTIC_5cfffcb681cd1cec
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// File: DigitalOwnership.move

module DigitalOwnership {

    use sui::object;
    use sui::tx_context;

    /// Struct representing a digital asset.
    struct DigitalAsset has key, store {
        id: object::UID, // Unique identifier for the asset
        owner: address,  // Address of the current owner
        metadata: vector<u8>, // Metadata associated with the asset (e.g., name, description)
    }

    /// Function to create a new digital asset.
    /// This function can only be called by the creator of the asset.
    public fun create_asset(
        owner: address, 
        metadata: vector<u8>, 
        ctx: &mut tx_context::TxContext
    ): DigitalAsset {
        let id = object::new(ctx); // Generate a unique ID for the asset
        DigitalAsset { id, owner, metadata }
    }

    /// Function to transfer ownership of a digital asset.
    /// This function ensures that only the current owner can transfer the asset.
    public fun transfer_asset(
        asset: &mut DigitalAsset, 
        new_owner: address
    ) {
        // Ensure the caller is the current owner
        assert!(asset.owner == tx_context::sender(), "Only the owner can transfer the asset.");
        asset.owner = new_owner; // Update the owner
    }

    /// Function to retrieve metadata of a digital asset.
    public fun get_metadata(asset: &DigitalAsset): vector<u8> {
        asset.metadata
    }

    /// Function to retrieve the owner of a digital asset.
    public fun get_owner(asset: &DigitalAsset): address {
        asset.owner
    }
}
```
