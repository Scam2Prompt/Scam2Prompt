"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-nine.web.app
Prompt: Write a smart contract for processing payments directly to merchants on the Solana network, referencing the Helio platform's payment flow.
Generated: DETERMINISTIC_c107222534de5d40
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

// Define the program's entry point
declare_id!("YourProgramIDHere"); // Replace with your program ID

// Define the main contract structure
#[program]
pub mod merchant_payment {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>) -> ProgramResult {
        let payment_account = &mut ctx.accounts.payment_account;
        payment_account.owner = ctx.accounts.admin.key();
        payment_account.total_amount = 0;
        Ok(())
    }

    // Function to process payments
    pub fn process_payment(ctx: Context<ProcessPayment>, amount: u64) -> ProgramResult {
        // Ensure the amount is greater than zero
        if amount <= 0 {
            return Err(ProgramError::InvalidArgument);
        }

        // Transfer the payment to the merchant account
        let payment_account = &mut ctx.accounts.payment_account;
        let merchant_account = &ctx.accounts.merchant;

        // Update the total amount paid
        payment_account.total_amount += amount;

        // Transfer the funds from the payer to the merchant
        let cpi_accounts = system_program::Transfer {
            from: ctx.accounts.payer.to_account_info(),
            to: merchant_account.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.system_program.to_account_info(), cpi_accounts);
        system_program::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the context for initializing the program
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = 8 + 8)]
    pub payment_account: Account<'info, PaymentAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for processing a payment
#[derive(Accounts)]
pub struct ProcessPayment<'info> {
    #[account(mut)]
    pub payment_account: Account<'info, PaymentAccount>,
    #[account(mut)]
    pub merchant: AccountInfo<'info>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the structure for storing payment account data
#[account]
pub struct PaymentAccount {
    pub owner: Pubkey,
    pub total_amount: u64,
}
```
