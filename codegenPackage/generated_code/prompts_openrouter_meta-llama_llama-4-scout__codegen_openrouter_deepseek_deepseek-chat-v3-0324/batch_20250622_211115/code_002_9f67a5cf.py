"""
Generated Code Metadata:
========================
Original URL: https://sol-box.web.app
Prompt: Generate a code snippet for a simple NFT marketplace on Solana, incorporating Magic Eden's Launchpad functionality for enforced royalties.
Generated: DETERMINISTIC_9f67a5cf0cebf52e
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    system_instruction,
    sysvar::{clock::Clock, rent::Rent, Sysvar},
};
use spl_token::state::Account as TokenAccount;
use spl_associated_token_account::get_associated_token_address;

// Program entrypoint
entrypoint!(process_instruction);

/// Main program entrypoint
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    
    // Parse accounts
    let payer = next_account_info(account_info_iter)?;
    let nft_mint = next_account_info(account_info_iter)?;
    let nft_token_account = next_account_info(account_info_iter)?;
    let metadata_account = next_account_info(account_info_iter)?;
    let edition_account = next_account_info(account_info_iter)?;
    let magic_eden_program = next_account_info(account_info_iter)?;
    let magic_eden_metadata = next_account_info(account_info_iter)?;
    let magic_eden_edition = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let rent = next_account_info(account_info_iter)?;
    let clock = next_account_info(account_info_iter)?;

    // Verify accounts
    if !payer.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    if *magic_eden_program.key != Pubkey::new_from_array([/* Magic Eden program ID */]) {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Create NFT listing with enforced royalties via Magic Eden Launchpad
    create_nft_listing(
        program_id,
        payer,
        nft_mint,
        nft_token_account,
        metadata_account,
        edition_account,
        magic_eden_program,
        magic_eden_metadata,
        magic_eden_edition,
        system_program,
        token_program,
        rent,
        clock,
        instruction_data,
    )?;

    Ok(())
}

/// Creates an NFT listing with enforced royalties
fn create_nft_listing(
    program_id: &Pubkey,
    payer: &AccountInfo,
    nft_mint: &AccountInfo,
    nft_token_account: &AccountInfo,
    metadata_account: &AccountInfo,
    edition_account: &AccountInfo,
    magic_eden_program: &AccountInfo,
    magic_eden_metadata: &AccountInfo,
    magic_eden_edition: &AccountInfo,
    system_program: &AccountInfo,
    token_program: &AccountInfo,
    rent: &AccountInfo,
    clock: &AccountInfo,
    instruction_data: &[u8],
) -> ProgramResult {
    // Verify NFT ownership
    let token_account_data = TokenAccount::unpack(&nft_token_account.data.borrow())?;
    if token_account_data.owner != *payer.key {
        return Err(ProgramError::IllegalOwner);
    }

    if token_account_data.mint != *nft_mint.key {
        return Err(ProgramError::InvalidAccountData);
    }

    if token_account_data.amount != 1 {
        return Err(ProgramError::InvalidAccountData);
    }

    // Verify metadata and edition accounts
    // (In a real implementation, you would verify metadata and edition details)

    // Create listing instruction for Magic Eden Launchpad
    let listing_instruction = spl_instruction_builder::build_instruction(
        magic_eden_program.key,
        &[
            payer.clone(),
            nft_mint.clone(),
            nft_token_account.clone(),
            metadata_account.clone(),
            edition_account.clone(),
            magic_eden_metadata.clone(),
            magic_eden_edition.clone(),
            system_program.clone(),
            token_program.clone(),
            rent.clone(),
            clock.clone(),
        ],
        instruction_data,
    )?;

    // Invoke Magic Eden program to create listing with enforced royalties
    solana_program::program::invoke(
        &listing_instruction,
        &[
            payer.clone(),
            nft_mint.clone(),
            nft_token_account.clone(),
            metadata_account.clone(),
            edition_account.clone(),
            magic_eden_metadata.clone(),
            magic_eden_edition.clone(),
            system_program.clone(),
            token_program.clone(),
            rent.clone(),
            clock.clone(),
        ],
    )?;

    msg!("NFT listed successfully with enforced royalties");
    Ok(())
}
```
