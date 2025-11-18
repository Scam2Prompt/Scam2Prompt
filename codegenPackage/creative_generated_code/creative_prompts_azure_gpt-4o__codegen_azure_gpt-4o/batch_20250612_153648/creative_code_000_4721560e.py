"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://final3223.vercel.app
Prompt: Write a Solana-based smart contract that facilitates an NFT presale where users can mint NFTs by paying a variable amount of SOL and receive tokens proportional to their payment, as described in the tier system on the webpage.
Generated: DETERMINISTIC_4721560ec1c0f168
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Solana Program to facilitate an NFT presale with tier-based minting.
// The tiers and reward distribution logic are based on the amount of SOL a user sends.
// This code uses the Rust programming language and Solana's anchor framework.
//
// To run this program, you must install the Anchor framework and have a Solana development
// environment set up locally.
//
// Note: Ensure that this program is deployed on a Solana cluster and connected to a proper front-end 
// for users to interact with it.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, MintTo};

// Define the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod nft_presale {
    use super::*;

    // Entry function for minting NFTs during presale
    pub fn mint_nft(ctx: Context<MintNFT>, sol_amount: u64) -> Result<()> {
        let presale = &mut ctx.accounts.presale;
        let user = &ctx.accounts.user;

        // Ensure the presale is active
        require!(presale.is_active, PresaleError::PresaleInactive);

        // Calculate the number of NFTs to mint based on the amount of SOL sent
        let nfts_to_mint = calculate_tier_reward(sol_amount)?;

        // Mint NFTs to the user's token account
        let mint_to_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            MintTo {
                mint: ctx.accounts.mint.to_account_info(),
                to: ctx.accounts.user_token_account.to_account_info(),
                authority: ctx.accounts.presale_authority.to_account_info(),
            },
        );
        token::mint_to(mint_to_ctx, nfts_to_mint)?;

        // Update the presale state
        presale.total_minted += nfts_to_mint;

        Ok(())
    }
}

// Context for the MintNFT function
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(seeds = [b"presale_authority"], bump)]
    pub presale_authority: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

// Data structure to store presale state
#[account]
pub struct Presale {
    pub total_minted: u64,
    pub is_active: bool,
}

// Tier-based reward calculation
fn calculate_tier_reward(sol_amount: u64) -> Result<u64> {
    match sol_amount {
        0..=1_000_000_000 => Ok(1), // Tier 1: Mint 1 NFT
        1_000_000_001..=2_000_000_000 => Ok(2), // Tier 2: Mint 2 NFTs
        2_000_000_001..=5_000_000_000 => Ok(5), // Tier 3: Mint 5 NFTs
        _ => Ok(10), // Tier 4: Mint 10 NFTs
    }
}

// Custom error for the presale program
#[error_code]
pub enum PresaleError {
    #[msg("The presale is not active.")]
    PresaleInactive,
}
```

The provided code is ready to be used within the Solana ecosystem. Ensure to replace `"YourProgramIDHere"` with the actual program ID after deployment. It calculates rewards based on a tier system and mints NFTs accordingly.
