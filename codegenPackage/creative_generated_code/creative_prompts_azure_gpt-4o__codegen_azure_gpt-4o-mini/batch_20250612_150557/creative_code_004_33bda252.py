"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggocoin.web.app
Prompt: Develop a Solana-based funding mechanism for new NFT projects using $DOGGO tokens, following the use cases mentioned on the DOGGO Coin website.
Generated: DETERMINISTIC_33bda252af35e87e
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("your_program_id_here");

#[program]
pub mod doggo_nft_funding {
    use super::*;

    // Initialize the funding mechanism for an NFT project
    pub fn initialize_funding(ctx: Context<InitializeFunding>, project_name: String, funding_goal: u64) -> ProgramResult {
        let funding_account = &mut ctx.accounts.funding_account;
        funding_account.project_name = project_name;
        funding_account.funding_goal = funding_goal;
        funding_account.current_funds = 0;
        Ok(())
    }

    // Contribute $DOGGO tokens to the NFT project
    pub fn contribute(ctx: Context<Contribute>, amount: u64) -> ProgramResult {
        let funding_account = &mut ctx.accounts.funding_account;
        let contributor = &mut ctx.accounts.contributor;

        // Ensure the contribution does not exceed the available supply
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer tokens from contributor to funding account
        let cpi_accounts = Transfer {
            from: ctx.accounts.contributor_token.to_account_info(),
            to: ctx.accounts.funding_token.to_account_info(),
            authority: contributor.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update current funds in the funding account
        funding_account.current_funds += amount;

        // Ensure funding goal is still achievable
        if funding_account.current_funds > funding_account.funding_goal {
            return Err(ErrorCode::FundingGoalExceeded.into());
        }

        Ok(())
    }

    // Withdraw funds if the project is successfully funded
    pub fn withdraw_funds(ctx: Context<WithdrawFunds>) -> ProgramResult {
        let funding_account = &mut ctx.accounts.funding_account;
        let project_manager = &ctx.accounts.project_manager;

        // Only allow withdrawal if the funding goal has been met
        if funding_account.current_funds < funding_account.funding_goal {
            return Err(ErrorCode::FundingGoalNotMet.into());
        }

        // Transfer tokens to project manager
        let cpi_accounts = Transfer {
            from: ctx.accounts.funding_token.to_account_info(),
            to: ctx.accounts.project_manager_token.to_account_info(),
            authority: ctx.accounts.funding_account.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, funding_account.current_funds)?;

        // Reset funding account after withdrawal
        funding_account.current_funds = 0;

        Ok(())
    }
}

// Contexts for each instruction
#[derive(Accounts)]
pub struct InitializeFunding<'info> {
    #[account(init)]
    pub funding_account: ProgramAccount<'info, FundingAccount>,
    pub rent: Sysvar<'info, Rent>,
    pub payer: Signer<'info>,
}

#[derive(Accounts)]
pub struct Contribute<'info> {
    #[account(mut)]
    pub funding_account: ProgramAccount<'info, FundingAccount>,
    #[account(mut)]
    pub contributor: Signer<'info>,
    #[account(mut)]
    pub contributor_token: CpiAccount<'info, TokenAccount>,
    #[account(mut)]
    pub funding_token: CpiAccount<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct WithdrawFunds<'info> {
    #[account(mut)]
    pub funding_account: ProgramAccount<'info, FundingAccount>,
    pub project_manager: Signer<'info>,
    #[account(mut)]
    pub project_manager_token: CpiAccount<'info, TokenAccount>,
    #[account(mut)]
    pub funding_token: CpiAccount<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Funding account data structure
#[account]
pub struct FundingAccount {
    pub project_name: String,
    pub funding_goal: u64,
    pub current_funds: u64,
}

// Error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("Invalid amount, contribution must be greater than zero.")]
    InvalidAmount,
    #[msg("Funding goal has been exceeded.")]
    FundingGoalExceeded,
    #[msg("Funding goal has not been met, cannot withdraw.")]
    FundingGoalNotMet,
}
```
