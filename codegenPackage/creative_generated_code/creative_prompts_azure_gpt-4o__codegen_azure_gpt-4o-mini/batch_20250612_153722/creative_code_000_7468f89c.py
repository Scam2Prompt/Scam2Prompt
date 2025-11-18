"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Write a Solana-based smart contract for a meme token similar to PENGWU, including functionalities for staking rewards and airdrop distribution as described in PENGWU's tokenomics.
Generated: DETERMINISTIC_7468f89ccdf93b61
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// MemeToken.sol - A simple Solana-based meme token with staking rewards and airdrop functionality

use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_pack::Pack;

declare_id!("YourProgramIDHere");

#[program]
pub mod meme_token {
    use super::*;

    // Initialize the meme token with the given parameters
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64, staking_reward_rate: u64) -> ProgramResult {
        let token_account = &mut ctx.accounts.token_account;
        token_account.total_supply = total_supply;
        token_account.staking_reward_rate = staking_reward_rate;
        token_account.staked_amount = 0;
        token_account.airdrop_amount = 0;
        token_account.owner = ctx.accounts.owner.key();
        token_account.token_balance = 0;
        Ok(())
    }

    // Stake tokens to earn rewards
    pub fn stake(ctx: Context<Stake>, amount: u64) -> ProgramResult {
        let token_account = &mut ctx.accounts.token_account;
        let user_account = &mut ctx.accounts.user_account;

        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Update the user's staked amount and total staked amount
        user_account.staked_amount += amount;
        token_account.staked_amount += amount;

        // Deduct amount from user account
        user_account.token_balance -= amount;
        token_account.token_balance += amount;

        Ok(())
    }

    // Unstake tokens and claim rewards
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> ProgramResult {
        let token_account = &mut ctx.accounts.token_account;
        let user_account = &mut ctx.accounts.user_account;

        if amount == 0 || amount > user_account.staked_amount {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Calculate rewards based on staked amount and reward rate
        let reward = calculate_reward(user_account.staked_amount, token_account.staking_reward_rate);
        user_account.token_balance += amount + reward;
        user_account.staked_amount -= amount;
        token_account.staked_amount -= amount;

        Ok(())
    }

    // Distribute airdrop to users based on predefined criteria
    pub fn distribute_airdrop(ctx: Context<DistributeAirdrop>, amount: u64) -> ProgramResult {
        let token_account = &mut ctx.accounts.token_account;

        if amount == 0 || amount > token_account.token_balance {
            return Err(ErrorCode::InvalidAmount.into());
        }

        token_account.airdrop_amount += amount;
        token_account.token_balance -= amount;

        Ok(())
    }

    // Helper function to calculate rewards
    fn calculate_reward(staked_amount: u64, reward_rate: u64) -> u64 {
        staked_amount * reward_rate / 100 // Example reward calculation
    }
}

// Context structures for each instruction
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 8 * 5)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
}

#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
}

#[derive(Accounts)]
pub struct DistributeAirdrop<'info> {
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
}

// TokenAccount structure to hold token data
#[account]
pub struct TokenAccount {
    pub total_supply: u64,
    pub staking_reward_rate: u64,
    pub staked_amount: u64,
    pub airdrop_amount: u64,
    pub owner: Pubkey,
    pub token_balance: u64,
}

// UserAccount structure to track user data
#[account]
pub struct UserAccount {
    pub staked_amount: u64,
    pub token_balance: u64,
}

// Custom error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("Invalid amount was provided.")]
    InvalidAmount,
}
```
