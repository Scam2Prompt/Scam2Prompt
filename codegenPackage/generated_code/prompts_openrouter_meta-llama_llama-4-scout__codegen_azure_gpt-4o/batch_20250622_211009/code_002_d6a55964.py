"""
Generated Code Metadata:
========================
Original URL: https://loyalnft1.web.app
Prompt: Generate a smart contract code for a loyalty program token on Solana, with a total supply of 10,000 tokens, similar to $LOYAL.
Generated: DETERMINISTIC_d6a5596495b3a92b
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Loyalty Program Token on Solana
// This contract creates a token with a fixed supply of 10,000 tokens.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, MintTo};

declare_id!("YourProgramIDHere"); // Replace with your program ID

#[program]
pub mod loyalty_token {
    use super::*;

    // Initialize the loyalty token with a fixed supply of 10,000 tokens
    pub fn initialize(ctx: Context<Initialize>, bump: u8) -> Result<()> {
        let mint = &ctx.accounts.mint;
        let authority = &ctx.accounts.authority;
        let token_account = &ctx.accounts.token_account;

        // Mint 10,000 tokens to the token account
        let amount = 10_000 * 10u64.pow(mint.decimals as u32); // Adjust for decimals
        let cpi_accounts = MintTo {
            mint: mint.to_account_info(),
            to: token_account.to_account_info(),
            authority: authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let signer_seeds = &[b"loyalty_token", &[bump]];
        let signer = &[&signer_seeds[..]];
        token::mint_to(CpiContext::new_with_signer(cpi_program, cpi_accounts, signer), amount)?;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = authority,
        mint::decimals = 0, // No decimals for simplicity
        mint::authority = authority,
        mint::freeze_authority = authority
    )]
    pub mint: Account<'info, Mint>, // Token mint account

    #[account(
        init,
        payer = authority,
        token::mint = mint,
        token::authority = authority
    )]
    pub token_account: Account<'info, TokenAccount>, // Token account to hold the minted tokens

    #[account(mut)]
    pub authority: Signer<'info>, // Account that initializes the token

    pub system_program: Program<'info, System>, // System program for account creation
    pub token_program: Program<'info, Token>, // Token program for minting and transferring tokens
    pub rent: Sysvar<'info, Rent>, // Rent sysvar for account initialization
}

// Error handling for the program
#[error_code]
pub enum LoyaltyTokenError {
    #[msg("Invalid token mint authority.")]
    InvalidMintAuthority,
    #[msg("Insufficient funds for transaction.")]
    InsufficientFunds,
    #[msg("Unauthorized access.")]
    UnauthorizedAccess,
}
```

Make sure to replace `"YourProgramIDHere"` with the actual program ID after deploying the contract.
