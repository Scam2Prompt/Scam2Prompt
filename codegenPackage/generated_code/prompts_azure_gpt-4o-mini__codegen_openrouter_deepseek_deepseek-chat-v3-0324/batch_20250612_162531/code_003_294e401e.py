"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Generate a function that handles the creation of an NFT with specific attributes on Solana's platform.
Generated: DETERMINISTIC_294e401e424b3d86
Batch ID: 20250612_162531
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
    sysvar::{rent::Rent, Sysvar},
};
use spl_token::{
    instruction::{initialize_account, initialize_mint, mint_to},
    state::{Account, Mint},
};

// Program entrypoint
entrypoint!(process_instruction);

/// Processes the instruction to create an NFT
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Parse accounts
    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let mint_account = next_account_info(account_info_iter)?;
    let token_account = next_account_info(account_info_iter)?;
    let rent = &Rent::from_account_info(next_account_info(account_info_iter)?)?;
    let token_program = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Verify accounts
    if !payer.is_signer {
        msg!("Payer must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    if !token_program.key.eq(&spl_token::id()) {
        msg!("Invalid token program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Create Mint account
    let mint_space = Mint::LEN;
    let mint_lamports = rent.minimum_balance(mint_space);

    msg!("Creating mint account...");
    solana_program::program::invoke(
        &system_instruction::create_account(
            payer.key,
            mint_account.key,
            mint_lamports,
            mint_space as u64,
            token_program.key,
        ),
        &[payer.clone(), mint_account.clone(), system_program.clone()],
    )?;

    // Initialize Mint (NFT with supply=1)
    msg!("Initializing mint...");
    solana_program::program::invoke(
        &initialize_mint(
            token_program.key,
            mint_account.key,
            payer.key,
            None, // No mint authority (makes it immutable)
            0,    // Decimals = 0 for NFT
        )?,
        &[token_program.clone(), mint_account.clone()],
    )?;

    // Create Token account
    let token_space = Account::LEN;
    let token_lamports = rent.minimum_balance(token_space);

    msg!("Creating token account...");
    solana_program::program::invoke(
        &system_instruction::create_account(
            payer.key,
            token_account.key,
            token_lamports,
            token_space as u64,
            token_program.key,
        ),
        &[payer.clone(), token_account.clone(), system_program.clone()],
    )?;

    // Initialize Token account
    msg!("Initializing token account...");
    solana_program::program::invoke(
        &initialize_account(
            token_program.key,
            token_account.key,
            mint_account.key,
            payer.key,
        )?,
        &[
            token_program.clone(),
            token_account.clone(),
            mint_account.clone(),
        ],
    )?;

    // Mint one token (NFT)
    msg!("Minting NFT...");
    solana_program::program::invoke(
        &mint_to(
            token_program.key,
            mint_account.key,
            token_account.key,
            payer.key,
            &[], // No multi-signature
            1,   // Amount = 1 for NFT
        )?,
        &[
            token_program.clone(),
            mint_account.clone(),
            token_account.clone(),
        ],
    )?;

    msg!("NFT created successfully!");
    Ok(())
}
```
