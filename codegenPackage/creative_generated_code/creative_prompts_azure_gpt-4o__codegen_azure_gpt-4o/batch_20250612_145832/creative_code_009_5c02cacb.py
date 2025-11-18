"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Provide a step-by-step guide to building a blockchain-based commerce application using Sui's dynamic and composable assets.
Generated: DETERMINISTIC_5c02cacbb280c7d3
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Sui Smart Contract for a Blockchain-based Commerce Application
// This code demonstrates creating a module for a commerce application using Sui's Move language.
// It includes dynamic and composable assets for transactions and payments.

module commerce::CommerceApp {
    use sui::transfer;
    use sui::balance;
    use sui::object;
    use sui::tx_context;

    /// Struct representing a Product in the commerce application.
    struct Product has key {
        id: u64,
        name: vector<u8>, // Name of the product
        price: u64,       // Price of the product in micro-SUI
        owner: address,   // Owner of the product
    }

    /// Struct representing a Receipt that confirms a purchase.
    struct Receipt has drop {
        product_id: u64,
        buyer: address,
        timestamp: u64,
    }

    /// Initializes a new product in the commerce system.
    public fun create_product(
        context: &mut tx_context::TxContext,
        name: vector<u8>,
        price: u64
    ): Product {
        let product_id = tx_context::generate_object_id(context);
        let owner = tx_context::sender(context);

        // Initialize the product
        Product {
            id: product_id,
            name,
            price,
            owner,
        }
    }

    /// Transfers ownership of the product to the buyer and generates a receipt.
    public fun purchase_product(
        product: Product,
        buyer: address,
        payment: balance::Balance<u64>, // SUI payment
        context: &mut tx_context::TxContext
    ): (Product, Receipt) acquires Product {
        // Validate payment
        assert!(payment.value >= product.price, "Insufficient payment");

        // Transfer ownership of the product
        let updated_product = Product {
            id: product.id,
            name: product.name,
            price: product.price,
            owner: buyer,
        };

        // Generate a receipt
        let receipt = Receipt {
            product_id: product.id,
            buyer,
            timestamp: tx_context::current_time(context),
        };

        // Transfer payment to the original owner
        balance::transfer(payment, product.owner);

        (updated_product, receipt)
    }

    /// Deletes a product from the system (only by the owner).
    public fun delete_product(
        product: Product,
        context: &mut tx_context::TxContext
    ) acquires Product {
        let sender = tx_context::sender(context);

        // Ensure only the owner can delete the product
        assert!(sender == product.owner, "Unauthorized deletion");

        // Delete the product
        object::delete(product);
    }
}
```
