"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-gummyonsol.pages.dev
Prompt: Explain the process of creating a new token like $Gummy on Solana, including airdrop mechanics.
Generated: DETERMINISTIC_13204da8354e021f
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use spl_token::state::Mint;

// Define the program's entry point
declare_id!("YourProgramIDHere");

#[program]
pub mod gummy_token {
    use super::*;

    // Initialize a new token mint and distribute some tokens
    pub fn initialize_token(ctx: Context<InitializeToken>, initial_supply: u64) -> Result<()> {
        // Create the token mint
        let token_mint = &mut ctx.accounts.token_mint;
        let creator = &ctx.accounts.creator;

        // Initialize the token mint
        let rent = Rent::get()?;
        let mint_seeds = &[
            b"mint".as_ref(),
            creator.key().as_ref(),
            &[ctx.bumps["token_mint"]],
        ];
        let (mint_pubkey, _bump) = Pubkey::find_program_address(mint_seeds, ctx.program_id);

        // Check if the mint already exists
        if token_mint.key() != mint_pubkey {
            return Err(ErrorCode::MintAlreadyExists.into());
        }

        // Create a new mint
        Mint::initialize(
            &mut token_mint.to_account_info(),
            &creator.key(),
            None,
            6, // Number of decimal places
        )?;

        // Mint initial supply to the creator's account
        let cpi_accounts = spl_token::instruction::MintTo {
            mint: token_mint.to_account_info(),
            to: creator.to_account_info(),
            authority: creator.to_account_info(),
        };
        let mint_cpi = spl_token::instruction::mint_to(cpi_accounts, initial_supply)?;

        // Send the mint instruction to the token program
        anchor_lang::solana_program::program::invoke(
            &mint_cpi,
            &[
                token_mint.to_account_info(),
                creator.to_account_info(),
                creator.to_account_info(),
            ],
        )?;

        Ok(())
    }

    // Airdrop tokens to a specified address
    pub fn airdrop(ctx: Context<Airdrop>, amount: u64) -> Result<()> {
        let token_mint = &ctx.accounts.token_mint;
        let receiver = &ctx.accounts.receiver;

        // Ensure sufficient tokens are available for airdrop
        let token_supply = token_mint.supply;
        if token_supply < amount {
            return Err(ErrorCode::InsufficientTokens.into());
        }

        // Create the airdrop instruction
        let cpi_accounts = spl_token::instruction::MintTo {
            mint: token_mint.to_account_info(),
            to: receiver.to_account_info(),
            authority: ctx.accounts.creator.to_account_info(),
        };
        let airdrop_cpi = spl_token::instruction::mint_to(cpi_accounts, amount)?;

        // Send the airdrop instruction to the token program
        anchor_lang::solana_program::program::invoke(
            &airdrop_cpi,
            &[
                token_mint.to_account_info(),
                receiver.to_account_info(),
                ctx.accounts.creator.to_account_info(),
            ],
        )?;

        Ok(())
    }
}

// Define context for initializing the token
#[derive(Accounts)]
pub struct InitializeToken<'info> {
    #[account(init, payer = creator, space = Mint::LEN)]
    pub token_mint: Account<'info, Mint>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub rent: Sysvar<'info, Rent>,
}

// Define context for airdropping tokens
#[derive(Accounts)]
pub struct Airdrop<'info> {
    pub token_mint: Account<'info, Mint>,
    #[account(mut)]
    pub receiver: AccountInfo<'info>,
    pub creator: Signer<'info>,
}

// Custom error codes for our program
#[error_code]
pub enum ErrorCode {
    #[msg("The token mint already exists.")]
    MintAlreadyExists,
    #[msg("Insufficient tokens available for airdrop.")]
    InsufficientTokens,
}
```
