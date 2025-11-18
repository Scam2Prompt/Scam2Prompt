"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-17.web.app
Prompt: Develop a smart contract on Solana that automates the distribution of DUST tokens to eligible wallets during an airdrop.
Generated: DETERMINISTIC_d70b8136d15b62d1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// This program automates the distribution of DUST tokens to eligible wallets during an airdrop on the Solana blockchain.

use anchor_lang::prelude::*;
use anchor_lang::solana_program::system_program;
use spl_token::state::Mint;

declare_id!("YourProgramIDHere");

#[program]
pub mod dust_airdrop {
    use super::*;

    /// Initializes the airdrop by setting the mint address and total amount of DUST tokens to distribute.
    pub fn initialize(ctx: Context<Initialize>, mint_address: Pubkey, total_amount: u64) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;
        airdrop_account.mint_address = mint_address;
        airdrop_account.total_amount = total_amount;
        airdrop_account.distributed_amount = 0;
        Ok(())
    }

    /// Distributes DUST tokens to eligible wallets. The function checks if the total amount distributed does not exceed the total available.
    pub fn distribute(ctx: Context<Distribute>, recipients: Vec<Pubkey>, amounts: Vec<u64>) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;

        // Ensure the number of recipients matches the number of amounts
        if recipients.len() != amounts.len() {
            return Err(ErrorCode::RecipientAmountMismatch.into());
        }

        let mut total_distributed: u64 = 0;

        for (recipient, amount) in recipients.iter().zip(amounts.iter()) {
            // Check if the total distributed amount exceeds the available amount
            if total_distributed + *amount > airdrop_account.total_amount {
                return Err(ErrorCode::ExceededTotalAmount.into());
            }

            // Transfer tokens to the recipient
            let cpi_accounts = spl_token::instruction::Transfer {
                from: ctx.accounts.token_account.to_account_info(),
                to: ctx.accounts.recipients_accounts[recipient].to_account_info(),
                authority: ctx.accounts.owner.to_account_info(),
            };
            let cpi_program = ctx.accounts.token_program.to_account_info();
            let amount_u64 = *amount;

            // Transfer tokens
            spl_token::instruction::transfer(cpi_program.clone(), cpi_accounts, amount_u64)?;

            total_distributed += amount_u64;
        }

        airdrop_account.distributed_amount += total_distributed;

        Ok(())
    }
}

/// The state of the airdrop account
#[account]
pub struct AirdropAccount {
    pub mint_address: Pubkey,
    pub total_amount: u64,
    pub distributed_amount: u64,
}

/// Context for the initialize function
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 40)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

/// Context for the distribute function
#[derive(Accounts)]
pub struct Distribute<'info> {
    #[account(mut)]
    pub token_account: Account<'info, Mint>,
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub token_program: Program<'info, spl_token::token::Token>,
    #[account(mut)]
    pub recipients_accounts: Vec<Account<'info, Mint>>,
}

/// Custom error codes for the smart contract
#[error]
pub enum ErrorCode {
    #[msg("The number of recipients does not match the number of amounts.")]
    RecipientAmountMismatch,
    #[msg("Total distributed amount exceeds the total amount allocated for the airdrop.")]
    ExceededTotalAmount,
}
```
