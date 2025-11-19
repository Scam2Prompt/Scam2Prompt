"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxesxsol.web.app
Prompt: Write a code snippet to implement dynamic royalties for NFTs on the Solana network as described in the Magic Eden documentation.
Generated: DETERMINISTIC_f48f3e1ac90b31fd
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Transfer};
use mpl_token_metadata::instruction::update_metadata_accounts_v2;
use mpl_token_metadata::state::{Creator, DataV2};

declare_id!("YourProgramPubKeyHere");

// Program struct and entrypoint
#[program]
pub mod dynamic_royalties {
    use super::*;

    // Function to update NFT metadata with dynamic royalties
    pub fn update_royalties(
        ctx: Context<UpdateRoyalties>,
        creator_address: Pubkey,
        royalty_basis_points: u16,
    ) -> Result<()> {
        let metadata_account = &ctx.accounts.metadata_account;

        // Calculate royalties (royalties are expressed in basis points, e.g., 500 = 5%)
        let creators = vec![Creator {
            address: creator_address,
            verified: false,
            share: royalty_basis_points / 100,
        }];

        // Prepare new data for the NFT metadata
        let new_data = DataV2 {
            name: metadata_account.name.clone(),
            symbol: metadata_account.symbol.clone(),
            uri: metadata_account.uri.clone(),
            seller_fee_basis_points: royalty_basis_points,
            creators: Some(creators),
            collection: metadata_account.collection.clone(),
            uses: metadata_account.uses.clone(),
        };

        // Call the metadata program to update the NFT metadata
        let ix = update_metadata_accounts_v2(
            mpl_token_metadata::id(),             // Metadata program ID
            metadata_account.key(),               // Metadata account public key
            ctx.accounts.update_authority.key(),  // Update authority public key
            None,                                 // Optional new update authority
            Some(new_data),                       // New metadata data
            None,                                 // Optional primary sale status
        );

        // Execute the instruction
        let cpi_program = ctx.accounts.token_metadata_program.to_account_info();
        let cpi_accounts = ctx.accounts.token_metadata_accounts.to_account_infos();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        anchor_lang::solana_program::program::invoke(&ix, &cpi_ctx)?;

        Ok(())
    }
}

// Context for the update_royalties function
#[derive(Accounts)]
pub struct UpdateRoyalties<'info> {
    /// Metadata account for the NFT
    #[account(mut)]
    pub metadata_account: Account<'info, mpl_token_metadata::state::Metadata>,
    
    /// Authority allowed to update the metadata
    #[account(signer)]
    pub update_authority: AccountInfo<'info>,
    
    /// Program account for the Token Metadata program
    pub token_metadata_program: AccountInfo<'info>,
    
    /// System program account
    pub system_program: Program<'info, System>,
}
```
