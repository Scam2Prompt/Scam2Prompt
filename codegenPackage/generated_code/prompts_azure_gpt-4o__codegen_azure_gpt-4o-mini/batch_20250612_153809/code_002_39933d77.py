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
// Sui Move module for tokenizing digital goods in a commerce application

module DigitalGoodsTokenization {

    // Struct to represent a digital good
    struct DigitalGood has store {
        id: u64,                     // Unique identifier for the digital good
        owner: address,              // Address of the current owner
        metadata: vector<u8>,        // Metadata associated with the digital good (e.g., name, description)
        price: u64                   // Price of the digital good in smallest currency unit (e.g., cents)
    }

    // Resource to hold the collection of digital goods
    struct DigitalGoodsCollection has store {
        goods: vector<DigitalGood>,   // Vector to store digital goods
    }

    // Event emitted when a digital good is created
    struct DigitalGoodCreatedEvent has store {
        good_id: u64,
        owner: address,
        price: u64,
    }

    // Event emitted when a digital good is purchased
    struct DigitalGoodPurchasedEvent has store {
        good_id: u64,
        buyer: address,
    }

    // Function to create a new digital good
    public fun create_digital_good(
        owner: &mut address,
        id: u64,
        metadata: vector<u8>,
        price: u64
    ) {
        // Ensure the price is positive
        assert!(price > 0, 0); // Error code 0: Invalid price

        // Create the new digital good
        let new_good = DigitalGood {
            id,
            owner: *owner,
            metadata,
            price,
        };

        // Add the new good to the owner's collection
        let collection = get_or_create_collection(*owner);
        collection.goods.push(new_good);

        // Emit event for the creation of the digital good
        emit DigitalGoodCreatedEvent {
            good_id: id,
            owner: *owner,
            price,
        };
    }

    // Function to purchase a digital good
    public fun purchase_digital_good(
        buyer: &mut address,
        good_id: u64
    ) {
        // Retrieve the digital goods collection of the buyer
        let collection = get_or_create_collection(*buyer);

        // Find the digital good by ID
        let index = find_good_index(&collection.goods, good_id);
        let good = &mut collection.goods[index];

        // Ensure the buyer has enough funds (this is a placeholder for actual payment logic)
        assert!(/* payment logic here */, 1); // Error code 1: Insufficient funds

        // Transfer ownership of the digital good
        good.owner = *buyer;

        // Emit event for the purchase of the digital good
        emit DigitalGoodPurchasedEvent {
            good_id,
            buyer: *buyer,
        };
    }

    // Helper function to get or create a digital goods collection for an address
    fun get_or_create_collection(owner: address): &mut DigitalGoodsCollection {
        // Check if the collection exists, if not, create it
        if (!exists<DigitalGoodsCollection>(owner)) {
            move_to(owner, DigitalGoodsCollection {
                goods: vector::empty<DigitalGood>(),
            });
        }
        return borrow_global_mut<DigitalGoodsCollection>(owner);
    }

    // Helper function to find the index of a digital good by ID
    fun find_good_index(goods: &vector<DigitalGood>, good_id: u64): u64 {
        let mut index: u64 = 0;
        let mut found: bool = false;

        // Iterate through the goods to find the index
        while (index < vector::length(goods)) {
            if (goods[index].id == good_id) {
                found = true;
                break;
            }
            index = index + 1;
        }

        // Ensure the good was found
        assert!(found, 2); // Error code 2: Good not found
        return index;
    }
}
```
