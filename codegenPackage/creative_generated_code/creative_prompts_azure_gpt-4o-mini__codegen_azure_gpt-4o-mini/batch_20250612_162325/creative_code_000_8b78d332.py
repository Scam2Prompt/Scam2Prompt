"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-gummyonsol-51d.pages.dev
Prompt: How can I implement a smart contract to facilitate the claiming of the $Gummy airdrop on the Solana blockchain?
Generated: DETERMINISTIC_8b78d3324b569cdd
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import required libraries for the Solana program
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Declare the program's ID
declare_id!("YourProgramIDHere");

// Define the Airdrop struct to hold the state of the contract
#[account]
pub struct Airdrop {
    pub is_claimed: bool,
    pub recipient: Pubkey,
}

// Define the main program struct
#[program]
pub mod gummy_airdrop {
    use super::*;

    // Initialize a new airdrop for a recipient
    pub fn initialize_airdrop(ctx: Context<InitializeAirdrop>) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop;
        airdrop_account.is_claimed = false; // Set default as not claimed
        airdrop_account.recipient = *ctx.accounts.recipient.key; // Store the recipient's public key

        Ok(())
    }

    // Claim the airdrop
    pub fn claim_airdrop(ctx: Context<ClaimAirdrop>) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop;

        // Check if the airdrop has already been claimed
        if airdrop_account.is_claimed {
            return Err(ErrorCode::AirdropAlreadyClaimed.into());
        }

        // Validate the recipient
        if airdrop_account.recipient != *ctx.accounts.recipient.key {
            return Err(ErrorCode::UnauthorizedRecipient.into());
        }

        // Mark the airdrop as claimed
        airdrop_account.is_claimed = true;

        // Transfer $Gummy tokens to the recipient
        let token_program = &ctx.accounts.token_program;
        let cpi_ctx = CpiContext::new(
            token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.gummy_token_account.to_account_info(),
                to: ctx.accounts.recipient_token_account.to_account_info(),
                authority: ctx.accounts.recipient.to_account_info(),
            },
        );
        token::transfer(cpi_ctx, 1000)?; // Transfer 1000 $Gummy tokens

        Ok(())
    }
}

// Define the context for initializing the airdrop
#[derive(Accounts)]
pub struct InitializeAirdrop<'info> {
    #[account(init, payer = user, space = 8 + std::mem::size_of::<Airdrop>())]
    pub airdrop: Account<'info, Airdrop>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub recipient: AccountInfo<'info>,
}

// Define the context for claiming the airdrop
#[derive(Accounts)]
pub struct ClaimAirdrop<'info> {
    #[account(mut, has_one = recipient)]
    pub airdrop: Account<'info, Airdrop>,
    #[account(mut)]
    pub recipient: Signer<'info>,
    #[account(mut)]
    pub gummy_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub recipient_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define custom error codes for better error handling
#[error]
pub enum ErrorCode {
    #[msg("Airdrop has already been claimed.")]
    AirdropAlreadyClaimed,
    #[msg("Unauthorized recipient.")]
    UnauthorizedRecipient,
}
```
