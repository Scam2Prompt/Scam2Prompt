"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Write a Move smart contract to implement royalties management for digital assets in a blockchain-based gaming platform.
Generated: DETERMINISTIC_91d24528027ecc9c
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module RoyaltiesManagement {
    // Import necessary modules
    use std::signer;
    use std::vector;
    use std::option;
    use std::address;
    use std::u64;

    // Struct to represent a digital asset with its royalty data
    struct Asset has key {
        id: u64,
        owner: address,
        royalty_percentage: u64,
        beneficiaries: vector<address>,
    }

    // Resource to manage the royalties of an asset
    resource struct RoyaltiesManager {
        asset_id: u64,
        total_royalties: u64,
    }

    // Function to create a new asset
    public fun create_asset(
        id: u64,
        owner: address,
        royalty_percentage: u64,
        beneficiaries: vector<address>
    ) {
        // Validate input parameters
        assert!(royalty_percentage <= 100, 1); // Royalty percentage must be between 0 and 100
        let asset = Asset {
            id,
            owner,
            royalty_percentage,
            beneficiaries,
        };
        // Store the asset in the global state (assuming a method to persist the asset)
        save_asset(asset);
    }

    // Function to distribute royalties based on the asset's royalties
    public fun distribute_royalties(asset_id: u64, total_sale_amount: u64) {
        // Retrieve the asset from the global state (assuming a method to retrieve the asset)
        let asset_opt = get_asset(asset_id);
        assert!(option::is_some(&asset_opt), 2); // Asset must exist

        let asset = option::extract(asset_opt);
        let royalty_amount = (total_sale_amount * asset.royalty_percentage) / 100;
        let share_per_beneficiary = royalty_amount / vector::length(&asset.beneficiaries);

        // Distribute royalties to each beneficiary
        for beneficiary in &asset.beneficiaries {
            // Assuming a method to transfer currency to the beneficiary
            transfer_currency(*beneficiary, share_per_beneficiary);
        }
    }

    // Function to update the royalty percentage of an asset
    public fun update_royalty_percentage(asset_id: u64, new_percentage: u64, signer: signer) {
        // Validate input parameters
        assert!(new_percentage <= 100, 3); // Royalty percentage must be between 0 and 100
        
        let mut asset_opt = get_asset(asset_id);
        assert!(option::is_some(&asset_opt), 4); // Asset must exist

        let mut asset = option::extract(asset_opt);
        assert!(asset.owner == signer.sender(), 5); // Only the owner can update royalties

        // Update the royalty percentage
        asset.royalty_percentage = new_percentage;
        // Save the updated asset back to the global state
        save_asset(asset);
    }

    // Mock function to save an asset (implementation depends on the actual storage mechanism)
    public fun save_asset(asset: Asset) {
        // Implement the logic to persist the asset
    }

    // Mock function to get an asset (implementation depends on the actual storage mechanism)
    public fun get_asset(asset_id: u64): option::Option<Asset> {
        // Implement the logic to retrieve the asset
    }

    // Mock function to transfer currency to a beneficiary (implementation depends on the actual currency mechanism)
    public fun transfer_currency(beneficiary: address, amount: u64) {
        // Implement the logic to transfer funds
    }
}
```
