"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobukineko.pages.dev
Prompt: Create a smart contract on Solana to support the $BOBUKI token presale, including functionality for swapping SOL and handling slippage settings.
Generated: DETERMINISTIC_6e638675963b5b10
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// BobukiTokenPresale Contract
// A smart contract for the $BOBUKI token presale on Solana.

use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;

declare_id!("ReplaceWithYourProgramID");

#[program]
pub mod bobuki_presale {
    use super::*;

    // Initialize the presale.
    pub fn initialize(ctx: Context<Initialize>, token_price: u64, max_slippage: u8) -> Result<()> {
        let presale_account = &mut ctx.accounts.presale_account;
        presale_account.owner = *ctx.accounts.owner.key;
        presale_account.token_price = token_price; // Price in lamports per token.
        presale_account.max_slippage = max_slippage; // Max slippage in percentage.
        presale_account.sol_balance = 0;
        Ok(())
    }

    // Swap SOL for $BOBUKI tokens.
    pub fn swap_sol(ctx: Context<SwapSol>, amount: u64) -> Result<()> {
        let presale_account = &mut ctx.accounts.presale_account;
        let user_account = &ctx.accounts.user;

        // Ensure sufficient SOL is sent.
        require!(amount > 0, SwapError::InsufficientFunds);

        // Calculate the number of tokens to be given.
        let tokens_to_mint = amount / presale_account.token_price;

        // Ensure slippage constraints are met.
        let slippage_limit = presale_account.token_price * (100 + presale_account.max_slippage as u64) / 100;
        require!(tokens_to_mint >= slippage_limit, SwapError::SlippageExceeded);

        // Update presale state.
        presale_account.sol_balance += amount;

        // Mint tokens (mock functionality, replace with actual token minting logic).
        let seeds = &[presale_account.to_account_info().key.as_ref()];
        let signer = &[&seeds[..]];
        anchor_lang::solana_program::program::invoke_signed(
            &anchor_lang::solana_program::system_instruction::transfer(
                &ctx.accounts.user.key,
                &presale_account.to_account_info().key,
                amount,
            ),
            &[
                user_account.to_account_info(),
                presale_account.to_account_info(),
                ctx.accounts.system_program.to_account_info(),
            ],
            signer,
        )?;

        Ok(())
    }
}

// Define custom errors for the presale contract.
#[error_code]
pub enum SwapError {
    #[msg("Insufficient funds sent.")]
    InsufficientFunds,
    #[msg("Slippage limit exceeded.")]
    SlippageExceeded,
}

// Define state for the presale account.
#[account]
pub struct PresaleAccount {
    pub owner: Pubkey,       // Owner of the presale.
    pub token_price: u64,    // Price per $BOBUKI token in lamports.
    pub max_slippage: u8,    // Max slippage percentage.
    pub sol_balance: u64,    // Balance of SOL collected in the presale.
}

// Contexts for contract instructions.
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 8 + 1 + 8)]
    pub presale_account: Account<'info, PresaleAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct SwapSol<'info> {
    #[account(mut)]
    pub presale_account: Account<'info, PresaleAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}
```

Replace "ReplaceWithYourProgramID" with your program's actual ID. Ensure that proper logic for minting tokens is implemented later, as this example only provides the framework for swapping SOL.
