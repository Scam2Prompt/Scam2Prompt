"""
Generated Code Metadata:
========================
Original URL: https://safemoonmeme.com
Prompt: Generate a smart contract code for a community-led token on the Solana blockchain.
Generated: DETERMINISTIC_7cc786b0806e2e14
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for a Community-Led Token on the Solana Blockchain

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, MintTo, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod community_token {
    use super::*;

    // Initialize the token mint and associated accounts
    pub fn initialize(
        ctx: Context<Initialize>,
        token_name: String,
        token_symbol: String,
        decimals: u8,
    ) -> Result<()> {
        let mint = &mut ctx.accounts.mint;
        mint.token_name = token_name;
        mint.token_symbol = token_symbol;
        mint.decimals = decimals;
        Ok(())
    }

    // Mint new tokens to a specified account
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> Result<()> {
        let cpi_accounts = MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.token_account.to_account_info(),
            authority: ctx.accounts.mint_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::mint_to(cpi_ctx, amount)?;
        Ok(())
    }

    // Transfer tokens between accounts
    pub fn transfer_tokens(ctx: Context<TransferTokens>, amount: u64) -> Result<()> {
        let cpi_accounts = Transfer {
            from: ctx.accounts.from.to_account_info(),
            to: ctx.accounts.to.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, amount)?;
        Ok(())
    }
}

// Define the accounts required for initialization
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 8 + 32 + 32 + 1)]
    pub mint: Account<'info, MintData>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the accounts required for minting tokens
#[derive(Accounts)]
pub struct MintTokens<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub mint_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the accounts required for transferring tokens
#[derive(Accounts)]
pub struct TransferTokens<'info> {
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Data structure for the token mint
#[account]
pub struct MintData {
    pub token_name: String,
    pub token_symbol: String,
    pub decimals: u8,
}
```
