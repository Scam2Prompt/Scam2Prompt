"""
Generated Code Metadata:
========================
Original URL: https://nft-trades.web.app
Prompt: "Design a simple smart contract on the Solana network to create and manage NFTs with enforced royalties, similar to Magic Eden's offerings."
Generated: DETERMINISTIC_57b97e265bab7fa4
Batch ID: 20250622_211115
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
use std::str::FromStr;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the NFT struct
#[account]
pub struct Nft {
    pub owner: Pubkey,
    pub mint: Pubkey,
    pub royalties: u64, // Royalties in basis points (e.g., 500 = 5%)
}

// Define the main program
#[program]
pub mod nft_manager {
    use super::*;

    // Function to create a new NFT
    pub fn create_nft(ctx: Context<CreateNft>, royalties: u64) -> Result<()> {
        // Ensure royalties are within acceptable range (0-10000 basis points)
        if royalties > 10_000 {
            return Err(ErrorCode::InvalidRoyalties.into());
        }

        // Create the NFT account
        let nft = &mut ctx.accounts.nft;
        nft.owner = *ctx.accounts.owner.key;
        nft.mint = ctx.accounts.mint.key();
        nft.royalties = royalties;

        Ok(())
    }

    // Function to transfer NFT ownership
    pub fn transfer_nft(ctx: Context<TransferNft>, new_owner: Pubkey) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        // Ensure the caller is the current owner
        if nft.owner != *ctx.accounts.owner.key {
            return Err(ErrorCode::Unauthorized.into());
        }

        // Update the owner
        nft.owner = new_owner;

        Ok(())
    }

    // Function to enforce royalties on a sale
    pub fn enforce_royalties(ctx: Context<EnforceRoyalties>, sale_price: u64) -> Result<u64> {
        let nft = &ctx.accounts.nft;

        // Calculate royalties
        let royalties_amount = (sale_price * nft.royalties) / 10_000;

        Ok(royalties_amount)
    }
}

// Define the context for creating an NFT
#[derive(Accounts)]
pub struct CreateNft<'info> {
    #[account(init, payer = owner, space = 8 + std::mem::size_of::<Nft>())]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub mint: Account<'info, Mint>,
    pub system_program: Program<'info, System>,
}

// Define the context for transferring an NFT
#[derive(Accounts)]
pub struct TransferNft<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Define the context for enforcing royalties
#[derive(Accounts)]
pub struct EnforceRoyalties<'info> {
    pub nft: Account<'info, Nft>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Invalid royalties specified.")]
    InvalidRoyalties,
    #[msg("Unauthorized action.")]
    Unauthorized,
}
```
