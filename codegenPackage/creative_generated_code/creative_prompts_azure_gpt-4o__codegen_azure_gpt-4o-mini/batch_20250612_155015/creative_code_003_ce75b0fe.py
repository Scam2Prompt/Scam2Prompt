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
// SPDX-License-Identifier: MIT
// This smart contract implements a tokenization system for digital goods.
// It adheres to the Sui Foundation's guidelines for open-source projects.

module DigitalGoodsToken::Tokenization {
    use std::signer;
    use std::vector;
    use std::string;

    // Define the structure of a digital good token
    struct Token has copy, drop, store {
        id: u64,
        owner: address,
        metadata: vector<u8>,
    }

    // State variable to keep track of the total number of tokens
    public fun total_tokens(): u64 {
        // Return the total number of tokens created
        self::get_total_tokens()
    }

    // Create a new token for a digital good
    public fun create_token(signer: &signer, metadata: vector<u8>): Token {
        let token_id = self::generate_token_id();
        let owner_address = signer.address();
        
        // Create a new token
        let new_token = Token {
            id: token_id,
            owner: owner_address,
            metadata: metadata,
        };

        // Store the token to ensure it persists
        Self::store_token(new_token);

        new_token // Return the created token
    }

    // Change the ownership of a token
    public fun transfer_token(signer: &signer, token_id: u64, new_owner: address) {
        let token = Self::get_token_by_id(token_id);

        // Check if the signer is the current owner
        if (token.owner != signer.address()) {
            abort(0); // Unauthorized access
        }

        // Update the owner
        token.owner = new_owner;

        // Store the updated token
        Self::store_token(token);
    }

    // Helper function to generate a unique token ID
    fun generate_token_id(): u64 {
        // Generate a unique token ID. In production, consider using a more robust ID generation.
        let current_id = self::get_total_tokens();
        self::increment_token_counter();
        current_id
    }

    // Store the token in the blockchain
    fun store_token(token: Token) {
        // Logic to store the token should be implemented here
        // This function should save the token to a suitable data structure
    }

    // Retrieve a token by its ID
    fun get_token_by_id(token_id: u64): Token {
        // Logic to retrieve the token from storage by its ID
        // This function should return the token if it exists, or abort if not found
    }

    // Increment the token counter
    fun increment_token_counter() {
        // Logic to increment the total token count
    }

    // Get the total number of tokens created
    fun get_total_tokens(): u64 {
        // Logic to retrieve the total number of tokens from storage
    }
}
```
