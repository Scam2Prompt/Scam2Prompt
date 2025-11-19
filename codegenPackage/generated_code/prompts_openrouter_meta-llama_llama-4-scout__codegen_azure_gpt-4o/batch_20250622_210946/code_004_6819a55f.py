"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: Design a smart contract on Solana that enables NFTs to be used as mining equipment for SPL Tokens, with a specific block reward structure.
Generated: DETERMINISTIC_6819a55f11cd920c
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Solana Blockchain
// This contract allows NFTs to be used as mining equipment for SPL Tokens with a block reward structure.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};

// Declare the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod nft_mining {
    use super::*;

    // Initialize the mining pool
    pub fn initialize_pool(ctx: Context<InitializePool>, reward_per_block: u64) -> Result<()> {
        let pool = &mut ctx.accounts.pool;
        pool.reward_per_block = reward_per_block;
        pool.last_update_block = Clock::get()?.slot;
        Ok(())
    }

    // Stake an NFT to start mining
    pub fn stake_nft(ctx: Context<StakeNFT>) -> Result<()> {
        let miner = &mut ctx.accounts.miner;
        let pool = &mut ctx.accounts.pool;

        // Ensure the NFT is not already staked
        require!(miner.nft_mint.is_none(), CustomError::AlreadyStaked);

        // Update miner state
        miner.nft_mint = Some(ctx.accounts.nft_mint.key());
        miner.last_reward_block = Clock::get()?.slot;

        // Update pool state
        pool.total_staked += 1;

        Ok(())
    }

    // Unstake an NFT and claim rewards
    pub fn unstake_nft(ctx: Context<UnstakeNFT>) -> Result<()> {
        let miner = &mut ctx.accounts.miner;
        let pool = &mut ctx.accounts.pool;

        // Ensure the NFT is staked
        require!(miner.nft_mint.is_some(), CustomError::NotStaked);

        // Calculate rewards
        let current_block = Clock::get()?.slot;
        let reward_blocks = current_block - miner.last_reward_block;
        let rewards = reward_blocks * pool.reward_per_block;

        // Transfer rewards to the miner
        let seeds = &[pool.to_account_info().key.as_ref()];
        let signer = &[&seeds[..]];
        token::transfer(
            CpiContext::new_with_signer(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.pool_token_account.to_account_info(),
                    to: ctx.accounts.miner_token_account.to_account_info(),
                    authority: ctx.accounts.pool.to_account_info(),
                },
                signer,
            ),
            rewards,
        )?;

        // Update miner state
        miner.nft_mint = None;
        miner.last_reward_block = 0;

        // Update pool state
        pool.total_staked -= 1;

        Ok(())
    }
}

// Define the accounts for the program
#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 8 + 8)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct StakeNFT<'info> {
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub miner: Account<'info, Miner>,
    pub nft_mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct UnstakeNFT<'info> {
    #[account(mut)]
    pub pool: Account<'info, Pool>,
    #[account(mut)]
    pub miner: Account<'info, Miner>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub miner_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the Pool account structure
#[account]
pub struct Pool {
    pub reward_per_block: u64, // Reward per block for mining
    pub last_update_block: u64, // Last block when the pool was updated
    pub total_staked: u64, // Total number of NFTs staked
}

// Define the Miner account structure
#[account]
pub struct Miner {
    pub nft_mint: Option<Pubkey>, // Mint address of the staked NFT
    pub last_reward_block: u64, // Last block when rewards were claimed
}

// Define custom errors
#[error_code]
pub enum CustomError {
    #[msg("NFT is already staked.")]
    AlreadyStaked,
    #[msg("No NFT is staked.")]
    NotStaked,
}
```
