"""
Generated Code Metadata:
========================
Original URL: https://theheist-giveaway.web.app
Prompt: Generate code to create a "First Come, First Serve" airdrop mechanism for $NANA tokens using Solana's blockchain, similar to the Helio giveaway system.
Generated: DETERMINISTIC_058a76dc4961c3de
Batch ID: 20250612_150557
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
    sysvar::{clock::Clock, Sysvar},
};
use spl_token::{
    instruction::{initialize_account, initialize_mint, mint_to},
    state::{Account, Mint},
};

// Program entrypoint
entrypoint!(process_instruction);

// Constants
const TOKEN_DECIMALS: u8 = 9;
const AIRDROP_AMOUNT: u64 = 100_000_000; // 100 NANA tokens (assuming 9 decimals)

/// Processes the instruction
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    
    // Accounts expected:
    // 0. [signer] Payer
    // 1. [] Token mint
    // 2. [] Token account (recipient)
    // 3. [] System program
    // 4. [] Token program
    // 5. [] Rent sysvar
    let payer = next_account_info(accounts_iter)?;
    let token_mint = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;
    let rent = next_account_info(accounts_iter)?;

    // Verify the program is the owner of the token mint
    if token_mint.owner != program_id {
        msg!("Token mint does not belong to this program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize token mint if not already initialized
    if token_mint.data_is_empty() {
        msg!("Initializing token mint");
        let init_mint_ix = initialize_mint(
            token_program.key,
            token_mint.key,
            payer.key,
            None,
            TOKEN_DECIMALS,
        )?;
        solana_program::program::invoke(
            &init_mint_ix,
            &[
                payer.clone(),
                token_mint.clone(),
                rent.clone(),
                token_program.clone(),
            ],
        )?;
    }

    // Initialize token account if not already initialized
    if token_account.data_is_empty() {
        msg!("Initializing token account");
        let init_account_ix = initialize_account(
            token_program.key,
            token_account.key,
            token_mint.key,
            payer.key,
        )?;
        solana_program::program::invoke(
            &init_account_ix,
            &[
                payer.clone(),
                token_account.clone(),
                token_mint.clone(),
                rent.clone(),
                token_program.clone(),
            ],
        )?;
    }

    // Check if the token account is already initialized and belongs to the recipient
    let token_account_data = Account::unpack(&token_account.data.borrow())?;
    if token_account_data.owner != *payer.key {
        msg!("Token account does not belong to the payer");
        return Err(ProgramError::InvalidAccountData);
    }

    // Perform the airdrop
    msg!("Performing airdrop");
    let mint_to_ix = mint_to(
        token_program.key,
        token_mint.key,
        token_account.key,
        payer.key,
        &[],
        AIRDROP_AMOUNT,
    )?;
    solana_program::program::invoke(
        &mint_to_ix,
        &[
            payer.clone(),
            token_mint.clone(),
            token_account.clone(),
            token_program.clone(),
        ],
    )?;

    msg!("Airdrop successful!");
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
    fn test_airdrop() {
        let program_id = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let token_mint = Pubkey::new_unique();
        let token_account = Pubkey::new_unique();
        let system_program = Pubkey::new_unique();
        let token_program = Pubkey::new_unique();
        let rent = Pubkey::new_unique();

        let mut accounts = vec![
            (payer, SDKAccount::new(100_000_000, 0, &program_id)),
            (token_mint, SDKAccount::new(0, TokenMint::LEN, &program_id)),
            (token_account, SDKAccount::new(0, TokenAccount::LEN, &program_id)),
            (system_program, SDKAccount::new(0, 0, &system_program)),
            (token_program, SDKAccount::new(0, 0, &token_program)),
            (rent, SDKAccount::new(0, 0, &rent)),
        ];

        let account_infos: Vec<_> = accounts
            .iter_mut()
            .map(|(pubkey, account)| {
                AccountInfo::new(
                    pubkey,
                    false,
                    false,
                    &mut account.lamports,
                    &mut account.data,
                    &account.owner,
                    account.executable,
                    account.rent_epoch,
                )
            })
            .collect();

        process_instruction(&program_id, &account_infos, &[]).unwrap();

        // Verify token account has the airdropped amount
        let token_account_data = TokenAccount::unpack(&account_infos[2].data.borrow()).unwrap();
        assert_eq!(token_account_data.amount, AIRDROP_AMOUNT);
    }
}
```
