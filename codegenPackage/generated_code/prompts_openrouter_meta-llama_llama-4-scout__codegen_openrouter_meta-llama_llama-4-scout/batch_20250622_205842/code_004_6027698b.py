"""
Generated Code Metadata:
========================
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a simple smart contract on Solana that handles whitelist minting with a public and whitelist price set to free.
Generated: DETERMINISTIC_6027698b12756c5e
Batch ID: 20250622_205842
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

// Define the program ID
declare_id!("");

// Define the WhitelistMint program
#[program]
pub mod whitelist_mint {
    use super::*;

    // Initialize the whitelist mint program
    pub fn initialize(ctx: Context<Initialize>, public_price: u64, whitelist_price: u64) -> Result<()> {
        let whitelist_mint_account = &mut ctx.accounts.whitelist_mint_account;
        whitelist_mint_account.public_price = public_price;
        whitelist_mint_account.whitelist_price = whitelist_price;
        whitelist_mint_account.mint_authority = ctx.accounts.mint_authority.key();
        Ok(())
    }

    // Mint token to public user
    pub fn mint_public(ctx: Context<MintPublic>) -> Result<()> {
        let whitelist_mint_account = &ctx.accounts.whitelist_mint_account;
        let token_account = &mut ctx.accounts.token_account;
        let mint = &ctx.accounts.mint;

        // Check if public price is 0 (free)
        if whitelist_mint_account.public_price > 0 {
            return Err(WhitelistMintError::PublicSaleNotStarted.into());
        }

        // Mint token
        token::mint_to(
            CpiContext::new(
                ctx.accounts.token_program.key(),
                token::MintTo {
                    mint: mint.key(),
                    to: token_account.key(),
                    authority: whitelist_mint_account.mint_authority,
                },
            ),
            1,
        )?;

        Ok(())
    }

    // Mint token to whitelisted user
    pub fn mint_whitelist(ctx: Context<MintWhitelist>) -> Result<()> {
        let whitelist_mint_account = &ctx.accounts.whitelist_mint_account;
        let token_account = &mut ctx.accounts.token_account;
        let mint = &ctx.accounts.mint;
        let whitelisted_user = &ctx.accounts.whitelisted_user;

        // Check if whitelist price is 0 (free)
        if whitelist_mint_account.whitelist_price > 0 {
            return Err(WhitelistMintError::WhitelistSaleNotStarted.into());
        }

        // Check if user is whitelisted
        if !whitelisted_user.is_whitelisted {
            return Err(WhitelistMintError::UserNotWhitelisted.into());
        }

        // Mint token
        token::mint_to(
            CpiContext::new(
                ctx.accounts.token_program.key(),
                token::MintTo {
                    mint: mint.key(),
                    to: token_account.key(),
                    authority: whitelist_mint_account.mint_authority,
                },
            ),
            1,
        )?;

        Ok(())
    }
}

// Define the WhitelistMintAccount struct
#[account]
pub struct WhitelistMintAccount {
    pub public_price: u64,
    pub whitelist_price: u64,
    pub mint_authority: Pubkey,
}

// Define the WhitelistedUser struct
#[account]
pub struct WhitelistedUser {
    pub user: Pubkey,
    pub is_whitelisted: bool,
}

// Define errors
#[error]
pub enum WhitelistMintError {
    #[msg("Public sale has not started")]
    PublicSaleNotStarted,
    #[msg("Whitelist sale has not started")]
    WhitelistSaleNotStarted,
    #[msg("User is not whitelisted")]
    UserNotWhitelisted,
}

// Define the Initialize context
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = mint_authority, space = 8 + 40)]
    pub whitelist_mint_account: Account<'info, WhitelistMintAccount>,
    #[account(mut)]
    pub mint_authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the MintPublic context
#[derive(Accounts)]
pub struct MintPublic<'info> {
    #[account(mut, has_one = mint_authority)]
    pub whitelist_mint_account: Account<'info, WhitelistMintAccount>,
    #[account(init, payer = buyer, space = 8 + 165)]
    pub token_account: Account<'info, token::TokenAccount>,
    pub mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    pub token_program: Program<'info, token::Token>,
    pub system_program: Program<'info, System>,
}

// Define the MintWhitelist context
#[derive(Accounts)]
pub struct MintWhitelist<'info> {
    #[account(mut, has_one = mint_authority)]
    pub whitelist_mint_account: Account<'info, WhitelistMintAccount>,
    #[account(init, payer = buyer, space = 8 + 165)]
    pub token_account: Account<'info, token::TokenAccount>,
    pub mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub whitelisted_user: Account<'info, WhitelistedUser>,
    pub token_program: Program<'info, token::Token>,
    pub system_program: Program<'info, System>,
}
```
