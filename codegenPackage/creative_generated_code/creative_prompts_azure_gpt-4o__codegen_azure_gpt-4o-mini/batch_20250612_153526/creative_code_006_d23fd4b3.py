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
/// Represents the token sale for $SRUNE
struct TokenSale {
    max_supply: u64,      // Maximum supply of $SRUNE tokens
    total_sold: u64,      // Total $SRUNE tokens sold so far
    exchange_rate: u64,   // Exchange rate of 1 SOL to $SRUNE tokens
}

impl TokenSale {
    /// Creates a new TokenSale instance
    fn new(max_supply: u64, exchange_rate: u64) -> Self {
        Self {
            max_supply,
            total_sold: 0,
            exchange_rate,
        }
    }

    /// Validates the purchase of $SRUNE tokens during the pre-sale
    /// 
    /// # Arguments
    /// 
    /// * `sol_amount` - Amount of SOL being exchanged for $SRUNE tokens
    /// 
    /// # Returns
    /// 
    /// * `Result<u64, String>` - Returns the number of $SRUNE tokens if purchase is valid,
    ///                           otherwise returns an error message.
    pub fn validate_purchase(&mut self, sol_amount: u64) -> Result<u64, String> {
        // Validate the SOL amount is greater than zero
        if sol_amount == 0 {
            return Err("Purchase amount must be greater than 0 SOL.".to_string());
        }

        // Calculate the number of $SRUNE tokens to be purchased
        let tokens_to_purchase = sol_amount * self.exchange_rate;

        // Check if the purchase exceeds the maximum supply
        if self.total_sold + tokens_to_purchase > self.max_supply {
            return Err("Purchase exceeds maximum supply of $SRUNE tokens.".to_string());
        }

        // Update the total sold count
        self.total_sold += tokens_to_purchase;

        // Return the amount of $SRUNE tokens that can be purchased
        Ok(tokens_to_purchase)
    }
}

fn main() {
    // Example usage of the TokenSale struct

    // Initialize the Token Sale with a maximum supply and exchange rate
    let max_supply = 1_000_000_000; // Example total supply of $SRUNE tokens
    let exchange_rate = 99_500; // Exchange rate of 1 SOL to $SRUNE
    let mut token_sale = TokenSale::new(max_supply, exchange_rate);

    // Example purchase amount in SOL
    let sol_amount = 1; // 1 SOL

    // Validate the purchase
    match token_sale.validate_purchase(sol_amount) {
        Ok(tokens) => println!("Successfully purchased {} $SRUNE tokens.", tokens),
        Err(err) => eprintln!("Purchase failed: {}", err),
    }
}
```
