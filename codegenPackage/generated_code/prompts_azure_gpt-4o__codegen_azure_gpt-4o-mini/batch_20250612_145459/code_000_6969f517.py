"""
Generated Code Metadata:
========================
Original URL: https://solana10x.com
Prompt: Write a Solana-based smart contract for a staking platform that distributes rewards every epoch (≈2 days) at a rate of 0.3836% per epoch, with a reward cap strategy limiting individual rewards to 5% of the total staking pool.
Generated: DETERMINISTIC_6969f5173e88cc21
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::clock::Clock;
use std::cmp;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the staking program
#[program]
pub mod staking_platform {
    use super::*;

    // Initialize the staking pool
    pub fn initialize(ctx: Context<Initialize>, total_stake: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.total_stake = total_stake;
        staking_pool.last_epoch = Clock::get()?.epoch;
        staking_pool.reward_rate = 0.003836; // 0.3836% per epoch
        staking_pool.reward_cap = 0.05; // 5% of total stake
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Update user's stake
        user.staked_amount += amount;
        staking_pool.total_stake += amount;

        // Ensure the total stake is updated correctly
        Ok(())
    }

    // Unstake tokens from the pool
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Ensure user has enough staked amount
        if user.staked_amount < amount {
            return Err(ErrorCode::InsufficientStake.into());
        }

        // Update user's stake and total stake
        user.staked_amount -= amount;
        staking_pool.total_stake -= amount;

        Ok(())
    }

    // Distribute rewards to users every epoch
    pub fn distribute_rewards(ctx: Context<DistributeRewards>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let current_epoch = Clock::get()?.epoch;

        // Check if an epoch has passed
        if current_epoch <= staking_pool.last_epoch {
            return Err(ErrorCode::EpochNotPassed.into());
        }

        // Calculate total rewards to distribute
        let total_rewards = (staking_pool.total_stake as f64 * staking_pool.reward_rate) as u64;
        let reward_cap = (staking_pool.total_stake as f64 * staking_pool.reward_cap) as u64;

        // Distribute rewards to each user
        for user in &mut ctx.accounts.users {
            let user_reward = cmp::min((user.staked_amount as f64 * staking_pool.reward_rate) as u64, reward_cap);
            user.reward_balance += user_reward;
        }

        // Update last epoch
        staking_pool.last_epoch = current_epoch;

        Ok(())
    }
}

// Define the staking pool structure
#[account]
pub struct StakingPool {
    pub total_stake: u64,
    pub last_epoch: u64,
    pub reward_rate: f64,
    pub reward_cap: f64,
}

// Define the user structure
#[account]
pub struct User {
    pub staked_amount: u64,
    pub reward_balance: u64,
}

// Define the context for initializing the staking pool
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + std::mem::size_of::<StakingPool>())]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Define the context for staking
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Account<'info, User>,
}

// Define the context for unstaking
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Account<'info, User>,
}

// Define the context for distributing rewards
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    pub users: Vec<Account<'info, User>>, // List of users to distribute rewards to
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient staked amount.")]
    InsufficientStake,
    #[msg("Epoch has not passed.")]
    EpochNotPassed,
}
```
