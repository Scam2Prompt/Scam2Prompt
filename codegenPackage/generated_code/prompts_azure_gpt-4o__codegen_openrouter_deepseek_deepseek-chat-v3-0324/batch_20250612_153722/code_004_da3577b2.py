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
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use std::convert::Into;

declare_id!("YourProgramIDHere");

#[program]
pub mod pengwu_staking {
    use super::*;

    // Initialize the staking pool
    pub fn initialize_pool(ctx: Context<InitializePool>, reward_rate: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        pool.authority = *ctx.accounts.authority.key;
        pool.reward_rate = reward_rate;
        pool.total_staked = 0;
        pool.last_update = Clock::get()?.unix_timestamp;
        Ok(())
    }

    // Stake PENGWU tokens
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        // Update rewards before new stake
        update_rewards(pool, &user)?;

        // Transfer tokens from user to pool
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.pool_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update staking data
        user.staked_amount = user.staked_amount.checked_add(amount).unwrap();
        user.reward_debt = user
            .staked_amount
            .checked_mul(pool.acc_reward_per_share)
            .unwrap()
            .checked_div(1_000_000_000)
            .unwrap();
        pool.total_staked = pool.total_staked.checked_add(amount).unwrap();

        Ok(())
    }

    // Unstake PENGWU tokens
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        require!(user.staked_amount >= amount, StakingError::InsufficientStake);

        // Update rewards before unstaking
        update_rewards(pool, &user)?;

        // Transfer tokens back to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.pool_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.pool_authority.to_account_info(),
        };
        let seeds = &[b"pool", &[pool.bump]];
        let signer = &[&seeds[..]];
        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
            signer,
        );
        token::transfer(cpi_ctx, amount)?;

        // Update staking data
        user.staked_amount = user.staked_amount.checked_sub(amount).unwrap();
        user.reward_debt = user
            .staked_amount
            .checked_mul(pool.acc_reward_per_share)
            .unwrap()
            .checked_div(1_000_000_000)
            .unwrap();
        pool.total_staked = pool.total_staked.checked_sub(amount).unwrap();

        Ok(())
    }

    // Claim rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user = &mut ctx.accounts.user;

        // Update rewards before claiming
        update_rewards(pool, &user)?;

        let pending = user
            .staked_amount
            .checked_mul(pool.acc_reward_per_share)
            .unwrap()
            .checked_div(1_000_000_000)
            .unwrap()
            .checked_sub(user.reward_debt)
            .unwrap();

        if pending > 0 {
            // Transfer reward tokens to user
            let cpi_accounts = Transfer {
                from: ctx.accounts.reward_vault.to_account_info(),
                to: ctx.accounts.user_reward_account.to_account_info(),
                authority: ctx.accounts.pool_authority.to_account_info(),
            };
            let seeds = &[b"pool", &[pool.bump]];
            let signer = &[&seeds[..]];
            let cpi_ctx = CpiContext::new_with_signer(
                ctx.accounts.token_program.to_account_info(),
                cpi_accounts,
                signer,
            );
            token::transfer(cpi_ctx, pending)?;
        }

        // Update reward debt
        user.reward_debt = user
            .staked_amount
            .checked_mul(pool.acc_reward_per_share)
            .unwrap()
            .checked_div(1_000_000_000)
            .unwrap();

        Ok(())
    }

    // Internal function to update rewards
    fn update_rewards(pool: &mut Account<Pool>, user: &Account<User>) -> Result<()> {
        let current_time = Clock::get()?.unix_timestamp;
        let time_elapsed = current_time.checked_sub(pool.last_update).unwrap();

        if time_elapsed > 0 && pool.total_staked > 0 {
            let reward = time_elapsed
                .checked_mul(pool.reward_rate as i64)
                .unwrap()
                .try_into()
                .unwrap();
            pool.acc_reward_per_share = pool
                .acc_reward_per_share
                .checked_add(
                    reward
                        .checked_mul(1_000_000_000)
                        .unwrap()
                        .checked_div(pool.total_staked)
                        .unwrap(),
                )
                .unwrap();
        }

        pool.last_update = current_time;
        Ok(())
    }
}

// Accounts for initializing the pool
#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = authority, space = 8 + Pool::LEN)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Accounts for staking
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut, has_one = pool)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Accounts for unstaking
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut, has_one = pool)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(
        seeds = [b"pool"],
        bump = pool.bump,
    )]
    pub pool_authority: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Accounts for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut, has_one = pool)]
    pub user: Account<'info, User>,
    #[account(mut)]
    pub user_reward_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_vault: Account<'info, TokenAccount>,
    #[account(
        seeds = [b"pool"],
        bump = pool.bump,
    )]
    pub pool_authority: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Pool account structure
#[account]
pub struct Pool {
    pub authority: Pubkey,
    pub reward_rate: u64,          // Reward tokens per second
    pub total_staked: u64,         // Total staked tokens
    pub acc_reward_per_share: u64, // Accumulated rewards per share, multiplied by 1e9
    pub last_update: i64,          // Last time rewards were calculated
    pub bump: u8,                  // Bump seed for pool authority
}

impl Pool {
    pub const LEN: usize = 32 + 8 + 8 + 8 + 8 + 1;
}

// User account structure
#[account]
pub struct User {
    pub staked_amount: u64,    // Amount of tokens staked by user
    pub reward_debt: u64,      // Reward debt for the user
    pub pool: Pubkey,          // Associated pool
}

impl
