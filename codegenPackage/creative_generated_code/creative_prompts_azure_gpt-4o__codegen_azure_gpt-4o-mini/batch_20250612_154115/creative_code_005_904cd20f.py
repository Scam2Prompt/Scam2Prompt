"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: Develop a smart contract on Solana to implement a fee distribution mechanism similar to the Stay Loud "4% fee split after Meteora."
Generated: DETERMINISTIC_904cd20fdfc1beaa
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program::invoke_signed;

// Define the program's ID and program structure
declare_id!("Fg6PaFpoGXkYsidMpWxTWq8h5B5R5SCYxQe9F7jD4NqR");

#[program]
pub mod fee_distribution {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>, fee_recipient: Pubkey) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.fee_recipient = fee_recipient;
        Ok(())
    }

    // Distribute fees
    pub fn distribute_fees(ctx: Context<DistributeFees>, amount: u64) -> Result<()> {
        // Calculate the 4% fee
        let fee = amount.checked_mul(4).ok_or(ErrorCode::MathError)?.checked_div(100).ok_or(ErrorCode::MathError)?;
        
        // Transfer fees to the recipient
        **ctx.accounts.user.to_account_info().try_borrow_mut_lamports()? -= fee;
        **ctx.accounts.fee_recipient.to_account_info().try_borrow_mut_lamports()? += fee;

        // Emit an event for fee distribution
        emit!(FeeDistributed { amount: fee });
        Ok(())
    }
}

// Context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32)]
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for distributing fees
#[derive(Accounts)]
pub struct DistributeFees<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub fee_recipient: AccountInfo<'info>,
    #[account(mut)]
    pub state: Account<'info, State>,
}

// Define the state structure for storing the fee recipient
#[account]
pub struct State {
    pub fee_recipient: Pubkey,
}

// Event for fee distributed
#[event]
pub struct FeeDistributed {
    pub amount: u64,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Math error occurred during fee calculation.")]
    MathError,
}
```
