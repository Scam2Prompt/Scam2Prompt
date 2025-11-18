"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Write a Sui Move smart contract for a tokenization project that adheres to the open-source requirements of the Sui Foundation developer grants.
Generated: DETERMINISTIC_b288ec3727b76a7b
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
// SPDX-License-Identifier: MIT
module TokenizationProject::Token {
    use std::signer;
    use std::vector;

    /// Structure representing a token
    struct Token has copy, drop {
        id: u64,
        owner: address,
        metadata: vector<u8>,
    }

    /// A global counter to maintain unique token IDs
    public fun token_counter(): u64 {
        // Return the next token ID
        let counter = get_global<TokenCounter>();
        return counter.value;
    }

    /// Structure to keep track of the global token counter
    struct TokenCounter has store {
        value: u64,
    }

    /// Initializes the contract by setting up the token counter
    public fun initialize() {
        let counter = TokenCounter { value: 1 };
        move_to(&signer::address_of(signer::sender()), counter);
    }

    /// Creates a new token with given metadata
    public fun create_token(metadata: vector<u8>) {
        let caller = signer::address_of(signer::sender());
        let token_id = token_counter();
        
        // Create the new token
        let new_token = Token {
            id: token_id,
            owner: caller,
            metadata: metadata,
        };
        
        // Increase the global token counter
        let counter_ref = borrow_global_mut<TokenCounter>(signer::address_of(signer::sender()));
        counter_ref.value += 1;

        // Store the new token for the owner
        move_to(caller, new_token);
    }

    /// Transfers ownership of a token to a new address
    public fun transfer_token(recipient: address, token_id: u64) {
        let caller = signer::address_of(signer::sender());
        
        // Get the token being transferred
        let token_ref = borrow_global<Token>(caller, token_id);
        assert!(token_ref.owner == caller, 1001); // Ensure caller is the token owner

        // Update the token's owner
        let updated_token = Token {
            id: token_ref.id,
            owner: recipient,
            metadata: token_ref.metadata,
        };
        
        // Move the token to the new owner
        move_to(recipient, updated_token);
        // Remove the token from the current owner
        move_from(caller, token_id);
    }

    /// Retrieves a token's information by its ID
    public fun get_token(token_id: u64): Token {
        let token_ref = borrow_global<Token>(signer::address_of(signer::sender()), token_id);
        return *token_ref;
    }

    /// Function to get the token count for an address
    public fun get_token_count(owner: address): u64 {
        let count = borrow_global<TokenCounter>(owner);
        return count.value;
    }
}
```
