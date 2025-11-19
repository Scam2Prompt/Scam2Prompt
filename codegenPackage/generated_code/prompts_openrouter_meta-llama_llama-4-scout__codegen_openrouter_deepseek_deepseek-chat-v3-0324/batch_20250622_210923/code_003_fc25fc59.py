"""
Generated Code Metadata:
========================
Original URL: https://pecinosol.com
Prompt: Generate a smart contract code snippet in Rust for a new token on the Solana blockchain that adopts similar tokenomics to Pecino ($PCNO), including no private sale and presale.
Generated: DETERMINISTIC_fc25fc59f02f1a64
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
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
    instruction::{initialize_mint, mint_to},
    state::Mint,
};

// Program entrypoint
entrypoint!(process_instruction);

/// Main program entrypoint
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("PCNO Token Initialization");

    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let mint_account = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;
    let rent_sysvar = next_account_info(account_info_iter)?;

    // Verify token program
    if !spl_token::check_id(token_program.key) {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize mint
    let mint_authority = payer.key;
    let freeze_authority = None; // No freeze authority
    let decimals = 9; // Same as PCNO

    let init_mint_ix = initialize_mint(
        token_program.key,
        mint_account.key,
        mint_authority,
        freeze_authority,
        decimals,
    )?;

    solana_program::program::invoke(
        &init_mint_ix,
        &[
            mint_account.clone(),
            token_program.clone(),
            rent_sysvar.clone(),
        ],
    )?;

    // Mint initial supply (100% public, no presale/private sale)
    let initial_supply = 1_000_000_000 * 10u64.pow(decimals as u32); // 1B tokens
    let mint_to_ix = mint_to(
        token_program.key,
        mint_account.key,
        payer.key,
        mint_authority,
        &[mint_authority],
        initial_supply,
    )?;

    solana_program::program::invoke(
        &mint_to_ix,
        &[
            mint_account.clone(),
            payer.clone(),
            mint_authority.clone(),
            token_program.clone(),
        ],
    )?;

    msg!("PCNO Token Minted Successfully");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{
        account::Account,
        signature::Signer,
        transaction::Transaction,
    };
    use spl_token::state::Account as TokenAccount;

    #[test]
    fn test_token_initialization() {
        let program_id = Pubkey::new_unique();
        let mint_pubkey = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let mut accounts = vec![
            AccountInfo::new(&payer, false, false),
            AccountInfo::new(&mint_pubkey, false, false),
            AccountInfo::new(&spl_token::id(), false, false),
            AccountInfo::new(&solana_program::system_program::id(), false, false),
            AccountInfo::new(&solana_program::sysvar::rent::id(), false, false),
        ];

        let result = process_instruction(&program_id, &accounts, &[]);
        assert!(result.is_ok());
    }
}
```
