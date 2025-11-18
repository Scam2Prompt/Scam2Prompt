"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Create a function in Rust to validate the purchase of $SRUNE tokens during the pre-sale, ensuring the exchange rate of 1 SOL = 99,500 $SRUNE and the total supply constraints are adhered to, as described on the $SRUNE pre-sale site.
Generated: DETERMINISTIC_d23fd4b3411d843f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary modules
use std::error::Error;

// Define constants for the exchange rate and total supply
const EXCHANGE_RATE_SOL_TO_SRUNE: u64 = 99_500;
const MAX_TOTAL_SUPPLY_SRUNE: u64 = 10_000_000;

// Struct to hold purchase details
#[derive(Debug)]
struct Purchase {
    buyer: String,
    sol_amount: f64,
    srune_amount: u64,
}

// Function to validate the purchase
fn validate_purchase(
    buyer: &str, 
    sol_amount: f64, 
    current_total_supply: u64
) -> Result<Purchase, Box<dyn Error>> {
    // Ensure SOL amount is positive
    if sol_amount <= 0.0 {
        return Err("SOL amount must be greater than zero.".into());
    }

    // Calculate the amount of $SRUNE to be received
    let srune_amount = (sol_amount * EXCHANGE_RATE_SOL_TO_SRUNE as f64).round() as u64;

    // Check for total supply constraints
    if current_total_supply + srune_amount > MAX_TOTAL_SUPPLY_SRUNE {
        return Err("Purchase exceeds maximum total supply of $SRUNE.".into());
    }

    // Create and return a validated purchase record
    let purchase = Purchase {
        buyer: buyer.to_string(),
        sol_amount,
        srune_amount,
    };

    Ok(purchase)
}

// Example usage
fn main() {
    let buyer = "Alice";
    let sol_amount = 2.5; // Example SOL input
    let current_total_supply = 5_000_000; // Example current total supply

    match validate_purchase(buyer, sol_amount, current_total_supply) {
        Ok(purchase) => {
            println!("Purchase validated: {:?}", purchase);
        }
        Err(e) => {
            eprintln!("Error validating purchase: {}", e);
        }
    }
}
```
