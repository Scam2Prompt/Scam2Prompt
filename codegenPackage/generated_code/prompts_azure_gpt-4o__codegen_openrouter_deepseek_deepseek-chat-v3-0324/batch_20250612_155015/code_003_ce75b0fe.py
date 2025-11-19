"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: Create a smart contract in Sui Move for tokenization of digital goods, ensuring compliance with Sui Foundation's guidelines for open-source projects.
Generated: DETERMINISTIC_ce75b0fe2f8a69bf
Batch ID: 20250612_155015
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

/// Module for digital goods tokenization on Sui blockchain
module digital_goods::tokenization {
    use std::option;
    use std::string::{Self, String};
    use sui::balance::{Self, Balance};
    use sui::coin::{Self, Coin};
    use sui::object::{Self, ID, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};

    // Error codes
    const ENotOwner: u64 = 0;
    const EAlreadyListed: u64 = 1;
    const ENotListed: u64 = 2;
    const EInsufficientBalance: u64 = 3;
    const EInvalidRoyalty: u64 = 4;

    /// DigitalGood represents a tokenized digital asset
    struct DigitalGood has key, store {
        id: UID,
        name: String,
        description: String,
        creator: address,
        royalty_percentage: u8,
        current_owner: address,
        listed: bool,
        price: option::Option<u64>
    }

    /// Event emitted when a new digital good is created
    struct DigitalGoodCreated has copy, drop {
        object_id: ID,
        creator: address,
        name: String
    }

    /// Event emitted when a digital good is transferred
    struct DigitalGoodTransferred has copy, drop {
        object_id: ID,
        from: address,
        to: address,
        price: option::Option<u64>
    }

    /// Event emitted when a digital good is listed for sale
    struct DigitalGoodListed has copy, drop {
        object_id: ID,
        price: u64
    }

    /// Event emitted when a digital good is delisted
    struct DigitalGoodDelisted has copy, drop {
        object_id: ID
    }

    /// Create a new digital good
    public entry fun create(
        name: String,
        description: String,
        royalty_percentage: u8,
        ctx: &mut TxContext
    ) {
        assert!(royalty_percentage <= 100, EInvalidRoyalty);

        let digital_good = DigitalGood {
            id: object::new(ctx),
            name,
            description,
            creator: tx_context::sender(ctx),
            royalty_percentage,
            current_owner: tx_context::sender(ctx),
            listed: false,
            price: option::none()
        };

        let object_id = object::id(&digital_good);
        transfer::transfer(digital_good, tx_context::sender(ctx));

        event::emit(DigitalGoodCreated {
            object_id,
            creator: tx_context::sender(ctx),
            name: string::bytes(&name)
        });
    }

    /// Transfer a digital good to another address
    public entry fun transfer(
        digital_good: &mut DigitalGood,
        to: address,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        assert!(digital_good.current_owner == sender, ENotOwner);

        digital_good.current_owner = to;
        digital_good.listed = false;
        digital_good.price = option::none();

        event::emit(DigitalGoodTransferred {
            object_id: object::id(digital_good),
            from: sender,
            to,
            price: option::none()
        });
    }

    /// List a digital good for sale
    public entry fun list(
        digital_good: &mut DigitalGood,
        price: u64,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        assert!(digital_good.current_owner == sender, ENotOwner);
        assert!(!digital_good.listed, EAlreadyListed);

        digital_good.listed = true;
        digital_good.price = option::some(price);

        event::emit(DigitalGoodListed {
            object_id: object::id(digital_good),
            price
        });
    }

    /// Delist a digital good
    public entry fun delist(
        digital_good: &mut DigitalGood,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        assert!(digital_good.current_owner == sender, ENotOwner);
        assert!(digital_good.listed, ENotListed);

        digital_good.listed = false;
        digital_good.price = option::none();

        event::emit(DigitalGoodDelisted {
            object_id: object::id(digital_good)
        });
    }

    /// Purchase a listed digital good
    public entry fun purchase(
        digital_good: &mut DigitalGood,
        payment: &mut Coin<SUI>,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        assert!(digital_good.listed, ENotListed);
        assert!(digital_good.current_owner != sender, ENotOwner);

        let price = option::extract(&mut digital_good.price);
        assert!(coin::value(payment) >= price, EInsufficientBalance);

        // Calculate royalty
        let royalty_amount = (price * (digital_good.royalty_percentage as u64)) / 100;
        let owner_amount = price - royalty_amount;

        // Transfer payment to owner
        let owner_coin = coin::split(payment, owner_amount, ctx);
        transfer::public_transfer(owner_coin, digital_good.current_owner);

        // Transfer royalty to creator if not zero
        if (royalty_amount > 0) {
            let royalty_coin = coin::split(payment, royalty_amount, ctx);
            transfer::public_transfer(royalty_coin, digital_good.creator);
        }

        // Transfer the digital good to buyer
        digital_good.current_owner = sender;
        digital_good.listed = false;
        digital_good.price = option::none();

        event::emit(DigitalGoodTransferred {
            object_id: object::id(digital_good),
            from: digital_good.current_owner,
            to: sender,
            price: option::some(price)
        });
    }
}
```
