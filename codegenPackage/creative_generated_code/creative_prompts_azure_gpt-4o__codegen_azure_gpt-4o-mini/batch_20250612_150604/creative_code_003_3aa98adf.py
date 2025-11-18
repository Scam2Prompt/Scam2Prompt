"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testooos.web.app
Prompt: Write a smart contract for Solana that facilitates free pre-sale transactions, as described in Helio's exclusive $CHILL pre-sale feature.
Generated: DETERMINISTIC_3aa98adf3643889d
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Declare the program and state
declare_id!("YourProgramIDHere");

#[program]
pub mod chill_presale {
    use super::*;

    /// Initialize the contract with necessary parameters
    pub fn initialize(ctx: Context<Initialize>, presale_start: i64, presale_end: i64) -> Result<()> {
        let presale = &mut ctx.accounts.presale;
        presale.owner = *ctx.accounts.owner.key;
        presale.presale_start = presale_start;
        presale.presale_end = presale_end;
        presale.total_collected = 0;
        Ok(())
    }

    /// Function to facilitate pre-sale transactions
    pub fn participate(ctx: Context<Participate>, amount: u64) -> Result<()> {
        let current_time = Clock::get()?.unix_timestamp;

        // Check if the presale is active
        require!(current_time >= ctx.accounts.presale.presale_start, ErrorCode::PresaleNotActive);
        require!(current_time <= ctx.accounts.presale.presale_end, ErrorCode::PresaleEnded);

        // Ensure the correct amount is provided (free presale, but may have checks)
        require!(amount == 0, ErrorCode::InvalidAmount);

        // Update total collected (for tracking)
        ctx.accounts.presale.total_collected += amount;

        msg!("Transaction successfully recorded for presale participant: {}", ctx.accounts.participant.key);
        Ok(())
    }
}

// Define the state structure for the presale
#[account]
pub struct Presale {
    pub owner: Pubkey,
    pub presale_start: i64,
    pub presale_end: i64,
    pub total_collected: u64,
}

// Define context for initializing the presale
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = Presale::LEN)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define context for participating in the presale
#[derive(Accounts)]
pub struct Participate<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub participant: Signer<'info>,
}

// Define custom error codes for better error handling
#[error]
pub enum ErrorCode {
    #[msg("The presale is not active yet.")]
    PresaleNotActive,
    #[msg("The presale has already ended.")]
    PresaleEnded,
    #[msg("Invalid transaction amount. This presale is free.")]
    InvalidAmount,
}

// Define the constant for account length
impl Presale {
    const LEN: usize = 8 + // discriminator
                      32 + // owner
                      8 +  // presale_start
                      8 +  // presale_end
                      8;   // total_collected
}
```
