"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memelauncher.vercel.app
Prompt: Write a Solana program that prevents minting additional tokens after the initial creation, adhering to the anti-rugpull practices mentioned on MemeLauncher.
Generated: DETERMINISTIC_8af9e2450c149d0c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_error::ProgramError;
use anchor_lang::solana_program::pubkey::Pubkey;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

declare_id!("YourProgramIdHere"); // Replace with your program ID

// Define the state of the token minting program
#[program]
pub mod anti_rugpull_mint {
    use super::*;

    // Initialize the mint with the specified parameters
    pub fn initialize_mint(ctx: Context<InitializeMint>, total_supply: u64) -> Result<()> {
        let mint = &mut ctx.accounts.mint;

        // Ensure the mint is initialized only once
        if mint.is_initialized {
            return Err(ProgramError::AccountAlreadyInitialized);
        }

        // Initialize the mint account
        token::initialize_mint(
            ctx.accounts.token_program.to_account_info(),
            mint.to_account_info(),
            &ctx.accounts.authority.key(),
            None,
            0, // Decimals
        )?;

        // Set the total supply
        mint.total_supply = total_supply;
        mint.is_initialized = true;

        Ok(())
    }

    // Function to mint tokens
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> Result<()> {
        let mint = &ctx.accounts.mint;

        // Prevent minting if already initialized
        if !mint.is_initialized {
            return Err(ProgramError::UninitializedAccount);
        }

        // Ensure there are no additional mints after initial creation
        if mint.total_supply > 0 {
            return Err(ProgramError::InvalidInstructionData);
        }

        // Mint tokens to the recipient
        let cpi_accounts = token::MintTo {
            mint: mint.to_account_info(),
            to: ctx.accounts.recipient.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.clone();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::mint_to(cpi_ctx, amount)?;

        // Update the total supply
        mint.total_supply += amount;

        Ok(())
    }
}

// Define the accounts for initializing the mint
#[derive(Accounts)]
pub struct InitializeMint<'info> {
    #[account(init, payer = authority, space = Mint::LEN + 8)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
}

// Define the accounts for minting tokens
#[derive(Accounts)]
pub struct MintTokens<'info> {
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub recipient: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the structure for the mint account
#[account]
pub struct Mint {
    pub total_supply: u64,
    pub is_initialized: bool,
}
```
