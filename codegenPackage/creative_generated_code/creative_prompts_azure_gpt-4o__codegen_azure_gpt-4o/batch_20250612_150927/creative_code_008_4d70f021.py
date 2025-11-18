"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Write a Solana smart contract to manage NFTs that burn themselves over time, as described in the Meta Blocks documentation.
Generated: DETERMINISTIC_4d70f0215ff58606
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint, Burn};
use std::time::{SystemTime, UNIX_EPOCH};

declare_id!("YourProgramIdHere");

#[program]
pub mod nft_self_burn {
    use super::*;

    pub fn initialize_nft(ctx: Context<InitializeNft>, expiry_duration: u64) -> Result<()> {
        let nft_account = &mut ctx.accounts.nft_account;
        let current_time = get_current_timestamp()?;
        nft_account.expiry_timestamp = current_time + expiry_duration;
        nft_account.owner = *ctx.accounts.owner.key;
        Ok(())
    }

    pub fn burn_expired_nft(ctx: Context<BurnExpiredNft>) -> Result<()> {
        let nft_account = &ctx.accounts.nft_account;
        
        // Check if the NFT has expired
        let current_time = get_current_timestamp()?;
        if current_time < nft_account.expiry_timestamp {
            return Err(ErrorCode::NftNotExpired.into());
        }

        // Burn the NFT
        let cpi_accounts = Burn {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.token_account.to_account_info(),
            authority: ctx.accounts.owner.to_account_info(),
        };
        let cpi_context = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::burn(cpi_context, 1)?;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeNft<'info> {
    #[account(mut)]
    pub owner: Signer<'info>,
    #[account(init, payer = owner, space = 8 + 40)]
    pub nft_account: Account<'info, NftAccount>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct BurnExpiredNft<'info> {
    #[account(mut, has_one = owner)]
    pub nft_account: Account<'info, NftAccount>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub owner: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct NftAccount {
    pub expiry_timestamp: u64, // The timestamp when the NFT expires
    pub owner: Pubkey,         // The owner of the NFT
}

/// Returns the current UNIX timestamp
fn get_current_timestamp() -> Result<u64> {
    let start = SystemTime::now();
    let since_epoch = start.duration_since(UNIX_EPOCH).map_err(|_| ErrorCode::TimestampError)?;
    Ok(since_epoch.as_secs())
}

#[error_code]
pub enum ErrorCode {
    #[msg("The current timestamp is earlier than the expiry timestamp.")]
    NftNotExpired,
    #[msg("Failed to retrieve the current timestamp.")]
    TimestampError,
}
```
