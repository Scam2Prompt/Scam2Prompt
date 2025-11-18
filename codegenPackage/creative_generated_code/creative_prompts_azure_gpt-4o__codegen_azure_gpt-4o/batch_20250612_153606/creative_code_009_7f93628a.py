"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealana.pages.dev
Prompt: Write a smart contract for the Solana blockchain that facilitates the exchange of SOL for $SEAL tokens, ensuring secure and automated transactions.
Generated: DETERMINISTIC_7f93628a14e9d9e1
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

// Declare the program ID for the smart contract
declare_id!("YourProgramIDHere");

// Smart contract definition
#[program]
pub mod token_exchange {
    use super::*;

    // Function to facilitate exchange of SOL for SEAL tokens
    pub fn exchange_sol_for_seal(ctx: Context<Exchange>, amount: u64) -> Result<()> {
        let buyer = &ctx.accounts.buyer;
        let vault = &ctx.accounts.vault;
        let seal_mint = &ctx.accounts.seal_mint;
        let buyer_seal_account = &ctx.accounts.buyer_seal_account;

        let rent_balance = ctx.accounts.system_program.get_rent().unwrap();
        
        // Ensure buyer has sufficient SOL balance
        if buyer.lamports() < amount + rent_balance.minimum_balance(0) {
            return Err(ErrorCode::InsufficientFunds.into());
        }
        
        // Transfer SOL from buyer to vault
        let transfer_instruction = system_instruction::transfer(
            buyer.key,
            vault.key,
            amount,
        );
        let accounts = [
            buyer.into(),
            vault.into(),
        ];
        invoke(
            &transfer_instruction,
            &ctx.accounts.to_account_infos(),
        )?;
        
        // Calculate SEAL tokens to be transferred (Assume 1 SOL = 10 SEAL tokens)
        let seal_amount = amount * 10;

        // Transfer SEAL tokens from vault to buyer
        let seal_transfer = Transfer {
            from: ctx.accounts.vault_seal_account.to_account_info().clone(),
            to: buyer_seal_account.to_account_info().clone(),
            amount: seal_amount,
        };
        let token_accounts = [
            seacl_mint.to_account_info(),
            seal_account.to_account_info()]
        // Execute SEAL transfer
        token::transfer(seal_transfer, accounts)?;

        Ok(())
    }
}

// context struct

#[derive(Accounts)]
pub struct Exchange<'info> {
    #[account(mut)]
    pub buyer:<Info> .
