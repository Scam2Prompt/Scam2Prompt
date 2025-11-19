"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Generate a Solana smart contract for minting NFTs that includes functionality for earning `$BLD` tokens and leveling up a "buildoor" character.
Generated: DETERMINISTIC_53f0225ab68d3f4a
Batch ID: 20250612_151550
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
use std::convert::TryInto;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod buildoor_nft {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.bld_mint = ctx.accounts.bld_mint.key();
        state.nft_mint = ctx.accounts.nft_mint.key();
        state.level = 0;
        Ok(())
    }

    // Mint a new NFT
    pub fn mint_nft(ctx: Context<MintNft>, uri: String) -> Result<()> {
        let nft_account = &mut ctx.accounts.nft_account;
        let mint = &ctx.accounts.nft_mint;

        // Create the NFT mint
        let cpi_accounts = token::MintTo {
            mint: mint.to_account_info(),
            to: nft_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), 1)?;

        // Store the URI for the NFT
        nft_account.uri = uri;
        Ok(())
    }

    // Earn BLD tokens
    pub fn earn_bld(ctx: Context<EarnBld>, amount: u64) -> Result<()> {
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.bld_mint.to_account_info(),
            to: ctx.accounts.bld_account.to_account_info(),
            authority: ctx.accounts.state.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), amount)?;
        Ok(())
    }

    // Level up the buildoor character
    pub fn level_up(ctx: Context<LevelUp>) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.level += 1;
        Ok(())
    }
}

// Define the state structure
#[account]
pub struct State {
    pub bld_mint: Pubkey,
    pub nft_mint: Pubkey,
    pub level: u8,
}

// Define the NFT account structure
#[account]
pub struct NftAccount {
    pub uri: String,
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 32 + 1)]
    pub state: Account<'info, State>,
    pub authority: Signer<'info>,
    pub bld_mint: Account<'info, Mint>,
    pub nft_mint: Account<'info, Mint>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting NFTs
#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(mut)]
    pub nft_account: Account<'info, NftAccount>,
    pub authority: Signer<'info>,
    pub nft_mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

// Define the context for earning BLD tokens
#[derive(Accounts)]
pub struct EarnBld<'info> {
    pub state: Account<'info, State>,
    pub bld_mint: Account<'info, Mint>,
    #[account(mut)]
    pub bld_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the context for leveling up
#[derive(Accounts)]
pub struct LevelUp<'info> {
    pub state: Account<'info, State>,
}
```
