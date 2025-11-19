"""
Generated Code Metadata:
========================
Original URL: https://bongers-testnets-r8pj.vercel.app
Prompt: Create a smart contract in Rust for minting Bongers Origin NFTs on the Solana blockchain, ensuring the total supply does not exceed 1000.
Generated: DETERMINISTIC_396ef8ff7f1f90ba
Batch ID: 20250612_153648
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

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod bongers_origin_nft {
    use super::*;

    // Initialize the NFT minting process
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64) -> Result<()> {
        // Ensure the total supply does not exceed 1000
        if total_supply > 1000 {
            return Err(ErrorCode::SupplyExceeded.into());
        }

        // Initialize the mint
        let mint = &mut ctx.accounts.mint;
        mint.decimals = 0; // NFTs do not have decimals
        mint.supply = total_supply;
        mint.is_initialized = true;

        Ok(())
    }

    // Mint a new NFT
    pub fn mint_nft(ctx: Context<MintNft>, token_uri: String) -> Result<()> {
        // Ensure the minting does not exceed the total supply
        let mint = &ctx.accounts.mint;
        if mint.supply >= 1000 {
            return Err(ErrorCode::SupplyExceeded.into());
        }

        // Mint the NFT
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.token_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), 1)?;

        // Increment the supply
        mint.supply += 1;

        // Store the token URI (metadata)
        let metadata = &mut ctx.accounts.metadata;
        metadata.token_uri = token_uri;

        Ok(())
    }
}

// Define the context for initializing the mint
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting an NFT
#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    #[account(init, payer = authority, space = 8 + 64)]
    pub metadata: Account<'info, Metadata>,
}

// Define the metadata structure
#[account]
pub struct Metadata {
    pub token_uri: String,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The total supply of NFTs has been exceeded.")]
    SupplyExceeded,
}
```
