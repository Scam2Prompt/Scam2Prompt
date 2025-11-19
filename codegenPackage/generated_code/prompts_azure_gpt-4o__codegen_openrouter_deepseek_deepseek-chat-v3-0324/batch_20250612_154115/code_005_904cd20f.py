"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Develop a smart contract on Solana to implement a fee distribution mechanism similar to the Stay Loud "4% fee split after Meteora."
Generated: DETERMINISTIC_904cd20fdfc1beaa
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod fee_distribution {
    use super::*;

    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = authority, space = 8 + 32 + 32 + 8)]
        pub fee_distributor: Account<'info, FeeDistributor>,
        #[account(mut)]
        pub authority: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[derive(Accounts)]
    pub struct DistributeFees<'info> {
        #[account(mut, has_one = authority)]
        pub fee_distributor: Account<'info, FeeDistributor>,
        #[account(mut)]
        pub fee_vault: Account<'info, TokenAccount>,
        #[account(mut)]
        pub recipient1: Account<'info, TokenAccount>,
        #[account(mut)]
        pub recipient2: Account<'info, TokenAccount>,
        #[account(mut)]
        pub recipient3: Account<'info, TokenAccount>,
        #[account(mut)]
        pub recipient4: Account<'info, TokenAccount>,
        pub authority: Signer<'info>,
        pub token_program: Program<'info, Token>,
    }

    #[account]
    pub struct FeeDistributor {
        pub authority: Pubkey,
        pub fee_vault: Pubkey,
    }

    pub fn initialize(ctx: Context<Initialize>, fee_vault: Pubkey) -> Result<()> {
        let fee_distributor = &mut ctx.accounts.fee_distributor;
        fee_distributor.authority = *ctx.accounts.authority.key;
        fee_distributor.fee_vault = fee_vault;
        Ok(())
    }

    pub fn distribute_fees(ctx: Context<DistributeFees>) -> Result<()> {
        let fee_vault = &ctx.accounts.fee_vault;
        let fee_amount = fee_vault.amount;
        
        if fee_amount == 0 {
            return Err(ErrorCode::NoFeesToDistribute.into());
        }

        let quarter_amount = fee_amount / 4;

        // Transfer to recipient 1
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.fee_vault.to_account_info(),
                    to: ctx.accounts.recipient1.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            quarter_amount,
        )?;

        // Transfer to recipient 2
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.fee_vault.to_account_info(),
                    to: ctx.accounts.recipient2.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            quarter_amount,
        )?;

        // Transfer to recipient 3
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.fee_vault.to_account_info(),
                    to: ctx.accounts.recipient3.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            quarter_amount,
        )?;

        // Transfer to recipient 4
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.fee_vault.to_account_info(),
                    to: ctx.accounts.recipient4.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            quarter_amount,
        )?;

        Ok(())
    }
}

#[error_code]
pub enum ErrorCode {
    #[msg("No fees available to distribute")]
    NoFeesToDistribute,
}
```
