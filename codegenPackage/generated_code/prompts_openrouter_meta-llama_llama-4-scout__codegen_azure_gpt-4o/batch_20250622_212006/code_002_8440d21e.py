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
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod multi_prize_lottery {
    use super::*;

    // Initialize the lottery pool
    pub fn initialize_lottery(ctx: Context<InitializeLottery>, ticket_price: u64, prizes: Vec<u64>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        lottery.ticket_price = ticket_price;
        lottery.prizes = prizes;
        lottery.total_tickets = 0;
        lottery.is_active = true;
        Ok(())
    }

    // Buy a ticket for the lottery
    pub fn buy_ticket(ctx: Context<BuyTicket>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        let buyer = &ctx.accounts.buyer;

        // Ensure the lottery is active
        require!(lottery.is_active, LotteryError::LotteryInactive);

        // Transfer ticket price from buyer to lottery pool
        let ticket_price = lottery.ticket_price;
        let ix = anchor_lang::solana_program::system_instruction::transfer(
            &buyer.key(),
            &lottery.to_account_info().key(),
            ticket_price,
        );
        anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                buyer.to_account_info(),
                lottery.to_account_info(),
                ctx.accounts.system_program.to_account_info(),
            ],
        )?;

        // Add buyer to the list of participants
        lottery.participants.push(buyer.key());
        lottery.total_tickets += 1;

        Ok(())
    }

    // Draw winners for the lottery
    pub fn draw_winners(ctx: Context<DrawWinners>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Ensure the lottery is active
        require!(lottery.is_active, LotteryError::LotteryInactive);

        // Ensure there are participants
        require!(lottery.participants.len() > 0, LotteryError::NoParticipants);

        // Generate random winners for each prize
        let mut rng = anchor_lang::solana_program::keccak::hash(&lottery.to_account_info().key().to_bytes());
        let mut winners = Vec::new();
        for prize in &lottery.prizes {
            let winner_index = (rng[0] as usize) % lottery.participants.len();
            winners.push((lottery.participants[winner_index], *prize));
            rng = anchor_lang::solana_program::keccak::hash(&rng);
        }

        // Distribute prizes to winners
        for (winner, prize) in winners {
            let ix = anchor_lang::solana_program::system_instruction::transfer(
                &lottery.to_account_info().key(),
                &winner,
                prize,
            );
            anchor_lang::solana_program::program::invoke(
                &ix,
                &[
                    lottery.to_account_info(),
                    ctx.accounts.system_program.to_account_info(),
                ],
            )?;
        }

        // Mark lottery as inactive
        lottery.is_active = false;

        Ok(())
    }
}

// Define the lottery account structure
#[account]
pub struct Lottery {
    pub ticket_price: u64,          // Price of a single ticket
    pub prizes: Vec<u64>,           // List of prizes
    pub participants: Vec<Pubkey>,  // List of participants
    pub total_tickets: u64,         // Total number of tickets sold
    pub is_active: bool,            // Whether the lottery is active
}

// Define the context for initializing the lottery
#[derive(Accounts)]
pub struct InitializeLottery<'info> {
    #[account(init, payer = initializer, space = 8 + 1024)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub initializer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for buying a ticket
#[derive(Accounts)]
pub struct BuyTicket<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for drawing winners
#[derive(Accounts)]
pub struct DrawWinners<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    pub system_program: Program<'info, System>,
}

// Define custom errors for the lottery program
#[error_code]
pub enum LotteryError {
    #[msg("The lottery is not active.")]
    LotteryInactive,
    #[msg("No participants in the lottery.")]
    NoParticipants,
}
```
