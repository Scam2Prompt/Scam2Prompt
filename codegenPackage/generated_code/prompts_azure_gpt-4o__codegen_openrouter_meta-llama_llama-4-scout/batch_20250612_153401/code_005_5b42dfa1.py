"""
Generated Code Metadata:
========================
Original URL: https://dust-cube.web.app
Prompt: Develop a smart contract on Solana to verify NFT ownership and distribute DUST tokens accordingly.
Generated: DETERMINISTIC_5b42dfa1bfae7291
Batch ID: 20250612_153401
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

use spl_token::state::Mint;

// Define the program's entry point
entrypoint!(process_instruction);

// Define the program's instruction processor
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is not empty
    if instruction_data.is_empty() {
        return Err(ProgramError::InvalidInstructionData);
    }

    // Deserialize the instruction data into a VerifyOwnership struct
    let instruction = VerifyOwnership::unpack(instruction_data)?;

    // Process the instruction based on the instruction type
    match instruction {
        VerifyOwnership::VerifyOwnership { nft_pubkey, user_pubkey, dust_mint_pubkey } => {
            verify_ownership(
                program_id,
                accounts,
                nft_pubkey,
                user_pubkey,
                dust_mint_pubkey,
            )?;
        }
    }

    Ok(())
}

// Define the VerifyOwnership struct
#[derive(Debug, PartialEq)]
enum VerifyOwnership {
    VerifyOwnership {
        nft_pubkey: Pubkey,
        user_pubkey: Pubkey,
        dust_mint_pubkey: Pubkey,
    },
}

impl VerifyOwnership {
    // Unpack the instruction data into a VerifyOwnership struct
    fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let nft_pubkey = Pubkey::try_from_slice(&input[0..32])?.to_owned();
        let user_pubkey = Pubkey::try_from_slice(&input[32..64])?.to_owned();
        let dust_mint_pubkey = Pubkey::try_from_slice(&input[64..96])?.to_owned();

        Ok(VerifyOwnership::VerifyOwnership {
            nft_pubkey,
            user_pubkey,
            dust_mint_pubkey,
        })
    }
}

// Verify NFT ownership and distribute DUST tokens
fn verify_ownership(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    nft_pubkey: Pubkey,
    user_pubkey: Pubkey,
    dust_mint_pubkey: Pubkey,
) -> ProgramResult {
    // Get the accounts
    let nft_account = next_account_info(accounts)?;
    let user_account = next_account_info(accounts)?;
    let dust_mint_account = next_account_info(accounts)?;
    let dust_token_account = next_account_info(accounts)?;

    // Check if the NFT account is owned by the user
    if nft_account.owner != &user_pubkey {
        return Err(ProgramError::InvalidAccountOwner);
    }

    // Check if the DUST mint account is valid
    if dust_mint_account.owner != &spl_token::id() {
        return Err(ProgramError::InvalidAccountOwner);
    }

    // Get the DUST mint
    let dust_mint = Mint::unpack(dust_mint_account.data.borrow())?;

    // Check if the DUST token account is valid
    if dust_token_account.owner != &user_pubkey {
        return Err(ProgramError::InvalidAccountOwner);
    }

    // Distribute DUST tokens to the user
    let dust_amount = 1_000_000; // 1 DUST
    spl_token::instruction::transfer(
        &spl_token::id(),
        dust_mint_account.key,
        dust_token_account.key,
        user_account.key,
        &[],
        dust_amount,
    )?;

    msg!("DUST tokens distributed to the user");

    Ok(())
}

// Get the next account info
fn next_account_info(accounts: &mut &[AccountInfo]) -> Result<AccountInfo, ProgramError> {
    if accounts.is_empty() {
        return Err(ProgramError::NotEnoughAccountData);
    }

    let account = accounts[0].clone();
    *accounts = &accounts[1..];

    Ok(account)
}
```
