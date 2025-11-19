"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-samoyed.web.app
Prompt: How can I implement a minting function for a token on the Solana blockchain similar to the Samoyed Coin minting process?
Generated: DETERMINISTIC_841702892ec6ead7
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};

// Define program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod samoyed_mint {
    use super::*;

    // Minting function for the token
    pub fn mint_token(ctx: Context<MintToken>, amount: u64) -> Result<()> {
        // Ensure the minting amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Get the mint account from the context
        let mint = &ctx.accounts.mint;
        let receiver = &ctx.accounts.receiver;

        // Mint the tokens to the receiver's account
        token::mint_to(
            ctx.accounts.token_program.to_account_info(),
            mint.to_account_info(),
            receiver.to_account_info(),
            ctx.accounts.authority.to_account_info(),
            &[],
            amount,
        )?;

        Ok(())
    }
}

// Define the context for the minting function
#[derive(Accounts)]
pub struct MintToken<'info> {
    #[account(mut)]
    pub authority: Signer<'info>, // The signer (authority) of the transaction
    #[account(mut)]
    pub mint: Box<Account<'info, Mint>>, // The mint account
    #[account(mut)]
    pub receiver: Box<Account<'info, TokenAccount>>, // The receiver's token account
    pub token_program: Program<'info, Token>, // The token program
}

// Define custom error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
