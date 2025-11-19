"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Generate an example of how to store code on-chain using sui.direct and the SUI blockchain.
Generated: DETERMINISTIC_05f327ffa890ba4c
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SUI Move module to store code on-chain using sui.direct
// This example demonstrates how to store and retrieve code on-chain in the SUI blockchain.

module sui_direct::CodeStorage {

    use sui::object::{Self, UID};
    use sui::transfer::{Self, Transfer};
    use sui::string::{Self, String};

    /// Struct to represent stored code
    /// Contains a unique ID and the code as a string
    struct StoredCode has key {
        id: UID,
        code: String,
    }

    /// Public entry function to store code on-chain
    /// Accepts the code as a string and creates a new `StoredCode` object
    public entry fun store_code(code: String): StoredCode {
        // Validate input: Ensure code is not empty
        assert!(!String::is_empty(&code), "Code cannot be empty");

        // Create a new `StoredCode` object with a unique ID
        let stored_code = StoredCode {
            id: UID::new(),
            code,
        };

        // Return the stored code object
        stored_code
    }

    /// Public entry function to retrieve stored code
    /// Accepts a `StoredCode` object and returns the code as a string
    public fun retrieve_code(stored_code: &StoredCode): String {
        // Return the code stored in the `StoredCode` object
        stored_code.code
    }

    /// Public entry function to transfer ownership of stored code
    /// Accepts a `StoredCode` object and transfers it to a new owner
    public entry fun transfer_code(stored_code: StoredCode, recipient: address) {
        // Transfer the `StoredCode` object to the recipient
        Transfer::transfer(stored_code, recipient);
    }
}
```
