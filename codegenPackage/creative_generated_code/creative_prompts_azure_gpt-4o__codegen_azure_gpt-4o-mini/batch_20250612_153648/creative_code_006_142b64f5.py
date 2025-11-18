"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Create a smart contract on Solana for managing NFT assets that support educational initiatives and streaming profits.
Generated: DETERMINISTIC_142b64f57ffb332d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
//! Smart Contract for Managing NFT Assets to Support Educational Initiatives on Solana
//! This contract allows minting, transferring, and streaming profits from NFTs.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};
use std::str::FromStr;

declare_id!("Fg6PaFpoGXkYsidMpWTKqZq9kM5e4s9eQ2E7vKejG9pT");

#[program]
pub mod edu_nft_manager {
    use super::*;

    /// Initializes the NFT manager context.
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let nft_manager = &mut ctx.accounts.nft_manager;
        nft_manager.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    /// Mints a new NFT asset.
    pub fn mint_nft(ctx: Context<MintNFT>, metadata_uri: String) -> Result<()> {
        let nft = &mut ctx.accounts.nft;
        nft.metadata_uri = metadata_uri;
        nft.owner = *ctx.accounts.owner.key;
        nft.profit_stream = ctx.accounts.profit_stream.key();

        // Call to external NFT minting function can be added here
        // Ensure proper checks and balances during minting

        Ok(())
    }

    /// Transfers ownership of an NFT asset.
    pub fn transfer_nft(ctx: Context<TransferNFT>, new_owner: Pubkey) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        // Ensure the caller is the current owner
        require!(nft.owner == *ctx.accounts.owner.key, CustomError::Unauthorized);

        nft.owner = new_owner;

        Ok(())
    }

    /// Streams profits from the NFT to a designated account.
    pub fn stream_profits(ctx: Context<StreamProfits>, amount: u64) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        // Validate the amount to be streamed
        require!(amount > 0, CustomError::InvalidAmount);

        // Logic to stream profits
        // Ensure to handle token transfers and updates accordingly

        Ok(())
    }
}

// Define the NFT struct
#[account]
pub struct Nft {
    pub owner: Pubkey,
    pub metadata_uri: String,
    pub profit_stream: Pubkey,
}

// Context for initializing the NFT manager
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32)]
    pub nft_manager: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for minting an NFT
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Context for transferring an NFT
#[derive(Accounts)]
pub struct TransferNFT<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Context for streaming profits from an NFT
#[derive(Accounts)]
pub struct StreamProfits<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub profit_stream: AccountInfo<'info>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Custom error types for the contract
#[error]
pub enum CustomError {
    #[msg("Unauthorized action.")]
    Unauthorized,
    #[msg("Invalid amount specified.")]
    InvalidAmount,
}
```
