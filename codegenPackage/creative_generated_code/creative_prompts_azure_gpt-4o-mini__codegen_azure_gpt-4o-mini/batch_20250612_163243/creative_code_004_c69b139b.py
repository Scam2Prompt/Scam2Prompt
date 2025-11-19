"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Provide an example of transferring tokens between accounts in a Solana smart contract using the Anchor framework as discussed in Meta Blocks documentation.
Generated: DETERMINISTIC_c69b139bf6253a18
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Anchor crates
use anchor_lang::prelude::*;
use anchor_spl::token::{self, TokenAccount, Transfer};

// Define the program's ID
declare_id!("YourProgramIdHere");

// Define the main program structure
#[program]
pub mod token_transfer {
    use super::*;

    // Entry point for transferring tokens
    pub fn transfer_tokens(ctx: Context<TransferTokens>, amount: u64) -> Result<()> {
        // Ensure the amount is non-zero
        if amount == 0 {
            return Err(error!(ErrorCode::InvalidAmount));
        }

        // Perform the token transfer
        let cpi_accounts = Transfer {
            from: ctx.accounts.from.clone(),
            to: ctx.accounts.to.clone(),
            authority: ctx.accounts.authority.clone(),
        };

        // Create a context for the CPI (Cross-Program Invocation)
        let cpi_program = ctx.accounts.token_program.to_account_info();
        
        // Invoke the token transfer
        token::transfer(CpiContext::new(cpi_program, cpi_accounts), amount)?;

        Ok(())
    }
}

// Define the context for the transfer_tokens function
#[derive(Accounts)]
pub struct TransferTokens<'info> {
    /// The account from which tokens are being transferred
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,
    /// The account to which tokens are being transferred
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    /// The authority that is authorizing the transfer
    pub authority: Signer<'info>,
    /// The token program
    pub token_program: Program<'info, token::Token>,
}

// Define custom error codes
#[error_code]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
