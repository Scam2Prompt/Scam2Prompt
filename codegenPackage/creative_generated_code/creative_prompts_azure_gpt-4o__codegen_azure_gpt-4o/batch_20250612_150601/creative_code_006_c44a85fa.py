"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasorng.web.app
Prompt: Create a smart contract on Solana to facilitate secure transactions for buying and selling allowlists in an allowlist marketplace like the one on Atlas3.
Generated: DETERMINISTIC_c44a85fa1c1bc2ad
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana libraries and dependencies
use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

// Define the program ID
declare_id!("YourProgramPublicKeyHere");

// Define the program module
#[program]
pub mod allowlist_marketplace {
    use super::*;
    
    /// Facilitates secure transactions for buying and selling allowlists.
    /// Buyers can purchase allowlists listed by sellers.
    pub fn create_listing(ctx: Context<CreateListing>, price: u64) -> Result<()> {
        let listing = &mut ctx.accounts.listing;
        listing.owner = *ctx.accounts.seller.key;
        listing.price = price;
        Ok(())
    }

    pub fn purchase_allowlist(ctx: Context<PurchaseAllowlist>) -> Result<()> {
        let listing = &ctx.accounts.listing;

        // Ensure the buyer sends the correct amount
        require!(ctx.accounts.buyer.lamports() >= listing.price, MarketplaceError::InsufficientFunds);

        // Transfer funds from buyer to seller
        let ix = anchor_lang::solana_program::system_instruction::transfer(
            ctx.accounts.buyer.key, 
            ctx.accounts.seller.key, 
            listing.price,
        );
        anchor_lang::solana_program::program::invoke(
            &ix,
            &[
                ctx.accounts.buyer.to_account_info(),
                ctx.accounts.seller.to_account_info(),
            ],
        )?;

        // Close listing account (allowlist is sold)
        **ctx.accounts.listing.to_account_info().lamports.borrow_mut() = 0;
        Ok(())
    }
}

// Define the account structures
#[derive(Accounts)]
pub struct CreateListing<'info> {
    #[account(init, payer = seller, space = 8 + 32 + 8)] // Rent-exempt account
    pub listing: Account<'info, AllowlistListing>,
    #[account(mut)]
    pub seller: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PurchaseAllowlist<'info> {
    #[account(mut)]
    pub listing: Account<'info, AllowlistListing>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub seller: SystemAccount<'info>,
    pub system_program: Program<'info, System>,
}

// Define the Allowlist Listing data structure
#[account]
pub struct AllowlistListing {
    pub owner: Pubkey, // Owner of the listing
    pub price: u64,    // Price to purchase the allowlist
}

// Define custom errors for better error handling
#[error_code]
pub enum MarketplaceError {
    #[msg("Buyer does not have sufficient funds to complete the transaction.")]
    InsufficientFunds,
}
```
