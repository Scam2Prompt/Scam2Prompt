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
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramPublicKeyHere");

#[program]
pub mod token_transfer {
    use super::*;

    pub fn transfer_tokens(
        ctx: Context<TransferTokens>,
        amount: u64,
    ) -> Result<()> {
        // Perform the token transfer
        let transfer_instruction = Transfer {
            from: ctx.accounts.from.to_account_info(),
            to: ctx.accounts.to.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };

        let result = token::transfer(
            CpiContext::new(ctx.accounts.token_program.to_account_info(), transfer_instruction),
            amount,
        );

        result
    }
}

#[derive(Accounts)]
pub struct TransferTokens<'info> {
    /// The source token account (sender)
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,

    /// The destination token account (receiver)
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,

    /// The authority that owns the source token account
    pub authority: Signer<'info>,

    /// The token program responsible for token operations
    pub token_program: Program<'info, Token>,
}
```

This code handles transferring tokens between two accounts using the Solana Anchor framework. It assumes the sender has signed the transaction and the token accounts have already been initialized. Proper comments are included throughout the code for clarity.
