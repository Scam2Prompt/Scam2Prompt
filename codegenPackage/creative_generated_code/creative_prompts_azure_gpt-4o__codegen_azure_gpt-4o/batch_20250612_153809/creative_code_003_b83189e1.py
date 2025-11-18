"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Provide an example of a smart contract in Sui Move that supports censorship-resistant data storage, following the guidelines of the Sui Foundation.
Generated: DETERMINISTIC_b83189e1174bda8e
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module data_storage::CensorshipResistantStorage {

    use sui::tx_context;

    /// Struct to hold stored data
    struct Data has key, store {
        content: vector<u8>,  // Data stored in raw bytes for flexibility
        owner: address,       // Address of the creator/owner of the data
    }

    /// Event emitted when new data is stored
    struct DataStored has drop {
        content_hash: vector<u8>,  // Hash of the stored content for integrity verification
        owner: address,            // Owner who stored the data
    }

    /// Public entry point to create and store new data
    public entry fun store_data(content: vector<u8>, ctx: &mut tx_context::TxContext) {
        // Validate input
        assert!(content.len() > 0, "Content cannot be empty");

        // Get the transaction sender address
        let sender = tx_context::sender(ctx);

        // Create the data struct
        let data = Data {
            content: content,
            owner: sender,
        };

        // Create the hash of the content for integrity
        let content_hash = hash_content(&data.content);

        // Emit the DataStored event
        tx_context::emit(ctx, DataStored {
            content_hash: content_hash,
            owner: sender,
        });

        // Save the data object into the blockchain
        tx_context::transfer_to_sender(ctx, data);
    }

    /// Helper function to hash content
    fun hash_content(content: &vector<u8>): vector<u8> {
        // Placeholder hashing mechanism (implement suitable hashing logic in production)
        content.clone()
    }

    /// Public function to access stored data (read-only)
    public fun get_data(data: &Data): (vector<u8>, address) {
        (copy data.content, copy data.owner)
    }
}
```
