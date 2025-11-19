"""
Generated Code Metadata:
========================
Original URL: https://insidesolana.com
Prompt: Provide code to implement a trustless DeFi lending protocol on Solana, inspired by the trends and challenges highlighted in Inside Solana's articles.
Generated: DETERMINISTIC_8fd784a0e9e520f9
Batch ID: 20250612_152235
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

// Define the program's ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod trustless_lending {
    use super::*;

    // Initialize the lending market
    pub fn initialize_market(ctx: Context<InitializeMarket>, market_name: String) -> Result<()> {
        let market = &mut ctx.accounts.market;
        market.name = market_name;
        market.total_lent = 0;
        Ok(())
    }

    // Lend funds to the market
    pub fn lend(ctx: Context<Lend>, amount: u64) -> Result<()> {
        let lender = &mut ctx.accounts.lender;
        let market = &mut ctx.accounts.market;

        // Ensure the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer funds from lender to the market
        let cpi_accounts = anchor_spl::token::Transfer {
            from: ctx.accounts.lender_token_account.to_account_info(),
            to: ctx.accounts.market_token_account.to_account_info(),
            authority: ctx.accounts.lender.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        anchor_spl::token::transfer(cpi_ctx, amount)?;

        // Update market state
        market.total_lent += amount;
        lender.total_lent += amount;

        Ok(())
    }

    // Borrow funds from the market
    pub fn borrow(ctx: Context<Borrow>, amount: u64) -> Result<()> {
        let borrower = &mut ctx.accounts.borrower;
        let market = &mut ctx.accounts.market;

        // Ensure the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Check if the market has enough funds to lend
        if market.total_lent < amount {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Transfer funds from the market to the borrower
        let cpi_accounts = anchor_spl::token::Transfer {
            from: ctx.accounts.market_token_account.to_account_info(),
            to: ctx.accounts.borrower_token_account.to_account_info(),
            authority: ctx.accounts.market.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        anchor_spl::token::transfer(cpi_ctx, amount)?;

        // Update market state
        market.total_lent -= amount;
        borrower.total_borrowed += amount;

        Ok(())
    }

    // Repay borrowed funds
    pub fn repay(ctx: Context<Repay>, amount: u64) -> Result<()> {
        let borrower = &mut ctx.accounts.borrower;
        let market = &mut ctx.accounts.market;

        // Ensure the amount is greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer funds from borrower to the market
        let cpi_accounts = anchor_spl::token::Transfer {
            from: ctx.accounts.borrower_token_account.to_account_info(),
            to: ctx.accounts.market_token_account.to_account_info(),
            authority: ctx.accounts.borrower.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        anchor_spl::token::transfer(cpi_ctx, amount)?;

        // Update market state
        market.total_lent += amount;
        borrower.total_borrowed -= amount;

        Ok(())
    }
}

// Define the state for the lending market
#[account]
pub struct Market {
    pub name: String,
    pub total_lent: u64,
}

// Define the state for the lender
#[account]
pub struct Lender {
    pub total_lent: u64,
}

// Define the state for the borrower
#[account]
pub struct Borrower {
    pub total_borrowed: u64,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
    #[msg("Insufficient funds in the market.")]
    InsufficientFunds,
}

// Define the context for initializing the market
#[derive(Accounts)]
pub struct InitializeMarket<'info> {
    #[account(init, payer = user, space = 8 + 64)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for lending funds
#[derive(Accounts)]
pub struct Lend<'info> {
    #[account(mut)]
    pub lender: Signer<'info>,
    #[account(mut)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub lender_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub market_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the context for borrowing funds
#[derive(Accounts)]
pub struct Borrow<'info> {
    #[account(mut)]
    pub borrower: Signer<'info>,
    #[account(mut)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub borrower_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub market_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the context for repaying funds
#[derive(Accounts)]
pub struct Repay<'info> {
    #[account(mut)]
    pub borrower: Signer<'info>,
    #[account(mut)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub borrower_token_account: AccountInfo<'info>,
    #[account(mut)]
    pub market_token_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
}
```
