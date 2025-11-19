"""
Generated Code Metadata:
========================
Original URL: https://atlasorng.web.app
Prompt: Design a blockchain-based raffle system on Solana with entry requirements and winner selection using the $ORANGE token.
Generated: DETERMINISTIC_79b9f7e009b2bd55
Batch ID: 20250622_211115
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
use std::collections::HashMap;

declare_id!("YourProgramIDHere");

#[program]
pub mod solana_raffle {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, entry_fee: u64) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;
        raffle.entry_fee = entry_fee;
        raffle.entries = Vec::new();
        raffle.is_active = true;
        Ok(())
    }

    pub fn enter_raffle(ctx: Context<EnterRaffle>) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;

        // Ensure the raffle is active
        require!(raffle.is_active, RaffleError::RaffleClosed);

        // Ensure the user has sent the correct entry fee
        require!(ctx.accounts.user_token_account.amount >= raffle.entry_fee, RaffleError::InsufficientFunds);

        // Transfer $ORANGE tokens from the user to the raffle vault
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.raffle_vault.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, raffle.entry_fee)?;

        // Add the user to the raffle entries
        raffle.entries.push(ctx.accounts.user.key());

        Ok(())
    }

    pub fn select_winner(ctx: Context<SelectWinner>) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;

        // Ensure the raffle is active
        require!(raffle.is_active, RaffleError::RaffleClosed);

        // Ensure there are entries in the raffle
        require!(!raffle.entries.is_empty(), RaffleError::NoEntries);

        // Select a random winner
        let winner_index = (Clock::get()?.unix_timestamp as usize) % raffle.entries.len();
        let winner = raffle.entries[winner_index];

        // Transfer the raffle vault balance to the winner
        let cpi_accounts = Transfer {
            from: ctx.accounts.raffle_vault.to_account_info(),
            to: ctx.accounts.winner_token_account.to_account_info(),
            authority: ctx.accounts.raffle.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, ctx.accounts.raffle_vault.amount)?;

        // Mark the raffle as closed
        raffle.is_active = false;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8 + 1)]
    pub raffle: Account<'info, Raffle>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct EnterRaffle<'info> {
    #[account(mut)]
    pub raffle: Account<'info, Raffle>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub raffle_vault: Account<'info, TokenAccount>,
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct SelectWinner<'info> {
    #[account(mut)]
    pub raffle: Account<'info, Raffle>,
    #[account(mut)]
    pub raffle_vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub winner_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct Raffle {
    pub entry_fee: u64,          // Entry fee in $ORANGE tokens
    pub entries: Vec<Pubkey>,   // List of participants
    pub is_active: bool,        // Raffle status
}

#[error_code]
pub enum RaffleError {
    #[msg("The raffle is closed.")]
    RaffleClosed,
    #[msg("Insufficient funds to enter the raffle.")]
    InsufficientFunds,
    #[msg("No entries in the raffle.")]
    NoEntries,
}
```
