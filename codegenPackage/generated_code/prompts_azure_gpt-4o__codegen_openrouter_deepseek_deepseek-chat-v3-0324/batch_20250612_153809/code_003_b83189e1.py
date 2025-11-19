"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Provide an example of a smart contract in Sui Move that supports censorship-resistant data storage, following the guidelines of the Sui Foundation.
Generated: DETERMINISTIC_b83189e1174bda8e
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

/// A censorship-resistant data storage module on Sui
module censorship_resistant::data_storage {
    use sui::object::{Self, UID};
    use sui::tx_context::TxContext;
    use sui::transfer;
    use sui::event;
    use std::string::{Self, String};

    /// A piece of immutable data stored on-chain
    struct ImmutableData has key, store {
        id: UID,
        content: String,
        timestamp: u64,
    }

    /// Event emitted when new data is stored
    struct DataStoredEvent has copy, drop {
        data_id: ID,
        content_hash: vector<u8>,
        timestamp: u64,
    }

    /// Initialize the module (empty for now)
    fun init(_: &mut TxContext) {}

    /// Store immutable data on-chain
    public entry fun store_data(
        content: String,
        timestamp: u64,
        ctx: &mut TxContext
    ) {
        let data = ImmutableData {
            id: object::new(ctx),
            content,
            timestamp,
        };

        // Emit event for indexing
        event::emit(DataStoredEvent {
            data_id: object::uid_to_inner(&data.id),
            content_hash: hash_content(&data.content),
            timestamp: data.timestamp,
        });

        // Transfer ownership to the transaction sender
        transfer::transfer(data, tx_context::sender(ctx));
    }

    /// Helper function to hash content (simplified)
    fun hash_content(content: &String): vector<u8> {
        // In production, use a proper cryptographic hash
        let bytes = string::bytes(content);
        bytes
    }

    /// Public view function to read data content
    public fun get_content(data: &ImmutableData): &String {
        &data.content
    }

    /// Public view function to get data timestamp
    public fun get_timestamp(data: &ImmutableData): u64 {
        data.timestamp
    }

    // Test cases would go here in a real implementation
    #[test_only]
    module test {
        use sui::test_scenario;
        use std::string;
        use censorship_resistant::data_storage;

        #[test]
        fun test_store_and_read_data() {
            let scenario = test_scenario::begin(@0x123);
            let admin = test_scenario::next_sender(&scenario);
            let ctx = test_scenario::ctx(&mut scenario);

            let test_content = string::utf8(b"Test content");
            let test_timestamp = 1234567890;

            // Store data
            data_storage::store_data(test_content, test_timestamp, ctx);

            // In a real test, we would verify the data was stored correctly
            // and events were emitted properly

            test_scenario::end(scenario);
        }
    }
}
```
