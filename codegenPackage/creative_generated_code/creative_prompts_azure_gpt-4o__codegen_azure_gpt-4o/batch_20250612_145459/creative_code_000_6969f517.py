"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Write a Solana-based smart contract for a staking platform that distributes rewards every epoch (≈2 days) at a rate of 0.3836% per epoch, with a reward cap strategy limiting individual rewards to 5% of the total staking pool.
Generated: DETERMINISTIC_6969f5173e88cc21
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

// Declare the program ID
declare_id!("StakingPlatform1111111111111111111111111111111");

#[program]
pub mod staking_platform {
    use super::*;

    const REWARD_RATE: f64 = 0.003836; // 0.3836% per epoch
    const MAX_REWARD_PERCENT: f64 = 0.05; // 5% of the total staking pool

    pub fn initialize_staking_pool(
        ctx: Context<InitializeStakingPool>,
        reward_mint: Pubkey,
        staking_pool_authority: Pubkey,
    ) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        staking_pool.total_staked = 0;
        staking_pool.reward_mint = reward_mint;
        staking_pool.staking_pool_authority = staking_pool_authority;
        staking_pool.last_reward_time = Clock::get()?.unix_timestamp;
        Ok(())
    }

    pub fn stake_tokens(ctx: Context<StakeTokens>, amount: u64) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let user_info = &mut ctx.accounts.user_info;

        // Transfer tokens from user's wallet to staking pool
        token::transfer(
            ctx.accounts.into_stake_context(),
            amount,
        )?;

        // Update staking pool and user stakes
        staking_pool.total_staked += amount;
        user_info.staked_amount += amount;
        Ok(())
    }

    pub fn distribute_rewards(ctx: Context<DistributeRewards>) -> Result<()> {
        let staking_pool = &mut ctx.accounts.staking_pool;
        let clock = Clock::get()?;

        // Ensure enough time has passed for an epoch
        let time_diff = clock.unix_timestamp - staking_pool.last_reward_time;
        require!(time_diff >= 2 * 24 * 60 * 60, CustomError::EpochNotElapsed);

        let total_staked = staking_pool.total_staked;
        let reward_mint_supply = ctx.accounts.reward_mint.supply;

        // Calculate rewards for each user
        for user_info in &mut ctx.remaining_accounts {
            let user_staked = user_info
                .try_borrow_data()?
                .staked_amount;

            let mut reward = (user_staked as u##
``
