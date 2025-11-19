"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Provide an example of how to integrate `$BLD` token rewards into a Solana-based NFT project, specifically for the Buildoors ecosystem.
Generated: DETERMINISTIC_07c66f21debad422
Batch ID: 20250612_151550
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
use anchor_spl::token::{Token, TokenAccount};

// Define the program ID
declare_id!("your-program-id");

// Define the Buildoors program
#[program]
pub mod buildoors {
    use super::*;

    // Initialize the program
    pub fn initialize(ctx: Context<Initialize>, start_date: i64, end_date: i64) -> Result<()> {
        // Get the program's state account
        let state_account = &mut ctx.accounts.state_account;

        // Initialize the state account
        state_account.authority = ctx.accounts.authority.key();
        state_account.start_date = start_date;
        state_account.end_date = end_date;
        state_account.bld_mint = ctx.accounts.bld_mint.key();
        state.account.bld_token_account = ctx.accounts.bld_token_account.key();

        Ok(())
    }

    // Claim $BLD token rewards
    pub fn claim(ctx: Context<Claim>, nft_mint: Pubkey) -> Result<()> {
        // Get the program's state account
        let state_account = &ctx.accounts.state_account;

        // Check if the claim period is active
        if state_account.start_date > Clock::get()?.unix_timestamp ||
            state_account.end_date < Clock::get()?.unix_timestamp {
            return err!(ErrorCode::InvalidClaimPeriod);
        }

        // Get the user's NFT account
        let nft_account = &ctx.accounts.nft_account;

        // Check if the user owns the NFT
        if nft_account.owner != ctx.accounts.claimant.key() {
            return err!(ErrorCode::InvalidNFTOwner);
        }

        // Get the $BLD token account
        let bld_token_account = &ctx.accounts.bld_token_account;

        // Check if the $BLD token account is valid
        if bld_token_account.mint != state_account.bld_mint {
            return err!(ErrorCode::InvalidBLDMint);
        }

        // Transfer $BLD tokens to the claimant
        let transfer_amount = 10 * 10u64.pow(6); // 10 $BLD tokens with 6 decimals
        transfer_tokens(
            ctx.accounts.bld_token_account,
            ctx.accounts.claimant_bld_token_account,
            state_account.authority,
            transfer_amount,
        )?;

        Ok(())
    }
}

// Define the accounts for the Initialize instruction
#[account]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 100)]
    pub state_account: Account<'info, StateAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub bld_mint: Account<'info, Mint>,
    #[account(init, payer = authority, space = 100)]
    pub bld_token_account: Account<'info, TokenAccount>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
}

// Define the accounts for the Claim instruction
#[account]
pub struct Claim<'info> {
    #[account(mut)]
    pub state_account: Account<'info, StateAccount>,
    #[account(mut)]
    pub nft_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub bld_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub claimant_bld_token_account: Account<'info, TokenAccount>,
    pub claimant: Signer<'info>,
    pub nft_mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

// Define the StateAccount struct
#[account]
pub struct StateAccount {
    pub authority: Pubkey,
    pub start_date: i64,
    pub end_date: i64,
    pub bld_mint: Pubkey,
    pub bld_token_account: Pubkey,
}

// Define error codes
#[error]
pub enum ErrorCode {
    #[msg("Invalid claim period")]
    InvalidClaimPeriod,
    #[msg("Invalid NFT owner")]
    InvalidNFTOwner,
    #[msg("Invalid $BLD mint")]
    InvalidBLDMint,
}

// Helper function to transfer tokens
fn transfer_tokens(
    from_token_account: AccountInfo,
    to_token_account: AccountInfo,
    authority: Pubkey,
    amount: u64,
) -> Result<()> {
    let cpi_program = anchor_spl::token::ID;
    let cpi_accounts = anchor_spl::token::Transfer {
        from: from_token_account,
        to: to_token_account,
        authority,
    };
    let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
    anchor_spl::token::transfer(cpi_ctx, amount)?;

    Ok(())
}
```
