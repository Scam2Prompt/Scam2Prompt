"""
Generated Code Metadata:
========================
Original URL: https://promo-ws108.github.io
Prompt: Write a code snippet in Rust that creates a Solana program to manage NFT items and their respective metadata, similar to those listed in the Degen Toy Machine inventory.
Generated: DETERMINISTIC_d9dbef8d5c28551d
Batch ID: 20250622_211009
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

// Define the NFT metadata struct
#[account]
pub struct NftMetadata {
    pub mint: Pubkey,
    pub name: String,
    pub symbol: String,
    pub uri: String,
    pub seller_fee_basis_points: u16,
}

// Define the NFT item struct
#[account]
pub struct NftItem {
    pub metadata: Pubkey,
    pub owner: Pubkey,
}

// Define the program interface
#[program]
pub mod nft_manager {
    use super::*;

    // Initialize the program
    pub fn initialize(ctx: Context<Initialize>, start_index: u64) -> Result<()> {
        Ok(())
    }

    // Create a new NFT item
    pub fn create_nft_item(ctx: Context<CreateNftItem>, metadata: NftMetadata) -> Result<()> {
        let nft_item = &mut ctx.accounts.nft_item;
        nft_item.metadata = ctx.accounts.metadata.key();
        nft_item.owner = ctx.accounts.owner.key();

        Ok(())
    }

    // Update NFT item metadata
    pub fn update_nft_item_metadata(ctx: Context<UpdateNftItemMetadata>, metadata: NftMetadata) -> Result<()> {
        let nft_metadata = &mut ctx.accounts.metadata;
        nft_metadata.name = metadata.name;
        nft_metadata.symbol = metadata.symbol;
        nft_metadata.uri = metadata.uri;
        nft_metadata.seller_fee_basis_points = metadata.seller_fee_basis_points;

        Ok(())
    }

    // Transfer NFT item ownership
    pub fn transfer_nft_item(ctx: Context<TransferNftItem>, new_owner: Pubkey) -> Result<()> {
        let nft_item = &mut ctx.accounts.nft_item;
        nft_item.owner = new_owner;

        Ok(())
    }
}

// Define the program accounts
#[account]
pub struct Metadata {
    pub mint: Pubkey,
}

#[account]
pub struct NftItemAccount {
    pub metadata: Pubkey,
    pub owner: Pubkey,
}

// Define the program instructions
#[derive(Accounts)]
pub struct Initialize<'info> {}

#[derive(Accounts)]
pub struct CreateNftItem<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32)]
    pub nft_item: Account<'info, NftItemAccount>,
    #[account(init, payer = owner, space = 8 + 32 + 32 + 200)]
    pub metadata: Account<'info, Metadata>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct UpdateNftItemMetadata<'info> {
    #[account(mut, has_one = owner)]
    pub metadata: Account<'info, Metadata>,
    pub owner: Signer<'info>,
}

#[derive(Accounts)]
pub struct TransferNftItem<'info> {
    #[account(mut, has_one = owner)]
    pub nft_item: Account<'info, NftItemAccount>,
    pub owner: Signer<'info>,
}
```
