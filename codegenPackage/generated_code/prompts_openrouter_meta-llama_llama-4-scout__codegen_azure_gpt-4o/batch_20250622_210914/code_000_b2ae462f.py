"""
Generated Code Metadata:
========================
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: "Write a smart contract for a token lockup mechanism with a flexible vesting schedule on Solana."
Generated: DETERMINISTIC_b2ae462fbf150aae
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Token Lockup Mechanism with Flexible Vesting Schedule on Solana

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod token_lockup {
    use super::*;

    // Initialize the vesting schedule
    pub fn initialize_vesting(
        ctx: Context<InitializeVesting>,
        beneficiary: Pubkey,
        total_amount: u64,
        start_time: i64,
        cliff_duration: i64,
        vesting_duration: i64,
    ) -> Result<()> {
        let vesting_account = &mut ctx.accounts.vesting_account;
        vesting_account.beneficiary = beneficiary;
        vesting_account.total_amount = total_amount;
        vesting_account.start_time = start_time;
        vesting_account.cliff_duration = cliff_duration;
        vesting_account.vesting_duration = vesting_duration;
        vesting_account.released_amount = 0;

        Ok(())
    }

    // Release vested tokens to the beneficiary
    pub fn release_tokens(ctx: Context<ReleaseTokens>) -> Result<()> {
        let vesting_account = &mut ctx.accounts.vesting_account;
        let current_time = Clock::get()?.unix_timestamp;

        // Ensure the vesting has started
        require!(
            current_time >= vesting_account.start_time,
            VestingError::VestingNotStarted
        );

        // Calculate the vested amount
        let elapsed_time = current_time - vesting_account.start_time;
        let vested_amount = if elapsed_time < vesting_account.cliff_duration {
            0
        } else if elapsed_time >= vesting_account.vesting_duration {
            vesting_account.total_amount
        } else {
            (vesting_account.total_amount as i128 * elapsed_time as i128
                / vesting_account.vesting_duration as i128) as u64
        };

        let releasable_amount = vested_amount.saturating_sub(vesting_account.released_amount);

        // Ensure there are tokens to release
        require!(releasable_amount > 0, VestingError::NoTokensToRelease);

        // Transfer tokens to the beneficiary
        let cpi_accounts = Transfer {
            from: ctx.accounts.vault.to_account_info(),
            to: ctx.accounts.beneficiary_token_account.to_account_info(),
            authority: ctx.accounts.vault_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let seeds = &[vesting_account.to_account_info().key.as_ref()];
        let signer = &[&seeds[..]];
        token::transfer(CpiContext::new_with_signer(
            cpi_program,
            cpi_accounts,
            signer,
        ), releasable_amount)?;

        // Update the released amount
        vesting_account.released_amount += releasable_amount;

        Ok(())
    }
}

// Context for initializing vesting
#[derive(Accounts)]
pub struct InitializeVesting<'info> {
    #[account(init, payer = payer, space = 8 + VestingAccount::LEN)]
    pub vesting_account: Account<'info, VestingAccount>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for releasing tokens
#[derive(Accounts)]
pub struct ReleaseTokens<'info> {
    #[account(mut)]
    pub vesting_account: Account<'info, VestingAccount>,
    #[account(mut)]
    pub vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub beneficiary_token_account: Account<'info, TokenAccount>,
    pub vault_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Vesting account structure
#[account]
pub struct VestingAccount {
    pub beneficiary: Pubkey,       // Beneficiary of the tokens
    pub total_amount: u64,         // Total amount of tokens to be vested
    pub start_time: i64,           // Start time of the vesting schedule
    pub cliff_duration: i64,       // Cliff duration in seconds
    pub vesting_duration: i64,     // Total vesting duration in seconds
    pub released_amount: u64,      // Amount of tokens already released
}

impl VestingAccount {
    const LEN: usize = 32 + 8 + 8 + 8 + 8 + 8; // Size of the VestingAccount structure
}

// Custom errors for the program
#[error_code]
pub enum VestingError {
    #[msg("Vesting has not started yet.")]
    VestingNotStarted,
    #[msg("No tokens available for release.")]
    NoTokensToRelease,
}
```
