"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heist-solana.web.app
Prompt: Generate a Solana-based smart contract that facilitates irreversible DeFi payments directly to merchants, as described on the Helio platform.
Generated: DETERMINISTIC_afbc6b98052aa304
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program's structure
declare_id!("YourProgramIdHere");

#[program]
pub mod defipay {
    use super::*;

    // Function to initialize a new payment
    pub fn initialize_payment(ctx: Context<InitializePayment>, amount: u64, merchant: Pubkey) -> Result<()> {
        // Ensure the payment amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Create a new payment record
        let payment = &mut ctx.accounts.payment;
        payment.amount = amount;
        payment.merchant = merchant;
        payment.timestamp = Clock::get()?.unix_timestamp;
        payment.is_completed = false;

        Ok(())
    }

    // Function to execute the payment
    pub fn execute_payment(ctx: Context<ExecutePayment>) -> Result<()> {
        // Ensure the payment has not already been completed
        let payment = &mut ctx.accounts.payment;
        require!(!payment.is_completed, ErrorCode::PaymentAlreadyCompleted);

        // Transfer funds to the merchant
        let cpi_accounts = anchor_lang::solana_program::system_instruction::Transfer {
            from: ctx.accounts.payer.to_account_info().key,
            to: ctx.accounts.merchant.to_account_info().key,
        };

        // Attempt to transfer the payment amount
        let ix = anchor_lang::solana_program::system_instruction::transfer(
            ctx.accounts.payer.key,
            ctx.accounts.merchant.key,
            payment.amount,
        );

        // Execute the transfer and handle potential errors
        let result = anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                ctx.accounts.payer.to_account_info(),
                ctx.accounts.merchant.to_account_info(),
                ctx.accounts.system_program.to_account_info(),
            ],
        );

        // Mark the payment as completed if transfer was successful
        if result.is_ok() {
            payment.is_completed = true;
            Ok(())
        } else {
            Err(ErrorCode::TransferFailed.into())
        }
    }
}

// Define the accounts that will be used in the contract
#[derive(Accounts)]
pub struct InitializePayment<'info> {
    #[account(init, payer = payer, space = 8 + 32 + 8 + 8)]
    pub payment: Account<'info, Payment>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ExecutePayment<'info> {
    #[account(mut)]
    pub payment: Account<'info, Payment>,
    #[account(mut)]
    pub payer: Signer<'info>,
    #[account(mut)]
    pub merchant: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

// Define the payment structure
#[account]
pub struct Payment {
    pub amount: u64,
    pub merchant: Pubkey,
    pub timestamp: i64,
    pub is_completed: bool,
}

// Define custom error codes for the smart contract
#[error_code]
pub enum ErrorCode {
    #[msg("The payment amount must be greater than zero.")]
    InvalidAmount,
    #[msg("The payment has already been completed.")]
    PaymentAlreadyCompleted,
    #[msg("The transfer of funds failed.")]
    TransferFailed,
}
```

Make sure to replace `"YourProgramIdHere"` with your actual program ID. This code is structured as a Solana smart contract using the Anchor framework, ensuring best practices for error handling and clarity.
