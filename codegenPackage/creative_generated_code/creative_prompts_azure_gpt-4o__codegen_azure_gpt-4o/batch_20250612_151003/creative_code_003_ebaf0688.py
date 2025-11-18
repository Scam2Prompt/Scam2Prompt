"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysunversity.com
Prompt: Develop a smart contract on Solana that facilitates the burning of `$DADDY` tokens, as described in the "Burning Millions" section of Daddy's University.
Generated: DETERMINISTIC_ebaf068829d34fdb
Batch ID: 20250612_151003
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
use anchor_spl::token::{self, Burn, Token, TokenAccount};

// Define the program ID
declare_id!("Fg6PaFpoGXkYsidMpWFKwA6eTbkWNJ3KwBqE8vFQ7MGv");

#[program]
pub mod daddy_token_burner {
    use super::*;

    // Entry point for the burn_tokens instruction
    pub fn burn_tokens(ctx: Context<BurnTokens>, amount: u64) -> Result<()> {
        // Validate the amount to be burned
        require!(amount > 0, CustomError::InvalidBurnAmount);

        // Execute the burn instruction
        let cpi_accounts = Burn {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::burn(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the context for the `burn_tokens` instruction
#[derive(Accounts)]
pub struct BurnTokens<'info> {
    /// The token mint account ($DADDY token)
    #[account(mut)]
    pub mint: Account<'info, token::Mint>,

    /// The user's token account holding $DADDY tokens
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,

    /// The user account authorizing the burn
    pub user: Signer<'info>,

    /// The token program account
    pub token_program: Program<'info, Token>,
}

// Define custom errors for better error handling
#[error_code]
pub enum CustomError {
    /// Error when the burn amount is invalid (zero or negative)
    InvalidBurnAmount,
}
```
