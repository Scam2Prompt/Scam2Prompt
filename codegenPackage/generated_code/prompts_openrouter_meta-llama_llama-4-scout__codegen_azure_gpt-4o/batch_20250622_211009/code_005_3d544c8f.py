"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: What are some best practices for implementing a secure and transparent NFT presale on the Solana blockchain, as seen in the Pepe project?
Generated: DETERMINISTIC_3d544c8ff96cb5c4
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
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod nft_presale {
    use super::*;

    // Initialize the presale account
    pub fn initialize_presale(
        ctx: Context<InitializePresale>,
        presale_start_time: i64,
        presale_end_time: i64,
        price_per_nft: u64,
    ) -> Result<()> {
        let presale_account = &mut ctx.accounts.presale_account;
        presale_account.presale_start_time = presale_start_time;
        presale_account.presale_end_time = presale_end_time;
        presale_account.price_per_nft = price_per_nft;
        presale_account.owner = ctx.accounts.owner.key();
        Ok(())
    }

    // Function to purchase an NFT during the presale
    pub fn purchase_nft(ctx: Context<PurchaseNFT>, amount: u64) -> Result<()> {
        let presale_account = &ctx.accounts.presale_account;
        let current_time = Clock::get()?.unix_timestamp;

        // Ensure the presale is active
        require!(
            current_time >= presale_account.presale_start_time
                && current_time <= presale_account.presale_end_time,
            PresaleError::PresaleNotActive
        );

        // Ensure the user has sent the correct amount
        let total_price = presale_account.price_per_nft.checked_mul(amount).ok_or(PresaleError::MathOverflow)?;
        require!(ctx.accounts.user_token_account.amount >= total_price, PresaleError::InsufficientFunds);

        // Transfer tokens from the user to the presale account
        let cpi_accounts = Transfer {
            from: ctx.accounts.user_token_account.to_account_info(),
            to: ctx.accounts.presale_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, total_price)?;

        // Mint the NFT to the user
        let mint_accounts = MintTo {
            mint: ctx.accounts.nft_mint.to_account_info(),
            to: ctx.accounts.user_nft_account.to_account_info(),
            authority: ctx.accounts.presale_account.to_account_info(),
        };
        let mint_program = ctx.accounts.token_program.to_account_info();
        let mint_ctx = CpiContext::new(mint_program, mint_accounts);
        token::mint_to(mint_ctx, amount)?;

        Ok(())
    }
}

// Define the presale account structure
#[account]
pub struct PresaleAccount {
    pub presale_start_time: i64, // Start time of the presale
    pub presale_end_time: i64,   // End time of the presale
    pub price_per_nft: u64,      // Price per NFT in tokens
    pub owner: Pubkey,           // Owner of the presale account
}

// Define the context for initializing the presale
#[derive(Accounts)]
pub struct InitializePresale<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 8 + 8 + 8)]
    pub presale_account: Account<'info, PresaleAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for purchasing an NFT
#[derive(Accounts)]
pub struct PurchaseNFT<'info> {
    #[account(mut)]
    pub presale_account: Account<'info, PresaleAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub presale_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub nft_mint: Account<'info, Mint>,
    #[account(mut)]
    pub user_nft_account: Account<'info, TokenAccount>,
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define custom errors for the presale
#[error_code]
pub enum PresaleError {
    #[msg("Presale is not active.")]
    PresaleNotActive,
    #[msg("Insufficient funds to purchase NFT.")]
    InsufficientFunds,
    #[msg("Math overflow occurred.")]
    MathOverflow,
}
```
