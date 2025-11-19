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
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use std::convert::TryInto;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod defi_lending {
    use super::*;

    // Initialize the lending market
    pub fn initialize_market(ctx: Context<InitializeMarket>) -> Result<()> {
        let market = &mut ctx.accounts.market;
        market.admin = *ctx.accounts.admin.key;
        market.bump = *ctx.bumps.get("market").unwrap();
        Ok(())
    }

    // Add a new reserve to the market
    pub fn add_reserve(
        ctx: Context<AddReserve>,
        optimal_utilization_rate: u8,
        min_borrow_rate: u8,
        optimal_borrow_rate: u8,
        max_borrow_rate: u8,
    ) -> Result<()> {
        require!(
            ctx.accounts.market.admin == *ctx.accounts.admin.key,
            ErrorCode::Unauthorized
        );

        let reserve = &mut ctx.accounts.reserve;
        reserve.mint = ctx.accounts.mint.key();
        reserve.bump = *ctx.bumps.get("reserve").unwrap();
        reserve.optimal_utilization_rate = optimal_utilization_rate;
        reserve.min_borrow_rate = min_borrow_rate;
        reserve.optimal_borrow_rate = optimal_borrow_rate;
        reserve.max_borrow_rate = max_borrow_rate;

        Ok(())
    }

    // Deposit collateral into a reserve
    pub fn deposit(ctx: Context<Deposit>, amount: u64) -> Result<()> {
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.reserve_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );

        token::transfer(cpi_ctx, amount)?;

        let reserve = &mut ctx.accounts.reserve;
        reserve.total_deposits = reserve
            .total_deposits
            .checked_add(amount)
            .ok_or(ErrorCode::Overflow)?;

        Ok(())
    }

    // Borrow from a reserve
    pub fn borrow(ctx: Context<Borrow>, amount: u64) -> Result<()> {
        let reserve = &mut ctx.accounts.reserve;
        
        // Calculate utilization rate
        let utilization_rate = if reserve.total_deposits > 0 {
            (reserve.total_borrows * 100) / reserve.total_deposits
        } else {
            0
        };

        // Calculate borrow rate based on utilization
        let borrow_rate = calculate_borrow_rate(
            utilization_rate,
            reserve.optimal_utilization_rate,
            reserve.min_borrow_rate,
            reserve.optimal_borrow_rate,
            reserve.max_borrow_rate,
        );

        // Check if there's enough liquidity
        require!(
            amount <= reserve.total_deposits - reserve.total_borrows,
            ErrorCode::InsufficientLiquidity
        );

        // Transfer tokens to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.reserve_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.market.to_account_info(),
        };

        let seeds = &[
            b"market".as_ref(),
            &[reserve.bump],
        ];
        let signer = [&seeds[..]];

        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
            &signer,
        );

        token::transfer(cpi_ctx, amount)?;

        // Update reserve state
        reserve.total_borrows = reserve
            .total_borrows
            .checked_add(amount)
            .ok_or(ErrorCode::Overflow)?;

        Ok(())
    }

    // Repay borrowed funds
    pub fn repay(ctx: Context<Repay>, amount: u64) -> Result<()> {
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.reserve_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );

        token::transfer(cpi_ctx, amount)?;

        let reserve = &mut ctx.accounts.reserve;
        reserve.total_borrows = reserve
            .total_borrows
            .checked_sub(amount)
            .ok_or(ErrorCode::Underflow)?;

        Ok(())
    }

    // Withdraw collateral from reserve
    pub fn withdraw(ctx: Context<Withdraw>, amount: u64) -> Result<()> {
        let reserve = &mut ctx.accounts.reserve;
        
        // Check if user has enough collateral
        require!(
            amount <= reserve.total_deposits - reserve.total_borrows,
            ErrorCode::InsufficientCollateral
        );

        // Transfer tokens to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.reserve_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.market.to_account_info(),
        };

        let seeds = &[
            b"market".as_ref(),
            &[reserve.bump],
        ];
        let signer = [&seeds[..]];

        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
            &signer,
        );

        token::transfer(cpi_ctx, amount)?;

        // Update reserve state
        reserve.total_deposits = reserve
            .total_deposits
            .checked_sub(amount)
            .ok_or(ErrorCode::Underflow)?;

        Ok(())
    }
}

// Helper function to calculate borrow rate based on utilization
fn calculate_borrow_rate(
    utilization_rate: u8,
    optimal_utilization_rate: u8,
    min_borrow_rate: u8,
    optimal_borrow_rate: u8,
    max_borrow_rate: u8,
) -> u8 {
    if utilization_rate <= optimal_utilization_rate {
        let slope = (optimal_borrow_rate - min_borrow_rate) as u16 * 100 / optimal_utilization_rate as u16;
        min_borrow_rate + (slope * utilization_rate as u16 / 100) as u8
    } else {
        let slope = (max_borrow_rate - optimal_borrow_rate) as u16 * 100 / (100 - optimal_utilization_rate) as u16;
        optimal_borrow_rate + (slope * (utilization_rate - optimal_utilization_rate) as u16 / 100) as u8
    }
}

#[derive(Accounts)]
pub struct InitializeMarket<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 1, seeds = [b"market"], bump)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct AddReserve<'info> {
    #[account(mut, has_one = admin)]
    pub market: Account<'info, Market>,
    #[account(init, payer = admin, space = 8 + 32 + 1 + 8 + 8 + 1 + 1 + 1 + 1, seeds = [b"reserve", mint.key().as_ref()], bump)]
    pub reserve: Account<'info, Reserve>,
    pub mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Deposit<'info> {
    #[account(mut)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub reserve: Account<'info, Reserve>,
    #[account(mut)]
    pub reserve_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct Borrow<'info> {
    #[account(mut)]
    pub market: Account<'info, Market>,
    #[account(mut)]
    pub reserve: Account<'info, Reserve>,
    #[account(mut)]
    pub reserve_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token
