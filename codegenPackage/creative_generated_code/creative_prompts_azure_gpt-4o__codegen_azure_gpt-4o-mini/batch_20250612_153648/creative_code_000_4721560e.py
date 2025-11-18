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
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

declare_id!("YourProgramId"); // Replace with your program's ID

#[program]
pub mod nft_presale {
    use super::*;

    // Initialize the presale
    pub fn initialize(ctx: Context<Initialize>, tier_prices: Vec<u64>, max_mint_per_user: u8) -> ProgramResult {
        let presale = &mut ctx.accounts.presale;

        presale.tier_prices = tier_prices;
        presale.max_mint_per_user = max_mint_per_user;
        presale.total_minted = 0;

        Ok(())
    }

    // Mint NFT function
    pub fn mint_nft(ctx: Context<MintNFT>, tier: usize) -> ProgramResult {
        let presale = &mut ctx.accounts.presale;

        // Check if tier is valid
        if tier >= presale.tier_prices.len() {
            return Err(ErrorCode::InvalidTier.into());
        }

        let payment_amount = presale.tier_prices[tier];

        // Check if user has already minted the maximum allowed number of NFTs
        if ctx.accounts.user_mint_counter.minted >= presale.max_mint_per_user {
            return Err(ErrorCode::MaxMintExceeded.into());
        }

        // Transfer SOL payment to the presale account
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.user.to_account_info(),
            to: ctx.accounts.presale.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Transfer payment
        token::transfer(cpi_ctx, payment_amount)?;

        // Update the user's mint counter
        ctx.accounts.user_mint_counter.minted += 1;

        // Mint the NFT (minting logic would go here)

        Ok(())
    }
}

// Context for initializing the presale
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 128)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for minting an NFT
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_mint_counter: Account<'info, UserMintCounter>,
    pub token_program: Program<'info, Token>,
}

// Presale data structure
#[account]
pub struct Presale {
    pub tier_prices: Vec<u64>, // Prices for each tier
    pub max_mint_per_user: u8, // Max NFTs a user can mint
    pub total_minted: u64,      // Total NFTs minted
}

// User minting counter
#[account]
pub struct UserMintCounter {
    pub minted: u8, // Number of NFTs minted by the user
}

// Custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Invalid tier selected.")]
    InvalidTier,
    #[msg("Maximum minting limit exceeded.")]
    MaxMintExceeded,
}
```
