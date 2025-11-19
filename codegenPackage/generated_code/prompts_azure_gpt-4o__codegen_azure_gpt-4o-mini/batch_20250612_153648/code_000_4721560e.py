"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Write a Solana-based smart contract that facilitates an NFT presale where users can mint NFTs by paying a variable amount of SOL and receive tokens proportional to their payment, as described in the tier system on the webpage.
Generated: DETERMINISTIC_4721560ec1c0f168
Batch ID: 20250612_153648
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
use anchor_lang::solana_program::pubkey::Pubkey;
use anchor_lang::solana_program::program_error::ProgramError;
use anchor_lang::solana_program::system_program;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

declare_id!("YourProgramIDHere");

#[program]
pub mod nft_presale {
    use super::*;

    // Initialize the presale with parameters
    pub fn initialize_presale(ctx: Context<InitializePresale>, tiers: Vec<Tier>) -> Result<()> {
        let presale = &mut ctx.accounts.presale;
        presale.tiers = tiers;
        presale.is_active = true;
        Ok(())
    }

    // Mint NFT function
    pub fn mint_nft(ctx: Context<MintNFT>, tier_index: usize) -> Result<()> {
        let presale = &ctx.accounts.presale;

        // Check if presale is active
        if !presale.is_active {
            return Err(ProgramError::Custom(0)); // Presale not active
        }

        // Validate tier index
        if tier_index >= presale.tiers.len() {
            return Err(ProgramError::Custom(1)); // Invalid tier index
        }

        let tier = &presale.tiers[tier_index];
        let payment_amount = tier.price;

        // Ensure the user has sent enough SOL
        if **ctx.accounts.user.lamports.borrow() < payment_amount {
            return Err(ProgramError::InsufficientFunds);
        }

        // Transfer SOL to the presale account
        let cpi_accounts = system_program::Transfer {
            from: ctx.accounts.user.to_account_info(),
            to: ctx.accounts.presale.to_account_info(),
        };
        let cpi_program = ctx.accounts.system_program.to_account_info();
        let transfer_ix = system_program::transfer(cpi_accounts, payment_amount)?;
        anchor_lang::solana_program::program::invoke(&transfer_ix, &[])?;

        // Mint the NFT to the user
        let mint = &ctx.accounts.mint;
        let user_token_account = &ctx.accounts.user_token_account;

        // Mint the NFT (this is a placeholder, implement your minting logic)
        // token::mint_to(ctx.accounts.mint_to_context(), 1)?;

        Ok(())
    }
}

// Define the presale account structure
#[account]
pub struct Presale {
    pub tiers: Vec<Tier>,
    pub is_active: bool,
}

// Define the tier structure
#[derive(Clone, AnchorSerialize, AnchorDeserialize)]
pub struct Tier {
    pub price: u64, // Price in SOL for this tier
    pub supply: u64, // Total supply for this tier
}

// Context for initializing the presale
#[derive(Accounts)]
pub struct InitializePresale<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8)] // Adjust space as needed
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
    pub mint: Account<'info, Mint>, // NFT mint account
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>, // User's token account
    pub system_program: Program<'info, System>,
}
```

Make sure to replace `"YourProgramIDHere"` with your actual program ID and implement the NFT minting logic as per your requirements.
