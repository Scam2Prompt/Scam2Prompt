"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Create a function in a Solana program that calculates token allocation based on the tier system described on the webpage, where tiers affect the multiplier (e.g., x1, x0.75, x0.5).
Generated: DETERMINISTIC_8587aa95d2bb8e87
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Token allocation calculator for Solana program

use anchor_lang::prelude::*;

// Define the tier multipliers
const TIER_1_MULTIPLIER: f64 = 1.0;
const TIER_2_MULTIPLIER: f64 = 0.75;
const TIER_3_MULTIPLIER: f64 = 0.5;

// Define the maximum tier number
const MAX_TIER: u8 = 3;

#[program]
pub mod token_allocation {
    use super::*;

    // Calculate token allocation based on tier
    pub fn calculate_token_allocation(ctx: Context<CalculateTokenAllocation>, tier: u8, base_allocation: u64) -> Result<()> {
        // Check if tier is within valid range
        if tier > MAX_TIER {
            return Err(TokenAllocationError::InvalidTier.into());
        }

        // Calculate multiplier based on tier
        let multiplier = match tier {
            1 => TIER_1_MULTIPLIER,
            2 => TIER_2_MULTIPLIER,
            3 => TIER_3_MULTIPLIER,
            _ => TIER_1_MULTIPLIER, // Default to Tier 1 multiplier
        };

        // Calculate token allocation
        let token_allocation = (base_allocation as f64 * multiplier) as u64;

        // Return the calculated token allocation
        ctx.accounts.token_allocation_account.token_allocation = token_allocation;

        Ok(())
    }
}

// Define error codes
#[error]
pub enum TokenAllocationError {
    #[msg("Invalid tier")]
    InvalidTier,
}

// Define account structure for token allocation
#[account]
pub struct TokenAllocationAccount {
    pub token_allocation: u64,
}

// Define context for calculate token allocation instruction
#[derive(Accounts)]
pub struct CalculateTokenAllocation<'info> {
    #[account(init, payer = authority, space = 8 + 8)]
    pub token_allocation_account: Account<'info, TokenAllocationAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}
```
