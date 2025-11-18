"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-130.web.app
Prompt: Create a smart contract on Solana to facilitate the claiming of DUST tokens based on NFT ownership verification.
Generated: DETERMINISTIC_7b6b08aa5d08e175
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Solana to facilitate claiming of DUST tokens based on NFT ownership verification.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("YourSmartContractProgramIDHere");

#[program]
pub mod nft_dust_claim {
    use super::*;

    // Instruction to claim DUST tokens
    pub fn claim_dust(ctx: Context<ClaimDust>) -> Result<()> {
        // Check NFT ownership
        let nft_account = &ctx.accounts.nft_account;
        require!(
            nft_account.amount > 0,
            CustomError::NftNotOwned,
        );

        // Transfer DUST tokens to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.token_pool.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.pool_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let seeds = &[b"pool_authority", &[ctx.accounts.pool_bump]];
        let signer = &[&seeds[..]];
        let cpi_ctx = CpiContext::new_with_signer(cpi_program, cpi_accounts, signer);
        token::transfer(cpi_ctx, ctx.accounts.dust_amount)?;

        Ok(())
    }
}

// Context for the `claim_dust` instruction
#[derive(Accounts)]
pub struct ClaimDust<'info> {
    // User token account to receive DUST
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,

    // Token pool to transfer DUST tokens from
    #[account(mut)]
    pub token_pool: Account<'info, TokenAccount>,

    // NFT account to verify ownership
    #[account(
        constraint = nft_account.mint == nft_mint.key() @ CustomError::InvalidNftMint
    )]
    pub nft_account: Account<'info, TokenAccount>,

    // Mint for the NFT
    pub nft_mint: Account<'info, Mint>,

    // Pool authority - program-derived address (PDA)
    #[account(seeds = [b"pool_authority"], bump = pool_bump)]
    pub pool_authority: AccountInfo<'info>,

    // Token program handler
    pub token_program: Program<'info, Token>,

    // Miscellaneous data
    pub dust_amount: u64, // Amount of DUST tokens to transfer
    pub pool_bump: u8,    // Bump seed for PDA
}

// Custom errors for clarity
#[error_code]
pub enum CustomError {
    #[msg("User does not own the specified NFT.")]
    NftNotOwned,
    #[msg("NFT mint address is invalid.")]
    InvalidNftMint,
}
```
