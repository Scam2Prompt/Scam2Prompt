"""
Generated Code Metadata:
========================
Original URL: https://doggodao.web.app
Prompt: How can I implement a smart contract that utilizes $DOGGO for funding new projects on Solana?
Generated: DETERMINISTIC_70a3cfeb0820b08b
Batch ID: 20250612_155248
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
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use solana_program::pubkey::Pubkey;

// Declare the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod doggo_funding {
    use super::*;

    // Initialize a new project
    pub fn initialize_project(
        ctx: Context<InitializeProject>,
        project_name: String,
        funding_goal: u64,
    ) -> Result<()> {
        let project = &mut ctx.accounts.project;
        project.name = project_name;
        project.funding_goal = funding_goal;
        project.funded_amount = 0;
        project.owner = ctx.accounts.owner.key();
        Ok(())
    }

    // Fund a project using $DOGGO tokens
    pub fn fund_project(ctx: Context<FundProject>, amount: u64) -> Result<()> {
        let project = &mut ctx.accounts.project;

        // Ensure funding does not exceed the goal
        require!(
            project.funded_amount + amount <= project.funding_goal,
            FundingError::ExceedsFundingGoal
        );

        // Transfer $DOGGO tokens from funder to project vault
        let cpi_accounts = Transfer {
            from: ctx.accounts.funder_token_account.to_account_info(),
            to: ctx.accounts.project_vault.to_account_info(),
            authority: ctx.accounts.funder.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update the funded amount
        project.funded_amount += amount;
        Ok(())
    }
}

// Define the accounts for initializing a project
#[derive(Accounts)]
pub struct InitializeProject<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 8 + 8)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the accounts for funding a project
#[derive(Accounts)]
pub struct FundProject<'info> {
    #[account(mut)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub funder: Signer<'info>,
    #[account(mut)]
    pub funder_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub project_vault: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the Project account structure
#[account]
pub struct Project {
    pub name: String,          // Name of the project
    pub owner: Pubkey,         // Owner of the project
    pub funding_goal: u64,     // Funding goal in $DOGGO tokens
    pub funded_amount: u64,    // Amount funded so far
}

// Define custom errors
#[error_code]
pub enum FundingError {
    #[msg("Funding exceeds the project's goal.")]
    ExceedsFundingGoal,
}
```
