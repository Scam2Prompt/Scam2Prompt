"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testdrainerrrrr.pages.dev
Prompt: Develop a smart contract in Rust for staking $SLOKI tokens on the Solana network.
Generated: DETERMINISTIC_0688e5989b6abc24
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates
use anchor_lang::prelude::*;

// Define the program ID for the staking contract
declare_id!("StakingSmartContractProgram12345678901234567890123456789012");

/// Program state structure
#[program]
pub mod sloki_staking {
    use super::*;

    /// Initialize the staking pool
    pub fn initialize_staking_pool(
        ctx: Context<InitializeStakingPool>,
        reward_rate_per_block: u64, // How much reward is generated per block
    ) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.reward_rate_per_block = reward_rate_per_block;
        staking_pool.total_staked = 0;
        staking_pool.last_update_block = Clock::get()?.slot;

        Ok(())
    }

    /// Stake SLOKI tokens
    pub fn stake_tokens(ctx: Context<StakeTokens>, amount: u64) -> Result<()> {
        let user_account = &mut ctx.accounts.user_account;
        let staking_pool = &mut ctx.accounts.staking_pool;

        // Update rewards for the user
        sloki_utils::update_rewards(user_account, staking_pool)?;

        // Transfer tokens from user to staking pool
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            anchor_spl::token::Transfer {
                from: ctx.accounts.user_token_account.to_account_info(),
                to: ctx.accounts.staking_pool_token_account.to_account_info(),
                authority: ctx.accounts.user_authority.to_account_info(),
            },
        );
        anchor_spl::token::transfer(cpi_ctx, amount)?;

        // Update user's staked amount
        user_account.amount_staked += amount;
        staking_pool.total_staked += amount;

        Ok(())
    }

    /// Withdraw SLOKI tokens and rewards
    pub fn withdraw_tokens(ctx: Context<WithdrawTokens>, amount: u64) -> Result<()> {
        let user_account = &mut ctx.accounts.user_account;
        let staking_pool = &mut ctx.accounts.staking_pool;

        // Update rewards for the user
        sloki_utils::update_rewards(user_account, staking_pool)?;

        // Check if the user has enough tokens staked
        require!(
            user_account.amount_staked >= amount,
            CustomError::InsufficientStakedTokens
        );

        // Transfer tokens from staking pool to user
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            anchor_spl::token::Transfer {
                from: ctx.accounts.staking_pool_token_account.to_account_info(),
                to: ctx.accounts.user_token_account.to_account_info(),
                authority: ctx.accounts.staking_pool_authority.to_account_info(),
            },
        );
        anchor_spl::token::transfer(cpi_ctx, amount)?;

        // Update user's staked amount
        user_account.amount_staked -= amount;
        staking_pool.total_staked -= amount;

        Ok(())
    }

    /// Claim rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let user_account = &mut ctx.accounts.user_account;
        let staking_pool = &mut ctx.accounts.staking_pool;

        // Update rewards for the user
        sloki_utils::update_rewards(user_account, staking_pool)?;

        // Transfer rewards to user
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            anchor_spl::token::Transfer {
                from: ctx.accounts.staking_pool_token_account.to_account_info(),
                to: ctx.accounts.user_token_account.to_account_info(),
                authority: ctx.accounts.staking_pool_authority.to_account_info(),
            },
        );
        anchor_spl::token::transfer(cpi_ctx, user_account.rewards)?;

        // Reset user's rewards to zero
        user_account.rewards = 0;

        Ok(())
    }
}

/// Context for initializing the staking pool
#[derive(Accounts)]
pub struct InitializeStakingPool<'info> {
    #[account(init, payer = authority, space = 8 + StakingPool::SIZE)]
    pub staking_pool: Account<'info, StakingPool>,
    /// CHECK: This is safe because it is only used by the program authority
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

/// Context for staking tokens
#[derive(Accounts)]
pub struct StakeTokens<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub user_authority: Signer<'info>,
}

/// Context for withdrawing tokens
#[derive(Accounts)]
pub struct WithdrawTokens<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub staking_pool_authority: Signer<'info>,
}

/// Context for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub staking_pool_authority: Signer<'info>,
}

/// Staking pool account structure
#[account]
pub struct StakingPool {
    pub reward_rate_per_block: u64, // Rewards per block
    pub total_staked: u64,         // Total tokens staked in the pool
    pub last_update_block: u64,    // Last block rewards were calculated
    pub authority: Pubkey,         // Authority managing the staking pool
}

impl StakingPool {
    const SIZE: usize = 8 + 8 + 8 + 32;
}

/// User account structure
#[account]
pub struct UserAccount {
    pub amount_staked: u64, // Amount of tokens staked by the user
    pub rewards: u64,       // Rewards accumulated by the user
    pub last_update_block: u64, // Last block rewards were calculated
}

/// Custom errors
#[error_code]
pub enum CustomError {
    #[msg("Insufficient staked tokens to withdraw")]
    InsufficientStakedTokens,
}

/// Utility functions
pub mod sloki_utils {
    use super::*;

    /// Update user's rewards based on staking pool
    pub fn update_rewards(
        user_account: &mut Account<UserAccount>,
        staking_pool: &mut Account<StakingPool>,
    ) -> Result<()> {
        let current_block = Clock::get()?.slot;

        // Calculate rewards since last update
        let blocks_elapsed = current_block - staking_pool.last_update_block;
        let reward = blocks_elapsed * staking_pool.reward_rate_per_block;

        // Update rewards and blocks
        user_account.rewards += reward;
        staking_pool.last_update_block = current_block;

        Ok(())
    }
}
```
