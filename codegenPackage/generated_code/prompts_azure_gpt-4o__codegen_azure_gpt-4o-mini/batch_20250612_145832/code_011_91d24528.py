"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Write a Move smart contract to implement royalties management for digital assets in a blockchain-based gaming platform.
Generated: DETERMINISTIC_91d24528027ecc9c
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// SPDX-License-Identifier: MIT
module GamingPlatform::RoyaltiesManager {
    use 0x1::address;
    use 0x1::vector;
    use 0x1::option;
    use 0x1::signer;

    // Struct to represent a digital asset with its royalty information
    struct Asset has key {
        id: u64,
        owner: address,
        royalty_percentage: u8, // Percentage of the sale that goes to the creator
    }

    // Resource to manage royalties for a specific asset
    struct RoyaltiesResource has key {
        asset_id: u64,
        creator: address,
        royalty_percentage: u8,
    }

    // Event emitted when a royalty is paid
    struct RoyaltyPaidEvent has key {
        asset_id: u64,
        amount: u64,
        creator: address,
    }

    // Function to create a new asset with royalty information
    public fun create_asset(
        id: u64,
        owner: address,
        royalty_percentage: u8,
        creator: address,
        signer: &signer
    ) {
        // Ensure the royalty percentage is valid
        assert!(royalty_percentage <= 100, 0);

        // Create the asset
        let asset = Asset {
            id,
            owner,
            royalty_percentage,
        };

        // Create the royalties resource
        let royalties_resource = RoyaltiesResource {
            asset_id: id,
            creator,
            royalty_percentage,
        };

        // Store the asset and royalties resource
        move_to(signer, asset);
        move_to(signer, royalties_resource);
    }

    // Function to pay royalties when an asset is sold
    public fun pay_royalties(asset_id: u64, sale_amount: u64, buyer: address, signer: &signer) {
        // Retrieve the royalties resource for the asset
        let royalties_resource = borrow_global<RoyaltiesResource>(signer.address());

        // Ensure the asset ID matches
        assert!(royalties_resource.asset_id == asset_id, 1);

        // Calculate the royalty amount
        let royalty_amount = (sale_amount * royalties_resource.royalty_percentage as u64) / 100;

        // Emit the royalty paid event
        emit_event(RoyaltyPaidEvent {
            asset_id,
            amount: royalty_amount,
            creator: royalties_resource.creator,
        });

        // Transfer the royalty amount to the creator
        // Note: This is a placeholder for actual transfer logic
        // transfer_funds(royalties_resource.creator, royalty_amount);
    }

    // Function to retrieve asset information
    public fun get_asset_info(asset_id: u64): option::Option<Asset> {
        // Attempt to borrow the asset from storage
        option::Option::some(borrow_global<Asset>(asset_id))
    }

    // Function to retrieve royalties information
    public fun get_royalties_info(asset_id: u64): option::Option<RoyaltiesResource> {
        // Attempt to borrow the royalties resource from storage
        option::Option::some(borrow_global<RoyaltiesResource>(asset_id))
    }
}
```
