"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Provide a step-by-step guide for integrating `$BLD` token rewards into an NFT minting process on Solana, referencing the gamified leveling system from the Buildoors project.
Generated: DETERMINISTIC_7b5f29c22909a861
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
use anchor_spl::token::{self, Mint, TokenAccount, Transfer};
use std::convert::TryInto;

// Define the program's entry point
declare_id!("YourProgramIDHere");

#[program]
pub mod nft_minting {
    use super::*;

    // Function to mint an NFT and reward the user with $BLD tokens
    pub fn mint_nft(ctx: Context<MintNft>, metadata_uri: String) -> Result<()> {
        // Ensure the metadata URI is valid
        if metadata_uri.is_empty() {
            return Err(ErrorCode::InvalidMetadataUri.into());
        }

        // Mint the NFT
        let nft_mint = &mut ctx.accounts.nft_mint;
        let user = &ctx.accounts.user;

        // Create the NFT mint
        let cpi_accounts = token::MintTo {
            mint: nft_mint.to_account_info(),
            to: user.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };

        // Call the minting function
        token::mint_to(ctx.accounts.token_program.clone(), cpi_accounts, 1)?;

        // Reward the user with $BLD tokens
        let reward_amount = 10; // Define the reward amount
        let cpi_accounts_reward = Transfer {
            from: ctx.accounts.bld_token_account.to_account_info(),
            to: ctx.accounts.user_bld_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };

        // Transfer the $BLD tokens
        token::transfer(ctx.accounts.token_program.clone(), cpi_accounts_reward, reward_amount)?;

        Ok(())
    }
}

// Define the context for the minting function
#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(mut)]
    pub user: Signer<'info>, // User who is minting the NFT
    #[account(mut)]
    pub nft_mint: Account<'info, Mint>, // NFT mint account
    #[account(mut)]
    pub user_bld_account: Account<'info, TokenAccount>, // User's $BLD token account
    #[account(mut)]
    pub bld_token_account: Account<'info, TokenAccount>, // $BLD token account for rewards
    pub authority: AccountInfo<'info>, // Authority to mint the NFT
    pub token_program: Program<'info, Token>, // SPL Token program
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The provided metadata URI is invalid.")]
    InvalidMetadataUri,
}
```

This code provides a basic structure for integrating `$BLD` token rewards into an NFT minting process on Solana, following best practices and including error handling. Make sure to replace `"YourProgramIDHere"` with your actual program ID.
