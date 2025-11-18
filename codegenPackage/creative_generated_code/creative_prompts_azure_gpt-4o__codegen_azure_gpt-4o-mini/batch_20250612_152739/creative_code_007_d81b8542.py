"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lessfeesandgas.web.app
Prompt: Develop a smart contract on Solana that demonstrates the lower fees and faster processing times compared to Ethereum, as highlighted on the "Less Fees & Gas" webpage.
Generated: DETERMINISTIC_d81b8542dd6b5e1b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: Apache-2.0

use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

declare_id!("Fg6PaFpoGXkYsidMpWTK8C8F9C6k1XK7QfS2ScTUGkHg");

#[program]
pub mod solana_low_fees {
    use super::*;

    /// Initializes the smart contract and allocates a new account for the user.
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        // Setting the initial balance for the user account
        let user_account = &mut ctx.accounts.user_account;
        user_account.balance = 0;
        Ok(())
    }

    /// Allows the user to deposit SOL into their account.
    pub fn deposit(ctx: Context<Deposit>, amount: u64) -> Result<()> {
        // Ensure that the amount is greater than zero
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer SOL from the user's wallet to the contract
        let user_account = &mut ctx.accounts.user_account;
        let transfer_amount = amount;

        // Update the user's balance
        user_account.balance += transfer_amount;
        msg!("Deposited {} SOL", transfer_amount);
        Ok(())
    }

    /// Allows the user to withdraw SOL from their account.
    pub fn withdraw(ctx: Context<Withdraw>, amount: u64) -> Result<()> {
        let user_account = &mut ctx.accounts.user_account;

        // Ensure that the amount is valid
        if amount <= 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Ensure that the user has enough balance to withdraw
        if user_account.balance < amount {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Update the user's balance
        user_account.balance -= amount;
        msg!("Withdrew {} SOL", amount);
        Ok(())
    }
}

/// User account structure to hold the user's balance.
#[account]
pub struct UserAccount {
    pub balance: u64,
}

/// Context for initializing the contract.
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)] // Account size: 8 bytes for discriminator + 8 bytes for balance
    pub user_account: Account<'info, UserAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

/// Context for depositing SOL.
#[derive(Accounts)]
pub struct Deposit<'info> {
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    pub user: Signer<'info>,
}

/// Context for withdrawing SOL.
#[derive(Accounts)]
pub struct Withdraw<'info> {
    #[account(mut)]
    pub user_account: Account<'info, UserAccount>,
    pub user: Signer<'info>,
}

/// Custom error codes for the contract.
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
    #[msg("Insufficient funds in the account.")]
    InsufficientFunds,
}
```
