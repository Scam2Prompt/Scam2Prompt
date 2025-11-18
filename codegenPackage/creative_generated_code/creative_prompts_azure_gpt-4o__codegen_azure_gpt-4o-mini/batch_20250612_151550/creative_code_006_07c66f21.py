"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Provide an example of how to integrate `$BLD` token rewards into a Solana-based NFT project, specifically for the Buildoors ecosystem.
Generated: DETERMINISTIC_07c66f21debad422
Batch ID: 20250612_151550
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
use anchor_spl::token::{self, Token, TokenAccount, Mint};
use std::convert::TryInto;

// Declare the program's ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod buildoors_nft_rewards {
    use super::*;

    // Function to initialize the reward system
    pub fn initialize_rewards(ctx: Context<InitializeRewards>) -> Result<()> {
        let reward_account = &mut ctx.accounts.reward_account;
        reward_account.total_rewards = 0; // Initialize total rewards to zero
        Ok(())
    }

    // Function to distribute $BLD rewards to an NFT holder
    pub fn distribute_rewards(ctx: Context<DistributeRewards>, amount: u64) -> Result<()> {
        let reward_account = &mut ctx.accounts.reward_account;
        let recipient = &ctx.accounts.recipient;

        // Ensure the amount is positive
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Update the total rewards
        reward_account.total_rewards += amount;

        // Transfer the $BLD tokens
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.reward_pool.to_account_info(),
            to: recipient.to_account_info(),
            authority: ctx.accounts.authority.clone(),
        };
        let cpi_context = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_context, amount)?;

        Ok(())
    }
}

// Define the accounts required for initializing rewards
#[derive(Accounts)]
pub struct InitializeRewards<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub reward_account: Account<'info, RewardAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the accounts required for distributing rewards
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_account: Account<'info, RewardAccount>,
    #[account(mut)]
    pub reward_pool: Account<'info, TokenAccount>, // Account holding $BLD tokens
    #[account(mut)]
    pub recipient: Account<'info, TokenAccount>, // Recipient's token account
    pub authority: Signer<'info>, // Authority to send tokens
    pub token_program: Program<'info, Token>, // SPL Token Program
}

// Define a struct to hold reward account data
#[account]
pub struct RewardAccount {
    pub total_rewards: u64, // Total rewards distributed
}

// Define error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("Amount must be greater than zero.")]
    InvalidAmount,
}
```
