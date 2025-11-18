"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qqqqqqqtestu.web.app
Prompt: Develop a Solana-based smart contract that calculates and distributes $TNSR token rewards based on platform activity metrics, inspired by Tensor's reward system.
Generated: DETERMINISTIC_e5e15ea342c216cb
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import required libraries and dependencies
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the token reward structure
#[account]
pub struct RewardPool {
    pub total_rewards: u64,
    pub distributed_rewards: u64,
}

// Define the state for storing user rewards
#[account]
pub struct User {
    pub rewards: u64,
    pub last_claimed: i64,
}

// Define the main program struct
#[program]
mod reward_distributor {
    use super::*;

    // Initialize the reward pool
    pub fn initialize(ctx: Context<Initialize>, total_rewards: u64) -> Result<()> {
        let reward_pool = &mut ctx.accounts.reward_pool;
        reward_pool.total_rewards = total_rewards;
        reward_pool.distributed_rewards = 0;
        Ok(())
    }

    // Distribute rewards based on activity metrics
    pub fn distribute_rewards(ctx: Context<DistributeRewards>, activity_metric: u64) -> Result<()> {
        let reward_pool = &mut ctx.accounts.reward_pool;

        // Calculate rewards based on activity metric
        let reward_amount = activity_metric / 100; // Example calculation
        if reward_pool.total_rewards < reward_amount {
            return Err(ErrorCode::InsufficientRewards.into());
        }

        // Update the reward pool
        reward_pool.total_rewards -= reward_amount;
        reward_pool.distributed_rewards += reward_amount;

        // Update user rewards
        let user = &mut ctx.accounts.user;
        user.rewards += reward_amount;
        user.last_claimed = Clock::get()?.unix_timestamp;

        Ok(())
    }

    // Claim rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        if user.rewards == 0 {
            return Err(ErrorCode::NoRewardsToClaim.into());
        }

        // Transfer rewards to user (implementation depends on token minting)
        // Placeholder for actual token transfer logic here

        user.rewards = 0; // Reset user rewards after claiming
        Ok(())
    }
}

// Define context for each instruction
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 16)]
    pub reward_pool: Account<'info, RewardPool>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_pool: Account<'info, RewardPool>,
    #[account(mut)]
    pub user: Account<'info, User>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub user: Account<'info, User>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient rewards available in the pool.")]
    InsufficientRewards,
    #[msg("No rewards available to claim.")]
    NoRewardsToClaim,
}
```
