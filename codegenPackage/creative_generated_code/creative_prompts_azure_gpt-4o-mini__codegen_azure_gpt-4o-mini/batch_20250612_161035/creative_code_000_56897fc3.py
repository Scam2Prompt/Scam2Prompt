"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy.pages.dev
Prompt: How can I create a smart contract to manage the $Gummy token airdrop on the Solana blockchain?
Generated: DETERMINISTIC_56897fc30ff19a2d
Batch ID: 20250612_161035
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
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};

// Define the program ID
declare_id!("YourProgramIdHere");

// Define the main program structure
#[program]
pub mod gummy_airdrop {
    use super::*;

    // Function to initialize the airdrop
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;
        airdrop_account.total_supply = total_supply;
        airdrop_account.claimed_amount = 0;
        Ok(())
    }

    // Function to claim tokens
    pub fn claim_tokens(ctx: Context<ClaimTokens>, amount: u64) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;

        // Ensure the amount to claim does not exceed the total supply
        if airdrop_account.claimed_amount + amount > airdrop_account.total_supply {
            return Err(ErrorCode::InsufficientSupply.into());
        }

        // Transfer tokens to the user's account
        let cpi_accounts = Transfer {
            from: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.airdrop_account.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update the claimed amount
        airdrop_account.claimed_amount += amount;
        Ok(())
    }
}

// Define the state for the airdrop
#[account]
pub struct AirdropAccount {
    pub total_supply: u64,
    pub claimed_amount: u64,
}

// Define the context for initializing the airdrop
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for claiming tokens
#[derive(Accounts)]
pub struct ClaimTokens<'info> {
    #[account(mut)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes for the airdrop
#[error]
pub enum ErrorCode {
    #[msg("Insufficient supply for this airdrop.")]
    InsufficientSupply,
}
```
