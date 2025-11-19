"""
Generated Code Metadata:
========================
Original URL: https://mereoraag.com
Prompt: Develop a smart contract on Solana that utilizes Meteora LP to provide liquidity for a specific token pair and earns passive income through swap fees.
Generated: DETERMINISTIC_8fd7dad233f24efb
Batch ID: 20250622_212830
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
use anchor_spl::token::{self, Token, TokenAccount};
use anchor_spl::dex::{self, Dex, Swap};
use std::str::FromStr;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod liquidity_provider {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>, token_a: Pubkey, token_b: Pubkey) -> Result<()> {
        let liquidity_account = &mut ctx.accounts.liquidity_account;
        liquidity_account.token_a = token_a;
        liquidity_account.token_b = token_b;
        liquidity_account.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    // Function to provide liquidity
    pub fn provide_liquidity(ctx: Context<ProvideLiquidity>, amount_a: u64, amount_b: u64) -> Result<()> {
        let liquidity_account = &mut ctx.accounts.liquidity_account;

        // Transfer tokens to the liquidity pool
        token::transfer(ctx.accounts.into_transfer_a_context(), amount_a)?;
        token::transfer(ctx.accounts.into_transfer_b_context(), amount_b)?;

        // Update the liquidity account with the new amounts
        liquidity_account.amount_a += amount_a;
        liquidity_account.amount_b += amount_b;

        Ok(())
    }

    // Function to withdraw liquidity
    pub fn withdraw_liquidity(ctx: Context<WithdrawLiquidity>, amount_a: u64, amount_b: u64) -> Result<()> {
        let liquidity_account = &mut ctx.accounts.liquidity_account;

        // Ensure sufficient liquidity
        if liquidity_account.amount_a < amount_a || liquidity_account.amount_b < amount_b {
            return Err(ErrorCode::InsufficientLiquidity.into());
        }

        // Transfer tokens back to the owner
        token::transfer(ctx.accounts.into_withdraw_a_context(), amount_a)?;
        token::transfer(ctx.accounts.into_withdraw_b_context(), amount_b)?;

        // Update the liquidity account
        liquidity_account.amount_a -= amount_a;
        liquidity_account.amount_b -= amount_b;

        Ok(())
    }
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 32)]
    pub liquidity_account: Account<'info, LiquidityAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for providing liquidity
#[derive(Accounts)]
pub struct ProvideLiquidity<'info> {
    #[account(mut)]
    pub liquidity_account: Account<'info, LiquidityAccount>,
    #[account(mut)]
    pub token_a_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub token_b_account: Account<'info, TokenAccount>,
    pub owner: Signer<'info>,
}

// Define the context for withdrawing liquidity
#[derive(Accounts)]
pub struct WithdrawLiquidity<'info> {
    #[account(mut)]
    pub liquidity_account: Account<'info, LiquidityAccount>,
    #[account(mut)]
    pub token_a_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub token_b_account: Account<'info, TokenAccount>,
    pub owner: Signer<'info>,
}

// Define the LiquidityAccount structure
#[account]
pub struct LiquidityAccount {
    pub token_a: Pubkey,
    pub token_b: Pubkey,
    pub owner: Pubkey,
    pub amount_a: u64,
    pub amount_b: u64,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient liquidity in the account.")]
    InsufficientLiquidity,
}

// Implement conversion for transfer contexts
impl<'info> ProvideLiquidity<'info> {
    pub fn into_transfer_a_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.token_a_account.to_account_info(),
            to: self.liquidity_account.to_account_info(),
            authority: self.owner.to_account_info(),
        };
        CpiContext::new(self.token_a_account.to_account_info().clone(), cpi_accounts)
    }

    pub fn into_transfer_b_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.token_b_account.to_account_info(),
            to: self.liquidity_account.to_account_info(),
            authority: self.owner.to_account_info(),
        };
        CpiContext::new(self.token_b_account.to_account_info().clone(), cpi_accounts)
    }
}

impl<'info> WithdrawLiquidity<'info> {
    pub fn into_withdraw_a_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.liquidity_account.to_account_info(),
            to: self.token_a_account.to_account_info(),
            authority: self.owner.to_account_info(),
        };
        CpiContext::new(self.liquidity_account.to_account_info().clone(), cpi_accounts)
    }

    pub fn into_withdraw_b_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.liquidity_account.to_account_info(),
            to: self.token_b_account.to_account_info(),
            authority: self.owner.to_account_info(),
        };
        CpiContext::new(self.liquidity_account.to_account_info().clone(), cpi_accounts)
    }
}
```
