"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-ido-lake.vercel.app
Prompt: Generate a code snippet for a smart contract that facilitates an Initial DEX Offering (IDO) for a token on the Solana blockchain.
Generated: DETERMINISTIC_25920d273d7aa9e9
Batch ID: 20250612_162203
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

// Declare the program ID for Anchor framework
declare_id!("YourProgramIDHere");

#[program]
pub mod ido_contract {
    use super::*;

    // Initialize the IDO configuration
    pub fn initialize_ido(
        ctx: Context<InitializeIDO>, 
        token_price: u64, 
        ido_token_supply: u64
    ) -> Result<()> {
        let ido_account = &mut ctx.accounts.ido_account;
        ido_account.token_price = token_price;
        ido_account.total_supply = ido_token_supply;
        ido_account.sold_tokens = 0;
        ido_account.authority = ctx.accounts.authority.key();
        Ok(())
    }

    // Allow users to purchase tokens
    pub fn purchase_tokens(ctx: Context<PurchaseTokens>, amount: u64) -> Result<()> {
        let ido_account = &mut ctx.accounts.ido_account;

        // Ensure sufficient tokens are available for sale
        let remaining_tokens = ido_account.total_supply - ido_account.sold_tokens;
        require!(remaining_tokens >= amount, IdoError::InsufficientTokensAvailable);

        // Calculate total cost for the purchase
        let cost = amount.checked_mul(ido_account.token_price)
            .ok_or(IdoError::ArithmeticError)?;

        // Transfer payment tokens (e.g., USDC) from the buyer to the IDO authority
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.buyer_payment_account.to_account_info(),
                    to: ctx.accounts.authority_payment_account.to_account_info(),
                    authority: ctx.accounts.buyer.to_account_info(),
                },
            ),
            cost,
        )?;

        // Transfer purchased tokens from IDO token account to the buyer
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.ido_token_account.to_account_info(),
                    to: ctx.accounts.buyer_token_account.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            amount,
        )?;

        // Update sold tokens count
        ido_account.sold_tokens = ido_account.sold_tokens.checked_add(amount)
            .ok_or(IdoError::ArithmeticError)?;

        Ok(())
    }
}

// Define accounts structures for each instruction

#[derive(Accounts)]
pub struct InitializeIDO<'info> {
    #[account(init, payer = authority, space = 8 + 8 + 8 + 8 + 32)]
    pub ido_account: Account<'info, IdoAccount>,
    pub authority: Signer<'info>,
    #[account(mut)]
    pub ido_token_account: Account<'info, TokenAccount>,
    pub mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PurchaseTokens<'info> {
    #[account(mut)]
    pub ido_account: Account<'info, IdoAccount>,
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub buyer_payment_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub buyer_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub authority_payment_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub ido_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// State for the IDO account
#[account]
pub struct IdoAccount {
    pub token_price: u64,       // Price per token in payment token units (e.g., USDC)
    pub total_supply: u64,      // Total token supply available for the IDO
    pub sold_tokens: u64,       // Number of tokens sold
    pub authority: Pubkey,      // Authority of the IDO (e.g., project owner)
}

// Error codes for the program
#[error_code]
pub enum IdoError {
    #[msg("Insufficient tokens available for purchase.")]
    InsufficientTokensAvailable,
    #[msg("Arithmetic operation resulted in an overflow or underflow.")]
    ArithmeticError,
}
```
