"""
Generated Code Metadata:
========================
Original URL: https://zip-4t3.pages.dev
Prompt: Develop a smart contract on Solana that interacts with Orca trade pools to automate token swaps between SOL and ORCA based on predefined conditions.
Generated: DETERMINISTIC_0df5c31368222cec
Batch ID: 20250612_154151
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
use orca_swap::cpi::accounts::Swap;
use orca_swap::program::OrcaSwap;
use orca_swap::{self, Swap as OrcaSwapInstruction};

declare_id!("YourProgramIDHere");

#[program]
pub mod auto_orca_swapper {
    use super::*;

    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = user, space = 8 + 32 + 32 + 8 + 8)]
        pub config: Account<'info, SwapConfig>,
        #[account(mut)]
        pub user: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[derive(Accounts)]
    pub struct ExecuteSwap<'info> {
        #[account(mut)]
        pub config: Account<'info, SwapConfig>,
        #[account(mut)]
        pub user: Signer<'info>,
        #[account(mut)]
        pub user_sol: AccountInfo<'info>,
        #[account(mut)]
        pub user_orca: Account<'info, TokenAccount>,
        #[account(mut)]
        pub orca_pool: AccountInfo<'info>,
        #[account(mut)]
        pub orca_pool_authority: AccountInfo<'info>,
        #[account(mut)]
        pub pool_sol: AccountInfo<'info>,
        #[account(mut)]
        pub pool_orca: Account<'info, TokenAccount>,
        pub token_program: Program<'info, Token>,
        pub orca_swap_program: Program<'info, OrcaSwap>,
        pub system_program: Program<'info, System>,
    }

    #[account]
    pub struct SwapConfig {
        pub owner: Pubkey,
        pub orca_pool: Pubkey,
        pub min_sol_amount: u64,
        pub min_orca_amount: u64,
    }

    pub fn initialize(
        ctx: Context<Initialize>,
        orca_pool: Pubkey,
        min_sol_amount: u64,
        min_orca_amount: u64,
    ) -> Result<()> {
        let config = &mut ctx.accounts.config;
        config.owner = *ctx.accounts.user.key;
        config.orca_pool = orca_pool;
        config.min_sol_amount = min_sol_amount;
        config.min_orca_amount = min_orca_amount;
        Ok(())
    }

    pub fn execute_swap(ctx: Context<ExecuteSwap>, amount: u64, swap_to_sol: bool) -> Result<()> {
        let config = &ctx.accounts.config;

        // Verify owner
        if config.owner != *ctx.accounts.user.key {
            return Err(ProgramError::IllegalOwner.into());
        }

        // Verify minimum amounts
        if swap_to_sol && amount < config.min_orca_amount {
            return Err(ErrorCode::AmountBelowMinimum.into());
        } else if !swap_to_sol && amount < config.min_sol_amount {
            return Err(ErrorCode::AmountBelowMinimum.into());
        }

        let cpi_program = ctx.accounts.orca_swap_program.to_account_info();
        let cpi_accounts = Swap {
            authority: ctx.accounts.orca_pool_authority.clone(),
            pool: ctx.accounts.orca_pool.clone(),
            pool_sol: ctx.accounts.pool_sol.clone(),
            pool_orca: ctx.accounts.pool_orca.to_account_info(),
            user_sol: ctx.accounts.user_sol.clone(),
            user_orca: ctx.accounts.user_orca.to_account_info(),
            token_program: ctx.accounts.token_program.to_account_info(),
        };

        let swap_instruction = OrcaSwapInstruction {
            amount,
            swap_to_sol,
        };

        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        orca_swap::cpi::swap(cpi_ctx, swap_instruction)?;

        Ok(())
    }
}

#[error_code]
pub enum ErrorCode {
    #[msg("Swap amount is below the minimum configured amount")]
    AmountBelowMinimum,
}
```
