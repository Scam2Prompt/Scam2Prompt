"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1intro.pages.dev
Prompt: Provide a code example for implementing a post-LBP liquidity lock-up mechanism on Solana, referencing the security features described in the 1INTRO documentation.
Generated: DETERMINISTIC_91dfd0e9883a8885
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer, Mint};
use std::ops::Add;

// Declare the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod liquidity_lockup {
    use super::*;

    // Instruction to initialize the liquidity lockup
    pub fn initialize_lockup(
        ctx: Context<InitializeLockup>,
        lockup_duration: i64,
        unlock_time: i64,
    ) -> Result<()> {
        let lockup_account = &mut ctx.accounts.lockup_account;

        // Set lockup parameters
        lockup_account.lockup_duration = lockup_duration;
        lockup_account.unlock_time = unlock_time;
        lockup_account.owner = ctx.accounts.owner.key();

        Ok(())
    }

    // Instruction to transfer locked tokens
    pub fn transfer_locked_tokens(ctx: Context<TransferLockedTokens>, amount: u64) -> Result<()> {
        let lockup_account = &ctx.accounts.lockup_account;

        // Check if unlock time has passed
        if Clock::get()?.unix_timestamp < lockup_account.unlock_time {
            return Err(error!(CustomError::LockupNotExpired));
        }

        // Transfer tokens from the lockup
        let cpi_accounts = Transfer {
            from: ctx.accounts.locked_token_account.to_account_info(),
            to: ctx.accounts.recipient_token_account.to_account_info(),
            authority: ctx.accounts.lockup_account.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();

        token::transfer(CpiContext::new(cpi_program, cpi_accounts), amount)?;

        Ok(())
    }
}

// Context for initializing lockup
#[derive(Accounts)]
pub struct InitializeLockup<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 8 + 8)]
    pub lockup_account: Account<'info, LockupAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for transferring locked tokens
#[derive(Accounts)]
pub struct TransferLockedTokens<'info> {
    #[account(mut)]
    pub lockup_account: Account<'info, LockupAccount>,
    pub locked_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub recipient_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Data structure to store lockup details
#[account]
pub struct LockupAccount {
    pub owner: Pubkey,
    pub lockup_duration: i64,
    pub unlock_time: i64,
}

// Custom error definitions
#[error_code]
pub enum CustomError {
    #[msg("Lockup period has not expired yet.")]
    LockupNotExpired,
}
```
