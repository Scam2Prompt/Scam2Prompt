"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-samoyed.web.app
Prompt: Write a smart contract example for managing token minting rights based on whitelist status in the Solana ecosystem.
Generated: DETERMINISTIC_5a56cc8e52c0e3b7
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// This is an example of a Solana smart contract for managing token minting rights 
// based on whitelist status.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

// Declare the program's namespace
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod token_mint_whitelist {
    use super::*;

    // Initializes a mint account with whitelist functionality
    pub fn initialize_mint(ctx: Context<InitializeMint>, bump: u8) -> Result<()> {
        let mint_data = &mut ctx.accounts.mint_data;
        mint_data.bump = bump;
        mint_data.authority = ctx.accounts.authority.key();
        Ok(())
    }

    // Adds a user to the whitelist
    pub fn add_to_whitelist(ctx: Context<ManageWhitelist>, user: Pubkey) -> Result<()> {
        let mint_data = &mut ctx.accounts.mint_data;
        require!(
            mint_data.authority == ctx.accounts.authority.key(),
            MyError::Unauthorized
        );
        if !mint_data.whitelist.contains(&user) {
            mint_data.whitelist.push(user);
        }
        Ok(())
    }

    // Removes a user from the whitelist
    pub fn remove_from_whitelist(ctx: Context<ManageWhitelist>, user: Pubkey) -> Result<()> {
        let mint_data = &mut ctx.accounts.mint_data;
        require!(
            mint_data.authority == ctx.accounts.authority.key(),
            MyError::Unauthorized
        );
        mint_data.whitelist.retain(|&u| u != user);
        Ok(())
    }

    // Mints tokens to a user, only if they are whitelisted
    pub fn mint_to(ctx: Context<MintTo>, amount: u64) -> Result<()> {
        let mint_data = &ctx.accounts.mint_data;
        require!(
            mint_data.whitelist.contains(&ctx.accounts.recipient.key()),
            MyError::NotWhitelisted
        );

        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.recipient.to_account_info(),
            authority: ctx.accounts.mint_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let mint_key = mint_data.key();
        let seeds = &[mint_key.as_ref(), &[mint_data.bump]];
        let signer = &[&seeds[..]];

        token::mint_to(CpiContext::new_with_signer(
            cpi_program,
            cpi_accounts,
            signer,
        ), amount)?;

        Ok(())
    }
}

// Define account structures
#[account]
pub struct MintData {
    pub bump: u8,                   // Bump seed for PDA
    pub authority: Pubkey,          // Authority for managing the whitelist
    pub whitelist: Vec<Pubkey>,     // List of whitelisted addresses
}

#[derive(Accounts)]
pub struct InitializeMint<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 4 + 1024)]
    pub mint_data: Account<'info, MintData>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ManageWhitelist<'info> {
    #[account(mut)]
    pub mint_data: Account<'info, MintData>,
    pub authority: Signer<'info>,
}

#[derive(Accounts)]
pub struct MintTo<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub recipient: Account<'info, TokenAccount>,
    #[account(mut)]
    pub mint_authority: Signer<'info>,
    #[account(mut)]
    pub mint_data: Account<'info, MintData>,
    pub token_program: Program<'info, Token>,
}

// Define custom error messages
#[error_code]
pub enum MyError {
    Unauthorized,      // Raised when an action is attempted without sufficient authority
    NotWhitelisted,    // Raised when a mint-to recipient is not whitelisted
}
```
