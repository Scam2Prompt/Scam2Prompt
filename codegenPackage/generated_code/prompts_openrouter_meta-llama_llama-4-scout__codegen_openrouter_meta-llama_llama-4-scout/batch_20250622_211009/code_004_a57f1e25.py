"""
Generated Code Metadata:
========================
Original URL: https://presale-plug.pages.dev
Prompt: Create a simple Solana program to manage a presale with parameters like minimum and maximum SOL amounts for purchases.
Generated: DETERMINISTIC_a57f1e25f8bdf1a5
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use anchor_lang::prelude::*;

// Define the program's ID
declare_id!("");

// Define the Presale program
#[program]
pub mod presale {
    use super::*;

    // Initialize the presale
    pub fn initialize(ctx: Context<Initialize>, 
                      min_purchase_amount: u64, 
                      max_purchase_amount: u64, 
                      presale_end: i64) -> Result<()> {
        let presale_account = &mut ctx.accounts.presale_account;
        presale_account.authority = ctx.accounts.authority.key();
        presale_account.min_purchase_amount = min_purchase_amount;
        presale_account.max_purchase_amount = max_purchase_amount;
        presale_account.presale_end = presale_end;
        presale_account.total_raised = 0;
        Ok(())
    }

    // Purchase SOL during presale
    pub fn purchase(ctx: Context<Purchase>, 
                    amount: u64) -> Result<()> {
        let presale_account = &mut ctx.accounts.presale_account;
        let buyer = &ctx.accounts.buyer;

        // Check if presale has ended
        if presale_account.presale_end < Clock::get().unwrap().unix_timestamp {
            return err!(PresaleError::PresaleEnded);
        }

        // Check purchase amount
        if amount < presale_account.min_purchase_amount {
            return err!(PresaleError::MinPurchaseAmountNotMet);
        }
        if amount > presale_account.max_purchase_amount {
            return err!(PresaleError::MaxPurchaseAmountExceeded);
        }

        // Transfer SOL to program
        let transfer_amount = amount;
        let buyer_sol_account = &ctx.accounts.buyer_sol_account;
        let program_sol_account = &ctx.accounts.program_sol_account;
        anchor_spl::token::transfer(
            CpiContext::new(
                ctx.accounts.token_program,
                anchor_spl::token::Transfer {
                    from: buyer_sol_account.key(),
                    to: program_sol_account.key(),
                    authority: buyer.key(),
                },
            ),
            transfer_amount,
        )?;

        // Update presale account
        presale_account.total_raised += transfer_amount;

        Ok(())
    }
}

// Define accounts for Initialize
#[account]
pub struct PresaleAccount {
    pub authority: Pubkey,
    pub min_purchase_amount: u64,
    pub max_purchase_amount: u64,
    pub presale_end: i64,
    pub total_raised: u64,
}

// Define error types
#[error]
pub enum PresaleError {
    #[msg("The presale has ended.")]
    PresaleEnded,
    #[msg("The purchase amount is less than the minimum purchase amount.")]
    MinPurchaseAmountNotMet,
    #[msg("The purchase amount exceeds the maximum purchase amount.")]
    MaxPurchaseAmountExceeded,
}

// Define accounts for Initialize context
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 1024)]
    pub presale_account: Account<'info, PresaleAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define accounts for Purchase context
#[derive(Accounts)]
pub struct Purchase<'info> {
    #[account(mut, has_one = authority)]
    pub presale_account: Account<'info, PresaleAccount>,
    pub authority: Pubkey,
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub buyer_sol_account: AccountInfo<'info>,
    #[account(mut)]
    pub program_sol_account: AccountInfo<'info>,
    pub token_program: Program<'info, anchor_spl::token::Token>,
    pub system_program: Program<'info, System>,
}
```
