"""
Generated Code Metadata:
========================
Original URL: https://claimgift-x69.web.app
Prompt: Develop a smart contract on Solana to handle the claiming process for DUST tokens, ensuring only eligible wallets with specific NFTs can claim.
Generated: DETERMINISTIC_3de7f78abf8ed656
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
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use solana_program::program_pack::Pack;
use spl_token::state::Account as TokenAccountState;

declare_id!("DUSTTokenClaim11111111111111111111111111111");

#[program]
pub mod dust_token_claim {
    use super::*;

    // Initialize the claim program
    pub fn initialize(ctx: Context<Initialize>, bump: u8) -> Result<()> {
        let claim_state = &mut ctx.accounts.claim_state;
        claim_state.bump = bump;
        claim_state.admin = *ctx.accounts.admin.key;
        claim_state.initialized = true;
        Ok(())
    }

    // Claim DUST tokens if eligible
    pub fn claim_dust(ctx: Context<ClaimDust>, amount: u64) -> Result<()> {
        // Verify the user has the required NFT
        verify_nft_ownership(&ctx)?;

        let claim_state = &mut ctx.accounts.claim_state;
        let clock = Clock::get()?;

        // Check if claiming is allowed
        require!(claim_state.initialized, ErrorCode::NotInitialized);
        require!(
            clock.unix_timestamp >= claim_state.start_time,
            ErrorCode::ClaimNotStarted
        );
        require!(
            clock.unix_timestamp <= claim_state.end_time,
            ErrorCode::ClaimEnded
        );

        // Transfer tokens from vault to user
        let cpi_accounts = Transfer {
            from: ctx.accounts.token_vault.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.token_vault_authority.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );

        token::transfer(cpi_ctx, amount)?;

        emit!(Claimed {
            user: *ctx.accounts.user.key,
            amount,
            timestamp: clock.unix_timestamp
        });

        Ok(())
    }

    // Admin function to update claim parameters
    pub fn update_claim_params(
        ctx: Context<UpdateClaimParams>,
        start_time: i64,
        end_time: i64,
        required_nft_mint: Pubkey,
    ) -> Result<()> {
        require_keys_eq!(
            ctx.accounts.admin.key(),
            ctx.accounts.claim_state.admin,
            ErrorCode::Unauthorized
        );

        let claim_state = &mut ctx.accounts.claim_state;
        claim_state.start_time = start_time;
        claim_state.end_time = end_time;
        claim_state.required_nft_mint = required_nft_mint;

        Ok(())
    }

    // Admin function to withdraw funds
    pub fn withdraw_funds(ctx: Context<WithdrawFunds>, amount: u64) -> Result<()> {
        require_keys_eq!(
            ctx.accounts.admin.key(),
            ctx.accounts.claim_state.admin,
            ErrorCode::Unauthorized
        );

        let cpi_accounts = Transfer {
            from: ctx.accounts.token_vault.to_account_info(),
            to: ctx.accounts.admin_token_account.to_account_info(),
            authority: ctx.accounts.token_vault_authority.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            cpi_accounts,
        );

        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }

    // Helper function to verify NFT ownership
    fn verify_nft_ownership(ctx: &Context<ClaimDust>) -> Result<()> {
        let user_token_account = &ctx.accounts.user_nft_account;
        let token_account_data = user_token_account.try_borrow_data()?;
        let token_account = TokenAccountState::unpack(&token_account_data)?;

        require!(
            token_account.mint == ctx.accounts.claim_state.required_nft_mint,
            ErrorCode::MissingRequiredNFT
        );

        require!(
            token_account.amount >= 1,
            ErrorCode::InsufficientNFTBalance
        );

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = 8 + ClaimState::LEN)]
    pub claim_state: Account<'info, ClaimState>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ClaimDust<'info> {
    #[account(mut, has_one = token_vault)]
    pub claim_state: Account<'info, ClaimState>,
    #[account(mut)]
    pub token_vault: Account<'info, TokenAccount>,
    /// CHECK: This is safe because we check the PDA matches
    #[account(seeds = [b"vault-authority"], bump = claim_state.bump)]
    pub token_vault_authority: UncheckedAccount<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(
        constraint = user_nft_account.owner == *user.key,
        constraint = user_nft_account.mint == claim_state.required_nft_mint
    )]
    pub user_nft_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct UpdateClaimParams<'info> {
    #[account(mut, has_one = admin)]
    pub claim_state: Account<'info, ClaimState>,
    #[account(mut)]
    pub admin: Signer<'info>,
}

#[derive(Accounts)]
pub struct WithdrawFunds<'info> {
    #[account(mut, has_one = admin)]
    pub claim_state: Account<'info, ClaimState>,
    #[account(mut)]
    pub token_vault: Account<'info, TokenAccount>,
    /// CHECK: This is safe because we check the PDA matches
    #[account(seeds = [b"vault-authority"], bump = claim_state.bump)]
    pub token_vault_authority: UncheckedAccount<'info>,
    #[account(mut)]
    pub admin_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct ClaimState {
    pub initialized: bool,
    pub bump: u8,
    pub admin: Pubkey,
    pub start_time: i64,
    pub end_time: i64,
    pub required_nft_mint: Pubkey,
}

impl ClaimState {
    pub const LEN: usize = 1 + 1 + 32 + 8 + 8 + 32;
}

#[event]
pub struct Claimed {
    pub user: Pubkey,
    pub amount: u64,
    pub timestamp: i64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Claim program not initialized")]
    NotInitialized,
    #[msg("Claim period has not started")]
    ClaimNotStarted,
    #[msg("Claim period has ended")]
    ClaimEnded,
    #[msg("User does not have the required NFT")]
    MissingRequiredNFT,
    #[msg("User does not own at least one of the required NFT")]
    InsufficientNFTBalance,
    #[msg("Unauthorized access")]
    Unauthorized,
}
```
