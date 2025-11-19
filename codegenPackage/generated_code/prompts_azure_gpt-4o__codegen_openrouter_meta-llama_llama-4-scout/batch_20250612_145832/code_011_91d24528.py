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
// Royalties Management Contract

module Royalties {
    use std::vector;
    use std::string;
    use std::option;

    // Struct to represent a digital asset
    struct DigitalAsset {
        id: u64,
        creator: address,
        royalty_percentage: u8,
    }

    // Struct to represent a royalty payment
    struct RoyaltyPayment {
        asset_id: u64,
        payer: address,
        amount: u64,
    }

    // Resource to store digital assets and their royalties
    resource DigitalAssets {
        assets: vector<DigitalAsset>,
    }

    // Resource to store royalty payments
    resource RoyaltyPayments {
        payments: vector<RoyaltyPayment>,
    }

    // Public function to create a new digital asset with royalty percentage
    public fun create_asset(
        creator: &signer,
        id: u64,
        royalty_percentage: u8,
    ): DigitalAsset {
        // Check if royalty percentage is within valid range (0-100)
        assert!(royalty_percentage <= 100, "Royalty percentage must be between 0 and 100");

        DigitalAsset {
            id,
            creator: *creator,
            royalty_percentage,
        }
    }

    // Public function to add a digital asset to the DigitalAssets resource
    public fun add_asset(
        assets: &mut DigitalAssets,
        asset: DigitalAsset,
    ) {
        vector::push_back(&mut assets.assets, asset);
    }

    // Public function to make a royalty payment
    public fun make_payment(
        payments: &mut RoyaltyPayments,
        asset_id: u64,
        payer: &signer,
        amount: u64,
    ) {
        // Find the digital asset and calculate the royalty amount
        let asset = find_asset(asset_id);
        let royalty_amount = (amount * (asset.royalty_percentage as u64)) / 100;

        // Create a new RoyaltyPayment
        let payment = RoyaltyPayment {
            asset_id,
            payer: *payer,
            amount: royalty_amount,
        };

        // Add the payment to the RoyaltyPayments resource
        vector::push_back(&mut payments.payments, payment);
    }

    // Private function to find a digital asset by ID
    fun find_asset(asset_id: u64): DigitalAsset {
        // Assume DigitalAssets resource is stored in a global variable
        let assets = global<DigitalAssets>(@Royalties);
        let asset = vector::iter(&assets.assets).find(|asset| asset.id == asset_id);
        option::unwrap_or(asset, DigitalAsset { id: 0, creator: @0x0, royalty_percentage: 0 })
    }

    // Public function to get the royalty payments for a digital asset
    public fun get_payments(asset_id: u64): vector<RoyaltyPayment> {
        // Assume RoyaltyPayments resource is stored in a global variable
        let payments = global<RoyaltyPayments>(@Royalties);
        vector::filter(&payments.payments, |payment| payment.asset_id == asset_id)
    }
}

// Example usage:
script {
    use Royalties;

    fun main(account: &signer) {
        // Create a new digital asset
        let asset = Royalties::create_asset(account, 1, 10);

        // Add the asset to the DigitalAssets resource
        let mut assets = global<DigitalAssets>(@Royalties);
        Royalties::add_asset(&mut assets, asset);

        // Make a royalty payment
        let mut payments = global<RoyaltyPayments>(@Royalties);
        Royalties::make_payment(&mut payments, 1, account, 100);

        // Get the royalty payments for the digital asset
        let payments = Royalties::get_payments(1);
    }
}
```
