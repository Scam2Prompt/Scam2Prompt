"""
Generated Code Metadata:
========================
Original URL: https://trumphyper.com
Prompt: "Create a smart contract on Solana for distributing NFT vouchers that can be exchanged for $TRUMP tokens, inspired by the Trump Memes project."
Generated: DETERMINISTIC_26f5810373af2713
Batch ID: 20250622_211343
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
use anchor_lang::solana_program::program_pack::Pack;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

// Declare the program ID
declare_id!("YourProgramIDHere");

// Define the program module
#[program]
pub mod nft_voucher_distributor {
    use super::*;

    // Function to initialize the voucher mint
    pub fn initialize_voucher_mint(
        ctx: Context<InitializeVoucherMint>,
        bump: u8,
    ) -> Result<()> {
        let voucher_mint = &mut ctx.accounts.voucher_mint;
        voucher_mint.bump = bump;
        voucher_mint.authority = ctx.accounts.authority.key();
        Ok(())
    }

    // Function to mint NFT vouchers
    pub fn mint_voucher(
        ctx: Context<MintVoucher>,
        amount: u64,
    ) -> Result<()> {
        let seeds = &[
            ctx.accounts.voucher_mint.to_account_info().key.as_ref(),
            &[ctx.accounts.voucher_mint.bump],
        ];
        let signer = &[&seeds[..]];

        token::mint_to(
            ctx.accounts.into_mint_to_context().with_signer(signer),
            amount,
        )?;
        Ok(())
    }

    // Function to redeem NFT vouchers for $TRUMP tokens
    pub fn redeem_voucher(
        ctx: Context<RedeemVoucher>,
        amount: u64,
    ) -> Result<()> {
        // Burn the voucher tokens
        token::burn(
            ctx.accounts.into_burn_context(),
            amount,
        )?;

        // Transfer $TRUMP tokens to the user
        token::transfer(
            ctx.accounts.into_transfer_context(),
            amount,
        )?;
        Ok(())
    }
}

// Define the voucher mint account structure
#[account]
pub struct VoucherMint {
    pub authority: Pubkey, // Authority that controls the mint
    pub bump: u8,          // Bump seed for PDA
}

// Context for initializing the voucher mint
#[derive(Accounts)]
pub struct InitializeVoucherMint<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 1)]
    pub voucher_mint: Account<'info, VoucherMint>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for minting NFT vouchers
#[derive(Accounts)]
pub struct MintVoucher<'info> {
    #[account(mut)]
    pub voucher_mint: Account<'info, VoucherMint>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Context for redeeming NFT vouchers
#[derive(Accounts)]
pub struct RedeemVoucher<'info> {
    #[account(mut)]
    pub voucher_mint: Account<'info, VoucherMint>,
    #[account(mut)]
    pub user_voucher_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub trump_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub trump_token_mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
}

// Helper methods for context conversion
impl<'info> MintVoucher<'info> {
    fn into_mint_to_context(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        let cpi_accounts = token::MintTo {
            mint: self.mint.to_account_info(),
            to: self.token_account.to_account_info(),
            authority: self.voucher_mint.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

impl<'info> RedeemVoucher<'info> {
    fn into_burn_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Burn<'info>> {
        let cpi_accounts = token::Burn {
            mint: self.voucher_mint.to_account_info(),
            to: self.user_voucher_account.to_account_info(),
            authority: self.voucher_mint.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }

    fn into_transfer_context(&self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.trump_token_account.to_account_info(),
            to: self.user_voucher_account.to_account_info(),
            authority: self.voucher_mint.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
