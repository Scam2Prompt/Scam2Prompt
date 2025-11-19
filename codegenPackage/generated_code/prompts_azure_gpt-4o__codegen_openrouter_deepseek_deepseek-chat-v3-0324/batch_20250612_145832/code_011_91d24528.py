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
// Move module for managing royalties on digital assets in a blockchain game
module game_platform::royalties {
    use std::error;
    use std::signer;
    use std::vector;
    use std::option::{Self, Option};
    use aptos_framework::object;

    // Errors
    const E_NOT_OWNER: u64 = 1;
    const E_INVALID_SHARES: u64 = 2;
    const E_INVALID_TOTAL: u64 = 3;
    const E_RECIPIENT_EXISTS: u64 = 4;
    const E_RECIPIENT_NOT_FOUND: u64 = 5;
    const E_INVALID_PAYMENT: u64 = 6;
    const E_INSUFFICIENT_BALANCE: u64 = 7;

    // Struct representing a royalty recipient and their share
    struct RoyaltyRecipient has store, copy, drop {
        address: address,
        share: u64
    }

    // Struct holding royalty information for an asset
    struct RoyaltyInfo has key {
        recipients: vector<RoyaltyRecipient>,
        total_shares: u64
    }

    // Initialize royalty info for a new asset
    public entry fun initialize_royalties(
        creator: &signer,
        object: Object<RoyaltyInfo>,
        initial_recipients: vector<RoyaltyRecipient>,
        total_shares: u64
    ) {
        assert!(signer::address_of(creator) == object::object_address(&object), error::permission_denied(E_NOT_OWNER));
        
        let sum: u64 = 0;
        let i = 0;
        let len = vector::length(&initial_recipients);
        while (i < len) {
            let recipient = vector::borrow(&initial_recipients, i);
            sum = sum + recipient.share;
            i = i + 1;
        };

        assert!(sum == total_shares, error::invalid_argument(E_INVALID_TOTAL));
        
        let royalty_info = RoyaltyInfo {
            recipients: initial_recipients,
            total_shares
        };

        move_to(object, royalty_info);
    }

    // Add a new royalty recipient
    public entry fun add_recipient(
        owner: &signer,
        object: Object<RoyaltyInfo>,
        recipient: address,
        share: u64
    ) acquires RoyaltyInfo {
        assert!(signer::address_of(owner) == object::object_address(&object), error::permission_denied(E_NOT_OWNER));
        assert!(share > 0, error::invalid_argument(E_INVALID_SHARES));

        let royalty_info = borrow_global_mut<RoyaltyInfo>(object::object_address(&object));
        
        // Check if recipient already exists
        let i = 0;
        let len = vector::length(&royalty_info.recipients);
        while (i < len) {
            let existing = vector::borrow(&royalty_info.recipients, i);
            if (existing.address == recipient) {
                abort error::already_exists(E_RECIPIENT_EXISTS)
            };
            i = i + 1;
        };

        royalty_info.total_shares = royalty_info.total_shares + share;
        vector::push_back(&mut royalty_info.recipients, RoyaltyRecipient { address: recipient, share });
    }

    // Update a recipient's share
    public entry fun update_recipient_share(
        owner: &signer,
        object: Object<RoyaltyInfo>,
        recipient: address,
        new_share: u64
    ) acquires RoyaltyInfo {
        assert!(signer::address_of(owner) == object::object_address(&object), error::permission_denied(E_NOT_OWNER));
        assert!(new_share > 0, error::invalid_argument(E_INVALID_SHARES));

        let royalty_info = borrow_global_mut<RoyaltyInfo>(object::object_address(&object));
        let found = false;
        let i = 0;
        let len = vector::length(&royalty_info.recipients);
        
        while (i < len) {
            let existing = vector::borrow_mut(&mut royalty_info.recipients, i);
            if (existing.address == recipient) {
                royalty_info.total_shares = royalty_info.total_shares - existing.share + new_share;
                existing.share = new_share;
                found = true;
                break
            };
            i = i + 1;
        };

        assert!(found, error::not_found(E_RECIPIENT_NOT_FOUND));
    }

    // Remove a royalty recipient
    public entry fun remove_recipient(
        owner: &signer,
        object: Object<RoyaltyInfo>,
        recipient: address
    ) acquires RoyaltyInfo {
        assert!(signer::address_of(owner) == object::object_address(&object), error::permission_denied(E_NOT_OWNER));

        let royalty_info = borrow_global_mut<RoyaltyInfo>(object::object_address(&object));
        let found = false;
        let i = 0;
        let len = vector::length(&royalty_info.recipients);
        
        while (i < len) {
            let existing = vector::borrow(&royalty_info.recipients, i);
            if (existing.address == recipient) {
                royalty_info.total_shares = royalty_info.total_shares - existing.share;
                vector::remove(&mut royalty_info.recipients, i);
                found = true;
                break
            };
            i = i + 1;
        };

        assert!(found, error::not_found(E_RECIPIENT_NOT_FOUND));
    }

    // Distribute royalties to recipients
    public fun distribute_royalties(
        object: Object<RoyaltyInfo>,
        payment_amount: u64
    ): vector<(address, u64)> acquires RoyaltyInfo {
        assert!(payment_amount > 0, error::invalid_argument(E_INVALID_PAYMENT));

        let royalty_info = borrow_global<RoyaltyInfo>(object::object_address(&object));
        let distributions = vector::empty();
        let i = 0;
        let len = vector::length(&royalty_info.recipients);
        
        while (i < len) {
            let recipient = vector::borrow(&royalty_info.recipients, i);
            let amount = (payment_amount * recipient.share) / royalty_info.total_shares;
            vector::push_back(&mut distributions, (recipient.address, amount));
            i = i + 1;
        };

        distributions
    }

    // Get royalty info for an asset
    public fun get_royalty_info(
        object: Object<RoyaltyInfo>
    ): (vector<RoyaltyRecipient>, u64) acquires RoyaltyInfo {
        let royalty_info = borrow_global<RoyaltyInfo>(object::object_address(&object));
        (royalty_info.recipients, royalty_info.total_shares)
    }
}
```
