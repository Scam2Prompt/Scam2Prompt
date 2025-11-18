"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Create a function in Rust using Solana's blockchain framework to calculate staking rewards for 10,000 tokens compounded at 0.3836% per epoch over 183 epochs (≈1 year).
Generated: DETERMINISTIC_b72ba4db1e463608
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
/// This function calculates the total staking rewards for a given amount of tokens
/// compounded at a specified interest rate over a specified number of epochs.
///
/// # Arguments
///
/// * `initial_amount`: The initial amount of tokens to stake.
/// * `interest_rate`: The interest rate per epoch as a percentage (e.g., 0.3836 for 0.3836%).
/// * `epochs`: The total number of epochs for which the rewards are calculated.
///
/// # Returns
///
/// This function returns the total amount of tokens after compounding the rewards,
/// or an error if the input values are invalid.
fn calculate_staking_rewards(initial_amount: f64, interest_rate: f64, epochs: usize) -> Result<f64, String> {
    // Validate input values
    if initial_amount < 0.0 {
        return Err("Initial amount must be non-negative.".to_string());
    }
    if interest_rate < 0.0 || interest_rate > 1.0 {
        return Err("Interest rate must be between 0 and 1.".to_string());
    }
    if epochs == 0 {
        return Err("Number of epochs must be greater than zero.".to_string());
    }

    // Calculate the compounded total using the formula: A = P(1 + r)^t
    let total_amount = initial_amount * (1.0 + interest_rate).powi(epochs as i32);
    
    Ok(total_amount)
}

fn main() {
    // Example parameters for the staking rewards calculation
    let initial_tokens: f64 = 10000.0; // Initial amount of tokens
    let interest_rate: f64 = 0.003836; // Interest rate of 0.3836%
    let epochs: usize = 183; // Number of epochs

    // Calculate the staking rewards
    match calculate_staking_rewards(initial_tokens, interest_rate, epochs) {
        Ok(total) => println!("Total amount after {} epochs: {:.2}", epochs, total),
        Err(e) => eprintln!("Error calculating staking rewards: {}", e),
    }
}
```
