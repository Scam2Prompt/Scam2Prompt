"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanaclaime.web.app
Prompt: Write a smart contract for Solana that handles first-come-first-serve (FCFS) airdrops of $NANA tokens, ensuring compatibility with Helio's payment platform.
Generated: DETERMINISTIC_94d19d28d2473109
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};

// Define the program ID
declare_id!("YourProgramIdHere");

// Define the main program structure
#[program]
pub mod nana_airdrop {
    use super::*;

    // Initialization function for the airdrop
    pub fn initialize(ctx: Context<Initialize>, airdrop_amount: u64) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;
        airdrop_account.airdrop_amount = airdrop_amount;
        airdrop_account.claimed = 0;
        Ok(())
    }

    // A function to claim airdrop tokens
    pub fn claim_airdrop(ctx: Context<ClaimAirdrop>) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;

        // Check if the airdrop has been claimed by the user
        if airdrop_account.claimed >= airdrop_account.airdrop_amount {
            return Err(ErrorCode::AirdropAlreadyClaimed.into());
        }

        // Transfer the specified amount of tokens to the claimer
        let amount_to_claim = airdrop_account.airdrop_amount - airdrop_account.claimed;
        token::transfer(ctx.accounts.into_transfer_context(), amount_to_claim)?;

        // Update the claimed amount
        airdrop_account.claimed += amount_to_claim;

        Ok(())
    }
}

// Define the airdrop account structure
#[account]
pub struct AirdropAccount {
    pub airdrop_amount: u64, // Total amount of tokens available for airdrop
    pub claimed: u64,        // Amount of tokens already claimed
}

// Define the context for initializing the airdrop
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for claiming the airdrop
#[derive(Accounts)]
pub struct ClaimAirdrop<'info> {
    #[account(mut)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_token_account: Box<Account<'info, TokenAccount>>,
    pub token_program: Program<'info, Token>,
}

// Define the error codes for the smart contract
#[error]
pub enum ErrorCode {
    #[msg("The airdrop has already been fully claimed.")]
    AirdropAlreadyClaimed,
}

// Implement conversion for token transfer context
impl<'info> ClaimAirdrop<'info> {
    fn into_transfer_context(self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.user_token_account.to_account_info(),
            to: self.airdrop_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
