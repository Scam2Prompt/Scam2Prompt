"""
Generated Code Metadata:
========================
Original URL: https://satyloud.io
Prompt: Develop a smart contract on Solana that implements Loud's fee distribution mechanics, ensuring compliance with the 4% fee split after Meteora.
Generated: DETERMINISTIC_f82a5b149a280324
Batch ID: 20250612_154057
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

declare_id!("YourProgramIDHere");

#[program]
pub mod loud_fee_distribution {
    use super::*;

    #[derive(Accounts)]
    pub struct InitializeFeeDistribution<'info> {
        #[account(init, payer = authority, space = 8 + 32 + 32 + 8)]
        pub fee_distribution: Account<'info, FeeDistribution>,
        #[account(mut)]
        pub authority: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[account]
    pub struct FeeDistribution {
        pub meteora_account: Pubkey,
        pub loud_account: Pubkey,
        pub total_fees_collected: u64,
    }

    #[derive(Accounts)]
    pub struct DistributeFees<'info> {
        #[account(mut, has_one = meteora_account, has_one = loud_account)]
        pub fee_distribution: Account<'info, FeeDistribution>,
        #[account(mut)]
        pub source_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub meteora_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub loud_token_account: Account<'info, TokenAccount>,
        pub authority: Signer<'info>,
        pub token_program: Program<'info, Token>,
    }

    pub fn initialize(
        ctx: Context<InitializeFeeDistribution>,
        meteora_account: Pubkey,
        loud_account: Pubkey,
    ) -> Result<()> {
        let fee_distribution = &mut ctx.accounts.fee_distribution;
        fee_distribution.meteora_account = meteora_account;
        fee_distribution.loud_account = loud_account;
        fee_distribution.total_fees_collected = 0;
        Ok(())
    }

    pub fn distribute_fees(ctx: Context<DistributeFees>, amount: u64) -> Result<()> {
        require!(amount > 0, ErrorCode::InvalidAmount);

        let fee_distribution = &mut ctx.accounts.fee_distribution;
        let meteora_share = amount * 96 / 100; // 96% to Meteora
        let loud_share = amount * 4 / 100;     // 4% to Loud

        // Transfer to Meteora
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.source_token_account.to_account_info(),
                    to: ctx.accounts.meteora_token_account.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            meteora_share,
        )?;

        // Transfer to Loud
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.source_token_account.to_account_info(),
                    to: ctx.accounts.loud_token_account.to_account_info(),
                    authority: ctx.accounts.authority.to_account_info(),
                },
            ),
            loud_share,
        )?;

        fee_distribution.total_fees_collected += amount;

        Ok(())
    }

    #[error_code]
    pub enum ErrorCode {
        #[msg("Amount must be greater than zero")]
        InvalidAmount,
    }
}
```
