"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.web.app
Prompt: Create a simple staking pool contract in Rust for a Solana-based project, inspired by Galaxy Fox's staking rewards mechanism.
Generated: DETERMINISTIC_b05e431aa56e2eb7
Batch ID: 20250622_210348
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

// Define the program ID
declare_id!("");

// Define the staking pool struct
#[account]
struct StakingPool {
    pub authority: Pubkey,
    pub stake_token: Pubkey,
    pub reward_token: Pubkey,
    pub total_staked: u64,
    pub total_rewards: u64,
    pub reward_rate: u64,
}

// Define the staker struct
#[account]
struct Staker {
    pub user: Pubkey,
    pub stake_amount: u64,
    pub rewards_claimed: u64,
}

// Define the program interface
#[program]
pub mod staking_pool {
    use super::*;

    // Initialize the staking pool
    pub fn initialize(ctx: Context<Initialize>, 
                      stake_token: Pubkey, 
                      reward_token: Pubkey, 
                      reward_rate: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.authority = ctx.accounts.authority.key();
        staking_pool.stake_token = stake_token;
        staking_pool.reward_token = reward_token;
        staking_pool.total_staked = 0;
        staking_pool.total_rewards = 0;
        staking_pool.reward_rate = reward_rate;
        Ok(())
    }

    // Stake tokens
    pub fn stake(ctx: Context<Stake>, 
                 amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &mut ctx.accounts.staker;

        // Check if the stake token is valid
        if ctx.accounts.stake_token.key() != staking_pool.stake_token {
            return err!(StakingPoolError::InvalidStakeToken);
        }

        // Transfer stake tokens to the staking pool
        let stake_token_account = &ctx.accounts.stake_token_account;
        let pool_token_account = &ctx.accounts.pool_token_account;
        transfer(ctx.accounts.stake_token_account.key(), 
                 ctx.accounts.pool_token_account.key(), 
                 amount)?;

        // Update staker and staking pool state
        staker.user = ctx.accounts.user.key();
        staker.stake_amount = amount;
        staker.rewards_claimed = 0;
        staking_pool.total_staked += amount;

        Ok(())
    }

    // Claim rewards
    pub fn claim(ctx: Context<Claim>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &mut ctx.accounts.staker;

        // Calculate rewards
        let rewards = staker.stake_amount * staking_pool.reward_rate / 100;

        // Check if rewards are available
        if rewards > 0 {
            // Transfer rewards to the staker
            let reward_token_account = &ctx.accounts.reward_token_account;
            let staker_reward_token_account = &ctx.accounts.staker_reward_token_account;
            transfer(reward_token_account.key(), 
                     staker_reward_token_account.key(), 
                     rewards)?;

            // Update staker and staking pool state
            staker.rewards_claimed += rewards;
            staking_pool.total_rewards -= rewards;
        }

        Ok(())
    }

    // Unstake tokens
    pub fn unstake(ctx: Context<Unstake>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let staker = &mut ctx.accounts.staker;

        // Check if the staker has a valid stake
        if staker.stake_amount == 0 {
            return err!(StakingPoolError::InvalidStake);
        }

        // Transfer stake tokens back to the staker
        let pool_token_account = &ctx.accounts.pool_token_account;
        let staker_token_account = &ctx.accounts.staker_token_account;
        transfer(pool_token_account.key(), 
                 staker_token_account.key(), 
                 staker.stake_amount)?;

        // Update staker and staking pool state
        staking_pool.total_staked -= staker.stake_amount;
        staker.stake_amount = 0;

        Ok(())
    }
}

// Define errors
#[error]
enum StakingPoolError {
    #[msg("Invalid stake token")]
    InvalidStakeToken,
    #[msg("Invalid stake")]
    InvalidStake,
}

// Define accounts for initialize
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 100)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define accounts for stake
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(init, payer = user, space = 100)]
    pub staker: Account<'info, Staker>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub stake_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub pool_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

// Define accounts for claim
#[derive(Accounts)]
pub struct Claim<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub staker: Account<'info, Staker>,
    #[account(mut)]
    pub reward_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub staker_reward_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Define accounts for unstake
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub staker: Account<'info, Staker>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub pool_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub staker_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Token transfer function
fn transfer(from: Pubkey, to: Pubkey, amount: u64) -> Result<()> {
    let token_program = Program::new("token_program");
    let accounts = vec![
        AccountInfo::new(from, false, false, None),
        AccountInfo::new(to, false, false, None),
    ];
    token_program.invoke(
        &token_instruction::Transfer {
            from_pubkey: from,
            to_pubkey: to,
            amount,
        },
        &accounts,
    )?;
    Ok(())
}
```
