"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimrlb-12.web.app
Prompt: Develop a smart contract on Solana to automate the distribution of RLB tokens to eligible addresses, similar to Rollbit's airdrop system.
Generated: DETERMINISTIC_c3bad0f93f49efb4
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Automating Distribution of RLB Tokens on Solana Blockchain

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

// Declare the program ID.
declare_id!("YourProgramIDHere");

#[program]
pub mod rlb_airdrop {
    use super::*;

    // Airdrop function to distribute RLB tokens to eligible addresses.
    pub fn distribute_tokens(
        ctx: Context<DistributeTokens>,
        amount: u64,
    ) -> Result<()> {
        let sender = &ctx.accounts.sender_token_account;
        let receiver = &ctx.accounts.receiver_token_account;

        // Check if sender has enough balance for the transfer.
        if sender.amount < amount {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Transfer tokens to the eligible receiver.
        let transfer_instruction = token::Transfer {
            from: ctx.accounts.sender_token_account.to_account_info(),
            to: ctx.accounts.receiver_token_account.to_account_info(),
            authority: ctx.accounts.sender.to_account_info(),
        };
        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), transfer_instruction);
        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the accounts involved in the transaction.
#[derive(Accounts)]
pub struct DistributeTokens<'info> {
    /// The sender's wallet address and associated token account.
    /// CHECK: This is not dangerous because the program checks the balance before transferring.
    #[account(mut)]
    pub sender: Signer<'info>,
    #[account(
        mut,
        constraint = sender_token_account.owner == sender.key() @ ErrorCode::InvalidOwner,
        constraint = sender_token_account.mint == token_mint.key() @ ErrorCode::InvalidMint
    )]
    pub sender_token_account: Account<'info, TokenAccount>,

    /// The receiver's wallet address and associated token account.
    /// CHECK: This is not dangerous because the program ensures valid conditions for the transfer.
    #[account(
        mut,
        constraint = receiver_token_account.owner == receiver.key() @ ErrorCode::InvalidOwner,
        constraint = receiver_token_account.mint == token_mint.key() @ ErrorCode::InvalidMint
    )]
    pub receiver_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub receiver: SystemAccount<'info>,

    /// Token mint used for the RLB token.
    #[account(mut)]
    pub token_mint: Account<'info, Mint>,

    /// Token program for SPL tokens.
    pub token_program: Program<'info, Token>,
}

// Define custom errors for the smart contract.
#[error_code]
pub enum ErrorCode {
    #[msg("Insufficient funds in the sender's account.")]
    InsufficientFunds,
    #[msg("The token account owner is invalid.")]
    InvalidOwner,
    #[msg("The token mint is invalid.")]
    InvalidMint,
}
```
