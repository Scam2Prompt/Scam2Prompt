"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Generate code using Sui Move to tokenize digital goods for a commerce application, as outlined in the Sui Foundation's grant program themes.
Generated: DETERMINISTIC_39933d778dcba382
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// Copyright (c) Mysten Labs, Inc.
// SPDX-License-Identifier: Apache-2.0

module commerce::digital_goods {
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{TxContext};
    use sui::url::{Self, Url};
    use std::string::{String};

    /// A digital good that can be bought and sold in the commerce application.
    /// Contains metadata about the good and a URL to access/download it.
    struct DigitalGood has key, store {
        id: UID,
        name: String,
        description: String,
        price: u64,
        access_url: Url,
        creator: address,
        is_locked: bool
    }

    /// A receipt proving ownership of a digital good.
    struct DigitalGoodReceipt has key, store {
        id: UID,
        good_id: ID,
        owner: address,
        purchase_date: u64
    }

    /// Error codes
    const EGOOD_NOT_FOUND: u64 = 0;
    const EGOOD_LOCKED: u64 = 1;
    const EINSUFFICIENT_FUNDS: u64 = 2;
    const ENOT_OWNER: u64 = 3;
    const EALREADY_OWNED: u64 = 4;

    /// Creates a new digital good that can be sold.
    public entry fun create_digital_good(
        name: String,
        description: String,
        price: u64,
        access_url: Url,
        ctx: &mut TxContext
    ) {
        let creator = tx_context::sender(ctx);
        let good = DigitalGood {
            id: object::new(ctx),
            name,
            description,
            price,
            access_url,
            creator,
            is_locked: false
        };

        transfer::transfer(good, creator);
    }

    /// Locks a digital good to prevent further sales.
    public entry fun lock_digital_good(
        good: &mut DigitalGood,
        ctx: &TxContext
    ) {
        assert!(good.creator == tx_context::sender(ctx), ENOT_OWNER);
        good.is_locked = true;
    }

    /// Unlocks a digital good to allow sales.
    public entry fun unlock_digital_good(
        good: &mut DigitalGood,
        ctx: &TxContext
    ) {
        assert!(good.creator == tx_context::sender(ctx), ENOT_OWNER);
        good.is_locked = false;
    }

    /// Updates the price of a digital good.
    public entry fun update_price(
        good: &mut DigitalGood,
        new_price: u64,
        ctx: &TxContext
    ) {
        assert!(good.creator == tx_context::sender(ctx), ENOT_OWNER);
        good.price = new_price;
    }

    /// Purchases a digital good and creates a receipt for the buyer.
    public entry fun purchase_digital_good(
        good: &mut DigitalGood,
        payment: &mut Coin<SUI>,
        ctx: &mut TxContext
    ) {
        let buyer = tx_context::sender(ctx);
        assert!(!good.is_locked, EGOOD_LOCKED);
        assert!(coin::value(payment) >= good.price, EINSUFFICIENT_FUNDS);

        // Transfer payment to creator
        let payment_amount = good.price;
        let creator_payment = coin::split(payment, payment_amount, ctx);
        transfer::transfer(creator_payment, good.creator);

        // Create and transfer receipt to buyer
        let receipt = DigitalGoodReceipt {
            id: object::new(ctx),
            good_id: object::id(good),
            owner: buyer,
            purchase_date: tx_context::epoch(ctx)
        };
        transfer::transfer(receipt, buyer);
    }

    /// Verifies ownership of a digital good.
    public fun verify_ownership(
        receipt: &DigitalGoodReceipt,
        good: &DigitalGood,
        owner: address
    ): bool {
        receipt.owner == owner && object::id(good) == receipt.good_id
    }

    /// Transfers a digital good receipt to a new owner.
    public entry fun transfer_receipt(
        receipt: DigitalGoodReceipt,
        new_owner: address,
        _ctx: &mut TxContext
    ) {
        transfer::transfer(receipt, new_owner);
    }

    /// Updates the access URL for a digital good (creator only).
    public entry fun update_access_url(
        good: &mut DigitalGood,
        new_url: Url,
        ctx: &TxContext
    ) {
        assert!(good.creator == tx_context::sender(ctx), ENOT_OWNER);
        good.access_url = new_url;
    }
}
```
