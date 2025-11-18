"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://timcheese.pages.dev
Prompt: Develop a smart contract in Solana's Anchor framework to enforce the 5 NFT max per transaction rule for Tim Cheese minting.
Generated: DETERMINISTIC_3c261decad87530a
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Anchor framework and Solana
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};

// Declare the program and specify the program's ID
declare_id!("YourProgramIDHere");

// Main program struct
#[program]
pub mod tim_cheese_mint {
    use super::*;

    // Function to mint NFTs, enforcing the max of 5 NFTs per transaction
    pub fn mint_nft(ctx: Context<MintNft>, nft_mint_count: u8) -> Result<()> {
        // Enforce the maximum number of NFTs to mint in a single transaction
        const MAX_NFTS_PER_TX: u8 = 5;
        
        // Check if the count exceeds the maximum allowed
        if nft_mint_count == 0 || nft_mint_count > MAX_NFTS_PER_TX {
            return Err(ErrorCode::InvalidNftCount.into());
        }

        // Mint the NFTs using SPL token library
        for _ in 0..nft_mint_count {
            token::mint_to(
                ctx.accounts.into_mint_to_context(),
                1, // Minting one NFT at a time
            )?;
        }

        Ok(())
    }
}

// Context struct for the minting function
#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(mut)]
    pub payer: Signer<'info>, // The payer of the transaction
    #[account(mut)]
    pub mint: Account<'info, Mint>, // The mint account for the NFT
    #[account(mut)]
    pub metadata: Account<'info, TokenAccount>, // Metadata account for the NFT
    pub token_program: Program<'info, Token>, // SPL Token program
}

// Custom error codes for the smart contract
#[error]
pub enum ErrorCode {
    #[msg("Invalid NFT count. Must be between 1 and 5.")]
    InvalidNftCount,
}

// Helper function to convert context for minting
impl<'info> MintNft<'info> {
    fn into_mint_to_context(&self) -> token::MintTo<'_, 'info> {
        token::MintTo {
            mint: self.mint.to_account_info(),
            to: self.metadata.to_account_info(),
            authority: self.payer.to_account_info(),
        }
    }
}
```
