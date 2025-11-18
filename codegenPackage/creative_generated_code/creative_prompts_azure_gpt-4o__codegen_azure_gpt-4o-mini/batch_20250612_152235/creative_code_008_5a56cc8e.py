"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-samoyed.web.app
Prompt: Write a smart contract example for managing token minting rights based on whitelist status in the Solana ecosystem.
Generated: DETERMINISTIC_5a56cc8e52c0e3b7
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};

declare_id!("YourProgramIDHere");

#[program]
pub mod token_minting {
    use super::*;

    /// Initializes the contract and sets up the mint and whitelist.
    pub fn initialize(ctx: Context<Initialize>, mint_authority: Pubkey) -> ProgramResult {
        let state = &mut ctx.accounts.state;
        state.mint_authority = mint_authority;
        state.whitelist = vec![];
        Ok(())
    }

    /// Mints tokens if the user is whitelisted.
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> ProgramResult {
        let state = &ctx.accounts.state;

        // Check if the sender is whitelisted
        if !state.whitelist.contains(&ctx.accounts.user.key()) {
            return Err(ErrorCode::UserNotWhitelisted.into());
        }

        // Execute the minting operation
        let cpi_accounts = token::MintTo {
            mint: ctx.accounts.mint.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.mint_authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::mint_to(CpiContext::new(cpi_program, cpi_accounts), amount)?;

        Ok(())
    }

    /// Adds a user to the whitelist.
    pub fn add_to_whitelist(ctx: Context<ModifyWhitelist>, user: Pubkey) -> ProgramResult {
        let state = &mut ctx.accounts.state;

        // Ensure that the caller is the mint authority
        if ctx.accounts.mint_authority.key() != state.mint_authority {
            return Err(ErrorCode::Unauthorized.into());
        }

        // Check if the user is already whitelisted
        if state.whitelist.contains(&user) {
            return Err(ErrorCode::UserAlreadyWhitelisted.into());
        }

        state.whitelist.push(user);
        Ok(())
    }

    /// Removes a user from the whitelist.
    pub fn remove_from_whitelist(ctx: Context<ModifyWhitelist>, user: Pubkey) -> ProgramResult {
        let state = &mut ctx.accounts.state;

        // Ensure that the caller is the mint authority
        if ctx.accounts.mint_authority.key() != state.mint_authority {
            return Err(ErrorCode::Unauthorized.into());
        }

        // Remove the user from the whitelist
        state.whitelist.retain(|&whitelisted_user| whitelisted_user != user);
        Ok(())
    }
}

/// State of the contract holding the mint authority and whitelist.
#[account]
pub struct State {
    pub mint_authority: Pubkey,
    pub whitelist: Vec<Pubkey>,
}

/// Context for initializing the contract.
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 4 * 32)]
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

/// Context for minting tokens.
#[derive(Accounts)]
pub struct MintTokens<'info> {
    #[account(mut)]
    pub state: Account<'info, State>,
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub mint_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

/// Context for modifying the whitelist.
#[derive(Accounts)]
pub struct ModifyWhitelist<'info> {
    #[account(mut)]
    pub state: Account<'info, State>,
    pub mint_authority: Signer<'info>,
}

/// Custom error codes for the smart contract.
#[error]
pub enum ErrorCode {
    #[msg("User is not whitelisted.")]
    UserNotWhitelisted,
    #[msg("User is already whitelisted.")]
    UserAlreadyWhitelisted,
    #[msg("Unauthorized access.")]
    Unauthorized,
}
```
