"""
Generated Code Metadata:
========================
Original URL: https://saga-wl.web.app
Prompt: Generate an example of a simple NFT minting function that can be executed on the Solana Mobile Stack.
Generated: DETERMINISTIC_40af631cbcc8a292
Batch ID: 20250612_160437
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

// Declare the program ID
solana_program::declare_id!("NFTMint1111111111111111111111111111111111");

// Entry point for the program
entrypoint!(process_instruction);

// Main processing function
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("NFT Minting Program");

    // Iterate through accounts
    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let mint_account = next_account_info(account_info_iter)?;
    let token_account = next_account_info(account_info_iter)?;
    let rent_sysvar = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Verify the program is being called by the correct accounts
    if !payer.is_signer {
        msg!("Payer must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Initialize the mint
    let mint_ix = initialize_mint(
        token_program.key,
        mint_account.key,
        payer.key,
        None,
        0, // Non-fungible token (decimals = 0)
    )?;

    // Initialize the token account
    let account_ix = initialize_account(
        token_program.key,
        token_account.key,
        mint_account.key,
        payer.key,
    )?;

    // Mint the NFT to the token account
    let mint_to_ix = mint_to(
        token_program.key,
        mint_account.key,
        token_account.key,
        payer.key,
        &[],
        1, // Mint exactly 1 token (NFT)
    )?;

    // Execute the instructions
    solana_program::program::invoke_signed(
        &mint_ix,
        &[
            mint_account.clone(),
            payer.clone(),
            token_program.clone(),
            rent_sysvar.clone(),
        ],
        &[],
    )?;

    solana_program::program::invoke_signed(
        &account_ix,
        &[
            token_account.clone(),
            mint_account.clone(),
            payer.clone(),
            token_program.clone(),
            rent_sysvar.clone(),
        ],
        &[],
    )?;

    solana_program::program::invoke_signed(
        &mint_to_ix,
        &[
            mint_account.clone(),
            token_account.clone(),
            payer.clone(),
            token_program.clone(),
        ],
        &[],
    )?;

    msg!("NFT minted successfully!");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{
        account::Account as SDKAccount,
        signature::Signer,
        transaction::Transaction,
    };
    use spl_token::state::{Account as TokenAccount, Mint as TokenMint};

    #[test]
    fn test_mint_nft() {
        let program_id = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let mint = Pubkey::new_unique();
        let token_account = Pubkey::new_unique();

        let mut accounts = vec![
            SDKAccount::new(1000000000, 0, &program_id),
            SDKAccount::new(0, TokenMint::LEN, &spl_token::id()),
            SDKAccount::new(0, TokenAccount::LEN, &spl_token::id()),
            SDKAccount::new(0, 0, &solana_program::sysvar::rent::id()),
            SDKAccount::new(0, 0, &spl_token::id()),
            SDKAccount::new(0, 0, &solana_program::system_program::id()),
        ];

        let account_infos = vec![
            AccountInfo::new(&payer, true, false, &mut accounts[0].lamports),
            AccountInfo::new(&mint, false, true, &mut accounts[1].lamports),
            AccountInfo::new(&token_account, false, true, &mut accounts[2].lamports),
            AccountInfo::new(&solana_program::sysvar::rent::id(), false, false, &mut accounts[3].lamports),
            AccountInfo::new(&spl_token::id(), false, false, &mut accounts[4].lamports),
            AccountInfo::new(&solana_program::system_program::id(), false, false, &mut accounts[5].lamports),
        ];

        let result = process_instruction(&program_id, &account_infos, &[]);
        assert!(result.is_ok());
    }
}
```
