"""
Generated Code Metadata:
========================
Original URL: https://nft-solad.web.app
Prompt: Design a simple smart contract in Rust for the Solana blockchain that enforces dynamic royalties for NFT creators, inspired by the features of Magic Eden's Open Creator Protocol.
Generated: DETERMINISTIC_4046729c55f92ae1
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID for the smart contract
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod dynamic_royalties {
    use super::*;

    // Initialize the contract with creator's address and royalty percentage
    pub fn initialize(ctx: Context<Initialize>, creator: Pubkey, royalty_percentage: u8) -> Result<()> {
        // Ensure the royalty percentage is within valid bounds
        if royalty_percentage > 100 {
            return Err(ErrorCode::InvalidRoyaltyPercentage.into());
        }

        // Set the creator and royalty percentage in the state
        let royalty_account = &mut ctx.accounts.royalty_account;
        royalty_account.creator = creator;
        royalty_account.royalty_percentage = royalty_percentage;

        Ok(())
    }

    // Function to update the royalty percentage
    pub fn update_royalty(ctx: Context<UpdateRoyalty>, new_royalty_percentage: u8) -> Result<()> {
        // Ensure the new royalty percentage is valid
        if new_royalty_percentage > 100 {
            return Err(ErrorCode::InvalidRoyaltyPercentage.into());
        }

        // Update the royalty percentage
        let royalty_account = &mut ctx.accounts.royalty_account;
        royalty_account.royalty_percentage = new_royalty_percentage;

        Ok(())
    }

    // Function to calculate royalties based on sale price
    pub fn calculate_royalty(ctx: Context<CalculateRoyalty>, sale_price: u64) -> Result<u64> {
        let royalty_account = &ctx.accounts.royalty_account;

        // Calculate the royalty amount
        let royalty_amount = (sale_price * royalty_account.royalty_percentage as u64) / 100;

        Ok(royalty_amount)
    }
}

// Define the state structure for the royalty account
#[account]
pub struct RoyaltyAccount {
    pub creator: Pubkey,          // Creator's public key
    pub royalty_percentage: u8,    // Royalty percentage (0-100)
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + std::mem::size_of::<RoyaltyAccount>())]
    pub royalty_account: Account<'info, RoyaltyAccount>, // Account to store royalty info
    #[account(mut)]
    pub user: Signer<'info>, // User who is initializing the contract
    pub system_program: Program<'info, System>, // System program for account creation
}

// Define the context for updating the royalty percentage
#[derive(Accounts)]
pub struct UpdateRoyalty<'info> {
    #[account(mut, has_one = creator)]
    pub royalty_account: Account<'info, RoyaltyAccount>, // Account to update royalty info
    pub creator: Signer<'info>, // Creator who is authorized to update
}

// Define the context for calculating royalties
#[derive(Accounts)]
pub struct CalculateRoyalty<'info> {
    pub royalty_account: Account<'info, RoyaltyAccount>, // Account to read royalty info
}

// Define custom error codes for the contract
#[error]
pub enum ErrorCode {
    #[msg("The royalty percentage must be between 0 and 100.")]
    InvalidRoyaltyPercentage,
}
```
