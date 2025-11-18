"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-solana.com
Prompt: Develop a smart contract that enforces the 3-minute expiration rule for claiming a Solana giveaway, as described on the webpage.
Generated: DETERMINISTIC_d9c81cbc6c1c7052
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Solana smart contract enforcing a 3-minute expiration rule for claiming a giveaway.

use anchor_lang::prelude::*;
use anchor_lang::solana_program::clock::Clock;

declare_id!("Fg6PaFpoGXkYsidMpWFKT3XdZ3KqZzYtRzt1a1B9NXs");

#[program]
pub mod solana_giveaway {
    use super::*;

    // Entry point for claiming a giveaway
    pub fn claim_giveaway(ctx: Context<ClaimGiveaway>, giveaway_id: String) -> Result<()> {
        let giveaway_account = &mut ctx.accounts.giveaway_account;

        // Ensure the giveaway has not expired
        let current_timestamp = Clock::get()?.unix_timestamp;
        if current_timestamp > giveaway_account.expiration_timestamp {
            return Err(ErrorCode::GiveawayExpired.into());
        }

        // Mark giveaway as claimed
        if giveaway_account.is_claimed {
            return Err(ErrorCode::AlreadyClaimed.into());
        }
        giveaway_account.is_claimed = true;

        Ok(())
    }

    // Initialize a new giveaway
    pub fn initialize_giveaway(
        ctx: Context<InitializeGiveaway>,
        giveaway_id: String,
        expiration_duration: i64,
    ) -> Result<()> {
        let giveaway_account = &mut ctx.accounts.giveaway_account;

        // Set giveaway ID and expiration timestamp
        giveaway_account.giveaway_id = giveaway_id;
        giveaway_account.expiration_timestamp = Clock::get()?.unix_timestamp + expiration_duration;
        giveaway_account.is_claimed = false;

        Ok(())
    }
}

// Account structure for storing giveaway data
#[account]
pub struct GiveawayAccount {
    pub giveaway_id: String,        // ID of the giveaway
    pub expiration_timestamp: i64, // Expiration time (Unix timestamp)
    pub is_claimed: bool,          // Status of claim
}

#[error_code]
pub enum ErrorCode {
    #[msg("Giveaway has expired.")]
    GiveawayExpired,
    #[msg("Giveaway has already been claimed.")]
    AlreadyClaimed,
}

// Context for claiming a giveaway
#[derive(Accounts)]
pub struct ClaimGiveaway<'info> {
    #[account(mut)]
    pub giveaway_account: Account<'info, GiveawayAccount>,
}

// Context for initializing a giveaway
#[derive(Accounts)]
pub struct InitializeGiveaway<'info> {
    #[account(init, payer = payer, space = 8 + 32 + 8 + 1)]
    pub giveaway_account: Account<'info, GiveawayAccount>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}
```
