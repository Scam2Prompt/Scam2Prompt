"""
Generated Code Metadata:
========================
Original URL: https://mag-boxdao.web.app
Prompt: "Design a simple smart contract in Rust for Solana that allows for the minting of NFTs with specific benefits like those described in the Magic Box project."
Generated: DETERMINISTIC_19ee2cf66aa64c75
Batch ID: 20250622_212100
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
use anchor_spl::token::{self, Mint, Token, TokenAccount, MintTo};

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod magic_box_nft {
    use super::*;

    // Function to mint an NFT with specific benefits
    pub fn mint_nft(ctx: Context<MintNFT>, uri: String, name: String, symbol: String) -> Result<()> {
        let mint = &ctx.accounts.mint;
        let token_account = &ctx.accounts.token_account;
        let authority = &ctx.accounts.authority;

        // Mint the NFT to the specified token account
        let cpi_accounts = MintTo {
            mint: mint.to_account_info(),
            to: token_account.to_account_info(),
            authority: authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Mint 1 token (NFTs typically have a supply of 1)
        token::mint_to(cpi_ctx, 1)?;

        // Store metadata (URI, name, symbol) in the mint account
        let metadata = &mut ctx.accounts.metadata;
        metadata.uri = uri;
        metadata.name = name;
        metadata.symbol = symbol;

        Ok(())
    }
}

// Define the context for the mint_nft function
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>, // The mint account for the NFT
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>, // The token account to receive the NFT
    pub authority: Signer<'info>, // The authority allowed to mint the NFT
    pub token_program: Program<'info, Token>, // The SPL Token program
    #[account(init, payer = authority, space = 8 + 32 + 32 + 32)]
    pub metadata: Account<'info, Metadata>, // Metadata account for storing NFT details
    pub system_program: Program<'info, System>, // System program for account creation
}

// Define the Metadata struct for storing NFT details
#[account]
pub struct Metadata {
    pub uri: String,   // URI pointing to the NFT metadata (e.g., JSON file)
    pub name: String,  // Name of the NFT
    pub symbol: String // Symbol of the NFT
}
```

Make sure to replace `"YourProgramIDHere"` with your actual program ID when deploying the smart contract.
