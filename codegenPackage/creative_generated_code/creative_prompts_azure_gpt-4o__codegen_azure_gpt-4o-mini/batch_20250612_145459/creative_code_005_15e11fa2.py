"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Write a Solana program that enforces a fair distribution system by limiting individual staking rewards to 5% of the total staking pool and capping annual rewards at 10,000 tokens.
Generated: DETERMINISTIC_15e11fa251734931
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import required libraries and modules from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program's ID
declare_id!("YourProgramIDHere");

// Define the StakingPool struct, which holds the staking pool data
#[account]
pub struct StakingPool {
    pub total_staked: u64,          // Total amount of tokens staked in the pool
    pub total_rewards_distributed: u64, // Total rewards distributed to stakers
    pub last_update_timestamp: i64,  // Last timestamp when rewards were updated
}

// Define the individual user staking data
#[account]
pub struct UserStaking {
    pub staked_amount: u64,          // Amount of tokens staked by the user
    pub rewards_claimed: u64,        // Total rewards claimed by the user
}

// Define the program's state
#[program]
pub mod fair_distribution {
    use super::*;

    // Initialize the staking pool
    pub fn initialize_pool(ctx: Context<InitializePool>) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        pool.total_staked = 0;
        pool.total_rewards_distributed = 0;
        pool.last_update_timestamp = Clock::get()?.unix_timestamp;
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake_tokens(ctx: Context<StakeTokens>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user_staking = &mut ctx.accounts.user_staking;

        // Check if the staking amount is greater than zero
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Update pool and user staking data
        pool.total_staked += amount;
        user_staking.staked_amount += amount;

        // Ensure the total staked does not exceed the limits
        if pool.total_staked < amount {
            return Err(ErrorCode::ExceededLimit.into());
        }

        Ok(())
    }

    // Claim staking rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        let user_staking = &mut ctx.accounts.user_staking;

        // Calculate eligible rewards for the user
        let user_rewards = calculate_rewards(user_staking, pool)?;

        // Check if the user exceeds the 5% distribution limit
        let max_user_reward = pool.total_staked * 5 / 100;
        if user_rewards > max_user_reward {
            return Err(ErrorCode::RewardLimitExceeded.into());
        }

        // Check if claiming will exceed the total cap of 10,000 tokens
        if pool.total_rewards_distributed + user_rewards > 10_000 {
            return Err(ErrorCode::AnnualRewardCapExceeded.into());
        }

        // Update the user's claimed rewards and the pool's distributed rewards
        user_staking.rewards_claimed += user_rewards;
        pool.total_rewards_distributed += user_rewards;

        Ok(())
    }

    // Function to calculate user rewards based on their staked amount and the pool
    fn calculate_rewards(user_staking: &UserStaking, pool: &StakingPool) -> Result<u64> {
        // Calculate rewards as a proportion of the user's stake to the total staked
        let user_reward = (user_staking.staked_amount as f64 / pool.total_staked as f64) * 10_000.0;
        Ok(user_reward as u64)
    }
}

// Define context for initializing the pool
#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = user, space = 8 + 32)]
    pub pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define context for staking tokens
#[derive(Accounts)]
pub struct StakeTokens<'info> {
    #[account(mut)]
    pub pool: Account<'info, StakingPool>,
    #[account(init_if_needed, payer = user, space = 8 + 32)]
    pub user_staking: Account<'info, UserStaking>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define context for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user_staking: Account<'info, UserStaking>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Define custom error codes for better error handling
#[error]
pub enum ErrorCode {
    #[msg("The staking amount must be greater than zero.")]
    InvalidAmount,
    #[msg("The operation exceeds the allowed limit.")]
    ExceededLimit,
    #[msg("The user's reward exceeds the 5% limit.")]
    RewardLimitExceeded,
    #[msg("Total rewards distributed exceed the annual cap of 10,000 tokens.")]
    AnnualRewardCapExceeded,
}
```
