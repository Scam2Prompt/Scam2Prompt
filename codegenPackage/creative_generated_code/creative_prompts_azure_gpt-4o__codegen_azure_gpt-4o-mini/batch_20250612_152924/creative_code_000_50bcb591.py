"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormholesolana.web.app
Prompt: Write a Solana smart contract for managing $WORMHOLE token airdrops, referencing the contract ID "W1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5."
Generated: DETERMINISTIC_50bcb59112cb3a75
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Solana program library
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};

// Declare the program ID for this smart contract
declare_id!("W1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5");

#[program]
mod wormhole_airdrop {
    use super::*;

    /// Main entry point for the airdrop functionality
    pub fn airdrop_tokens(ctx: Context<AirdropTokens>, amount: u64) -> Result<()> {
        // Validate that the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer tokens from the airdrop account to the recipient
        token::transfer(
            ctx.accounts.into_transfer_context(),
            amount,
        )?;

        Ok(())
    }
}

// Context struct for airdrop tokens
#[derive(Accounts)]
pub struct AirdropTokens<'info> {
    /// The account that will receive the tokens
    #[account(mut)]
    pub recipient: AccountInfo<'info>,

    /// The account that holds the tokens to be airdropped
    #[account(mut)]
    pub airdrop_account: Account<'info, TokenAccount>,

    /// Token program
    pub token_program: Program<'info, Token>,
}

// Implementation for contextual token transfer
impl<'info> AirdropTokens<'info> {
    fn into_transfer_context(&self) -> token::Transfer<'_, 'info> {
        token::Transfer {
            from: self.airdrop_account.to_account_info(),
            to: self.recipient.clone(),
            authority: self.airdrop_account.to_account_info(),
        }
    }
}

// Custom error codes for the program
#[error]
pub enum ErrorCode {
    /// Error thrown when the provided amount for airdrop is invalid (zero)
    #[msg("Invalid amount. The amount must be greater than zero.")]
    InvalidAmount,
}
```

Make sure to configure the Solana CLI and Anchor correctly before deploying this contract to the Solana blockchain. Also, test thoroughly in a development environment before going to production.
