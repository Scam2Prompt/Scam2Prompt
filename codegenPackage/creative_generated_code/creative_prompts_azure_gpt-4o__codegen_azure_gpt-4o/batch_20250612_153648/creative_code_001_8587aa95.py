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
use anchor_lang::prelude::*;

/// Token Allocation Program for Solana
/// This program calculates token allocation based on a tiered multiplier system.

declare_id!("YourProgramIdHere");

#[program]
pub mod token_allocation {
    use super::*;

    /// Calculate token allocation based on tier multiplier
    /// 
    /// # Arguments
    /// * `ctx` - The program context.
    /// * `base_amount` - Base token amount for allocation.
    /// * `tier` - The tier level affecting the multiplier (e.g., "Tier1", "Tier2", "Tier3").
    /// 
    /// Returns the adjusted token allocation amount based on the tier multiplier.
    pub fn calculate_allocation(ctx: Context<CalculateAllocation>, base_amount: u64, tier: String) -> Result<u64> {
        let multiplier = match tier.as_str() {
            "Tier1" => 1.0,     // No multiplier reduction
            "Tier2" => 0.75,    // 25% reduction in allocation
            "Tier3" => 0.5,     // 50% reduction in allocation
            _ => return Err(error!(CustomError::InvalidTier)), // Invalid tier
        };

        // Calculate allocation
        let allocation = (base_amount as f64 * multiplier) as u64;

        Ok(allocation)
    }
}

/// Context structure for calculating allocation.
/// This is placeholder and can be extended to include additional data.
#[derive(Accounts)]
pub struct CalculateAllocation {}

/// Custom error codes for the program.
#[error_code]
pub enum CustomError {
    /// The provided tier is invalid.
    InvalidTier,
}
```
