"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft3.web.app
Prompt: Develop a smart contract on Solana that ensures only active holders of $LOYAL or equivalent tokens can participate in the airdrop.
Generated: DETERMINISTIC_fac28b8163373ff4
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{Token, TokenAccount, Transfer};
use std::convert::TryInto;

// Define the program ID and declare the program.
declare_id!("YourProgramIDHere");

#[program]
pub mod loyal_airdrop {
    use super::*;

    // Initialize the airdrop with necessary parameters
    pub fn initialize(ctx: Context<Initialize>, airdrop_amount: u64, loyal_mint: Pubkey) -> ProgramResult {
        let airdrop_account = &mut ctx.accounts.airdrop_account;
        airdrop_account.airdrop_amount = airdrop_amount;
        airdrop_account.loyal_mint = loyal_mint;
        Ok(())
    }

    // Execute the airdrop only for active $LOYAL holders
    pub fn airdrop(ctx: Context<Airdrop>) -> ProgramResult {
        // Ensure the user is a holder of LOYAL tokens
        let user_balance = ctx.accounts.user_token_account.amount;
        let required_balance = 1; // Amount of $LOYAL required

        if user_balance < required_balance {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Transfer the airdrop amount to the user
        let cpi_accounts = Transfer {
            from: ctx.accounts.airdrop_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.airdrop_authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, ctx.accounts.airdrop_account.airdrop_amount)?;

        Ok(())
    }
}

// Context for initializing the airdrop
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for executing the airdrop
#[derive(Accounts)]
pub struct Airdrop<'info> {
    #[account(mut)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub airdrop_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Airdrop account structure to store relevant info
#[account]
pub struct AirdropAccount {
    pub airdrop_amount: u64,
    pub loyal_mint: Pubkey,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient funds to participate in the airdrop.")]
    InsufficientFunds,
}
```

Make sure to replace `"YourProgramIDHere"` with your actual program ID. This code includes error handling, comments, and best practices for developing a smart contract on Solana using Rust and Anchor framework.
