"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Implement a staking pool smart contract for PENGWU tokens on Solana, enabling users to earn rewards as outlined in the PENGWU staking pool feature.
Generated: DETERMINISTIC_da3577b2842e1264
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Solana Staking Pool Smart Contract for PENGWU Tokens

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod pengwu_staking {
    use super::*;

    // Initialize the staking pool
    pub fn initialize_pool(ctx: Context<InitializePool>, reward_rate: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        pool.mint = ctx.accounts.mint.key();
        pool.reward_rate = reward_rate;
        pool.total_staked = 0;
        pool.bump = *ctx.bumps.get("pool").unwrap();
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        // Transfer tokens from the user to the pool
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.pool_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_context = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_context, amount)?;

        // Update pool and user state
        pool.total_staked += amount;
        user.staked_amount += amount;
        user.last_update_time = Clock::get()?.unix_timestamp;
        Ok(())
    }

    // Unstake tokens from the pool
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        require!(user.staked_amount >= amount, StakingError::InsufficientStake);

        // Transfer tokens back to the user
        let seeds = &[pool.to_account_info().key.as_ref(), &[pool.bump]];
        let signer = &[&seeds[..]];
        let cpi_accounts = Transfer {
            from: ctx.accounts.pool_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.pool.to_account_info(),
        };
        let cpi_context = CpiContext::new_with_signer(ctx.accounts.token_program.to_account_info(), cpi_accounts, signer);
        token::transfer(cpi_context, amount)?;

        // Update pool and user state
        pool.total_staked -= amount;
        user.staked_amount -= amount;
        user.last_update_time = Clock::get()?.unix_timestamp;
        Ok(())
    }

    // Claim rewards from the pool
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        let current_time = Clock::get()?.unix_timestamp;
        let reward_rate = pool.reward_rate;
        let staked_duration = current_time - user.last_update_time;
        let rewards = (user.staked_amount as u128 * reward_rate as u128 * staked_duration as u128) / 1_000_000;

        // Transfer reward tokens to the user
        let seeds = &[pool.to_account_info().key.as_ref(), &[pool.bump]];
        let signer = &[&seeds[..]];
        let cpi_accounts = Transfer {
            from: ctx.accounts.pool_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.pool.to_account_info(),
        };
        let cpi_context = CpiContext::new_with_signer(ctx.accounts.token_program.to_account_info(), cpi_accounts, signer);
        token::transfer(cpi_context, rewards as u64)?;

        // Update user state
        user.last_update_time = current_time;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = authority, space = 8 + 40, seeds = [b"pool", mint.key().as_ref()], bump)]
    pub pool: Account<'info, Pool>,
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut, seeds = [b"pool", pool.mint.as_ref()], bump = pool.bump)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut, seeds = [b"pool", pool.mint.as_ref()], bump = pool.bump)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut, seeds = [b"pool", pool.mint.as_ref()], bump = pool.bump)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct Pool {
    pub mint: Pubkey,           // The mint address of the token being staked
    pub reward_rate: u64,       // Reward rate per second per token staked
    pub total_staked: u64,      // Total tokens staked in the pool
    pub bump: u8,               // Bump seed for PDA
}

#[account]
pub struct User {
    pub staked_amount: u64,     // Amount of tokens staked by the user
    pub last_update_time: i64,  // Last time user interacted with staking pool
}

#[error_code]
pub enum StakingError {
    #[msg("User does not have sufficient staked tokens to perform this operation.")]
    InsufficientStake,
}
```
