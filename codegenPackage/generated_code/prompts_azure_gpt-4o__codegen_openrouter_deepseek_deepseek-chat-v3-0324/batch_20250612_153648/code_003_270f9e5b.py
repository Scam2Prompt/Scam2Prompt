"""
Generated Code Metadata:
========================
Original URL: https://plugged.pages.dev
Prompt: Create a smart contract on Solana for a project launch, inspired by the "Plug" announcement page.
Generated: DETERMINISTIC_270f9e5b83691730
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};
use std::str::FromStr;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod project_launch {
    use super::*;

    // Initialize the project launch
    pub fn initialize(ctx: Context<Initialize>, name: String, symbol: String, uri: String) -> Result<()> {
        let project = &mut ctx.accounts.project;
        project.name = name;
        project.symbol = symbol;
        project.uri = uri;
        project.authority = *ctx.accounts.authority.key;
        project.bump = *ctx.bumps.get("project").unwrap();
        Ok(())
    }

    // Contribute to the project
    pub fn contribute(ctx: Context<Contribute>, amount: u64) -> Result<()> {
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.contributor_token_account.to_account_info(),
                to: ctx.accounts.project_token_account.to_account_info(),
                authority: ctx.accounts.contributor.to_account_info(),
            },
        );

        token::transfer(cpi_ctx, amount)?;

        let project = &mut ctx.accounts.project;
        project.total_contributions += amount;
        project.contributors += 1;

        emit!(ContributionEvent {
            contributor: *ctx.accounts.contributor.key,
            amount,
            timestamp: Clock::get()?.unix_timestamp,
        });

        Ok(())
    }

    // Withdraw funds from the project (only by authority)
    pub fn withdraw(ctx: Context<Withdraw>, amount: u64) -> Result<()> {
        require!(
            *ctx.accounts.authority.key == ctx.accounts.project.authority,
            ErrorCode::Unauthorized
        );

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.project_token_account.to_account_info(),
                to: ctx.accounts.authority_token_account.to_account_info(),
                authority: ctx.accounts.project.to_account_info(),
            },
        );

        token::transfer(cpi_ctx, amount)?;

        emit!(WithdrawalEvent {
            authority: *ctx.accounts.authority.key,
            amount,
            timestamp: Clock::get()?.unix_timestamp,
        });

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = authority,
        space = 8 + 32 + 32 + 256 + 8 + 8 + 1,
        seeds = [b"project", authority.key().as_ref()],
        bump
    )]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Contribute<'info> {
    #[account(mut, has_one = authority)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub contributor: Signer<'info>,
    #[account(mut)]
    pub contributor_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub project_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Withdraw<'info> {
    #[account(mut, has_one = authority)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub authority: Signer<'info>,
    #[account(mut)]
    pub authority_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub project_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct Project {
    pub name: String,               // Project name
    pub symbol: String,             // Project symbol
    pub uri: String,                // Project metadata URI
    pub authority: Pubkey,          // Project authority
    pub total_contributions: u64,   // Total contributions received
    pub contributors: u64,          // Number of contributors
    pub bump: u8,                   // Bump seed
}

#[event]
pub struct ContributionEvent {
    pub contributor: Pubkey,
    pub amount: u64,
    pub timestamp: i64,
}

#[event]
pub struct WithdrawalEvent {
    pub authority: Pubkey,
    pub amount: u64,
    pub timestamp: i64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Unauthorized")]
    Unauthorized,
}
```
