"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Create a smart contract in Sui Move for tokenization of digital goods, ensuring compliance with Sui Foundation's guidelines for open-source projects.
Generated: DETERMINISTIC_ce75b0fe2f8a69bf
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module Tokenization::DigitalGoods {

    use sui::coin;
    use sui::address;
    use sui::string;
    use sui::event;

    /// Struct to represent a tokenized digital good
    public struct DigitalGood has key, store {
        id: UID,                       // Unique identifier for the digital good
        name: string::String,          // Name of the digital good
        owner: address::Address,       // Address of the owner
        metadata: string::String,      // Metadata describing the digital good
    }

    /// Event to emit when a new digital good is created
    public struct DigitalGoodCreated has drop, store {
        id: address::Address,
        name: string::String,
        metadata: string::String,
    }

    /// Initialize a new tokenized digital good
    public entry fun create_digital_good(
        name: string::String,
        metadata: string::String,
        ctx: &mut sui::TransactionContext
    ): DigitalGood {
        // Validate input
        assert!(
            string::length(&name) > 0,
            "Digital good name must not be empty"
        );
        assert!(
            string::length(&metadata) > 0,
            "Digital good metadata must not be empty"
        );

        // Generate a unique ID for the digital good
        let id = sui::object::new_uid(ctx);

        // Get the creator's address
        let creator_address = sui::sender(ctx);

        // Create the DigitalGood instance
        let digital_good = DigitalGood {
            id,
            name: name.clone(),
            owner: creator_address,
            metadata: metadata.clone(),
        };

        // Emit the DigitalGoodCreated event
        event::emit(
            ctx,
            DigitalGoodCreated {
                id: creator_address,
                name: name,
                metadata: metadata,
            }
        );

        // Return the digital good object
        digital_good
    }

    /// Transfer ownership of the digital good
    public entry fun transfer_digital_good(
        good: DigitalGood,
        new_owner: address::Address,
        ctx: &mut sui::TransactionContext
    ): DigitalGood {
        // Validate input
        assert!(
            sui::sender(ctx) == good.owner,
            "Only the owner can transfer the digital good"
        );
        
        // Update the owner field
        let updated_good = DigitalGood {
            id: good.id,
            name: good.name,
            owner: new_owner,
            metadata: good.metadata,
        };

        updated_good
    }

    /// View metadata of a digital good
    public fun view_metadata(good: &DigitalGood): string::String {
        good.metadata.clone()
    }

    /// Get the owner of a digital good
    public fun get_owner(good: &DigitalGood): address::Address {
        good.owner
    }
}
```
