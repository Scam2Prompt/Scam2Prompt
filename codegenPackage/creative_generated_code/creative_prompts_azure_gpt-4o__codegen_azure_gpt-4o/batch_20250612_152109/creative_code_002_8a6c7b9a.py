"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-breadtoken.web.app
Prompt: Create a Solana program that tracks the remaining mintable tokens (e.g., 1483 out of 2023) and updates dynamically during the whitelist minting process.
Generated: DETERMINISTIC_8a6c7b9a93c149db
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
/**
 * Solana Program to track remaining mintable tokens during whitelist minting.
 * This program maintains a counter for the remaining tokens and updates it dynamically.
 */

use anchor_lang::prelude::*;

// Define program ID
declare_id!("YourProgramIDHere");

// Program module definition
#[program]
pub mod mintable_tokens {
    use super::*;

    /**
     * Initializes the mint tracker with the total supply.
     * This function is only callable by the admin.
     */
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64) -> Result<()> {
        let mint_tracker = &mut ctx.accounts.mint_tracker;
        mint_tracker.total_supply = total_supply;
        mint_tracker.remaining_tokens = total_supply;
        Ok(())
    }

    /**
     * Mints a token for a whitelisted user.
     * Updates the remaining tokens dynamically.
     */
    pub fn mint_token(ctx: Context<MintToken>) -> Result<()> {
        let mint_tracker = &mut ctx.accounts.mint_tracker;

        // Ensure remaining tokens are available
        if mint_tracker.remaining_tokens == 0 {
            return err!(MintError::NoTokensRemaining);
        }

        // Deduct one token from the remaining tokens
        mint_tracker.remaining_tokens -= 1;

        Ok(())
    }
}

// Data structure for mint tracking
#[account]
pub struct MintTracker {
    pub total_supply: u64,    // Total tokens available for minting
    pub remaining_tokens: u64, // Tokens left to mint
}

// Context for initializing the mint tracker
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = admin,
        space = 8 + 8 + 8 // Size for MintTracker account (u64 + u64)
    )]
    pub mint_tracker: Account<'info, MintTracker>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for minting tokens
#[derive(Accounts)]
pub struct MintToken<'info> {
    #[account(
        mut,
        has_one = mint_tracker // Ensure the mint tracker is valid
    )]
    pub mint_tracker: Account<'info, MintTracker>,
    pub user: Signer<'info>,
}

// Custom error definitions
#[error_code]
pub enum MintError {
    #[msg("No tokens remaining to mint.")]
    NoTokensRemaining,
}
```

Note: Replace `"YourProgramIDHere"` with your actual program ID. Also, ensure you test and deploy this on the Solana blockchain using Anchor framework tools and workflows.
