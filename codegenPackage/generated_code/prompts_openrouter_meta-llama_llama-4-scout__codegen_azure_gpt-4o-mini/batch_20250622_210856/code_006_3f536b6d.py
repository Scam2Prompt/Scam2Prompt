"""
Generated Code Metadata:
========================
Original URL: https://holddao.web.app
Prompt: Develop a smart contract on Solana to create, buy, and sell NFTs, considering the features and functionalities observed on https://holddao.web.app.
Generated: DETERMINISTIC_3f536b6d457a83a1
Batch ID: 20250622_210856
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

declare_id!("YourProgramIDHere");

#[program]
pub mod nft_marketplace {
    use super::*;

    // Initialize the NFT marketplace
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let marketplace = &mut ctx.accounts.marketplace;
        marketplace.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    // Create a new NFT
    pub fn create_nft(ctx: Context<CreateNFT>, name: String, uri: String) -> Result<()> {
        let nft = &mut ctx.accounts.nft;
        nft.name = name;
        nft.uri = uri;
        nft.owner = *ctx.accounts.owner.key;
        nft.is_sold = false;
        Ok(())
    }

    // Buy an NFT
    pub fn buy_nft(ctx: Context<BuyNFT>, nft_id: Pubkey) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        // Ensure the NFT is available for sale
        if nft.is_sold {
            return Err(ErrorCode::NftAlreadySold.into());
        }

        // Transfer the payment
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.buyer_token_account.to_account_info(),
            to: ctx.accounts.seller_token_account.to_account_info(),
            authority: ctx.accounts.buyer.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(CpiContext::new(cpi_program, cpi_accounts), nft.price)?;

        // Update NFT ownership
        nft.owner = *ctx.accounts.buyer.key;
        nft.is_sold = true;

        Ok(())
    }

    // Sell an NFT
    pub fn sell_nft(ctx: Context<SellNFT>, nft_id: Pubkey, price: u64) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        // Ensure the seller is the owner of the NFT
        if nft.owner != *ctx.accounts.seller.key {
            return Err(ErrorCode::Unauthorized.into());
        }

        // Set the price for the NFT
        nft.price = price;
        nft.is_sold = false;

        Ok(())
    }
}

// Define the NFT structure
#[account]
pub struct Nft {
    pub name: String,
    pub uri: String,
    pub owner: Pubkey,
    pub price: u64,
    pub is_sold: bool,
}

// Define the marketplace structure
#[account]
pub struct Marketplace {
    pub owner: Pubkey,
}

// Context for initializing the marketplace
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32)]
    pub marketplace: Account<'info, Marketplace>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for creating an NFT
#[derive(Accounts)]
pub struct CreateNFT<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 64 + 256)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for buying an NFT
#[derive(Accounts)]
pub struct BuyNFT<'info> {
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub buyer_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub seller_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    pub token_program: Program<'info, Token>,
}

// Context for selling an NFT
#[derive(Accounts)]
pub struct SellNFT<'info> {
    #[account(mut)]
    pub seller: Signer<'info>,
    #[account(mut)]
    pub nft: Account<'info, Nft>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The NFT has already been sold.")]
    NftAlreadySold,
    #[msg("Unauthorized action.")]
    Unauthorized,
}
```
