"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solgotchi.vercel.app
Prompt: Write a Solana blockchain smart contract that allows users to mint a "Gotchi" NFT, referencing the minting process described on the Solgotchi website.
Generated: DETERMINISTIC_722280867975b0fb
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates for interacting with the Solana blockchain
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, MintTo};

// Declare the program module
#[program]
pub mod solgotchi {
    use super::*;

    // Instruction to mint a Gotchi NFT
    pub fn mint_gotchi(ctx: Context<MintGotchi>, gotchi_name: String) -> Result<()> {
        let gotchi_metadata = &mut ctx.accounts.gotchi_metadata;

        // Validate input: Gotchi name should not be empty
        if gotchi_name.is_empty() {
            return Err(ErrorCode::GotchiNameEmpty.into());
        }

        // Ensure the mint authority is correct for security
        let mint_authority = ctx.accounts.mint_authority.key();
        let expected_mint_authority = ctx.accounts.mint.to_account_info().owner;
        if &mint_authority != expected_mint_authority {
            return Err(ErrorCode::InvalidMintAuthority.into());
        }

        // Mint the token (NFT)
        let cpi_accounts = MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.token_account.to_account_info(),
            authority: ctx.accounts.mint_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let mint_to_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::mint_to(
            mint_to_ctx,
            1, // Minting exactly 1 token for the Gotchi NFT
        )?;

        // Save Gotchi metadata (e.g., name and owner)
        gotchi_metadata.owner = ctx.accounts.user.key();
        gotchi_metadata.name = gotchi_name;

        Ok(())
    }
}

// Define the context for the MintGotchi instruction
#[derive(Accounts)]
pub struct MintGotchi<'info> {
    /// The mint account for the NFT
    #[account(mut)]
    pub mint: Account<'info, Mint>,

    /// Token account to hold the minted NFT
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,

    /// Mint authority (must sign the transaction)
    #[account(signer)]
    pub mint_authority: AccountInfo<'info>,

    /// User who is minting the NFT
    #[account(mut)]
    pub user: Signer<'info>,

    /// Metadata storage for Gotchi NFT
    #[account(init, payer = user, space = 8 + 32 + 64)]
    pub gotchi_metadata: Account<'info, GotchiMetadata>,

    /// Token program for minting NFTs
    pub token_program: Program<'info, Token>,

    /// System program for creating accounts
    pub system_program: Program<'info, System>,
}

// Define Gotchi metadata structure
#[account]
pub struct GotchiMetadata {
    pub owner: Pubkey, // Owner of the Gotchi NFT
    pub name: String,  // Name of the Gotchi NFT
}

// Define custom error codes for the program
#[error_code]
pub enum ErrorCode {
    #[msg("Gotchi name cannot be empty.")]
    GotchiNameEmpty,
    #[msg("Invalid mint authority.")]
    InvalidMintAuthority,
}
```
