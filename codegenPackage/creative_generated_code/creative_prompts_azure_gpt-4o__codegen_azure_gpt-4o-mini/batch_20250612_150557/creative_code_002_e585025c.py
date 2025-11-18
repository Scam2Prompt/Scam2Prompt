"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theheist-solana.web.app
Prompt: Create a smart contract for Solana that facilitates irreversible DeFi payments directly to merchants, similar to Helio's functionality.
Generated: DETERMINISTIC_e585025c7a09d2d2
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import required libraries and modules from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_error::ProgramError;

// Declare the program and its structure
declare_id!("YourProgramIdHere");

#[program]
pub mod defipay {
    use super::*;

    // Initialize the smart contract
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    // Facilitate a payment to a merchant
    pub fn make_payment(ctx: Context<MakePayment>, amount: u64) -> Result<()> {
        // Check that the payment amount is greater than zero
        if amount <= 0 {
            return Err(ProgramError::InvalidArgument.into());
        }

        // Transfer the amount to the merchant's account
        let ix = anchor_lang::solana_program::system_program::transfer(
            &ctx.accounts.payer.key(),
            &ctx.accounts.merchant.key(),
            amount,
        );

        // Invoke the transfer instruction
        anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                ctx.accounts.payer.to_account_info(),
                ctx.accounts.merchant.to_account_info(),
                ctx.accounts.system_program.to_account_info(),
            ],
        )?;
        
        // Emit an event for the payment
        emit!(PaymentMade {
            payer: *ctx.accounts.payer.key,
            merchant: *ctx.accounts.merchant.key,
            amount,
        });

        Ok(())
    }
}

// Define the state of the smart contract
#[account]
pub struct State {
    pub owner: Pubkey,
}

// Define the context for initializing the smart contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32)]
    pub state: Account<'info, State>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for making a payment
#[derive(Accounts)]
pub struct MakePayment<'info> {
    #[account(mut)]
    pub payer: Signer<'info>, // The account making the payment
    #[account(mut)]
    pub merchant: AccountInfo<'info>, // The merchant receiving the payment
    pub system_program: Program<'info, System>, // System program for transfer
}

// Define the event to be emitted on payment
#[event]
pub struct PaymentMade {
    pub payer: Pubkey,
    pub merchant: Pubkey,
    pub amount: u64,
}
```
