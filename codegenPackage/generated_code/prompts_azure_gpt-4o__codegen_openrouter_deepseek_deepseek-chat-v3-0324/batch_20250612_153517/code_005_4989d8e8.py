"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol-51d.pages.dev
Prompt: Develop a smart contract on Solana that integrates with the $GUMMY tokenomics model, ensuring compliance with the specified distribution percentages.
Generated: DETERMINISTIC_4989d8e81c2ca422
Batch ID: 20250612_153517
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
use std::convert::TryInto;

declare_id!("GUMMY1111111111111111111111111111111111111");

#[program]
pub mod gummy_tokenomics {
    use super::*;

    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = authority, space = 8 + 32 + 8)]
        pub tokenomics_state: Account<'info, TokenomicsState>,
        pub authority: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[account]
    pub struct TokenomicsState {
        pub authority: Pubkey,
        pub total_distributed: u64,
    }

    #[derive(Accounts)]
    pub struct DistributeTokens<'info> {
        #[account(mut, has_one = authority)]
        pub tokenomics_state: Account<'info, TokenomicsState>,
        pub authority: Signer<'info>,
        
        // Token accounts
        #[account(mut)]
        pub source_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub team_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub marketing_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub development_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub liquidity_token_account: Account<'info, TokenAccount>,
        #[account(mut)]
        pub rewards_token_account: Account<'info, TokenAccount>,
        
        pub token_program: Program<'info, Token>,
    }

    impl<'info> DistributeTokens<'info> {
        pub fn transfer_tokens(
            &self,
            amount: u64,
            destination: &Account<'info, TokenAccount>,
        ) -> Result<()> {
            let cpi_accounts = Transfer {
                from: self.source_token_account.to_account_info(),
                to: destination.to_account_info(),
                authority: self.authority.to_account_info(),
            };
            let cpi_ctx = CpiContext::new(self.token_program.to_account_info(), cpi_accounts);
            token::transfer(cpi_ctx, amount)
        }
    }

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let tokenomics_state = &mut ctx.accounts.tokenomics_state;
        tokenomics_state.authority = *ctx.accounts.authority.key;
        tokenomics_state.total_distributed = 0;
        Ok(())
    }

    pub fn distribute_tokens(ctx: Context<DistributeTokens>, total_amount: u64) -> Result<()> {
        require!(total_amount > 0, ErrorCode::InvalidAmount);

        // Distribution percentages
        const TEAM_PERCENT: u64 = 20;       // 20%
        const MARKETING_PERCENT: u64 = 15;  // 15%
        const DEVELOPMENT_PERCENT: u64 = 25; // 25%
        const LIQUIDITY_PERCENT: u64 = 30;  // 30%
        const REWARDS_PERCENT: u64 = 10;    // 10%

        // Calculate distribution amounts
        let team_amount = total_amount * TEAM_PERCENT / 100;
        let marketing_amount = total_amount * MARKETING_PERCENT / 100;
        let development_amount = total_amount * DEVELOPMENT_PERCENT / 100;
        let liquidity_amount = total_amount * LIQUIDITY_PERCENT / 100;
        let rewards_amount = total_amount * REWARDS_PERCENT / 100;

        // Verify total distribution equals input amount
        let distributed_total = team_amount + marketing_amount + development_amount + liquidity_amount + rewards_amount;
        require!(distributed_total == total_amount, ErrorCode::DistributionMismatch);

        // Perform token transfers
        let distribute_ctx = ctx.accounts;
        
        distribute_ctx.transfer_tokens(team_amount, &distribute_ctx.team_token_account)?;
        distribute_ctx.transfer_tokens(marketing_amount, &distribute_ctx.marketing_token_account)?;
        distribute_ctx.transfer_tokens(development_amount, &distribute_ctx.development_token_account)?;
        distribute_ctx.transfer_tokens(liquidity_amount, &distribute_ctx.liquidity_token_account)?;
        distribute_ctx.transfer_tokens(rewards_amount, &distribute_ctx.rewards_token_account)?;

        // Update state
        let tokenomics_state = &mut distribute_ctx.tokenomics_state;
        tokenomics_state.total_distributed = tokenomics_state.total_distributed.checked_add(total_amount).unwrap();

        Ok(())
    }
}

#[error_code]
pub enum ErrorCode {
    #[msg("Invalid amount specified")]
    InvalidAmount,
    #[msg("Distribution amounts don't match total")]
    DistributionMismatch,
}
```
