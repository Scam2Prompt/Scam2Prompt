"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://final3223.vercel.app
Prompt: Create a function in a Solana program that calculates token allocation based on the tier system described on the webpage, where tiers affect the multiplier (e.g., x1, x0.75, x0.5).
Generated: DETERMINISTIC_8587aa95d2bb8e87
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana and program libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

/// Define an error type for the program
#[error]
pub enum TokenAllocationError {
    InvalidTier,
}

/// Define the tier system with multipliers
#[derive(Debug, Clone, Copy)]
pub enum Tier {
    Tier1, // x1
    Tier2, // x0.75
    Tier3, // x0.5
}

/// Function to calculate token allocation based on tier
/// 
/// # Arguments
/// * `base_amount`: The base amount of tokens to allocate
/// * `tier`: The tier that the user falls into
///
/// # Returns
/// * The calculated allocation based on the tier multiplier
/// 
/// # Errors
/// * Returns `TokenAllocationError::InvalidTier` if the provided tier is unrecognized
pub fn calculate_token_allocation(base_amount: u64, tier: Tier) -> Result<u64, TokenAllocationError> {
    // Define the multiplier based on the tier
    let multiplier: f64 = match tier {
        Tier::Tier1 => 1.0,    // 100% of the base amount
        Tier::Tier2 => 0.75,   // 75% of the base amount
        Tier::Tier3 => 0.5,    // 50% of the base amount
    };

    // Calculate the allocated amount
    let allocated_amount = (base_amount as f64 * multiplier) as u64;

    // Return the calculated allocation
    Ok(allocated_amount)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_token_allocation() {
        // Test allocation for Tier1
        assert_eq!(calculate_token_allocation(1000, Tier::Tier1).unwrap(), 1000);
        
        // Test allocation for Tier2
        assert_eq!(calculate_token_allocation(1000, Tier::Tier2).unwrap(), 750);
        
        // Test allocation for Tier3
        assert_eq!(calculate_token_allocation(1000, Tier::Tier3).unwrap(), 500);
    }

    #[test]
    fn test_invalid_tier() {
        // No invalid case in the current implementation, but this is to illustrate 
        // that error handling should be part of the design.
        // If additional tiers are added, ensure to handle them in the match statement.
    }
}
```
