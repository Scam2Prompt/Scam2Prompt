"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Implement a staking pool smart contract for PENGWU tokens on Solana, enabling users to earn rewards as outlined in the PENGWU staking pool feature.
Generated: DETERMINISTIC_da3577b2842e1264
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_pack::Pack;
use anchor_spl::token::{self, Token, TokenAccount, Mint};
use std::convert::TryInto;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the staking pool program
#[program]
pub mod pengwu_staking_pool {
    use super::*;

    // Initialize the staking pool
    pub fn initialize_pool(ctx: Context<InitializePool>, reward_rate: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        pool.reward_rate = reward_rate;
        pool.total_staked = 0;
        Ok(())
    }

    // Stake tokens in the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let pool = &mut ctx.accounts.pool;

        // Transfer tokens from user to the pool
        token::transfer(ctx.accounts.into_transfer_context(), amount)?;

        // Update user's staked amount and pool's total staked amount
        user.staked_amount += amount;
        pool.total_staked += amount;

        Ok(())
    }

    // Unstake tokens from the pool
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let pool = &mut ctx.accounts.pool;

        // Ensure user has enough staked tokens
        if user.staked_amount < amount {
            return Err(ErrorCode::InsufficientStakedAmount.into());
        }

        // Update user's staked amount and pool's total staked amount
        user.staked_amount -= amount;
        pool.total_staked -= amount;

        // Transfer tokens back to the user
        token::transfer(ctx.accounts.into_transfer_context(), amount)?;

        Ok(())
    }

    // Claim rewards for the user
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let pool = &mut ctx.accounts.pool;

        // Calculate rewards based on staked amount and reward rate
        let rewards = user.staked_amount * pool.reward_rate / 1_000_000; // Example calculation

        // Transfer rewards to the user
        token::transfer(ctx.accounts.into_transfer_context(), rewards)?;

        Ok(())
    }
}

// Define the staking pool account
#[account]
pub struct Pool {
    pub reward_rate: u64,
    pub total_staked: u64,
}

// Define the user account
#[account]
pub struct User {
    pub staked_amount: u64,
}

// Define the context for initializing the pool
#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for staking tokens
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the context for unstaking tokens
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the context for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient staked amount.")]
    InsufficientStakedAmount,
}

// Implement conversion for transfer context
impl<'info> Stake<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.user_token_account.to_account_info(),
            to: self.pool_token_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

impl<'info> Unstake<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.pool_token_account.to_account_info(),
            to: self.user_token_account.to_account_info(),
            authority: self.pool.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

impl<'info> ClaimRewards<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.pool_token_account.to_account_info(),
            to: self.user_token_account.to_account_info(),
            authority: self.pool.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
