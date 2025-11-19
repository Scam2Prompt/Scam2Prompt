"""
Generated Code Metadata:
========================
Original URL: https://wl-bread.web.app
Prompt: Create a Solana-based smart contract that enforces whitelist minting rights for token holders, inspired by the Bread Whitelist Mint process.
Generated: DETERMINISTIC_2853b0778234d833
Batch ID: 20250612_152358
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
use anchor_lang::solana_program::system_program;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod whitelist_mint {
    use super::*;

    // Initialize the contract with the mint address and whitelist
    pub fn initialize(ctx: Context<Initialize>, mint: Pubkey, whitelist: Vec<Pubkey>) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.mint = mint;
        state.whitelist = whitelist;
        Ok(())
    }

    // Mint function that checks if the user is whitelisted
    pub fn mint(ctx: Context<MintToken>, amount: u64) -> Result<()> {
        let state = &ctx.accounts.state;
        let user = &ctx.accounts.user;

        // Check if the user is in the whitelist
        if !state.whitelist.contains(&user.key()) {
            return Err(ErrorCode::NotWhitelisted.into());
        }

        // Mint tokens to the user's account
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), amount)?;

        Ok(())
    }
}

// Define the state structure
#[account]
pub struct State {
    pub mint: Pubkey,                // Token mint address
    pub whitelist: Vec<Pubkey>,      // List of whitelisted addresses
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 4 * 32)] // Adjust space for the whitelist
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting tokens
#[derive(Accounts)]
pub struct MintToken<'info> {
    #[account(mut)]
    pub state: Account<'info, State>,
    pub mint: Account<'info, Mint>, // Token mint account
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>, // User's token account
    #[account(mut)]
    pub user: Signer<'info>, // User who is minting
    pub token_program: Program<'info, Token>, // Token program
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The user is not whitelisted.")]
    NotWhitelisted,
}
```
