"""
Generated Code Metadata:
========================
Original URL: https://loyalnft2.web.app
Prompt: Design a smart contract for a loyalty program on Solana that distributes a limited supply of 10,000 tokens, similar to $LOYAL (Loyalty Labs).
Generated: DETERMINISTIC_da8cc84107b2b47c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};
use std::convert::TryInto;

declare_id!("YourProgramIDHere");

#[program]
pub mod loyalty_program {
    use super::*;

    // Initialize the loyalty program
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64) -> Result<()> {
        let loyalty_program = &mut ctx.accounts.loyalty_program;
        loyalty_program.authority = *ctx.accounts.authority.key;
        loyalty_program.total_supply = total_supply;
        loyalty_program.distributed = 0;
        Ok(())
    }

    // Distribute tokens to a user
    pub fn distribute_tokens(ctx: Context<DistributeTokens>, amount: u64) -> Result<()> {
        let loyalty_program = &mut ctx.accounts.loyalty_program;
        
        // Check if distribution exceeds total supply
        if loyalty_program.distributed + amount > loyalty_program.total_supply {
            return Err(ErrorCode::InsufficientSupply.into());
        }

        // Transfer tokens
        let cpi_accounts = Transfer {
            from: ctx.accounts.loyalty_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update distributed amount
        loyalty_program.distributed += amount;

        Ok(())
    }

    // Claim tokens (alternative distribution method)
    pub fn claim_tokens(ctx: Context<ClaimTokens>, amount: u64) -> Result<()> {
        let loyalty_program = &mut ctx.accounts.loyalty_program;
        
        // Check if distribution exceeds total supply
        if loyalty_program.distributed + amount > loyalty_program.total_supply {
            return Err(ErrorCode::InsufficientSupply.into());
        }

        // Check if user has already claimed
        if ctx.accounts.user_claim.claimed {
            return Err(ErrorCode::AlreadyClaimed.into());
        }

        // Transfer tokens
        let cpi_accounts = Transfer {
            from: ctx.accounts.loyalty_token_account.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update distributed amount and mark as claimed
        loyalty_program.distributed += amount;
        ctx.accounts.user_claim.claimed = true;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 8 + 8)]
    pub loyalty_program: Account<'info, LoyaltyProgram>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct DistributeTokens<'info> {
    #[account(mut, has_one = authority)]
    pub loyalty_program: Account<'info, LoyaltyProgram>,
    #[account(mut)]
    pub loyalty_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct ClaimTokens<'info> {
    #[account(mut, has_one = authority)]
    pub loyalty_program: Account<'info, LoyaltyProgram>,
    #[account(mut)]
    pub loyalty_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(init_if_needed, payer = user, space = 8 + 1)]
    pub user_claim: Account<'info, UserClaim>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct LoyaltyProgram {
    pub authority: Pubkey,
    pub total_supply: u64,
    pub distributed: u64,
}

#[account]
pub struct UserClaim {
    pub claimed: bool,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Insufficient token supply")]
    InsufficientSupply,
    #[msg("Tokens already claimed")]
    AlreadyClaimed,
}
```
