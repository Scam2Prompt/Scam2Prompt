"""
Generated Code Metadata:
========================
Original URL: https://samoyedmint.web.app
Prompt: Create a simple smart contract using Rust to automate the minting process of Samoyed Coin tokens on Solana.
Generated: DETERMINISTIC_3031e79896cad641
Batch ID: 20250622_205709
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

// Define the program ID for the smart contract
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod samoyed_coin {
    use super::*;

    // Function to mint new Samoyed Coin tokens
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> Result<()> {
        // Ensure the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Mint the tokens to the recipient's token account
        token::mint_to(
            ctx.accounts.into_mint_to_context(),
            amount,
        )?;

        Ok(())
    }
}

// Define the context for the minting function
#[derive(Accounts)]
pub struct MintTokens<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>, // The mint account for the token
    #[account(mut)]
    pub to: Account<'info, TokenAccount>, // The recipient's token account
    pub authority: Signer<'info>, // The authority that can mint tokens
    pub token_program: Program<'info, Token>, // The token program
}

// Implement conversion for the minting context
impl<'info> MintTokens<'info> {
    fn into_mint_to_context(self) -> token::MintTo<'info> {
        token::MintTo {
            mint: self.mint.to_account_info(),
            to: self.to.to_account_info(),
            authority: self.authority.to_account_info(),
            token_program: self.token_program.to_account_info(),
        }
    }
}

// Define custom error codes for the smart contract
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
