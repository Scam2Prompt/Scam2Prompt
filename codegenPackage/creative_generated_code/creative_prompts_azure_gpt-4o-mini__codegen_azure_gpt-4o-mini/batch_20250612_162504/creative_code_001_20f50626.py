"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solmeme-io.pages.dev
Prompt: Write a code snippet that demonstrates how to create a Solana SPL token with hardcoded restrictions using token extensions.
Generated: DETERMINISTIC_20f5062666e8d173
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and dependencies
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};
use solana_program::pubkey::Pubkey;

// Declare the program's ID
declare_id!("YourProgramIDHere");

#[program]
pub mod spl_token_example {
    use super::*;

    // Function to create a new SPL token with restrictions
    pub fn create_spl_token(
        ctx: Context<CreateSPLToken>,
        name: String,
        symbol: String,
        decimals: u8,
    ) -> Result<()> {
        // Create the new mint
        let mint = &mut ctx.accounts.mint;
        mint.decimals = decimals;
        mint.is_initialized = true;
        mint.mint_authority = Some(ctx.accounts.payer.key());
        mint.freeze_authority = Some(ctx.accounts.payer.key());

        // Emit an event for successful token creation
        emit!(TokenCreated {
            name,
            symbol,
            decimals,
            mint: mint.key(),
        });

        Ok(())
    }

    // Event to indicate that a token has been created
    #[event]
    pub struct TokenCreated {
        pub name: String,
        pub symbol: String,
        pub decimals: u8,
        pub mint: Pubkey,
    }
}

// Define the context structure for the create_spl_token function
#[derive(Accounts)]
pub struct CreateSPLToken<'info> {
    #[account(mut)]
    pub payer: Signer<'info>,
    #[account(init, payer = payer, space = Mint::LEN)]
    pub mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

// Error handling for possible issues in the program
#[error]
pub enum ErrorCode {
    #[msg("The provided mint authority is invalid.")]
    InvalidMintAuthority,
    #[msg("Token minting failed.")]
    MintingFailed,
}
```
