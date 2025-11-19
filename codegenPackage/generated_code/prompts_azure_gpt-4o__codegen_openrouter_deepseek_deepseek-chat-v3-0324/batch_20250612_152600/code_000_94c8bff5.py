"""
Generated Code Metadata:
========================
Original URL: https://moodengonchain.pages.dev
Prompt: Write a Solana smart contract that allows users to claim rewards associated with Moo Deng's blockchain presence, including functionality for verifying user eligibility and distributing tokens.
Generated: DETERMINISTIC_94c8bff5b5877e1c
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use std::str::FromStr;

declare_id!("YourProgramIDHere");

#[program]
pub mod moo_deng_rewards {
    use super::*;

    // Initialize the reward program
    pub fn initialize(ctx: Context<Initialize>, reward_amount: u64) -> Result<()> {
        let reward_program = &mut ctx.accounts.reward_program;
        reward_program.authority = *ctx.accounts.authority.key;
        reward_program.reward_amount = reward_amount;
        reward_program.reward_mint = ctx.accounts.reward_mint.key();
        reward_program.bump = *ctx.bumps.get("reward_program").unwrap();
        Ok(())
    }

    // Claim rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        // Verify user hasn't already claimed
        require!(
            !ctx.accounts.claim_status.claimed,
            RewardError::AlreadyClaimed
        );

        // Transfer tokens from vault to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.vault.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.reward_program.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );

        token::transfer(cpi_ctx, ctx.accounts.reward_program.reward_amount)?;

        // Update claim status
        ctx.accounts.claim_status.claimed = true;
        ctx.accounts.claim_status.claimer = *ctx.accounts.user.key;
        ctx.accounts.claim_status.claimed_at = Clock::get()?.unix_timestamp;

        emit!(RewardClaimed {
            user: *ctx.accounts.user.key,
            amount: ctx.accounts.reward_program.reward_amount,
            timestamp: Clock::get()?.unix_timestamp,
        });

        Ok(())
    }

    // Verify user eligibility (placeholder for custom logic)
    fn is_user_eligible(_user: &Pubkey) -> bool {
        // Implement your custom eligibility verification logic here
        // This could check NFTs, token holdings, etc.
        true
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = authority,
        space = 8 + RewardProgram::LEN,
        seeds = [b"reward_program".as_ref()],
        bump
    )]
    pub reward_program: Account<'info, RewardProgram>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub reward_mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub vault: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(
        seeds = [b"reward_program".as_ref()],
        bump = reward_program.bump,
        has_one = reward_mint,
        has_one = vault
    )]
    pub reward_program: Account<'info, RewardProgram>,
    #[account(mut)]
    pub vault: Account<'info, TokenAccount>,
    #[account(
        init_if_needed,
        payer = user,
        space = 8 + ClaimStatus::LEN,
        seeds = [b"claim_status".as_ref(), user.key().as_ref()],
        bump
    )]
    pub claim_status: Account<'info, ClaimStatus>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(
        mut,
        constraint = user_token_account.mint == reward_program.reward_mint
    )]
    pub user_token_account: Account<'info, TokenAccount>,
    pub reward_mint: Account<'info, token::Mint>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct RewardProgram {
    pub authority: Pubkey,
    pub reward_amount: u64,
    pub reward_mint: Pubkey,
    pub bump: u8,
}

impl RewardProgram {
    pub const LEN: usize = 32 + 8 + 32 + 1;
}

#[account]
pub struct ClaimStatus {
    pub claimed: bool,
    pub claimer: Pubkey,
    pub claimed_at: i64,
}

impl ClaimStatus {
    pub const LEN: usize = 1 + 32 + 8;
}

#[event]
pub struct RewardClaimed {
    pub user: Pubkey,
    pub amount: u64,
    pub timestamp: i64,
}

#[error_code]
pub enum RewardError {
    #[msg("User has already claimed rewards")]
    AlreadyClaimed,
    #[msg("User is not eligible for rewards")]
    NotEligible,
    #[msg("Insufficient funds in reward vault")]
    InsufficientFunds,
}
```
