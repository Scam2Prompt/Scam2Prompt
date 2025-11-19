"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggoclaim.web.app
Prompt: Generate a code snippet for integrating the $DOGGO token into a Solana NFT project for staking rewards.
Generated: DETERMINISTIC_1d0b22220ed6aaa9
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};
use std::convert::TryInto;

/// State for the NFT staking program
#[derive(Accounts)]
pub struct StakeNFT<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub nft_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub doggo_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub doggo_mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

/// Instruction to stake NFT and earn $DOGGO tokens
#[program]
pub mod nft_staking {
    use super::*;

    pub fn stake_nft(ctx: Context<StakeNFT>, amount: u64) -> Result<()> {
        // Ensure the amount is valid and greater than zero
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer NFT to the staking program's account
        let nft_account = &ctx.accounts.nft_account;
        let user = &ctx.accounts.user;

        // Log the staking action
        msg!("Staking NFT: {:?}", nft_account.key());

        // Perform the transfer
        token::transfer(
            ctx.accounts.into_transfer_context(),
            1, // Assuming staking one NFT
        )?;

        // Mint $DOGGO tokens as staking rewards
        mint_doggo_tokens(ctx, user, amount)?;
        
        Ok(())
    }

    // Helper function to mint $DOGGO tokens
    fn mint_doggo_tokens(ctx: &Context<StakeNFT>, user: &Signer<'info>, amount: u64) -> Result<()> {
        let doggo_mint = &ctx.accounts.doggo_mint;
        let doggo_token_account = &ctx.accounts.doggo_token_account;

        // Mint $DOGGO tokens to the user's account
        token::mint_to(
            ctx.accounts.into_mint_to_context(user),
            amount,
        )?;

        // Log the minting action
        msg!("Minted {} $DOGGO tokens to {:?}", amount, user.key());

        Ok(())
    }
}

// Custom error codes for the program
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}

// Conversion functions for accounts context
impl<'info> StakeNFT<'info> {
    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.nft_account.to_account_info(),
            to: self.user.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }

    fn into_mint_to_context(&self, user: &Signer<'info>) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        let cpi_accounts = token::MintTo {
            mint: self.doggo_mint.to_account_info(),
            to: self.doggo_token_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
