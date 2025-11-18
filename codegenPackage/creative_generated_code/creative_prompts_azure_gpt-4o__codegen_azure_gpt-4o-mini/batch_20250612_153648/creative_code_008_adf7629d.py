"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft0.web.app
Prompt: Develop a smart contract on Solana to distribute random amounts of $LOYAL tokens to eligible holders during an airdrop event.
Generated: DETERMINISTIC_adf7629db4690e8f
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana and token libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{Token, TokenAccount, Mint, Transfer};
use rand::Rng; // For generating random numbers

declare_id!("YourProgramIDHere");

#[program]
pub mod loyal_airdrop {
    use super::*;

    // Entry point for the airdrop function
    pub fn distribute_airdrop(ctx: Context<DistributeAirdrop>, total_amount: u64, eligible_holders: Vec<Pubkey>) -> Result<()> {
        let rng = rand::thread_rng();
        let airdrop_amounts: Vec<u64> = eligible_holders.iter()
            .map(|_| rng.gen_range(1..=total_amount / eligible_holders.len() as u64))
            .collect();

        let mut remaining_amount = total_amount;
        
        for (i, holder) in eligible_holders.iter().enumerate() {
            let amount = airdrop_amounts[i];
            remaining_amount -= amount;

            // Transfer LOYAL tokens to the eligible holder
            let cpi_accounts = Transfer {
                from: ctx.accounts.token_account.to_account_info(),
                to: ctx.accounts.recipient_accounts[i].to_account_info(),
                authority: ctx.accounts.payer.to_account_info(),
            };
            let cpi_program = ctx.accounts.token_program.clone();

            // Ensure we don't transfer more than we have
            if amount > remaining_amount + amount {
                return Err(ErrorCode::InsufficientFunds.into());
            }

            // Perform the transfer
            anchor_spl::token::transfer(CpiContext::new(cpi_program, cpi_accounts), amount)?;
        }

        Ok(())
    }
}

// Context for the airdrop function
#[derive(Accounts)]
pub struct DistributeAirdrop<'info> {
    #[account(mut)]
    pub payer: Signer<'info>, // The account of the payer initiating the airdrop
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>, // The token account holding the LOYAL tokens
    #[account(mut)]
    pub recipient_accounts: Vec<Account<'info, TokenAccount>>, // The accounts of the eligible recipients
    pub token_program: Program<'info, Token>, // The token program
}

// Custom error codes for better error handling
#[error]
pub enum ErrorCode {
    #[msg("Insufficient funds in the token account.")]
    InsufficientFunds,
}
```
