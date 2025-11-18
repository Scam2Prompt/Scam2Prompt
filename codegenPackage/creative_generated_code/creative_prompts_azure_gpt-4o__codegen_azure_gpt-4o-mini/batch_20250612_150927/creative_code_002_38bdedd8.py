"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Generate a Solana smart contract using the Anchor framework to transfer SPL tokens between accounts, as described in the Meta Blocks documentation.
Generated: DETERMINISTIC_38bdedd81b00b3a4
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from Anchor and Solana
use anchor_lang::prelude::*;
use spl_token::state::Account as TokenAccount;

declare_id!("YourProgramIdHere"); // Replace with your program ID

#[program]
pub mod token_transfer {
    use super::*;

    // Function to transfer SPL tokens between accounts
    pub fn transfer_tokens(
        ctx: Context<TransferTokens>,
        amount: u64,
    ) -> Result<()> {
        // Ensure that the amount is greater than zero
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Get references to the accounts involved in the transaction
        let sender = &ctx.accounts.from;
        let receiver = &ctx.accounts.to;
        let token_program = &ctx.accounts.token_program;

        // Use the SPL token program's transfer instruction
        let transfer_ix = spl_token::instruction::transfer(
            token_program.key,
            sender.key,
            receiver.key,
            ctx.accounts.owner.key,
            &[],
            amount,
        )?;

        // Send the transfer instruction to the Solana runtime
        anchor_lang::solana_program::program::invoke(
            &transfer_ix,
            &[
                sender.clone(),
                receiver.clone(),
                ctx.accounts.owner.clone(),
                token_program.clone(),
            ],
        )?;

        Ok(())
    }
}

// Define context for the transfer_tokens function
#[derive(Accounts)]
pub struct TransferTokens<'info> {
    #[account(mut)]
    pub from: AccountInfo<'info>,     // Account holding the tokens to send
    #[account(mut)]
    pub to: AccountInfo<'info>,       // Account that will receive the tokens
    pub owner: Signer<'info>,         // Owner of the sender account, must sign the transaction
    pub token_program: Program<'info, Token>, // SPL Token program
}

// Define custom error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
