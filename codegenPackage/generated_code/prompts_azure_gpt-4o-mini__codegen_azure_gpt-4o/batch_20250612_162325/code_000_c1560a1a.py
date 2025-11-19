"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Generate a smart contract for the PUNDU token on Solana, incorporating the tokenomics where 45% goes to liquidity pool and 45% to presale participants.
Generated: DETERMINISTIC_c1560a1adfdb8034
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// PUNDU Token Smart Contract for Solana Blockchain
// This contract implements tokenomics where 45% of the supply goes to the liquidity pool
// and 45% goes to presale participants. The remaining 10% is reserved for other purposes.

// Import necessary Solana libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

// Declare the program ID
declare_id!("YourProgramIDHere");

#[program]
pub mod pundu_token {
    use super::*;

    // Initialize the PUNDU token mint and distribute initial supply
    pub fn initialize(
        ctx: Context<Initialize>,
        total_supply: u64,
    ) -> Result<()> {
        let mint = &mut ctx.accounts.mint;
        let liquidity_pool_account = &ctx.accounts.liquidity_pool_account;
        let presale_account = &ctx.accounts.presale_account;
        let remaining_account = &ctx.accounts.remaining_account;

        // Set the mint authority to the program
        mint.set_authority(ctx.accounts.authority.key(), None)?;

        // Calculate token allocations
        let liquidity_pool_tokens = total_supply * 45 / 100; // 45% to liquidity pool
        let presale_tokens = total_supply * 45 / 100;        // 45% to presale participants
        let remaining_tokens = total_supply - liquidity_pool_tokens - presale_tokens; // Remaining 10%

        // Mint tokens to the respective accounts
        token::mint_to(
            ctx.accounts.into_mint_to_context_liquidity(),
            liquidity_pool_tokens,
        )?;
        token::mint_to(
            ctx.accounts.into_mint_to_context_presale(),
            presale_tokens,
        )?;
        token::mint_to(
            ctx.accounts.into_mint_to_context_remaining(),
            remaining_tokens,
        )?;

        Ok(())
    }
}

// Context for the `initialize` function
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, mint::decimals = 9, mint::authority = authority)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub liquidity_pool_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub presale_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub remaining_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}

impl<'info> Initialize<'info> {
    // Helper function to create mint_to context for liquidity pool
    fn into_mint_to_context_liquidity(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        CpiContext::new(
            self.token_program.to_account_info(),
            token::MintTo {
                mint: self.mint.to_account_info(),
                to: self.liquidity_pool_account.to_account_info(),
                authority: self.authority.to_account_info(),
            },
        )
    }

    // Helper function to create mint_to context for presale participants
    fn into_mint_to_context_presale(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        CpiContext::new(
            self.token_program.to_account_info(),
            token::MintTo {
                mint: self.mint.to_account_info(),
                to: self.presale_account.to_account_info(),
                authority: self.authority.to_account_info(),
            },
        )
    }

    // Helper function to create mint_to context for remaining tokens
    fn into_mint_to_context_remaining(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        CpiContext::new(
            self.token_program.to_account_info(),
            token::MintTo {
                mint: self.mint.to_account_info(),
                to: self.remaining_account.to_account_info(),
                authority: self.authority.to_account_info(),
            },
        )
    }
}
```
