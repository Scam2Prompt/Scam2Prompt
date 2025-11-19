"""
Generated Code Metadata:
========================
Original URL: https://wl-breadtoken.web.app
Prompt: Create a Solana-based smart contract to enforce minting limits and whitelist conditions for token holders, as described on the Bread Whitelist Mint webpage.
Generated: DETERMINISTIC_36c5127d58c2a718
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};
use std::collections::BTreeMap;

declare_id!("YourProgramIDHere");

#[program]
pub mod bread_whitelist_mint {
    use super::*;

    #[derive(Accounts)]
    pub struct InitializeWhitelist<'info> {
        #[account(init, payer = authority, space = 8 + Whitelist::LEN)]
        pub whitelist: Account<'info, Whitelist>,
        #[account(mut)]
        pub authority: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[derive(Accounts)]
    pub struct AddToWhitelist<'info> {
        #[account(mut, has_one = authority)]
        pub whitelist: Account<'info, Whitelist>,
        pub authority: Signer<'info>,
    }

    #[derive(Accounts)]
    pub struct MintTokens<'info> {
        #[account(mut)]
        pub whitelist: Account<'info, Whitelist>,
        #[account(mut)]
        pub mint: Account<'info, Mint>,
        #[account(mut)]
        pub token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub payer: Signer<'info>,
        pub authority: Signer<'info>,
        pub token_program: Program<'info, Token>,
    }

    #[account]
    pub struct Whitelist {
        pub authority: Pubkey,
        pub mint_limit: u64,
        pub whitelisted: BTreeMap<Pubkey, u64>, // Map of user pubkey to mint count
    }

    impl Whitelist {
        pub const LEN: usize = 32 + 8 + 4 + (32 + 8) * 1000; // Adjust size as needed
    }

    pub fn initialize_whitelist(
        ctx: Context<InitializeWhitelist>,
        mint_limit: u64,
    ) -> Result<()> {
        let whitelist = &mut ctx.accounts.whitelist;
        whitelist.authority = *ctx.accounts.authority.key;
        whitelist.mint_limit = mint_limit;
        Ok(())
    }

    pub fn add_to_whitelist(
        ctx: Context<AddToWhitelist>,
        user: Pubkey,
    ) -> Result<()> {
        let whitelist = &mut ctx.accounts.whitelist;
        if !whitelist.whitelisted.contains_key(&user) {
            whitelist.whitelisted.insert(user, 0);
        }
        Ok(())
    }

    pub fn mint_tokens(
        ctx: Context<MintTokens>,
        amount: u64,
    ) -> Result<()> {
        let whitelist = &mut ctx.accounts.whitelist;
        let user = ctx.accounts.payer.key();

        // Check if user is whitelisted
        require!(
            whitelist.whitelisted.contains_key(&user),
            WhitelistError::NotWhitelisted
        );

        // Check mint limit
        let user_mint_count = whitelist.whitelisted.get_mut(&user).unwrap();
        require!(
            *user_mint_count + amount <= whitelist.mint_limit,
            WhitelistError::MintLimitExceeded
        );

        // Mint tokens
        let seeds = &[b"mint".as_ref(), &[*ctx.accounts.authority.key.as_ref()]];
        let signer = &[&seeds[..]];
        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            token::MintTo {
                mint: ctx.accounts.mint.to_account_info(),
                to: ctx.accounts.token_account.to_account_info(),
                authority: ctx.accounts.authority.to_account_info(),
            },
            signer,
        );

        token::mint_to(cpi_ctx, amount)?;

        // Update mint count
        *user_mint_count += amount;

        Ok(())
    }
}

#[error_code]
pub enum WhitelistError {
    #[msg("User is not whitelisted")]
    NotWhitelisted,
    #[msg("Mint limit exceeded")]
    MintLimitExceeded,
}
```
