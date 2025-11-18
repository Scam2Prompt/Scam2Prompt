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
// Import necessary crates and modules from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID for the staking pool
declare_id!("YourProgramIDHere");

// Define the staking pool program
#[program]
pub mod pengwu_staking_pool {
    use super::*;

    // Initialize the staking pool
    pub fn initialize(ctx: Context<Initialize>, pool_reward: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.pool_reward = pool_reward;
        staking_pool.total_staked = 0;
        staking_pool.reward_per_token = 0;
        Ok(())
    }

    // Stake tokens into the pool
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Update the total staked and the user's staked amount
        staking_pool.total_staked += amount;
        user.amount_staked += amount;

        // Transfer PENGWU tokens from the user to the staking pool
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.pool_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(cpi_ctx.with_signer(&[&user.signer_seeds()]), amount)?;

        Ok(())
    }

    // Unstake tokens from the pool
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user = &mut ctx.accounts.user;

        // Ensure the user has enough staked amount to unstake
        require!(user.amount_staked >= amount, StakingError::InsufficientFunds);

        // Update the total staked and the user's staked amount
        staking_pool.total_staked -= amount;
        user.amount_staked -= amount;

        // Transfer PENGWU tokens back to the user
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.pool_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.staking_pool.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(cpi_ctx.with_signer(&[&staking_pool.signer_seeds()]), amount)?;

        Ok(())
    }

    // Claim rewards for the user
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let staking_pool = &mut ctx.accounts.staking_pool;

        // Calculate rewards based on staked amount and reward per token
        let rewards = user.amount_staked * staking_pool.reward_per_token;
        user.claimed_rewards += rewards;

        // Transfer rewards to the user
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.pool_reward_account.to_account_info(),
            to: ctx.accounts.user_reward_account.to_account_info(),
            authority: ctx.accounts.staking_pool.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(cpi_ctx.with_signer(&[&staking_pool.signer_seeds()]), rewards)?;

        Ok(())
    }
}

// Define the staking pool struct
#[account]
pub struct StakingPool {
    pub pool_reward: u64,
    pub total_staked: u64,
    pub reward_per_token: u64,
}

// Define the user struct
#[account]
pub struct User {
    pub amount_staked: u64,
    pub claimed_rewards: u64,
}

// Define error types
#[error]
pub enum StakingError {
    #[msg("Insufficient funds for unstaking.")]
    InsufficientFunds,
}

// Define the context structs for each instruction
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init)]
    pub staking_pool: ProgramAccount<'info, StakingPool>,
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_pool: ProgramAccount<'info, StakingPool>,
    pub user: Account<'info, User>,
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_pool: ProgramAccount<'info, StakingPool>,
    pub user: Account<'info, User>,
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    pub staking_pool: ProgramAccount<'info, StakingPool>,
    pub user: Account<'info, User>,
    pub user_reward_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_reward_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}
```
