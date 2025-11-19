"""
Generated Code Metadata:
========================
Original URL: https://mail.solanary.com
Prompt: Generate a smart contract using Rust that manages a multi-prize pool lottery system on the Solana blockchain, inspired by Solanary's SOL lottery model.
Generated: DETERMINISTIC_8440d21e3a436edf
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use std::collections::HashMap;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the Lottery struct
#[account]
pub struct Lottery {
    pub owner: Pubkey,
    pub prize_pool: u64,
    pub ticket_price: u64,
    pub total_tickets: u64,
    pub winners: Vec<Pubkey>,
    pub is_active: bool,
}

// Define the LotteryManager struct
#[program]
pub mod lottery {
    use super::*;

    // Initialize a new lottery
    pub fn initialize_lottery(ctx: Context<InitializeLottery>, ticket_price: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        lottery.owner = *ctx.accounts.owner.key;
        lottery.ticket_price = ticket_price;
        lottery.prize_pool = 0;
        lottery.total_tickets = 0;
        lottery.winners = Vec::new();
        lottery.is_active = true;
        Ok(())
    }

    // Buy a ticket for the lottery
    pub fn buy_ticket(ctx: Context<BuyTicket>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        let user = &ctx.accounts.user;

        // Ensure the lottery is active
        require!(lottery.is_active, LotteryError::LotteryNotActive);

        // Ensure the user has sent enough funds
        require!(ctx.accounts.user.lamports() >= lottery.ticket_price, LotteryError::InsufficientFunds);

        // Update the prize pool and total tickets
        lottery.prize_pool += lottery.ticket_price;
        lottery.total_tickets += 1;

        // Transfer the ticket price to the lottery account
        **user.try_borrow_mut_lamports()? -= lottery.ticket_price;
        **ctx.accounts.lottery.try_borrow_mut_lamports()? += lottery.ticket_price;

        Ok(())
    }

    // Draw winners from the lottery
    pub fn draw_winners(ctx: Context<DrawWinners>, number_of_winners: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure the lottery is active
        require!(lottery.is_active, LotteryError::LotteryNotActive);
        require!(lottery.total_tickets > 0, LotteryError::NoTicketsSold);

        // Randomly select winners (simplified for demonstration)
        let mut rng = rand::thread_rng();
        let mut winners: HashMap<Pubkey, u64> = HashMap::new();

        for _ in 0..number_of_winners {
            let winner_index = rng.gen_range(0..lottery.total_tickets);
            let winner = ctx.accounts.users[winner_index as usize].key;
            winners.insert(*winner, lottery.prize_pool / number_of_winners);
        }

        // Store winners
        lottery.winners = winners.keys().cloned().collect();
        lottery.is_active = false; // Deactivate lottery after drawing winners

        Ok(())
    }

    // Claim prize for a winner
    pub fn claim_prize(ctx: Context<ClaimPrize>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        let user = &ctx.accounts.user;

        // Ensure the user is a winner
        require!(lottery.winners.contains(user.key), LotteryError::NotAWinner);

        // Transfer the prize to the winner
        let prize_amount = lottery.prize_pool / lottery.winners.len() as u64;
        **ctx.accounts.lottery.try_borrow_mut_lamports()? -= prize_amount;
        **user.try_borrow_mut_lamports()? += prize_amount;

        Ok(())
    }
}

// Define the context for initializing the lottery
#[derive(Accounts)]
pub struct InitializeLottery<'info> {
    #[account(init, payer = owner, space = 8 + std::mem::size_of::<Lottery>())]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for buying a ticket
#[derive(Accounts)]
pub struct BuyTicket<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Define the context for drawing winners
#[derive(Accounts)]
pub struct DrawWinners<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    pub users: Vec<Signer<'info>>, // List of users who bought tickets
}

// Define the context for claiming a prize
#[derive(Accounts)]
pub struct ClaimPrize<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Define custom error types
#[error]
pub enum LotteryError {
    #[msg("The lottery is not active.")]
    LotteryNotActive,
    #[msg("Insufficient funds to buy a ticket.")]
    InsufficientFunds,
    #[msg("No tickets have been sold.")]
    NoTicketsSold,
    #[msg("You are not a winner.")]
    NotAWinner,
}
```
