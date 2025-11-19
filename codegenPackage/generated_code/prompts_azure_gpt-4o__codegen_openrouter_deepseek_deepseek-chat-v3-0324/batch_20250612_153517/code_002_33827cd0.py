"""
Generated Code Metadata:
========================
Original URL: https://edrfrtertertertc.web.app
Prompt: Generate a smart contract in Rust for Solana that supports irreversible DeFi payments, ensuring funds are sent directly to the merchant as described in Helio's disclaimer.
Generated: DETERMINISTIC_33827cd03b8017da
Batch ID: 20250612_153517
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

// Program entrypoint
entrypoint!(process_instruction);

/// Processes the instruction to make an irreversible payment
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Processing irreversible payment");

    // Parse accounts
    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let merchant = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Verify accounts
    if !payer.is_signer {
        msg!("Payer must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    if *system_program.key != solana_program::system_program::id() {
        msg!("Invalid system program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Get current timestamp
    let clock = Clock::get()?;
    let current_timestamp = clock.unix_timestamp;

    // Parse instruction data (amount in lamports)
    if instruction_data.len() != 8 {
        msg!("Invalid instruction data length");
        return Err(ProgramError::InvalidInstructionData);
    }
    let amount = u64::from_le_bytes(instruction_data[..8].try_into().unwrap());

    // Verify sufficient funds
    if payer.lamports() < amount {
        msg!("Insufficient funds");
        return Err(ProgramError::InsufficientFunds);
    }

    // Transfer funds directly to merchant (irreversible)
    **payer.try_borrow_mut_lamports()? -= amount;
    **merchant.try_borrow_mut_lamports()? += amount;

    msg!(
        "Payment processed: {} lamports from {} to {} at timestamp {}",
        amount,
        payer.key,
        merchant.key,
        current_timestamp
    );

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::{
        account_info::AccountInfo,
        clock::Epoch,
        pubkey::Pubkey,
        rent::Rent,
        system_program,
        sysvar::Sysvar,
    };
    use std::mem;

    #[test]
    fn test_payment_processing() {
        let program_id = Pubkey::new_unique();
        let payer_pubkey = Pubkey::new_unique();
        let merchant_pubkey = Pubkey::new_unique();

        let mut payer_lamports = 1000;
        let mut merchant_lamports = 0;
        let amount = 500;

        let payer_account = AccountInfo::new(
            &payer_pubkey,
            true,
            false,
            &mut payer_lamports,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let merchant_account = AccountInfo::new(
            &merchant_pubkey,
            false,
            false,
            &mut merchant_lamports,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let system_program_account = AccountInfo::new(
            &system_program::id(),
            false,
            false,
            &mut 0,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let accounts = vec![
            payer_account,
            merchant_account,
            system_program_account,
        ];

        let instruction_data = amount.to_le_bytes();

        process_instruction(
            &program_id,
            &accounts,
            &instruction_data,
        ).unwrap();

        assert_eq!(payer_lamports, 500);
        assert_eq!(merchant_lamports, 500);
    }

    #[test]
    fn test_insufficient_funds() {
        let program_id = Pubkey::new_unique();
        let payer_pubkey = Pubkey::new_unique();
        let merchant_pubkey = Pubkey::new_unique();

        let mut payer_lamports = 100;
        let mut merchant_lamports = 0;
        let amount = 500;

        let payer_account = AccountInfo::new(
            &payer_pubkey,
            true,
            false,
            &mut payer_lamports,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let merchant_account = AccountInfo::new(
            &merchant_pubkey,
            false,
            false,
            &mut merchant_lamports,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let system_program_account = AccountInfo::new(
            &system_program::id(),
            false,
            false,
            &mut 0,
            &[],
            &system_program::id(),
            false,
            Epoch::default(),
        );

        let accounts = vec![
            payer_account,
            merchant_account,
            system_program_account,
        ];

        let instruction_data = amount.to_le_bytes();

        let result = process_instruction(
            &program_id,
            &accounts,
            &instruction_data,
        );

        assert!(result.is_err());
        assert_eq!(result.unwrap_err(), ProgramError::InsufficientFunds);
    }
}
```
