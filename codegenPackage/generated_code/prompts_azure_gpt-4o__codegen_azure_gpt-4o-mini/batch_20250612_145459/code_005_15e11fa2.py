"""
Generated Code Metadata:
========================
Original URL: https://solana10x.com
Prompt: Write a Solana program that enforces a fair distribution system by limiting individual staking rewards to 5% of the total staking pool and capping annual rewards at 10,000 tokens.
Generated: DETERMINISTIC_15e11fa251734931
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program's ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod fair_distribution {
    use super::*;

    // Initialize the staking pool
    pub fn initialize(ctx: Context<Initialize>, total_stake: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.total_stake = total_stake;
        staking_pool.total_rewards = 0;
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Ensure the amount is positive
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Update user's stake
        user.staked_amount += amount;
        staking_pool.total_stake += amount;

        Ok(())
    }

    // Claim rewards based on staking
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Calculate the user's share of the rewards
        let user_share = user.staked_amount as f64 / staking_pool.total_stake as f64;
        let max_reward = (staking_pool.total_rewards as f64 * 0.05).min(10000.0);
        let user_reward = (user_share * max_reward).round() as u64;

        // Ensure the user does not exceed the annual cap
        if user_reward + user.claimed_rewards > 10000 {
            return Err(ErrorCode::AnnualCapExceeded.into());
        }

        // Update user's claimed rewards
        user.claimed_rewards += user_reward;
        staking_pool.total_rewards -= user_reward;

        Ok(())
    }
}

// Define the staking pool structure
#[account]
pub struct StakingPool {
    pub total_stake: u64,
    pub total_rewards: u64,
}

// Define the user structure
#[account]
pub struct User {
    pub staked_amount: u64,
    pub claimed_rewards: u64,
}

// Define the context for initializing the staking pool
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for staking tokens
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Account<'info, User>,
}

// Define the context for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Account<'info, User>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
    #[msg("The annual cap of 10,000 tokens has been exceeded.")]
    AnnualCapExceeded,
}
```
