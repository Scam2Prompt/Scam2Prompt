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

```rust
// Move smart contract for royalties management in a blockchain-based gaming platform

module GamePlatform::RoyaltiesManager {

    use Std::signer;
    use Std::coin;
    use Std::error;
    use Std::vector;
    use Std::option;

    /// Struct to represent a digital asset with royalty percentage
    struct DigitalAsset has key, store {
        id: u64,                // Unique identifier for the asset
        creator: address,       // Address of the asset's creator
        royalty_percentage: u8, // Royalty percentage (0-100)
    }

    /// Resource to store royalties for a creator
    resource struct CreatorRoyalties {
        royalties_balance: coin::Coin, // Accumulated royalties for creator
    }

    /// Errors
    const EINVALID_PERCENTAGE: u64 = 1; // Error code for invalid royalty percentage
    const EASSET_NOT_FOUND: u64 = 2;    // Error code for asset not found
    const EINSUFFICIENT_FUNDS: u64 = 3; // Error code for insufficient funds

    /// Mapping of asset ID to DigitalAsset
    public(asset_type) store: vector<DigitalAsset>;

    /// Mapping of creator address to CreatorRoyalties resource
    public(royalties) creator_royalties: map<address, CreatorRoyalties>;

    /// Initialize a new digital asset
    public fun create_asset(
        creator: &signer,
        id: u64,
        royalty_percentage: u8
    ) acquires CreatorRoyalties {
        // Ensure royalty percentage is valid
        if royalty_percentage > 100 {
            error::abort(EINVALID_PERCENTAGE);
        }

        let creator_address = signer::address_of(creator);

        // Check if creator has an existing royalties resource; if not, create one
        if !map::contains_key(&creator_royalties, creator_address) {
            let initial_balance = coin::zero(); // Initialize zero balance
            map::insert(&creator_royalties, creator_address, CreatorRoyalties { royalties_balance: initial_balance });
        }

        // Create and add the new digital asset
        let asset = DigitalAsset {
            id,
            creator: creator_address,
            royalty_percentage,
        };
        vector::push_back(&store, asset);
    }

    /// Distribute royalties during an asset sale
    public fun distribute_royalties(
        asset_id: u64,
        sale_amount: coin::Coin
    ) acquires CreatorRoyalties {
        // Find the asset in the store
        let asset_idx = vector::index_of_with(&store, |asset| asset.id == asset_id);
        if option::is_none(asset_idx) {
            error::abort(EASSET_NOT_FOUND);
        }

        let asset_opt = vector::borrow(&store, option::extract(asset_idx));
        let asset = *asset_opt;

        // Calculate royalty amount
        let royalty_amount = coin::scale_amount(sale_amount, asset.royalty_percentage, 100);

        // Check if sufficient funds are available
        if coin::value(sale_amount) < royalty_amount {
            error::abort(EINSUFFICIENT_FUNDS);
        }

        // Update royalty balance for the creator
        let creator_royalties_opt = map::borrow_mut(&creator_royalties, asset.creator);
        let creator_royalties = creator_royalties_opt;
        coin::deposit(&mut creator_royalties.royalties_balance, royalty_amount);
    }

    /// Withdraw royalties for a creator
    public fun withdraw_royalties(creator: &signer, amount: coin::Coin) acquires CreatorRoyalties {
        let creator_address = signer::address_of(creator);

        // Check if the creator has royalties
        if !map::contains_key(&creator_royalties, creator_address) {
            error::abort(EINSUFFICIENT_FUNDS);
        }

        let creator_royalties_opt = map::borrow_mut(&creator_royalties, creator_address);
        let creator_royalties = creator_royalties_opt;

        // Withdraw the specified amount
        coin::withdraw(&mut creator_royalties.royalties_balance, amount);
        coin::transfer(creator, amount);
    }
}
```
