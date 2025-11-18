"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scream-buy.pages.dev
Prompt: Write a smart contract on Solana that supports staking $SCREAM tokens and implements a voting utility for stakers as described in the roadmap.
Generated: DETERMINISTIC_f58641a92b89754d
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program struct
#[program]
mod scream_staking {
    use super::*;

    // Initialize the staking contract
    pub fn initialize(ctx: Context<Initialize>, token_mint: Pubkey) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        staking_account.token_mint = token_mint;
        staking_account.total_staked = 0;
        Ok(())
    }

    // Function to stake tokens
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        let staker = &mut ctx.accounts.staker;

        // Validate the amount to stake
        require!(amount > 0, StakeError::InvalidAmount);

        // Update staker's balance and total staked
        staker.amount_staked += amount;
        staking_account.total_staked += amount;

        // Transfer tokens from staker's account to the staking account
        let cpi_accounts = spl_token::Transfer {
            from: ctx.accounts.staker_token_account.to_account_info(),
            to: ctx.accounts.staking_token_account.to_account_info(),
            authority: ctx.accounts.staker.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Perform the token transfer
        spl_token::transfer(cpi_ctx, amount)?;

        Ok(())
    }

    // Function to unstake tokens
    pub fn unstake(ctx: Context<Unstake>, amount: u64) -> Result<()> {
        let staking_account = &mut ctx.accounts.staking_account;
        let staker = &mut ctx.accounts.staker;

        // Validate the amount to unstake
        require!(amount > 0 && amount <= staker.amount_staked, StakeError::InvalidAmount);

        // Update staker's balance and total staked
        staker.amount_staked -= amount;
        staking_account.total_staked -= amount;

        // Transfer tokens from staking account back to the staker's account
        let cpi_accounts = spl_token::Transfer {
            from: ctx.accounts.staking_token_account.to_account_info(),
            to: ctx.accounts.staker_token_account.to_account_info(),
            authority: ctx.accounts.staking_account.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Perform the token transfer
        spl_token::transfer(cpi_ctx, amount)?;

        Ok(())
    }

    // Function for voting by stakers
    pub fn vote(ctx: Context<Vote>, proposal_id: u64, support: bool) -> Result<()> {
        let staker = &mut ctx.accounts.staker;

        // Ensure the staker has staked tokens
        require!(staker.amount_staked > 0, StakeError::NotStaking);

        // Record the vote
        let vote = Vote {
            proposal_id,
            support,
            staker: *ctx.accounts.staker.key,
        };

        ctx.accounts.voting_account.votes.push(vote);

        Ok(())
    }
}

// Define accounts used in the context for staking
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub rent: Sysvar<'info, Rent>,
}

// Define accounts used in the context for staking
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub staker: Signer<'info>,
    #[account(mut)]
    pub staker_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define accounts used in the context for unstaking
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub staker: Signer<'info>,
    #[account(mut)]
    pub staker_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub staking_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define accounts used in the context for voting
#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub voting_account: Account<'info, VotingAccount>,
    #[account(mut)]
    pub staker: Signer<'info>,
}

// Define the staking account structure
#[account]
pub struct StakingAccount {
    pub token_mint: Pubkey,
    pub total_staked: u64,
}

// Define the voting account structure
#[account]
pub struct VotingAccount {
    pub votes: Vec<Vote>,
}

// Define the vote structure
#[derive(Clone)]
pub struct Vote {
    pub proposal_id: u64,
    pub support: bool,
    pub staker: Pubkey,
}

// Define possible errors for the staking contract
#[error]
pub enum StakeError {
    #[msg("Invalid staking amount.")]
    InvalidAmount,
    #[msg("Not currently staking.")]
    NotStaking,
}
```
