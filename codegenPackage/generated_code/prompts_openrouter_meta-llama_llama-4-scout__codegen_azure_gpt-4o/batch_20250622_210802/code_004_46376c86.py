"""
Generated Code Metadata:
========================
Original URL: https://sugarglidercoin.vercel.app
Prompt: Create a simple raffle contract in Rust for a Solana-based project like Sugar Glider.
Generated: DETERMINISTIC_46376c8670e10032
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod raffle_contract {
    use super::*;

    // Initialize the raffle
    pub fn initialize_raffle(ctx: Context<InitializeRaffle>, name: String) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;
        raffle.name = name;
        raffle.owner = *ctx.accounts.owner.key;
        raffle.entries = vec![];
        Ok(())
    }

    // Enter the raffle
    pub fn enter_raffle(ctx: Context<EnterRaffle>) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;
        let participant = *ctx.accounts.participant.key;

        // Ensure the participant hasn't already entered
        if raffle.entries.contains(&participant) {
            return Err(error!(RaffleError::AlreadyEntered));
        }

        // Add the participant to the raffle
        raffle.entries.push(participant);
        Ok(())
    }

    // Pick a winner
    pub fn pick_winner(ctx: Context<PickWinner>) -> Result<()> {
        let raffle = &mut ctx.accounts.raffle;

        // Ensure there are entries in the raffle
        if raffle.entries.is_empty() {
            return Err(error!(RaffleError::NoEntries));
        }

        // Select a random winner
        let random_index = anchor_lang::solana_program::sysvar::clock::Clock::get()?.unix_timestamp as usize % raffle.entries.len();
        raffle.winner = Some(raffle.entries[random_index]);
        Ok(())
    }
}

// Define the accounts structure for initializing the raffle
#[derive(Accounts)]
pub struct InitializeRaffle<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 4 + 1000)] // Space calculation: discriminator + owner + name + entries
    pub raffle: Account<'info, Raffle>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the accounts structure for entering the raffle
#[derive(Accounts)]
pub struct EnterRaffle<'info> {
    #[account(mut)]
    pub raffle: Account<'info, Raffle>,
    pub participant: Signer<'info>,
}

// Define the accounts structure for picking a winner
#[derive(Accounts)]
pub struct PickWinner<'info> {
    #[account(mut, has_one = owner)]
    pub raffle: Account<'info, Raffle>,
    pub owner: Signer<'info>,
}

// Define the Raffle account structure
#[account]
pub struct Raffle {
    pub name: String,           // Name of the raffle
    pub owner: Pubkey,          // Owner of the raffle
    pub entries: Vec<Pubkey>,   // List of participants
    pub winner: Option<Pubkey>, // Winner of the raffle
}

// Define custom errors for the program
#[error_code]
pub enum RaffleError {
    #[msg("Participant has already entered the raffle.")]
    AlreadyEntered,
    #[msg("No entries in the raffle.")]
    NoEntries,
}
```
