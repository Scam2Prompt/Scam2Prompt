"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edrfrtertertertc.web.app
Prompt: Generate a smart contract in Rust for Solana that supports irreversible DeFi payments, ensuring funds are sent directly to the merchant as described in Helio's disclaimer.
Generated: DETERMINISTIC_33827cd03b8017da
Batch ID: 20250612_153517
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

// Declare the program ID
declare_id!("MerchantPubkey1234567890abcdef1234567890abcdef");

// Program entry point
#[program]
pub mod irreversible_defi_payments {
    use super::*;

    /// Function to initiate an irreversible payment to a merchant
    /// - `ctx`: Context containing required accounts
    /// - `amount`: Amount to transfer
    pub fn process_payment(ctx: Context<ProcessPayment>, amount: u64) -> Result<()> {
        // Ensure the amount is positive
        require!(amount > 0, PaymentError::InvalidAmount);

        // Transfer the funds from the payer to the merchant
        let payer_account = &ctx.accounts.payer;
        let merchant_account = &ctx.accounts.merchant;
        let system_program = &ctx.accounts.system_program;

        // Perform the transfer
        anchor_lang::solana_program::program::invoke(
            &anchor_lang::solana_program::system_instruction::transfer(
                &payer_account.key,
                &merchant_account.key,
                amount,
            ),
            &[
                payer_account.to_account_info(),
                merchant_account.to_account_info(),
                system_program.to_account_info(),
            ],
        )?;

        Ok(())
    }
}

// Define the context and accounts used in the program
#[derive(Accounts)]
pub struct ProcessPayment<'info> {
    /// The account of the payer (sender of funds)
    #[account(mut)]
    pub payer: Signer<'info>,

    /// The merchant account to receive funds
    #[account(mut)]
    pub merchant: AccountInfo<'info>,

    /// System program required for the transfer
    pub system_program: Program<'info, System>,
}

// Define custom errors for the program
#[error_code]
pub enum PaymentError {
    /// Error for invalid payment amounts
    InvalidAmount,
}
```
