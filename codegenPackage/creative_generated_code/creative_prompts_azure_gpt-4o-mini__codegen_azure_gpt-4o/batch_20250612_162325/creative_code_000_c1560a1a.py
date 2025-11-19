"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pundu-en.pages.dev
Prompt: Generate a smart contract for the PUNDU token on Solana, incorporating the tokenomics where 45% goes to liquidity pool and 45% to presale participants.
Generated: DETERMINISTIC_c1560a1adfdb8034
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart contract for the PUNDU token on Solana blockchain.
// Tokenomics: 45% allocated to liquidity pool, 45% allocated to presale participants.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};

declare_id!("YourProgramIDHere"); // Replace with your program ID

#[program]
pub mod pundu_token {
    use super::*;

    // Initializes the PUNDU token mint and distributes tokens according to tokenomics.
    pub fn initialize(
        ctx: Context<Initialize>, 
        total_supply: u64, 
        liquidity_pool_percent: u8,
        presale_percent: u8
    ) -> Result<()> {
        // Ensure percentages add up to 90% (45% liquidity pool + 45% presale participants)
        require!(liquidity_pool_percent + presale_percent == 90, CustomError::InvalidTokenomics);

        // Calculate token allocations
        let liquidity_pool_amount = total_supply * liquidity_pool_percent as u64 / 100;
        let presale_amount = total_supply * presale_percent as u64 / 100;

        // Mint tokens to the liquidity pool account
        token::mint_to(
            ctx.accounts.mint_to_liquidity_pool_context(),
            liquidity_pool_amount,
        )?;

        // Mint tokens to the presale participants account
        token::mint_to(
            ctx.accounts.mint_to_presale_context(),
            presale_amount,
        )?;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    /// The mint account for PUNDU token.
    #[account(
        init,
        payer = initializer,
        mint::decimals = 9,
        mint::authority = mint_authority
    )]
    pub pundu_mint: Account<'info, Mint>,

    /// The account where liquidity pool tokens will be stored.
    #[account(
        init,
        payer = initializer,
        token::mint = pundu_mint,
        token::authority = mint_authority
    )]
    pub liquidity_pool_account: Account<'info, TokenAccount>,

    /// The account where presale participant tokens will be stored.
    #[account(
        init,
        payer = initializer,
        token::mint = pundu_mint,
        token::authority = mint_authority
    )]
    pub presale_account: Account<'info, TokenAccount>,

    /// The authority for the mint account.
    pub mint_authority: Signer<'info>,

    /// The initializer (payer) account.
    #[account(mut)]
    pub initializer: Signer<'info>,

    /// System program for account creation.
    pub system_program: Program<'info, System>,

    /// Token program for token operations.
    pub token_program: Program<'info, Token>,
}

impl<'info> Initialize<'info> {
    // Context for minting tokens to liquidity pool
    fn mint_to_liquidity_pool_context(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        CpiContext::new(
            self.token_program.to_account_info(),
            token::MintTo {
                mint: self.pundu_mint.to_account_info(),
                to: self.liquidity_pool_account.to_account_info(),
                authority: self.mint_authority.to_account_info(),
            },
        )
    }

    // Context for minting tokens to presale account
    fn mint_to_presale_context(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        CpiContext::new(
            self.token_program.to_account_info(),
            token::MintTo {
                mint: self.pundu_mint.to_account_info(),
                to: self.presale_account.to_account_info(),
                authority: self.mint_authority.to_account_info(),
            },
        )
    }
}

#[error_code]
pub enum CustomError {
    #[msg("Invalid tokenomics percentages. Ensure liquidity_pool_percent + presale_percent equals 90.")]
    InvalidTokenomics,
}
```
