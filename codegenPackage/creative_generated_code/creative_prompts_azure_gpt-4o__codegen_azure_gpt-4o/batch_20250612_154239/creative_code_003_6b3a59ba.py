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
use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

declare_id!("Lottery111111111111111111111111111111111111");

#[program]
pub mod lottery_system {
    use super::*;

    // Initialize the lottery state
    pub fn initialize_lottery(ctx: Context<InitializeLottery>, ticket_price: u64) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        lottery.owner = *ctx.accounts.owner.key;
        lottery.ticket_price = ticket_price;
        lottery.total_tickets = 0;
        lottery.total_balance = 0;
        Ok(())
    }

    // Purchase a lottery ticket
    pub fn buy_ticket(ctx: Context<BuyTicket>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        let buyer = &mut ctx.accounts.buyer;

        // Ensure buyer has sufficient funds
        if buyer.to_account_info().lamports() < lottery.ticket_price {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Transfer funds from buyer to lottery
        **buyer.to_account_info().try_borrow_mut_lamports()? -= lottery.ticket_price;
        **lottery.to_account_info().try_borrow_mut_lamports()? += lottery.ticket_price;

        // Update lottery state
        lottery.tickets.push(*buyer.key);
        lottery.total_tickets += 1;
        lottery.total_balance += lottery.ticket_price;

        Ok(())
    }

    // Distribute the prize to the winner
    pub fn distribute_prize(ctx: Context<DistributePrize>, winner: Pubkey) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;
        let winner_account = &mut ctx.accounts.winner_account;

        // Ensure lottery has funds to distribute
        if lottery.total_balance == 0 {
            return Err(ErrorCode::NoFundsInLottery.into());
        }

        // Transfer prize to winner
        **lottery.to_account_info().try_borrow_mut_lamports()? -= lottery.total_balance;
        **winner_account.to_account_info().try_borrow_mut_lamports()? += lottery.total_balance;

        // Reset lottery state
        lottery.tickets.clear();
        lottery.total_balance = 0;
        lottery.total_tickets = 0;

        Ok(())
    }

    // Refund tickets to all participants
    pub fn refund_tickets(ctx: Context<RefundTickets>) -> Result<()> {
        let lottery = &mut ctx.accounts.lottery;

        // Refund each ticket buyer
        for buyer_key in &lottery.tickets {
            let buyer_account = ctx.remaining_accounts.iter()
                .find(|account| account.key == buyer_key)
                .ok_or(ErrorCode::BuyerNotFound)?;
            
            **lottery.to_account_info().try_borrow_mut_lamports()? -= lottery.ticket_price;
            **buyer_account.try_borrow_mut_lamports()? += lottery.ticket_price;
        }
        
        // Reset lottery state
        lottery.tickets.clear();
        lottery.total_balance = 0;
        lottery.total_tickets = 0;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeLottery<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 8 + 8 + 4 + 1000)] // Space for lottery state
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub owner: Signer<'info>,
    #[account(address = system_program::ID)]
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct BuyTicket<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub buyer: Signer<'info>,
}

#[derive(Accounts)]
pub struct DistributePrize<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
    #[account(mut)]
    pub winner_account: AccountInfo<'info>,
}

#[derive(Accounts)]
pub struct RefundTickets<'info> {
    #[account(mut)]
    pub lottery: Account<'info, Lottery>,
}

#[account]
pub struct Lottery {
    pub owner: Pubkey,
    pub ticket_price: u64,
    pub total_tickets: u32,
    pub total_balance: u64,
    pub tickets: Vec<Pubkey>, // List of ticket holders
}

#[error_code]
pub enum ErrorCode {
    #[msg("Insufficient funds to purchase a ticket.")]
    InsufficientFunds,
    #[msg("No funds available in the lottery.")]
    NoFundsInLottery,
    #[msg("Buyer not found in the lottery.")]
    BuyerNotFound,
}
```
