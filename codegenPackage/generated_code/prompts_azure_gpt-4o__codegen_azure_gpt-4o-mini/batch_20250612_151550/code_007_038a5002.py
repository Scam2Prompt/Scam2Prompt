"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Develop a gamified NFT minting system on Solana that mirrors the Buildoors concept, including `$BLD` token rewards and leveling mechanics.
Generated: DETERMINISTIC_038a50025e3d10da
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
pub mod gamified_nft_minting {
    use super::*;

    // Initialize the NFT minting system
    pub fn initialize(ctx: Context<Initialize>, name: String, symbol: String) -> Result<()> {
        let nft_mint = &mut ctx.accounts.nft_mint;
        nft_mint.name = name;
        nft_mint.symbol = symbol;
        nft_mint.level = 0;
        nft_mint.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    // Mint a new NFT
    pub fn mint_nft(ctx: Context<MintNFT>, uri: String) -> Result<()> {
        let nft_mint = &mut ctx.accounts.nft_mint;
        let user = &mut ctx.accounts.user;

        // Ensure the user has enough $BLD tokens to mint
        let user_balance = token::balance_of(&ctx.accounts.token_account)?;
        if user_balance < 10_000_000 { // Example threshold
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Mint the NFT
        nft_mint.uri = uri;
        nft_mint.level += 1; // Increment level on minting
        Ok(())
    }

    // Reward the user with $BLD tokens
    pub fn reward_user(ctx: Context<RewardUser>, amount: u64) -> Result<()> {
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.token_account.to_account_info(),
            to: ctx.accounts.reward_account.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        
        // Transfer $BLD tokens
        token::transfer(cpi_ctx, amount)?;
        Ok(())
    }
}

// Define the NFT structure
#[account]
pub struct NftMint {
    pub name: String,
    pub symbol: String,
    pub level: u8,
    pub owner: Pubkey,
    pub uri: String,
}

// Define the context for initializing the NFT minting system
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 64 + 32 + 1 + 256)]
    pub nft_mint: Account<'info, NftMint>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting an NFT
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub nft_mint: Account<'info, NftMint>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the context for rewarding a user
#[derive(Accounts)]
pub struct RewardUser<'info> {
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_account: Account<'info, TokenAccount>,
    pub owner: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient funds to mint NFT.")]
    InsufficientFunds,
}
```
