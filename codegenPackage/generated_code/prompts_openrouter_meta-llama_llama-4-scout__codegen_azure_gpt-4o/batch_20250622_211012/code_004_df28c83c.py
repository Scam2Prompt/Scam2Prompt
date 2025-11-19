"""
Generated Code Metadata:
========================
Original URL: https://clm-dst-lv.web.app
Prompt: Create a smart contract on Solana that automates the process of airdropping DUST tokens to users who meet certain criteria, such as holding a specific NFT.
Generated: DETERMINISTIC_df28c83c3821c3a6
Batch ID: 20250622_211012
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
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod dust_airdrop {
    use super::*;

    // Function to perform the airdrop
    pub fn airdrop_dust(ctx: Context<AirdropDust>, amount: u64) -> Result<()> {
        let user_nft_account = &ctx.accounts.user_nft_account;
        let required_nft_mint = &ctx.accounts.required_nft_mint;

        // Check if the user holds the required NFT
        if user_nft_account.mint != required_nft_mint.key() {
            return Err(ErrorCode::InvalidNft.into());
        }

        // Perform the token transfer (airdrop)
        let cpi_accounts = Transfer {
            from: ctx.accounts.airdrop_source.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.airdrop_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Transfer the specified amount of DUST tokens
        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the context for the airdrop function
#[derive(Accounts)]
pub struct AirdropDust<'info> {
    /// The account holding the required NFT
    #[account(
        constraint = user_nft_account.owner == user.key(),
        constraint = user_nft_account.amount > 0
    )]
    pub user_nft_account: Account<'info, TokenAccount>,

    /// The mint address of the required NFT
    pub required_nft_mint: Account<'info, Mint>,

    /// The user's token account to receive the DUST tokens
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,

    /// The source account for the DUST tokens
    #[account(mut)]
    pub airdrop_source: Account<'info, TokenAccount>,

    /// The authority allowed to transfer DUST tokens
    pub airdrop_authority: Signer<'info>,

    /// The user receiving the airdrop
    pub user: Signer<'info>,

    /// The token program
    pub token_program: Program<'info, Token>,
}

// Define custom error codes
#[error_code]
pub enum ErrorCode {
    #[msg("User does not hold the required NFT.")]
    InvalidNft,
}
```
