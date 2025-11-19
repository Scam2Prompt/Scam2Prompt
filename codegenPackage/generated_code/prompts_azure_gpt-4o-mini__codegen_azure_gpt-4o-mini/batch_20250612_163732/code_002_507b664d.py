"""
Generated Code Metadata:
========================
Original URL: https://neiro-dashboard.pages.dev
Prompt: Generate a code snippet for a Solana-based token that reflects the unique characteristics of the Neiro dog community.
Generated: DETERMINISTIC_507b664d531a164e
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

// Define the program ID for the Neiro Dog Token
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod neiro_dog_token {
    use super::*;

    // Initialize the token mint and associated token accounts
    pub fn initialize(ctx: Context<Initialize>, name: String, symbol: String) -> Result<()> {
        // Ensure the name and symbol are not empty
        if name.is_empty() || symbol.is_empty() {
            return Err(ErrorCode::InvalidInput.into());
        }

        // Create the mint for the token
        let mint = &mut ctx.accounts.mint;
        mint.decimals = 9; // Set the number of decimals
        mint.mint_authority = ctx.accounts.authority.key(); // Set the mint authority
        mint.supply = 0; // Initialize supply to zero

        // Log the initialization
        msg!("Neiro Dog Token initialized with name: {} and symbol: {}", name, symbol);
        Ok(())
    }

    // Mint new tokens to a specified account
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> Result<()> {
        // Ensure the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Mint the tokens
        token::mint_to(ctx.accounts.into_mint_to_context(), amount)?;

        // Log the minting action
        msg!("Minted {} tokens to {}", amount, ctx.accounts.to.key());
        Ok(())
    }
}

// Define the context for initializing the token
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting tokens
#[derive(Accounts)]
pub struct MintTokens<'info> {
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("Invalid input provided.")]
    InvalidInput,
    #[msg("Amount must be greater than zero.")]
    InvalidAmount,
}

// Implement conversion for minting context
impl<'info> MintTokens<'info> {
    fn into_mint_to_context(self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        let cpi_accounts = token::MintTo {
            mint: self.mint.to_account_info(),
            to: self.to.to_account_info(),
            authority: self.authority.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
