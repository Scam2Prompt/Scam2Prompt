"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Explain how to use the Solana blockchain to implement a grand prize draw triggered when a certain number of keys are purchased, as described in a lottery system.
Generated: DETERMINISTIC_718bc24dc8614273
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program's ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod lottery {
    use super::*;

    // Initialize the lottery with a specified number of keys required for the draw
    pub fn initialize_lottery(ctx: Context<InitializeLottery>, required_keys: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        lottery.required_keys = required_keys;
        lottery.current_keys = 0;
        lottery.is_active = true;
        Ok(())
    }

    // Purchase a key for the lottery
    pub fn purchase_key(ctx: Context<PurchaseKey>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure the lottery is active
        require!(lottery.is_active, LotteryError::LotteryNotActive);

        // Increment the current keys purchased
        lottery.current_keys += 1;

        // Check if the required number of keys has been reached
        if lottery.current_keys >= lottery.required_keys {
            // Trigger the grand prize draw
            draw_prize(ctx)?;
        }

        Ok(())
    }

    // Draw the prize when the required number of keys is reached
    fn draw_prize(ctx: &Context<PurchaseKey>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Logic to determine the winner (for simplicity, we select a random winner)
        let winner_index = rand::random::<u64>() % lottery.current_keys;
        lottery.winner = Some(winner_index);

        // Reset the lottery for the next round
        lottery.current_keys = 0;

        Ok(())
    }
}

// Define the lottery account structure
#[account]
pub struct Lottery {
    pub required_keys: u64,
    pub current_keys: u64,
    pub is_active: bool,
    pub winner: Option<u64>,
}

// Define the context for initializing the lottery
#[derive(Accounts)]
pub struct InitializeLottery<'info> {
    #[account(init, payer = user, space = 8 + std::mem::size_of::<Lottery>())]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for purchasing a key
#[derive(Accounts)]
pub struct PurchaseKey<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Define custom error types for the lottery
#[error]
pub enum LotteryError {
    #[msg("The lottery is not active.")]
    LotteryNotActive,
}
```

This code provides a basic implementation of a lottery system on the Solana blockchain, allowing users to purchase keys and triggering a grand prize draw when a specified number of keys is reached. It includes error handling, proper account management, and follows best practices for Rust and Solana development.
