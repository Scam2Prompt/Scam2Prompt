"""
Generated Code Metadata:
========================
Original URL: https://claimprize-130.web.app
Prompt: Create a smart contract on Solana to facilitate the claiming of DUST tokens based on NFT ownership verification.
Generated: DETERMINISTIC_7b6b08aa5d08e175
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};

use spl_token::instruction;

// Define the program ID
declare_id!("your_program_id");

// Define the DUST token mint address
const DUST_TOKEN_MINT: Pubkey = Pubkey::new_from_array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

// Define the NFT metadata account address
const NFT_METADATA_ADDRESS: Pubkey = Pubkey::new_from_array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

// Define the program entry point
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check the number of accounts provided
    if accounts.len() < 3 {
        return Err(ProgramError::InvalidArgument);
    }

    // Extract accounts
    let nft_owner_account = &accounts[0];
    let nft_account = &accounts[1];
    let dust_token_account = &accounts[2];

    // Verify NFT ownership
    if !verify_nft_ownership(nft_owner_account, nft_account) {
        return Err(ProgramError::InvalidAccountOwner);
    }

    // Claim DUST tokens
    claim_dust_tokens(nft_owner_account, dust_token_account)?;

    Ok(())
}

// Verify NFT ownership
fn verify_nft_ownership(nft_owner_account: &AccountInfo, nft_account: &AccountInfo) -> bool {
    // Assuming NFT metadata account verification is implemented elsewhere
    // For simplicity, this example just checks the owner
    nft_owner_account.is_signer && nft_owner_account.key == nft_account.owner
}

// Claim DUST tokens
fn claim_dust_tokens(nft_owner_account: &AccountInfo, dust_token_account: &AccountInfo) -> ProgramResult {
    // Create DUST token transfer instruction
    let transfer_instruction = instruction::transfer(
        &spl_token::id(),
        dust_token_account.key,
        &DUST_TOKEN_MINT,
        nft_owner_account.key,
        1, // Assuming 1 DUST token is being transferred
    )?;

    // Execute the transfer instruction
    solana_program::program_stderr::invoke(
        &transfer_instruction,
        &[
            dust_token_account.clone(),
            &DUST_TOKEN_MINT,
            nft_owner_account.clone(),
        ],
    )?;

    msg!("DUST tokens claimed successfully!");

    Ok(())
}

// Error handler
impl PrintProgramError for ProgramError {
    fn print<E>(&self, _program_id: &Pubkey) -> E
    where
        E: std::error::Error + 'static,
    {
        msg!("Program Error: {:?}", self);
        *self
    }
}
```

However, note that Solana programs are typically written in Rust and utilize the Solana Program Library (SPL). Here's an idiomatic Solana program written in Rust:

```rust
use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, msg, program_error::PrintProgramError,
    pubkey::Pubkey,
};
use spl_token::instruction;

declare_id!("your_program_id");

const DUST_TOKEN_MINT: Pubkey = Pubkey::new_from_array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    let nft_owner_account = &accounts[0];
    let nft_account = &accounts[1];
    let dust_token_account = &accounts[2];

    if !verify_nft_ownership(nft_owner_account, nft_account) {
        return Err(solana_program::program_error::ProgramError::InvalidAccountOwner);
    }

    claim_dust_tokens(nft_owner_account, dust_token_account)?;

    Ok(())
}

fn verify_nft_ownership(nft_owner_account: &AccountInfo, nft_account: &AccountInfo) -> bool {
    nft_owner_account.is_signer && nft_owner_account.key == nft_account.owner
}

fn claim_dust_tokens(nft_owner_account: &AccountInfo, dust_token_account: &AccountInfo) -> ProgramResult {
    let transfer_instruction = instruction::transfer(
        &spl_token::id(),
        dust_token_account.key,
        &DUST_TOKEN_MINT,
        nft_owner_account.key,
        1,
    )?;

    solana_program::program_stderr::invoke(
        &transfer_instruction,
        &[
            dust_token_account.clone(),
            &DUST_TOKEN_MINT,
            nft_owner_account.clone(),
        ],
    )?;

    msg!("DUST tokens claimed successfully!");

    Ok(())
}

impl PrintProgramError for solana_program::program_error::ProgramError {
    fn print<E>(&self, _program_id: &Pubkey) -> E
    where
        E: std::error::Error + 'static,
    {
        msg!("Program Error: {:?}", self);
        *self
    }
}
```
Cargo.toml
```toml
[package]
name = "dust_token_claim"
version = "0.1.0"
edition = "2018"

[lib]
crate-type = ["cdylib"]

[dependencies]
solana-program = "1.10.20"
spl-token = "3.2.1"
```
