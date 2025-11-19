"""
Generated Code Metadata:
========================
Original URL: https://deqodsmeta.web.app
Prompt: Generate a smart contract code in Rust for staking DeGods and earning $DUST tokens on the Solana blockchain.
Generated: DETERMINISTIC_068e8e13bdd8abb1
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod degods_staking {
    use super::*;

    // Initialize the staking account
    pub fn initialize_staking(ctx: Context<InitializeStaking>, reward_rate: u64) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        staking_account.reward_rate = reward_rate;
        staking_account.last_update_time = Clock::get()?.unix_timestamp;
        staking_account.total_staked = 0;
        Ok(())
    }

    // Stake DeGods NFT
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        let user_account = &mut ctx.accounts.user_account;

        // Transfer DeGods NFT to the staking account
        token::transfer(
            ctx.accounts.into_transfer_context(),
            amount,
        )?;

        // Update staking account state
        staking_account.total_staked += amount;
        user_account.staked_amount += amount;
        user_account.last_staked_time = Clock::get()?.unix_timestamp;

        Ok(())
    }

    // Claim $DUST rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        let user_account = &mut ctx.accounts.user_account;

        // Calculate rewards
        let current_time = Clock::get()?.unix_timestamp;
        let staking_duration = current_time - user_account.last_staked_time;
        let rewards = staking_duration as u64 * staking_account.reward_rate * user_account.staked_amount;

        // Transfer $DUST tokens to the user
        token::transfer(
            ctx.accounts.into_transfer_context(),
            rewards,
        )?;

        // Update user account state
        user_account.last_staked_time = current_time;

        Ok(())
    }

    // Unstake DeGods NFT
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        let user_account = &mut ctx.accounts.user_account;

        require!(user_account.staked_amount >= amount, StakingError::InsufficientStakedAmount);

        // Transfer DeGods NFT back to the user
        token::transfer(
            ctx.accounts.into_transfer_context(),
            amount,
        )?;

        // Update staking account state
        staking_account.total_staked -= amount;
        user_account.staked_amount -= amount;

        Ok(())
    }
}

// Define the accounts structure
#[derive(Accounts)]
pub struct InitializeStaking<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8 + 8)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub reward_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the staking account structure
#[account]
pub struct StakingAccount {
    pub reward_rate: u64,          // Reward rate per second per staked token
    pub last_update_time: i64,    // Last time the staking account was updated
    pub total_staked: u64,        // Total amount of tokens staked
}

// Define the user account structure
#[account]
pub struct UserAccount {
    pub staked_amount: u64,       // Amount of tokens staked by the user
    pub last_staked_time: i64,    // Last time the user staked tokens
}

// Define custom errors
#[error_code]
pub enum StakingError {
    #[msg("Insufficient staked amount.")]
    InsufficientStakedAmount,
}

// Helper functions for token transfer context
impl<'info> Stake<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, Transfer<'info>> {
        let cpi_accounts = Transfer {
            from: self.user_token_account.to_account_info(),
            to: self.staking_token_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

impl<'info> ClaimRewards<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, Transfer<'info>> {
        let cpi_accounts = Transfer {
            from: self.staking_token_account.to_account_info(),
            to: self.reward_token_account.to_account_info(),
            authority: self.staking_account.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

impl<'info> Unstake<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, Transfer<'info>> {
        let cpi_accounts = Transfer {
            from: self.staking_token_account.to_account_info(),
            to: self.user_token_account.to_account_info(),
            authority: self.staking_account.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
