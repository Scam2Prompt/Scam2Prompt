"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-gummyonsol.pages.dev
Prompt: Generate a Solana-based smart contract snippet to distribute $GUMMY tokens according to the tokenomics percentages provided (e.g., 30% airdrop, 20% marketing).
Generated: DETERMINISTIC_653d36fbe618723c
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

// Define the program's ID
declare_id!("YourProgramIdHere");

// Define the main program structure
#[program]
pub mod gummy_distribution {
    use super::*;

    // Entry point for distributing tokens
    pub fn distribute_tokens(
        ctx: Context<DistributeTokens>,
        total_supply: u64,
    ) -> ProgramResult {
        // Calculate the amount for each distribution category based on tokenomics
        let airdrop_amount = total_supply * 30 / 100;
        let marketing_amount = total_supply * 20 / 100;

        // Transfer tokens to the designated accounts
        token::transfer(
            ctx.accounts.into_transfer_context(),
            airdrop_amount,
        )?;

        token::transfer(
            ctx.accounts.into_transfer_context_marketing(),
            marketing_amount,
        )?;

        Ok(())
    }
}

// Define the context for the distribution function
#[derive(Accounts)]
pub struct DistributeTokens<'info> {
    #[account(mut)]
    pub payer: Signer<'info>, // The user initiating the distribution

    #[account(mut)]
    pub airdrop_account: Account<'info, TokenAccount>, // Account for airdrop tokens
    #[account(mut)]
    pub marketing_account: Account<'info, TokenAccount>, // Account for marketing tokens
    pub mint: Account<'info, Mint>, // Mint for the $GUMMY token
    pub token_program: Program<'info, Token>, // The SPL Token Program
}

// Implement conversion methods for transfer contexts
impl<'info> DistributeTokens<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        token::Transfer::new(&self.airdrop_account, &self.mint, self.payer.key())
    }

    fn into_transfer_context_marketing(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        token::Transfer::new(&self.marketing_account, &self.mint, self.payer.key())
    }
}

// Implement a custom error type for the program
#[error]
pub enum GummyDistributionError {
    #[msg("Insufficient funds for transfer.")]
    InsufficientFunds,
    #[msg("Invalid token mint.")]
    InvalidTokenMint,
}
```
