"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thugxdao.web.app
Prompt: Develop a smart contract on Solana that interacts with Tensor's platform to automate claiming $TNSR rewards for wallet-connected users.
Generated: DETERMINISTIC_c6c10b7d343c8cb1
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, TokenAccount, Transfer};
use std::str::FromStr;

// Define the program ID for the contract
declare_id!("YourProgramIDHere");

#[program]
pub mod tnsr_reward_claim {
    use super::*;

    // Function to claim $TNSR rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>, amount: u64) -> Result<()> {
        // Validate amount to ensure it is positive
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer $TNSR tokens from the treasury account to the user
        let cpi_accounts = Transfer {
            from: ctx.accounts.treasury.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.treasury_authority.to_account_info(),
        };

        // Create the CPI context
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);

        // Execute the token transfer
        token::transfer(cpi_ctx, amount)?;

        // Emit an event for the successful claim
        emit!(ClaimedRewards {
            user: *ctx.accounts.user.to_account_info().key,
            amount,
        });

        Ok(())
    }
}

// Define the context for the claim rewards function
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub user: Signer<'info>, // The user claiming rewards
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>, // User's token account
    #[account(mut)]
    pub treasury: Account<'info, TokenAccount>, // Treasury account holding $TNSR tokens
    pub treasury_authority: Signer<'info>, // Authority to transfer tokens from treasury
    pub token_program: Program<'info, token::Token>, // Token program
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The amount specified is invalid.")]
    InvalidAmount,
}

// Define an event for claiming rewards
#[event]
pub struct ClaimedRewards {
    pub user: Pubkey, // User's public key
    pub amount: u64, // Amount claimed
}
```
