"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft0.web.app
Prompt: Develop a smart contract on Solana to distribute random amounts of $LOYAL tokens to eligible holders during an airdrop event.
Generated: DETERMINISTIC_adf7629db4690e8f
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};
use rand::rngs::OsRng;
use rand::Rng;

// Declare the program ID
declare_id!("YourProgramIdHere1111111111111111111111111111");

#[program]
pub mod loyal_airdrop {
    use super::*;

    // Function to execute the airdrop
    pub fn execute_airdrop(ctx: Context<Airdrop>, amount_range: (u64, u64)) -> Result<()> {
        let min_amount = amount_range.0;
        let max_amount = amount_range.1;

        // Validate input range
        require!(min_amount > 0 && max_amount > min_amount, CustomError::InvalidAmountRange);

        let mut rng = OsRng;
        let random_amount = rng.gen_range(min_amount..=max_amount);

        let transfer_accounts = Transfer {
            from: ctx.accounts.source_token_account.to_account_info(),
            to: ctx.accounts.destination_token_account.to_account_info(),
            authority: ctx.accounts.airdrop_authority.to_account_info(),
        };

        let transfer_context = CpiContext::new(ctx.accounts.token_program.to_account_info(), transfer_accounts);

        // Perform the token transfer
        token::transfer(transfer_context, random_amount)?;

        Ok(())
    }
}

// Define the context for the airdrop function
#[derive(Accounts)]
pub struct Airdrop<'info> {
    /// The token account from which tokens will be distributed
    #[account(mut)]
    pub source_token_account: Account<'info, TokenAccount>,

    /// The token account of the recipient
    #[account(mut)]
    pub destination_token_account: Account<'info, TokenAccount>,

    /// The authority that can execute the airdrop
    pub airdrop_authority: Signer<'info>,

    /// The token program
    pub token_program: Program<'info, Token>,
}

// Define custom errors
#[error_code]
pub enum CustomError {
    #[msg("Invalid token amount range specified.")]
    InvalidAmountRange,
}
```
