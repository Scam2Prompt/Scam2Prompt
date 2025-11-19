"""
Generated Code Metadata:
========================
Original URL: https://solana10x.com
Prompt: Develop a smart contract on Solana that distributes staking rewards every epoch (approximately 2 days) at a rate of 0.3836% per epoch, with a minimum stake of 100 SOL10x tokens.
Generated: DETERMINISTIC_70cfb5336c27431f
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Solana to distribute staking rewards every epoch

use anchor_lang::prelude::*;
use anchor_lang::solana_program::clock::Clock;

declare_id!("YourProgramIDHere");

#[program]
pub mod staking_rewards {
    use super::*;

    // Initialize the staking pool
    pub fn initialize(ctx: Context<Initialize>, reward_rate: f64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.reward_rate = reward_rate;
        staking_pool.last_epoch_timestamp = Clock::get()?.unix_timestamp;
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user_account = &mut ctx.accounts.user_account;

        // Ensure minimum stake requirement
        require!(amount >= 100 * 10u64.pow(9), StakingError::InsufficientStake);

        // Update user account and pool state
        user_account.staked_amount += amount;
        staking_pool.total_staked += amount;

        Ok(())
    }

    // Distribute rewards to stakers
    pub fn distribute_rewards(ctx: Context<DistributeRewards>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let clock = Clock::get()?;
        let current_timestamp = clock.unix_timestamp;

        // Check if an epoch has passed (approx. 2 days = 172800 seconds)
        require!(
            current_timestamp - staking_pool.last_epoch_timestamp >= 172800,
            StakingError::EpochNotElapsed
        );

        // Calculate rewards for each staker
        for user_account in &mut ctx.remaining_accounts {
            let user_account = Account::<UserAccount>::try_from(user_account)?;
            let reward = (user_account.staked_amount as f64 * staking_pool.reward_rate / 100.0) as u64;
            user_account.rewards_earned += reward;
        }

        // Update last epoch timestamp
        staking_pool.last_epoch_timestamp = current_timestamp;

        Ok(())
    }
}

// Contexts for instructions
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 8 + 8)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
}

#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
}

// Account structures
#[account]
pub struct StakingPool {
    pub reward_rate: f64, // Reward rate per epoch (e.g., 0.3836%)
    pub total_staked: u64, // Total staked amount in the pool
    pub last_epoch_timestamp: i64, // Timestamp of the last epoch
}

#[account]
pub struct UserAccount {
    pub staked_amount: u64, // Amount staked by the user
    pub rewards_earned: u64, // Total rewards earned by the user
}

// Custom error types
#[error_code]
pub enum StakingError {
    #[msg("Insufficient stake amount. Minimum is 100 SOL10x tokens.")]
    InsufficientStake,
    #[msg("An epoch has not yet elapsed.")]
    EpochNotElapsed,
}
```
