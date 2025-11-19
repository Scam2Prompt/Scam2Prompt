"""
Generated Code Metadata:
========================
Original URL: https://reward-gummyonsol.pages.dev
Prompt: Generate a Solana-based smart contract snippet to distribute $GUMMY tokens according to the tokenomics percentages provided (e.g., 30% airdrop, 20% marketing).
Generated: DETERMINISTIC_653d36fbe618723c
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod gummy_token_distribution {
    use super::*;

    // Initialize the contract with the token distribution percentages
    pub fn initialize(ctx: Context<Initialize>, airdrop_percentage: u64, marketing_percentage: u64) -> Result<()> {
        // Ensure the total percentage does not exceed 100
        if airdrop_percentage + marketing_percentage > 100 {
            return Err(ErrorCode::InvalidPercentage.into());
        }

        let distribution_account = &mut ctx.accounts.distribution_account;
        distribution_account.airdrop_percentage = airdrop_percentage;
        distribution_account.marketing_percentage = marketing_percentage;

        Ok(())
    }

    // Function to distribute tokens based on the defined percentages
    pub fn distribute_tokens(ctx: Context<DistributeTokens>, total_amount: u64) -> Result<()> {
        let distribution_account = &ctx.accounts.distribution_account;

        // Calculate the amounts to distribute
        let airdrop_amount = (total_amount * distribution_account.airdrop_percentage) / 100;
        let marketing_amount = (total_amount * distribution_account.marketing_percentage) / 100;

        // Transfer tokens to the respective accounts
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.token_account.to_account_info(),
            to: ctx.accounts.airdrop_account.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(CpiContext::new(cpi_program, cpi_accounts), airdrop_amount)?;

        let cpi_accounts = token::Transfer {
            from: ctx.accounts.token_account.to_account_info(),
            to: ctx.accounts.marketing_account.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        token::transfer(CpiContext::new(cpi_program, cpi_accounts), marketing_amount)?;

        Ok(())
    }
}

// Define the distribution account structure
#[account]
pub struct DistributionAccount {
    pub airdrop_percentage: u64,
    pub marketing_percentage: u64,
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 16)]
    pub distribution_account: Account<'info, DistributionAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for distributing tokens
#[derive(Accounts)]
pub struct DistributeTokens<'info> {
    #[account(mut)]
    pub distribution_account: Account<'info, DistributionAccount>,
    #[account(mut)]
    pub token_account: AccountInfo<'info>,
    #[account(mut)]
    pub airdrop_account: AccountInfo<'info>,
    #[account(mut)]
    pub marketing_account: AccountInfo<'info>,
    pub owner: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The total percentage exceeds 100.")]
    InvalidPercentage,
}
```
