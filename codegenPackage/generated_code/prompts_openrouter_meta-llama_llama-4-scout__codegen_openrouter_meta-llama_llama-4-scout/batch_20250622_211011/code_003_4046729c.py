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
// Import required libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the program
#[program]
pub mod dynamic_royalties {
    use super::*;

    // Initialize the program
    pub fn initialize(ctx: Context<Initialize>, creator: Pubkey, royalty_basis_points: u16) -> Result<()> {
        // Create a new account for the royalty configuration
        let royalty_config = &mut ctx.accounts.royalty_config;
        royalty_config.creator = creator;
        royalty_config.royalty_basis_points = royalty_basis_points;
        Ok(())
    }

    // Update the royalty configuration
    pub fn update_royalty_config(ctx: Context<UpdateRoyaltyConfig>, royalty_basis_points: u16) -> Result<()> {
        // Get the royalty configuration account
        let royalty_config = &mut ctx.accounts.royalty_config;
        // Check if the updater is the creator
        require!(royalty_config.creator == ctx.accounts.updater.key(), DynamicRoyaltiesError::Unauthorized);
        royalty_config.royalty_basis_points = royalty_basis_points;
        Ok(())
    }

    // Calculate the royalty amount
    pub fn calculate_royalty(ctx: Context<CalculateRoyalty>, sale_price: u64) -> Result<u64> {
        // Get the royalty configuration account
        let royalty_config = &ctx.accounts.royalty_config;
        // Calculate the royalty amount
        let royalty_amount = sale_price * royalty_config.royalty_basis_points as u64 / 10_000;
        Ok(royalty_amount)
    }
}

// Define the accounts
#[account]
pub struct RoyaltyConfig {
    pub creator: Pubkey,
    pub royalty_basis_points: u16,
}

// Define the errors
#[error]
pub enum DynamicRoyaltiesError {
    #[msg("Unauthorized")]
    Unauthorized,
}

// Define the instructions
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = creator, space = 8 + 32 + 2)]
    pub royalty_config: Account<'info, RoyaltyConfig>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct UpdateRoyaltyConfig<'info> {
    #[account(mut, has_one = creator)]
    pub royalty_config: Account<'info, RoyaltyConfig>,
    pub updater: Signer<'info>,
}

#[derive(Accounts)]
pub struct CalculateRoyalty<'info> {
    pub royalty_config: Account<'info, RoyaltyConfig>,
}
```
