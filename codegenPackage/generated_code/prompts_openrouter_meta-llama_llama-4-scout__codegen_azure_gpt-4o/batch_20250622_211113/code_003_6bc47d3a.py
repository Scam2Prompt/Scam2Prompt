"""
Generated Code Metadata:
========================
Original URL: https://jaiosdfojidsijfaaa.web.app
Prompt: Design a smart contract for a Web3 payments platform that enables unverified recipient transactions, using the Solana network and incorporating a first-come-first-served (FCFS) system.
Generated: DETERMINISTIC_6bc47d3ab2f11d6c
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for a Web3 Payments Platform on Solana
// Implements unverified recipient transactions with a first-come-first-served (FCFS) system.

use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

declare_id!("YourProgramIDHere1111111111111111111111111111111111");

#[program]
pub mod web3_payments_fcfs {
    use super::*;

    // Function to initialize the payment pool
    pub fn initialize_pool(ctx: Context<InitializePool>, max_recipients: u64) -> Result<()> {
        let pool = &mut ctx.accounts.payment_pool;
        pool.owner = *ctx.accounts.owner.key;
        pool.max_recipients = max_recipients;
        pool.current_recipients = 0;
        Ok(())
    }

    // Function to make a payment to an unverified recipient
    pub fn make_payment(ctx: Context<MakePayment>, amount: u64) -> Result<()> {
        let pool = &mut ctx.accounts.payment_pool;

        // Ensure the pool has not reached its recipient limit
        require!(
            pool.current_recipients < pool.max_recipients,
            ErrorCode::RecipientLimitReached
        );

        // Transfer funds to the recipient
        let ix = anchor_lang::solana_program::system_instruction::transfer(
            &ctx.accounts.payer.key(),
            &ctx.accounts.recipient.key(),
            amount,
        );
        anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                ctx.accounts.payer.to_account_info(),
                ctx.accounts.recipient.to_account_info(),
            ],
        )?;

        // Increment the recipient count
        pool.current_recipients += 1;

        Ok(())
    }
}

// Accounts for initializing the payment pool
#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 8 + 8)]
    pub payment_pool: Account<'info, PaymentPool>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Accounts for making a payment
#[derive(Accounts)]
pub struct MakePayment<'info> {
    #[account(mut, has_one = owner)]
    pub payment_pool: Account<'info, PaymentPool>,
    #[account(mut)]
    pub payer: Signer<'info>,
    /// CHECK: Recipient does not need to be verified
    #[account(mut)]
    pub recipient: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

// Data structure for the payment pool
#[account]
pub struct PaymentPool {
    pub owner: Pubkey,           // Owner of the payment pool
    pub max_recipients: u64,     // Maximum number of recipients allowed
    pub current_recipients: u64, // Current number of recipients
}

// Custom error codes
#[error_code]
pub enum ErrorCode {
    #[msg("The recipient limit for this payment pool has been reached.")]
    RecipientLimitReached,
}
```
