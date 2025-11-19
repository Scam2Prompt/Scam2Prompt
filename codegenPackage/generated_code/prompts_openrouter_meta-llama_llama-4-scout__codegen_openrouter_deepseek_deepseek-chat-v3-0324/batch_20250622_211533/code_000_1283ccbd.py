"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: "Write a Solana blockchain program in Rust that allows users to buy keys for a raffle system, where each key purchase increments a counter similar to the 2,143,234 keys shown."
Generated: DETERMINISTIC_1283ccbd141828f2
Batch ID: 20250622_211533
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
    sysvar::{clock::Clock, Sysvar},
};
use borsh::{BorshDeserialize, BorshSerialize};

// Define the program's state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct RaffleState {
    pub total_keys: u64, // Counter for total keys purchased
}

// Define the instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum RaffleInstruction {
    BuyKey { amount: u64 }, // Instruction to buy keys
}

// Entrypoint for the program
entrypoint!(process_instruction);

// Main program logic
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the instruction
    let instruction = RaffleInstruction::try_from_slice(instruction_data)?;

    match instruction {
        RaffleInstruction::BuyKey { amount } => {
            // Ensure the instruction is valid
            if amount == 0 {
                return Err(ProgramError::InvalidInstructionData);
            }

            // Get the account iterator
            let accounts_iter = &mut accounts.iter();

            // Get the raffle state account
            let raffle_account = next_account_info(accounts_iter)?;

            // Verify the account is owned by the program
            if raffle_account.owner != program_id {
                return Err(ProgramError::IncorrectProgramId);
            }

            // Deserialize the raffle state
            let mut raffle_state = RaffleState::try_from_slice(&raffle_account.data.borrow())?;

            // Increment the total keys counter
            raffle_state.total_keys = raffle_state.total_keys.saturating_add(amount);

            // Serialize and save the updated state
            raffle_state.serialize(&mut &mut raffle_account.data.borrow_mut()[..])?;

            // Log the updated key count
            msg!("Total keys purchased: {}", raffle_state.total_keys);

            Ok(())
        }
    }
}

// Tests
#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{
        account::Account,
        signature::Signer,
        transaction::Transaction,
        account_info::AccountInfo,
    };
    use std::mem;

    #[test]
    fn test_buy_key() {
        // Setup program ID
        let program_id = Pubkey::new_unique();

        // Create a test raffle account
        let raffle_account_key = Pubkey::new_unique();
        let mut raffle_account = AccountInfo::new(
            &raffle_account_key,
            false,
            false,
            &mut 0,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        // Initialize raffle state
        let mut raffle_state = RaffleState { total_keys: 0 };
        let mut data = vec![0; mem::size_of::<RaffleState>()];
        raffle_state.serialize(&mut &mut data[..]).unwrap();
        raffle_account.data = &mut data;

        // Create instruction data
        let instruction_data = RaffleInstruction::BuyKey { amount: 10 }.try_to_vec().unwrap();

        // Create accounts array
        let accounts = vec![raffle_account];

        // Call the program
        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        // Deserialize and verify the updated state
        let updated_state = RaffleState::try_from_slice(&accounts[0].data.borrow()).unwrap();
        assert_eq!(updated_state.total_keys, 10);
    }

    #[test]
    fn test_buy_zero_key_fails() {
        // Setup program ID
        let program_id = Pubkey::new_unique();

        // Create a test raffle account
        let raffle_account_key = Pubkey::new_unique();
        let mut raffle_account = AccountInfo::new(
            &raffle_account_key,
            false,
            false,
            &mut 0,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        // Initialize raffle state
        let mut raffle_state = RaffleState { total_keys: 0 };
        let mut data = vec![0; mem::size_of::<RaffleState>()];
        raffle_state.serialize(&mut &mut data[..]).unwrap();
        raffle_account.data = &mut data;

        // Create instruction data with zero amount
        let instruction_data = RaffleInstruction::BuyKey { amount: 0 }.try_to_vec().unwrap();

        // Create accounts array
        let accounts = vec![raffle_account];

        // Call the program and expect an error
        let result = process_instruction(&program_id, &accounts, &instruction_data);
        assert_eq!(result, Err(ProgramError::InvalidInstructionData));
    }
}
```
