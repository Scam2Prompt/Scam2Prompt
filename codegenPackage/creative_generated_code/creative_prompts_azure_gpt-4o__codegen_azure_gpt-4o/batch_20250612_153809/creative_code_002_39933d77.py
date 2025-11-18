"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Generate code using Sui Move to tokenize digital goods for a commerce application, as outlined in the Sui Foundation's grant program themes.
Generated: DETERMINISTIC_39933d778dcba382
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module commerce::DigitalGoodsToken {

    use sui::transfer;
    use sui::tx_context;

    /// Struct representing a digital goods token in the commerce application.
    struct DigitalGoodsToken has key, store {
        id: UID,                   // Unique identifier for the token
        name: String,              // Name of the digital good
        description: String,       // Description of the digital good
        owner: address,            // Owner address
        price: u64,                // Price of the digital good in smallest unit
    }

    /// Function to mint a new digital goods token
    public fun mint_token(
        name: String,
        description: String,
        price: u64,
        ctx: &mut tx_context::TxContext
    ): DigitalGoodsToken {
        // Validate price input
        if (price == 0) {
            abort 0;
        }

        // Create a new UID for the token and initialize the struct
        let id = tx_context::new_uid(ctx);
        let owner = tx_context::sender(ctx);
        return DigitalGoodsToken { id, name, description, owner, price };
    }

    /// Function to transfer ownership of a digital goods token to a new owner
    public fun transfer_token(
        token: DigitalGoodsToken,
        new_owner: address,
        ctx: &mut tx_context::TxContext
    ) {
        // Ensure the sender is the current owner of the token
        if (token.owner != tx_context::sender(ctx)) {
            abort 1;
        }

        // Update ownership of the token
        token.owner = new_owner;

        // Transfer the token to the new owner
        transfer::transfer(token, new_owner);
    }

    /// Function to update the price of a digital goods token
    public fun update_price(
        token: &mut DigitalGoodsToken,
        new_price: u64,
        ctx: &tx_context::TxContext
    ) {
        // Validate price input
        if (new_price == 0) {
            abort 2;
        }

        // Ensure the sender is the current owner of the token
        if (token.owner != tx_context::sender(ctx)) {
            abort 3;
        }

        // Update the price of the token
        token.price = new_price;
    }

    /// Function to get details of a digital goods token
    public fun get_token_details(token: &DigitalGoodsToken): (String, String, address, u64) {
        return (token.name, token.description, token.owner, token.price);
    }

    /// Entry point for module initialization
    public entry fun init_module(ctx: &mut tx_context::TxContext) {
        // Initialize any module-level state here if needed
        // Currently no initialization logic is required in this implementation
    }
}
```
