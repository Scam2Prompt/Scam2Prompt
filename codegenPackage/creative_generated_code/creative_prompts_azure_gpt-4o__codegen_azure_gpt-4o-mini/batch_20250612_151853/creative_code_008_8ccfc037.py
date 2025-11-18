"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggodao.web.app
Prompt: Provide an example of a Solana program for funding new NFT projects using $DOGGO tokens, with detailed transaction handling.
Generated: DETERMINISTIC_8ccfc0377ded8dd1
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};
use std::mem;

// Define the program's ID
declare_id!("YOUR_PROGRAM_ID_HERE");

// Define the main program structure
#[program]
pub mod doggo_nft_fund {
    use super::*;

    // Function to fund a new NFT project
    pub fn fund_nft_project(
        ctx: Context<FundNftProject>,
        amount: u64,
    ) -> Result<()> {
        // Check if the amount is non-zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer DOGGO tokens from the user to the NFT project account
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.project_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        
        // Create the transfer instruction
        let transfer_instruction = token::Transfer::try_from_slice(
            &cpi_accounts.try_to_vec()?,
        )?;
        
        // Transfer the tokens
        token::transfer(cpi_context, amount)?;

        Ok(())
    }
}

// Define context structure for the fund_nft_project function
#[derive(Accounts)]
pub struct FundNftProject<'info> {
    #[account(mut)]
    pub user: Signer<'info>,  // The user funding the project
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>, // User's DOGGO token account
    #[account(mut)]
    pub project_token_account: Account<'info, TokenAccount>, // NFT project DOGGO token account
    pub token_program: Program<'info, Token>, // Token program account
}

// Define custom error types for the program
#[error_code]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
