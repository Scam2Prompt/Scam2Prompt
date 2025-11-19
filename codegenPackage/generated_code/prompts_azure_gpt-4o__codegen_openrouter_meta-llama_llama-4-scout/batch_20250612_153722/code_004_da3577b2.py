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
// Import required libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{Token, TokenAccount};

// Define the PENGWU token mint address
declare_id!("PENGWU_TOKEN_MINT_ADDRESS");

// Define the staking pool program ID
declare_id!("STAKING_POOL_PROGRAM_ID");

// Define the StakingPool struct
#[account]
pub struct StakingPool {
    pub authority: Pubkey,
    pub token_account: Pubkey,
    pub reward_token_account: Pubkey,
    pub total_staked: u64,
    pub total_rewards: u64,
    pub reward_rate: u64,
}

// Define the Staker struct
#[account]
pub struct Staker {
    pub user: Pubkey,
    pub staking_pool: Pubkey,
    pub stake_amount: u64,
}

// Initialize the staking pool
#[program]
pub mod pengwu_staking_pool {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, reward_rate: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.authority = ctx.program_id;
        staking_pool.token_account = ctx.accounts.token_account.key();
        staking_pool.reward_token_account = ctx.accounts.reward_token_account.key();
        staking_pool.total_staked = 0;
        staking_pool.total_rewards = 0;
        staking_pool.reward_rate = reward_rate;

        Ok(())
    }

    // Stake PENGWU tokens
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &mut ctx.accounts.staker;
        let token_account = &ctx.accounts.token_account;

        // Check if the token account is valid
        require!(token_account.amount >= amount, StakingPoolError::InsufficientTokens);

        // Transfer tokens to the staking pool
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program,
                token::Transfer {
                    from: token_account.key(),
                    to: staking_pool.token_account,
                    authority: staker.user,
                },
            ),
            amount,
        )?;

        // Update staker information
        staker.user = staker.user;
        staker.staking_pool = staking_pool.key();
        staker.stake_amount += amount;

        // Update staking pool information
        staking_pool.total_staked += amount;

        Ok(())
    }

    // Unstake PENGWU tokens
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &mut ctx.accounts.staker;
        let token_account = &ctx.accounts.token_account;

        // Check if the staker has enough stake
        require!(staker.stake_amount >= amount, StakingPoolError::InsufficientStake);

        // Transfer tokens from the staking pool
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program,
                token::Transfer {
                    from: staking_pool.token_account,
                    to: token_account.key(),
                    authority: staking_pool.authority,
                },
            ),
            amount,
        )?;

        // Update staker information
        staker.stake_amount -= amount;

        // Update staking pool information
        staking_pool.total_staked -= amount;

        Ok(())
    }

    // Claim rewards
    pub fn claim(ctx: Context<Claim>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &ctx.accounts.staker;
        let reward_token_account = &ctx.accounts.reward_token_account;

        // Calculate rewards
        let rewards = staker.stake_amount * staking_pool.reward_rate / 100;

        // Check if rewards are available
        require!(staking_pool.total_rewards >= rewards, StakingPoolError::InsufficientRewards);

        // Transfer rewards to the staker
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program,
                token::Transfer {
                    from: staking_pool.reward_token_account,
                    to: reward_token_account.key(),
                    authority: staking_pool.authority,
                },
            ),
            rewards,
        )?;

        // Update staking pool information
        staking_pool.total_rewards -= rewards;

        Ok(())
    }
}

// Define errors
#[error]
pub enum StakingPoolError {
    #[msg("Insufficient tokens")]
    InsufficientTokens,
    #[msg("Insufficient stake")]
    InsufficientStake,
    #[msg("Insufficient rewards")]
    InsufficientRewards,
}

// Define accounts for Initialize
#[account]
pub struct InitializeAccounts {
    #[account(init, payer = authority, space = 8 + 32 + 32 + 32 + 32 + 8 + 8 + 8)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub reward_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

// Define accounts for Stake
#[account]
pub struct StakeAccounts {
    #[account(mut, has_one = authority)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(init, payer = user, space = 8 + 32 + 32 + 8)]
    pub staker: Account<'info, Staker>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

// Define accounts for Unstake
#[account]
pub struct UnstakeAccounts {
    #[account(mut, has_one = authority)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut, has_one = staking_pool)]
    pub staker: Account<'info, Staker>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define accounts for Claim
#[account]
pub struct ClaimAccounts {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    pub staker: Account<'info, Staker>,
    pub reward_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// CPI context for Initialize
#[cpi]
pub struct InitializeCpi<'info> {
    pub staking_pool: Account<'info, StakingPool>,
    pub authority: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub reward_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

// CPI context for Stake
#[cpi]
pub struct StakeCpi<'info> {
    pub staking_pool: Account<'info, StakingPool>,
    pub staker: Account<'info, Staker>,
    pub user: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// CPI context for Unstake
#[cpi]
pub struct UnstakeCpi<'info> {
    pub staking_pool: Account<'info, StakingPool>,
    pub staker: Account<'info, Staker>,
    pub user: Signer<'info>,
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// CPI context for Claim
#[cpi]
pub struct ClaimCpi<'info> {
    pub staking_pool: Account<'info, StakingPool>,
    pub staker: Account<'info, Staker>,
    pub reward_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}
```
