"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daotops.web.app
Prompt: Create a smart contract on Solana that tracks and distributes rewards in $TNSR tokens based on user activity metrics, as implemented on the Tensor platform.
Generated: DETERMINISTIC_a161f2950585ab1b
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary modules and crates
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer, Mint};

// Declare the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod reward_distributor {
    use super::*;

    // Initialize the reward pool
    pub fn initialize(ctx: Context<Initialize>, reward_mint: Pubkey) -> Result<()> {
        let reward_pool = &mut ctx.accounts.reward_pool;
        reward_pool.reward_mint = reward_mint;
        reward_pool.admin = ctx.accounts.admin.key();
        reward_pool.total_rewards = 0;
        Ok(())
    }

    // Add rewards to the pool
    pub fn add_rewards(ctx: Context<AddRewards>, amount: u64) -> Result<()> {
        let pool_account = &mut ctx.accounts.reward_pool;
        token::transfer(ctx.accounts.transfer_context(), amount)?;
        pool_account.total_rewards += amount;
        Ok(())
    }

    // Distribute rewards based on user activity metrics
    pub fn distribute_rewards(ctx: Context<DistributeRewards>, user_activity_metrics: u64) -> Result<()> {
        let reward_pool = &mut ctx.accounts.reward_pool;
        let reward_amount = calculate_rewards(user_activity_metrics);

        require!(
            reward_pool.total_rewards >= reward_amount,
            RewardError::InsufficientRewardsInPool
        );

        token::transfer(
            ctx.accounts.distribution_context(),
            reward_amount
        )?;
        reward_pool.total_rewards -= reward_amount;
        Ok(())
    }
}

// Context Structures
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 32 + 8)]
    pub reward_pool: Account<'info, RewardPool>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct AddRewards<'info> {
    #[account(mut)]
    pub reward_pool: Account<'info, RewardPool>,
    #[account(mut)]
    pub reward_source: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_pool_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Helper for transferring rewards during distribution
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_pool: Account<'info, RewardPool>,
    #[account(mut)]
    pub user_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_pool_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Reward Pool Account
#[account]
pub struct RewardPool {
    pub reward_mint: Pubkey, // Token mint address for $TNSR
    pub admin: Pubkey,       // Admin who controls the pool
    pub total_rewards: u64,  // Total rewards available in the pool
}

// Reward Calculation Logic
fn calculate_rewards(activity_metrics: u64) -> u64 {
    // Example logic: 1 reward token per activity unit
    activity_metrics
}

// Custom Errors
#[error_code]
pub enum RewardError {
    #[msg("Insufficient rewards in the pool.")]
    InsufficientRewardsInPool,
}

```
