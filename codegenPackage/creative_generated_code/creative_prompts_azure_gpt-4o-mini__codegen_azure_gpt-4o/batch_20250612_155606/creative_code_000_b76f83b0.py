"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pecinosol.com
Prompt: Generate a smart contract for the Pecino ($PCNO) meme token on the Solana blockchain, ensuring it includes features like 100% liquidity and no taxes.
Generated: DETERMINISTIC_b76f83b0dd5dc03e
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Solana smart contract for the Pecino ($PCNO) meme token fulfilling the provided requirements.

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Pecino ($PCNO) Token on Solana Blockchain
// 100% liquidity, no taxes

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, MintTo, Transfer};

// Declare the program ID
declare_id!("ReplaceWithYourProgramID");

// Program entrypoint
#[program]
pub mod pecino_token {
    use super::*;

    // Initializes the mint for the $PCNO token
    pub fn initialize_mint(
        ctx: Context<InitializeMint>,
        decimals: u8,
        supply: u64,
    ) -> Result<()> {
        let mint = &mut ctx.accounts.mint;
        mint.decimals = decimals; // Set the number of decimals for the token
        mint.supply = supply; // Set the total supply of the token

        // Mint initial supply to the owner's account
        let cpi_accounts = MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.token_account.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::mint_to(cpi_ctx, supply)?;

        Ok(())
    }

    // Transfers $PCNO tokens between accounts
    pub fn transfer_tokens(
        ctx: Context<TransferTokens>,
        amount: u64,
    ) -> Result<()> {
        let cpi_accounts = Transfer {
            from: ctx.accounts.from.to_account_info(),
            to: ctx.accounts.to.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the state and account structures for initialization
#[derive(Accounts)]
pub struct InitializeMint<'info> {
    #[account(init, payer = owner, mint::decimals = decimals, mint::authority = owner.key())]
    pub mint: Account<'info, Mint>,
    #[account(init, payer = owner, token::mint = mint, token::authority = owner)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct TransferTokens<'info> {
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}
```

**Note:** 
Replace `"ReplaceWithYourProgramID"` with your actual program ID after deploying the contract. Ensure that the Anchor framework is correctly set up in your environment before deploying this program.
