"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: Develop a smart contract in Solana's Anchor framework to enforce the 5 NFT max per transaction rule for Tim Cheese minting.
Generated: DETERMINISTIC_3c261decad87530a
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod tim_cheese_mint {
    use super::*;

    // Context for the minting instruction
    #[derive(Accounts)]
    pub struct MintTimCheese<'info> {
        #[account(mut)]
        pub payer: Signer<'info>,
        #[account(mut)]
        pub mint_authority: Signer<'info>,
        #[account(
            mut,
            constraint = mint.key() == tim_cheese_mint.key()
        )]
        pub mint: Account<'info, Mint>,
        #[account(
            init_if_needed,
            payer = payer,
            associated_token::mint = mint,
            associated_token::authority = payer
        )]
        pub payer_ata: Account<'info, TokenAccount>,
        #[account(
            seeds = [b"tim_cheese_mint".as_ref()],
            bump
        )]
        pub tim_cheese_mint: Account<'info, Mint>,
        pub token_program: Program<'info, Token>,
        pub system_program: Program<'info, System>,
        pub rent: Sysvar<'info, Rent>,
    }

    // Instruction to mint Tim Cheese NFTs
    pub fn mint_tim_cheese(ctx: Context<MintTimCheese>, amount: u8) -> Result<()> {
        // Validate that the amount doesn't exceed 5 NFTs per transaction
        require!(amount <= 5, ErrorCode::MaxMintExceeded);

        let seeds = &[b"tim_cheese_mint".as_ref(), &[*ctx.bumps.get("tim_cheese_mint").unwrap()]];
        let signer = &[&seeds[..]];

        // Create the mint CPI context
        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            token::MintTo {
                mint: ctx.accounts.mint.to_account_info(),
                to: ctx.accounts.payer_ata.to_account_info(),
                authority: ctx.accounts.tim_cheese_mint.to_account_info(),
            },
            signer,
        );

        // Mint the specified amount of NFTs (1 token per NFT)
        for _ in 0..amount {
            token::mint_to(cpi_ctx.clone(), 1)?;
        }

        Ok(())
    }
}

#[error_code]
pub enum ErrorCode {
    #[msg("Cannot mint more than 5 Tim Cheese NFTs per transaction")]
    MaxMintExceeded,
}
```
