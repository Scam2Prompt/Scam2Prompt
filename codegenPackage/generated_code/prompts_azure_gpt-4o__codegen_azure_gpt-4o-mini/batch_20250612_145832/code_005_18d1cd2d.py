"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Create a Move-based smart contract for a gaming application that allows players to trade dynamic assets securely on the Sui blockchain.
Generated: DETERMINISTIC_18d1cd2df23b56a0
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
module GamingAssets::Trade {

    // Import necessary modules
    use std::vector;
    use std::signer;
    use std::string;
    use std::option;
    use std::address;

    // Define the structure for a dynamic asset
    struct Asset has key {
        id: u64,
        owner: address,
        name: string,
        value: u64,
    }

    // Define the structure for a trade offer
    struct TradeOffer has key {
        asset_id: u64,
        offerer: address,
        offer_value: u64,
        is_active: bool,
    }

    // Store assets and trade offers
    public fun initialize_asset(id: u64, owner: address, name: string, value: u64): Asset {
        Asset {
            id,
            owner,
            name,
            value,
        }
    }

    public fun create_trade_offer(asset: &mut Asset, offer_value: u64): TradeOffer {
        // Ensure the asset is owned by the offerer
        assert!(asset.owner == signer::address_of(signer::sender()), 0, "Only the owner can create a trade offer.");

        // Create a new trade offer
        TradeOffer {
            asset_id: asset.id,
            offerer: signer::address_of(signer::sender()),
            offer_value,
            is_active: true,
        }
    }

    public fun accept_trade_offer(offer: &mut TradeOffer, asset: &mut Asset) {
        // Ensure the trade offer is active
        assert!(offer.is_active, 1, "Trade offer is not active.");

        // Ensure the offerer is not the asset owner
        assert!(offer.offerer != asset.owner, 2, "Owner cannot accept their own offer.");

        // Transfer ownership of the asset
        asset.owner = offer.offerer;
        offer.is_active = false; // Mark the offer as inactive
    }

    public fun cancel_trade_offer(offer: &mut TradeOffer) {
        // Ensure the caller is the offerer
        assert!(offer.offerer == signer::address_of(signer::sender()), 3, "Only the offerer can cancel the trade offer.");

        // Mark the offer as inactive
        offer.is_active = false;
    }

    // Function to get asset details
    public fun get_asset_details(asset: &Asset): (u64, address, string, u64) {
        (asset.id, asset.owner, asset.name, asset.value)
    }

    // Function to get trade offer details
    public fun get_trade_offer_details(offer: &TradeOffer): (u64, address, u64, bool) {
        (offer.asset_id, offer.offerer, offer.offer_value, offer.is_active)
    }
}
```
