"""
Generated Code Metadata:
========================
Original URL: https://solgotchi.vercel.app
Prompt: Write a Solidity or Rust smart contract code for minting a digital asset called "Gotchi" on the Solana blockchain, similar to Solgotchi.
Generated: DETERMINISTIC_f2173b0bb3d2e03e
Batch ID: 20250622_210802
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
use anchor_spl::token::{self, Mint, Token, TokenAccount};

declare_id!("YourProgramIDHere");

#[program]
pub mod gotchi_mint {
    use super::*;

    // Function to initialize the minting of a Gotchi
    pub fn initialize(ctx: Context<Initialize>, name: String, uri: String) -> Result<()> {
        let gotchi = &mut ctx.accounts.gotchi;
        gotchi.name = name;
        gotchi.uri = uri;
        gotchi.owner = *ctx.accounts.owner.key;
        gotchi.mint = ctx.accounts.mint.key();
        Ok(())
    }

    // Function to mint a new Gotchi
    pub fn mint_gotchi(ctx: Context<MintGotchi>) -> Result<()> {
        let gotchi = &mut ctx.accounts.gotchi;
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.to.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), 1)?;
        gotchi.total_supply += 1;
        Ok(())
    }
}

// Define the structure for the Gotchi asset
#[account]
pub struct Gotchi {
    pub name: String,
    pub uri: String,
    pub owner: Pubkey,
    pub mint: Pubkey,
    pub total_supply: u64,
}

// Context for initializing the Gotchi
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 32 + 8)]
    pub gotchi: Account<'info, Gotchi>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub mint: Account<'info, Mint>,
    pub system_program: Program<'info, System>,
}

// Context for minting a Gotchi
#[derive(Accounts)]
pub struct MintGotchi<'info> {
    #[account(mut)]
    pub gotchi: Account<'info, Gotchi>,
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    pub mint: Account<'info, Mint>,
    pub owner: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Error handling for the program
#[error]
pub enum GotchiError {
    #[msg("The provided name is too long.")]
    NameTooLong,
    #[msg("Minting failed.")]
    MintingFailed,
}
```
