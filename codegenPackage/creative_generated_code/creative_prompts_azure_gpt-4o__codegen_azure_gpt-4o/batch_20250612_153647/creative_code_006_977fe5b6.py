"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-89.web.app
Prompt: Develop a smart contract on Solana that automates the claiming process for DUST tokens based on NFT ownership.
Generated: DETERMINISTIC_977fe5b644dc407e
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for claiming DUST tokens based on NFT ownership on Solana

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};

declare_id!("YourProgramPublicKeyHere");

#[program]
pub mod dust_claim {
    use super::*;

    // Function to claim DUST tokens based on NFT ownership
    pub fn claim_dust(
        ctx: Context<ClaimDust>, 
        amount: u64
    ) -> Result<()> {
        let nft_account = &ctx.accounts.nft_account;

        // Validate NFT ownership
        if nft_account.owner != ctx.accounts.user.key() {
            return Err(ErrorCode::InvalidNftOwnership.into());
        }

        // Perform the token transfer
        let cpi_accounts = Transfer {
            from: ctx.accounts.token_vault.to_account_info(),
            to: ctx.accounts.user_dust_account.to_account_info(),
            authority: ctx.accounts.token_vault_authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(CpiContext::new_with_signer(
            cpi_program,
            cpi_accounts,
            &[&[
                b"token_vault",
                &[ctx.accounts.token_vault_bump],
            ]],
        ), amount)?;

        Ok(())
    }
}

// Context for claiming DUST tokens
#[derive(Accounts)]
pub struct ClaimDust<'info> {
    /// CHECK: This account is manually validated
    #[account(mut)]
    pub user: Signer<'info>,
    
    #[account(
        mut,
        constraint = user_dust_account.owner == user.key(),
        constraint = user_dust_account.mint == dust_mint.key(),
    )]
    pub user_dust_account: Account<'info, TokenAccount>,
    
    #[account(
        mut,
        constraint = nft_account.owner == user.key(),
        constraint = nft_account.mint == nft_mint.key(),
    )]
    pub nft_account: Account<'info, TokenAccount>,
    
    #[account(mut)]
    pub token_vault: Account<'info, TokenAccount>,
    
    pub dust_mint: Account<'info, Mint>,
    pub nft_mint: Account<'info, Mint>,
    
    /// CHECK: This account is manually validated
    pub token_vault_authority: AccountInfo<'info>,
    
    #[account(
        seeds = [b"token_vault"],
        bump
    )]
    pub token_vault_bump: u8,
    
    pub token_program: Program<'info, Token>,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Invalid NFT ownership.")]
    InvalidNftOwnership,
}
```
