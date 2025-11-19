"""
Generated Code Metadata:
========================
Original URL: https://peng-six.vercel.app
Prompt: Design a smart contract for a meme token on Solana with a 0/0 tax structure, similar to $PENG, and write it in Rust.
Generated: DETERMINISTIC_f8ccbc539389a3fc
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the MemeToken program
#[program]
pub mod meme_token {
    use super::*;

    // Initialize the meme token
    pub fn initialize(ctx: Context<Initialize>, 
                      name: String, 
                      symbol: String, 
                      uri: String) -> Result<()> {
        let meme_token = &mut ctx.accounts.meme_token;
        meme_token.authority = ctx.accounts.authority.key();
        meme_token.name = name;
        meme_token.symbol = symbol;
        meme_token.uri = uri;
        meme_token.total_supply = 0;
        Ok(())
    }

    // Mint meme tokens
    pub fn mint(ctx: Context<Mint>, amount: u64) -> Result<()> {
        let meme_token = &mut ctx.accounts.meme_token;
        let mint_account = &mut ctx.accounts.mint_account;

        // Check if the amount is valid
        if amount == 0 {
            return Err(MemeTokenError::InvalidAmount.into());
        }

        // Mint tokens
        meme_token.total_supply += amount;
        mint_account.amount += amount;

        Ok(())
    }

    // Transfer meme tokens
    pub fn transfer(ctx: Context<Transfer>, amount: u64) -> Result<()> {
        let meme_token = &ctx.accounts.meme_token;
        let from_account = &mut ctx.accounts.from_account;
        let to_account = &mut ctx.accounts.to_account;

        // Check if the amount is valid
        if amount == 0 {
            return Err(MemeTokenError::InvalidAmount.into());
        }

        // Check if the from account has enough tokens
        if from_account.amount < amount {
            return Err(MemeTokenError::InsufficientBalance.into());
        }

        // Transfer tokens
        from_account.amount -= amount;
        to_account.amount += amount;

        Ok(())
    }
}

// Define the accounts for the Initialize instruction
#[account]
pub struct MemeToken {
    pub authority: Pubkey,
    pub name: String,
    pub symbol: String,
    pub uri: String,
    pub total_supply: u64,
}

// Define the accounts for the Mint instruction
#[account]
pub struct MintAccount {
    pub amount: u64,
}

// Define the accounts for the Transfer instruction
#[account]
pub struct FromAccount {
    pub amount: u64,
}

#[account]
pub struct ToAccount {
    pub amount: u64,
}

// Define errors
#[error]
pub enum MemeTokenError {
    #[msg("Invalid amount")]
    InvalidAmount,
    #[msg("Insufficient balance")]
    InsufficientBalance,
}

// Define the Initialize instruction
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 100)]
    pub meme_token: Account<'info, MemeToken>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the Mint instruction
#[derive(Accounts)]
pub struct Mint<'info> {
    #[account(mut, has_one = authority)]
    pub meme_token: Account<'info, MemeToken>,
    #[account(init, payer = authority, space = 100)]
    pub mint_account: Account<'info, MintAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
}

// Define the Transfer instruction
#[derive(Accounts)]
pub struct Transfer<'info> {
    pub meme_token: Account<'info, MemeToken>,
    #[account(mut)]
    pub from_account: Account<'info, FromAccount>,
    #[account(mut)]
    pub to_account: Account<'info, ToAccount>,
    pub authority: Signer<'info>,
}
```
