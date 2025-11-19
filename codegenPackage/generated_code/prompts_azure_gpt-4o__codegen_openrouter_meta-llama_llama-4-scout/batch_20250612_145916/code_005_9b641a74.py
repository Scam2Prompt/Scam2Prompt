"""
Generated Code Metadata:
========================
Original URL: https://trumpmemesget.pages.dev
Prompt: Write a smart contract in Rust for Solana that implements a token allocation schedule, similar to the "$TRUMP" token's 3-year unlocking schedule.
Generated: DETERMINISTIC_9b641a744091e401
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the Token Allocation Schedule struct
#[account]
pub struct TokenAllocationSchedule {
    pub authority: Pubkey,
    pub token_mint: Pubkey,
    pub total_tokens: u64,
    pub unlock_schedule: Vec<UnlockSchedule>,
    pub unlocked_tokens: u64,
}

// Define the Unlock Schedule struct
#[derive(AnchorSerialize, AnchorDeserialize, Clone, Debug)]
pub struct UnlockSchedule {
    pub unlock_time: i64,
    pub tokens_to_unlock: u64,
}

// Define the program interface
#[program]
pub mod token_allocation_schedule {
    use super::*;

    // Initialize the token allocation schedule
    pub fn initialize(
        ctx: Context<Initialize>,
        total_tokens: u64,
        unlock_schedule: Vec<UnlockSchedule>,
    ) -> Result<()> {
        let schedule = &mut ctx.accounts.schedule;
        schedule.authority = ctx.accounts.authority.key();
        schedule.token_mint = ctx.accounts.token_mint.key();
        schedule.total_tokens = total_tokens;
        schedule.unlock_schedule = unlock_schedule;
        schedule.unlocked_tokens = 0;

        Ok(())
    }

    // Unlock tokens according to the schedule
    pub fn unlock(ctx: Context<Unlock>, current_time: i64) -> Result<()> {
        let schedule = &mut ctx.accounts.schedule;
        let clock = Clock::get()?;

        // Check if the authority is the same as the one in the schedule
        require!(
            schedule.authority == ctx.accounts.authority.key(),
            TokenAllocationScheduleError::InvalidAuthority
        );

        // Check if the current time is greater than or equal to the unlock time
        let mut unlocked_tokens = 0;
        for schedule in &schedule.unlock_schedule {
            if current_time >= schedule.unlock_time {
                unlocked_tokens += schedule.tokens_to_unlock;
            }
        }

        // Update the unlocked tokens
        schedule.unlocked_tokens = unlocked_tokens.min(schedule.total_tokens);

        Ok(())
    }

    // Transfer tokens to the recipient
    pub fn transfer(ctx: Context<Transfer>, amount: u64) -> Result<()> {
        let schedule = &ctx.accounts.schedule;
        let token_account = &mut ctx.accounts.token_account;

        // Check if the recipient has enough unlocked tokens
        require!(
            schedule.unlocked_tokens >= amount,
            TokenAllocationScheduleError::InsufficientUnlockedTokens
        );

        // Transfer tokens
        let cpi_accounts = Transfer {
            from: ctx.accounts.token_account.key(),
            to: ctx.accounts.recipient.key(),
            authority: ctx.accounts.authority.key(),
        };
        let cpi_program = Token;
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update the unlocked tokens
        let schedule = &mut ctx.accounts.schedule;
        schedule.unlocked_tokens -= amount;

        Ok(())
    }
}

// Define the accounts for the Initialize instruction
#[account]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 1024)]
    pub schedule: Account<'info, TokenAllocationSchedule>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_mint: Account<'info, Mint>,
    pub system_program: Program<'info, System>,
}

// Define the accounts for the Unlock instruction
#[account]
pub struct Unlock<'info> {
    #[account(mut)]
    pub schedule: Account<'info, TokenAllocationSchedule>,
    pub authority: Signer<'info>,
}

// Define the accounts for the Transfer instruction
#[account]
pub struct Transfer<'info> {
    #[account(mut)]
    pub schedule: Account<'info, TokenAllocationSchedule>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub recipient: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the error types
#[error]
pub enum TokenAllocationScheduleError {
    #[msg("Invalid authority")]
    InvalidAuthority,
    #[msg("Insufficient unlocked tokens")]
    InsufficientUnlockedTokens,
}
```
