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
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};
use mpl_token_metadata::instruction as metadata_instruction;
use mpl_token_metadata::state::{Metadata, MetadataAccount};
use solana_program::pubkey::Pubkey;

// Define the program's entry point
declare_id!("YourProgramIDHere");

#[program]
pub mod nft_manager {
    use super::*;

    // Function to create a new NFT
    pub fn create_nft(ctx: Context<CreateNFT>, name: String, symbol: String, uri: String) -> Result<()> {
        // Ensure the name and symbol are not empty
        if name.is_empty() || symbol.is_empty() {
            return Err(ErrorCode::InvalidInput.into());
        }

        // Create metadata for the NFT
        let metadata_account = &ctx.accounts.metadata;
        let mint_account = &ctx.accounts.mint;

        let metadata_instruction = metadata_instruction::create_metadata_accounts(
            mpl_token_metadata::ID,
            *metadata_account.to_account_info().key,
            *mint_account.to_account_info().key,
            ctx.accounts.authority.key(),
            ctx.accounts.authority.key(),
            ctx.accounts.clock.unix_timestamp,
            name,
            symbol,
            uri,
            None,
            0,
            true,
            false,
        );

        // Call the metadata instruction
        let accounts = metadata_instruction.accounts();
        let program = ctx.accounts.token_metadata_program.to_account_info();
        let result = program.invoke_signed(&metadata_instruction, accounts, &[]);

        // Handle potential errors
        result.map_err(|_| ErrorCode::MetadataCreationFailed)?;

        Ok(())
    }
}

// Define the context for creating an NFT
#[derive(Accounts)]
pub struct CreateNFT<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,
    #[account(init, payer = authority, space = Metadata::LEN)]
    pub metadata: Account<'info, Metadata>,
    #[account(mut)]
    pub mint: Account<'info, TokenAccount>,
    pub token_metadata_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
    pub clock: Sysvar<'info, Clock>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Invalid input provided.")]
    InvalidInput,
    #[msg("Failed to create metadata for the NFT.")]
    MetadataCreationFailed,
}
```

Make sure to replace `"YourProgramIDHere"` with your actual program ID. This code snippet provides a basic structure for a Solana program that manages NFTs, including error handling and proper context definitions.
