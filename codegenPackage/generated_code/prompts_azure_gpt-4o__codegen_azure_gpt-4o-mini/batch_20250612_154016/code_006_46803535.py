"""
Generated Code Metadata:
========================
Original URL: https://suifox.online
Prompt: Write a function in SUI Move to implement a giveaway mechanism for SuiFOX tokens, ensuring compliance with the tokenomics and community-driven ethos described on the website.
Generated: DETERMINISTIC_46803535336682bd
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// SUI Move code for a giveaway mechanism for SuiFOX tokens

module SuiFOX::Giveaway {

    // Import necessary modules
    use std::signer;
    use std::vector;
    use SuiFOX::Token;

    // Struct to hold giveaway details
    struct Giveaway {
        creator: address,
        token_amount: u64,
        recipients: vector<address>,
        claimed: vector<bool>,
    }

    // Public function to create a new giveaway
    public fun create_giveaway(
        creator: &signer,
        token_amount: u64,
        recipients: vector<address>
    ): Giveaway {
        // Ensure the token amount is positive
        assert!(token_amount > 0, 0);

        // Ensure there are recipients
        assert!(vector::length(&recipients) > 0, 1);

        // Create a new giveaway instance
        let giveaway = Giveaway {
            creator: signer::address_of(creator),
            token_amount,
            recipients,
            claimed: vector::empty<bool>(),
        };

        // Initialize claimed vector with false for each recipient
        let num_recipients = vector::length(&recipients);
        let claimed_vector = vector::empty<bool>();
        for (_i in 0..num_recipients) {
            vector::push_back(&mut claimed_vector, false);
        }
        giveaway.claimed = claimed_vector;

        // Return the created giveaway
        giveaway
    }

    // Public function to claim tokens from a giveaway
    public fun claim_tokens(
        giveaway: &mut Giveaway,
        recipient: &signer
    ) {
        // Get the recipient's address
        let recipient_address = signer::address_of(recipient);

        // Check if the recipient is eligible
        let index = vector::index_of(&giveaway.recipients, recipient_address);
        assert!(index.is_some(), 2); // Recipient not in the giveaway

        let idx = index.unwrap();
        assert!(!vector::borrow(&giveaway.claimed, idx), 3); // Already claimed

        // Mark the tokens as claimed
        vector::borrow_mut(&mut giveaway.claimed, idx) = true;

        // Transfer tokens to the recipient
        Token::transfer(giveaway.token_amount, giveaway.creator, recipient_address);
    }

    // Function to check if a recipient has claimed their tokens
    public fun has_claimed(giveaway: &Giveaway, recipient: address): bool {
        let index = vector::index_of(&giveaway.recipients, recipient);
        if (index.is_some()) {
            return vector::borrow(&giveaway.claimed, index.unwrap());
        }
        false
    }
}
```
