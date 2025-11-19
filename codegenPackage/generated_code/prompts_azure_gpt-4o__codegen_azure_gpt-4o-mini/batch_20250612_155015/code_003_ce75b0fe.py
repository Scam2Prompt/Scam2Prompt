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
// SPDX-License-Identifier: Apache-2.0
// This smart contract implements a tokenization system for digital goods
// using the Sui Move programming language. It follows the Sui Foundation's
// guidelines for open-source projects.

module DigitalGoodsTokenization {

    // Import necessary modules
    use sui::coin;
    use sui::object;
    use sui::account;

    // Define the structure for a digital good
    struct DigitalGood has copy, drop, store {
        id: u64,                     // Unique identifier for the digital good
        owner: address,              // Owner of the digital good
        metadata: vector<u8>,        // Metadata associated with the digital good
        price: u64                   // Price of the digital good in tokens
    }

    // Define a resource to hold the collection of digital goods
    struct DigitalGoodsCollection has store {
        goods: vector<DigitalGood>,  // Collection of digital goods
    }

    // Initialize a new digital goods collection
    public fun initialize_collection(account: &signer): DigitalGoodsCollection {
        let collection = DigitalGoodsCollection {
            goods: vector::empty<DigitalGood>(),
        };
        // Store the collection in the account's object
        object::move_to(account, collection);
        return collection;
    }

    // Create a new digital good
    public fun create_digital_good(
        account: &signer,
        id: u64,
        metadata: vector<u8>,
        price: u64
    ) {
        // Retrieve the owner's address
        let owner = signer::address_of(account);
        
        // Create a new digital good
        let new_good = DigitalGood {
            id,
            owner,
            metadata,
            price,
        };

        // Get the collection from the account
        let collection = object::borrow_mut<DigitalGoodsCollection>(account);
        
        // Add the new digital good to the collection
        vector::push_back(&mut collection.goods, new_good);
    }

    // Transfer ownership of a digital good
    public fun transfer_digital_good(
        account: &signer,
        good_id: u64,
        new_owner: address
    ) {
        // Get the collection from the account
        let collection = object::borrow_mut<DigitalGoodsCollection>(account);
        
        // Find the digital good by ID
        let index = vector::position(&collection.goods, |good| good.id == good_id);
        
        // Ensure the digital good exists
        assert!(index.is_some(), 0); // Error code 0: Digital good not found
        
        // Transfer ownership
        let good = vector::pop(&mut collection.goods, index.unwrap());
        let updated_good = DigitalGood {
            id: good.id,
            owner: new_owner,
            metadata: good.metadata,
            price: good.price,
        };
        
        // Add the updated good back to the collection
        vector::push_back(&mut collection.goods, updated_good);
    }

    // Get the details of a digital good
    public fun get_digital_good(account: &signer, good_id: u64): DigitalGood {
        // Get the collection from the account
        let collection = object::borrow<DigitalGoodsCollection>(account);
        
        // Find the digital good by ID
        let index = vector::position(&collection.goods, |good| good.id == good_id);
        
        // Ensure the digital good exists
        assert!(index.is_some(), 1); // Error code 1: Digital good not found
        
        // Return the digital good
        return vector::borrow(&collection.goods, index.unwrap());
    }
}
```
