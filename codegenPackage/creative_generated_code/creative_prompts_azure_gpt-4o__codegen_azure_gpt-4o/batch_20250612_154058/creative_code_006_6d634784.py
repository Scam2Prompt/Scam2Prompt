"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumphyper.com
Prompt: Provide code for creating a collectible NFT voucher on the Solana blockchain that can be exchanged for $TRUMP tokens, as described on the website.
Generated: DETERMINISTIC_6d634784ac32f3ae
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

// Declare the program ID and necessary configurations
declare_id!("YourProgramPublicKeyHere");

#[program]
mod nft_voucher {
    use super::*;

    // Function to mint an NFT voucher that can be exchanged for $TRUMP tokens
    pub fn create_nft_voucher(
        ctx: Context<CreateNftVoucher>,
        metadata_uri: String, // URI for NFT metadata
        trump_token_amount: u64, // Amount of $TRUMP tokens the voucher is redeemable for
    ) -> Result<()> {
        let voucher = &mut ctx.accounts.voucher;
        voucher.owner = ctx.accounts.owner.key();
        voucher.metadata_uri = metadata_uri;
        voucher.trump_token_amount = trump_token_amount;

        // Mint the NFT voucher
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.voucher_token_account.to_account_info(),
            authority: ctx.accounts.mint_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let mint_to_ctx = CpiContext::new(cpi_program, cpi_accounts);

        // Mint a single token representing the voucher
        token::mint_to(mint_to_ctx, 1)?;

        Ok(())
    }

    // Function to redeem the NFT voucher for $TRUMP tokens
    pub fn redeem_nft_voucher(ctx: Context<RedeemNftVoucher>) -> Result<()> {
        let voucher = &mut ctx.accounts.voucher;

        // Ensure the voucher is owned by the user redeeming it
        require!(
            voucher.owner == ctx.accounts.redeemer.key(),
            CustomError::UnauthorizedRedemption
        );

        // Transfer $TRUMP tokens to the redeemer
        let cpi_accounts = Transfer {
            from: ctx.accounts.trump_token_account.to_account_info(),
            to: ctx.accounts.redeemer_token_account.to_account_info(),
            authority: ctx.accounts.voucher_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let transfer_ctx = CpiContext::new(cpi_program, cpi_accounts);

        token::transfer(transfer_ctx, voucher.trump_token_amount)?;

        // Burn the NFT voucher token
        let burn_cpi_accounts = token::Burn {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.voucher_token_account.to_account_info(),
            authority: ctx.accounts.burn_authority.to_account_info(),
        };
        let burn_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), burn_cpi_accounts);

        token::burn(burn_ctx, 1)?;

        Ok(())
    }
}

// Account structures and context definitions

#[derive(Accounts)]
pub struct CreateNftVoucher<'info> {
    #[account(mut)]
    pub owner: Signer<'info>,
    #[account(init, payer = owner, space = 8 + 64 + 8 + 32)]
    pub voucher: Account<'info, Voucher>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub voucher_token_account: Account<'info, TokenAccount>,
    pub mint_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct RedeemNftVoucher<'info> {
    #[account(mut)]
    pub redeemer: Signer<'info>,
    #[account(mut)]
    pub trump_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub redeemer_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub voucher: Account<'info, Voucher>,
    #[account(mut)]
    pub voucher_token_account: Account<'info, TokenAccount>,
    pub mint: Account<'info, Mint>,
    pub voucher_authority: Signer<'info>,
    pub burn_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct Voucher {
    pub owner: Pubkey,
    pub metadata_uri: String,
    pub trump_token_amount: u64,
}

// Custom errors for handling specific cases
#[error_code]
pub enum CustomError {
    UnauthorizedRedemption,
}
```
