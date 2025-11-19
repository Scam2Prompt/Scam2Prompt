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
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_error::ProgramError;

// Define the program's ID
declare_id!("YourProgramIDHere");

// Define the Presale struct to hold presale parameters
#[program]
pub mod presale {
    use super::*;

    // Initialize the presale with minimum and maximum purchase amounts
    pub fn initialize_presale(ctx: Context<InitializePresale>, min_amount: u64, max_amount: u64) -> Result<()> {
        let presale = &mut ctx.accounts.presale;
        presale.min_amount = min_amount;
        presale.max_amount = max_amount;
        presale.total_sold = 0;
        Ok(())
    }

    // Function to purchase during the presale
    pub fn purchase(ctx: Context<Purchase>, amount: u64) -> Result<()> {
        let presale = &mut ctx.accounts.presale;

        // Check if the purchase amount is within the allowed range
        if amount < presale.min_amount || amount > presale.max_amount {
            return Err(ProgramError::InvalidArgument.into());
        }

        // Update the total sold amount
        presale.total_sold += amount;

        // Transfer SOL from buyer to the presale account
        let cpi_accounts = anchor_lang::solana_program::system_instruction::Transfer {
            from: ctx.accounts.buyer.to_account_info(),
            to: ctx.accounts.presale.to_account_info(),
        };
        let cpi_program = ctx.accounts.system_program.to_account_info();
        let ix = anchor_lang::solana_program::system_instruction::transfer(
            &ctx.accounts.buyer.key(),
            &ctx.accounts.presale.key(),
            amount,
        );
        anchor_lang::solana_program::program::invoke(&ix, &[
            ctx.accounts.buyer.to_account_info(),
            ctx.accounts.presale.to_account_info(),
            ctx.accounts.system_program.to_account_info(),
        ])?;

        Ok(())
    }
}

// Define the context for initializing the presale
#[derive(Accounts)]
pub struct InitializePresale<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8 + 8)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for purchasing during the presale
#[derive(Accounts)]
pub struct Purchase<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the Presale account structure
#[account]
pub struct Presale {
    pub min_amount: u64, // Minimum amount of SOL for purchase
    pub max_amount: u64, // Maximum amount of SOL for purchase
    pub total_sold: u64, // Total amount of SOL sold in the presale
}
```
