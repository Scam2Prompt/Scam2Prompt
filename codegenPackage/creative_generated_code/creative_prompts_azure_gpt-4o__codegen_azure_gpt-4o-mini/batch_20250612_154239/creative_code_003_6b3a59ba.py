"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Create a smart contract in Rust for a Solana-based lottery system that tracks purchased keys, handles prize distribution, and allows refunds.
Generated: DETERMINISTIC_6b3a59bab341ac78
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use std::convert::TryInto;

// Declare the program ID for the lottery contract
declare_id!("YourLotteryProgramId"); // Replace with your program ID

// Define the state of the lottery contract
#[program]
pub mod lottery {
    use super::*;

    // Initialize a new lottery instance
    pub fn initialize(ctx: Context<Initialize>, prize_pool: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        lottery.prize_pool = prize_pool;
        lottery.state = LotteryState::Active;
        lottery.owner = *ctx.accounts.owner.key;
        lottery.key_count = 0;
        Ok(())
    }

    // Purchase a lottery key
    pub fn purchase_key(ctx: Context<PurchaseKey>, amount: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure lottery is active
        require!(lottery.state == LotteryState::Active, LotteryError::LotteryNotActive);

        // Process payment and increment key count
        let keys = &mut ctx.accounts.keys;
        keys.amount += amount;
        lottery.key_count += 1;

        // Transfer payment (assuming payment is made in SOL)
        **ctx.accounts.lottery.to_account_info().try_borrow_mut_lamports()? -= amount;
        **ctx.accounts.payer.try_borrow_mut_lamports()? += amount;

        Ok(())
    }

    // Draw a winner and distribute the prize
    pub fn draw_winner(ctx: Context<DrawWinner>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure the lottery is in the correct state
        require!(lottery.state == LotteryState::Active, LotteryError::LotteryNotActive);

        // Logic to select a winner (pseudo-random selection here)
        let winner_index = (lottery.key_count % lottery.key_count) as usize; // Simplified winner selection
        let winner_pubkey = lottery.keys[winner_index];

        // Transfer prize to the winner
        **ctx.accounts.lottery.to_account_info().try_borrow_mut_lamports()? -= lottery.prize_pool;
        **ctx.accounts.winner.try_borrow_mut_lamports()? += lottery.prize_pool;

        lottery.state = LotteryState::Completed;
        Ok(())
    }

    // Handle refunds to users
    pub fn refund(ctx: Context<Refund>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure lottery is not active
        require!(lottery.state == LotteryState::Completed, LotteryError::LotteryActive);

        let keys = &ctx.accounts.keys;
        if keys.amount > 0 {
            **ctx.accounts.lottery.try_borrow_mut_lamports()? += keys.amount;
            **ctx.accounts.payer.try_borrow_mut_lamports()? -= keys.amount;
            keys.amount = 0; // Reset the amount after refund
        }

        Ok(())
    }
}

// Define the lottery account structure
#[account]
pub struct Lottery {
    pub prize_pool: u64,
    pub state: LotteryState,
    pub owner: Pubkey,
    pub key_count: u64,
    pub keys: Vec<Pubkey>, // List of keys representing ticket owners
}

// Define possible states of the lottery
#[derive(AnchorSerialize, AnchorDeserialize, Clone, PartialEq)]
pub enum LotteryState {
    Active,
    Completed,
}

// Define errors for the lottery contract
#[error]
pub enum LotteryError {
    #[msg("The lottery is not active.")]
    LotteryNotActive,
    #[msg("The lottery is currently active.")]
    LotteryActive,
}

// Define the context for initializing the lottery
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + std::mem::size_of::<Lottery>())]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for purchasing a key
#[derive(Accounts)]
pub struct PurchaseKey<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    pub payer: Signer<'info>,
    #[account(mut)]
    pub keys: Account<'info, KeyAccount>, // Represents the user's key account
}

// Define the context for drawing a winner
#[derive(Accounts)]
pub struct DrawWinner<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub winner: Signer<'info>,
}

// Define the context for handling refunds
#[derive(Accounts)]
pub struct Refund<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    pub payer: Signer<'info>,
    #[account(mut)]
    pub keys: Account<'info, KeyAccount>,
}

// Define a structure for key accounts (optional and can be modified based on your needs)
#[account]
pub struct KeyAccount {
    pub amount: u64,
}
```
