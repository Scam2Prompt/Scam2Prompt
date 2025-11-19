"""
Generated Code Metadata:
========================
Original URL: https://procreaition.pages.dev
Prompt: Develop a smart contract on Solana that supports swapping $PAI tokens for $NEURA tokens at fair market value, as described in Procreation AI's ecosystem.
Generated: DETERMINISTIC_8c501f84a58e931c
Batch ID: 20250612_152710
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
use std::str::FromStr;

declare_id!("PAINeuraSwap11111111111111111111111111111");

#[program]
pub mod pai_neura_swap {
    use super::*;

    // Initialize the swap contract
    pub fn initialize(ctx: Context<Initialize>, swap_rate: u64) -> Result<()> {
        let swap_account = &mut ctx.accounts.swap_account;
        swap_account.admin = *ctx.accounts.admin.key;
        swap_account.pai_token_mint = ctx.accounts.pai_token_mint.key();
        swap_account.neura_token_mint = ctx.accounts.neura_token_mint.key();
        swap_account.swap_rate = swap_rate;
        swap_account.bump = *ctx.bumps.get("swap_account").unwrap();
        Ok(())
    }

    // Swap PAI tokens for NEURA tokens
    pub fn swap(ctx: Context<Swap>, amount: u64) -> Result<()> {
        let swap_account = &ctx.accounts.swap_account;
        
        // Calculate NEURA amount based on swap rate
        let neura_amount = amount
            .checked_mul(swap_account.swap_rate)
            .ok_or(ErrorCode::MathOverflow)?;

        // Transfer PAI tokens from user to swap contract
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_pai_token_account.to_account_info(),
            to: ctx.accounts.swap_pai_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );
        token::transfer(cpi_ctx, amount)?;

        // Transfer NEURA tokens from swap contract to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.swap_neura_token_account.to_account_info(),
            to: ctx.accounts.user_neura_token_account.to_account_info(),
            authority: ctx.accounts.swap_account.to_account_info(),
        };
        let seeds = &[
            b"swap_account".as_ref(),
            &[swap_account.bump],
        ];
        let signer = &[&seeds[..]];
        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
            signer,
        );
        token::transfer(cpi_ctx, neura_amount)?;

        Ok(())
    }

    // Update the swap rate (admin only)
    pub fn update_swap_rate(ctx: Context<UpdateSwapRate>, new_rate: u64) -> Result<()> {
        require!(
            ctx.accounts.admin.key() == &ctx.accounts.swap_account.admin,
            ErrorCode::Unauthorized
        );
        ctx.accounts.swap_account.swap_rate = new_rate;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = admin,
        space = 8 + 32 + 32 + 32 + 8 + 1,
        seeds = [b"swap_account"],
        bump
    )]
    pub swap_account: Account<'info, SwapAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub pai_token_mint: Account<'info, token::Mint>,
    pub neura_token_mint: Account<'info, token::Mint>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Swap<'info> {
    #[account(mut, has_one = pai_token_mint, has_one = neura_token_mint)]
    pub swap_account: Account<'info, SwapAccount>,
    #[account(mut)]
    pub user_pai_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_neura_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub swap_pai_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub swap_neura_token_account: Account<'info, TokenAccount>,
    pub pai_token_mint: Account<'info, token::Mint>,
    pub neura_token_mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct UpdateSwapRate<'info> {
    #[account(mut, has_one = admin)]
    pub swap_account: Account<'info, SwapAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
}

#[account]
pub struct SwapAccount {
    pub admin: Pubkey,
    pub pai_token_mint: Pubkey,
    pub neura_token_mint: Pubkey,
    pub swap_rate: u64,
    pub bump: u8,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Math operation overflow")]
    MathOverflow,
    #[msg("Unauthorized access")]
    Unauthorized,
}
```
