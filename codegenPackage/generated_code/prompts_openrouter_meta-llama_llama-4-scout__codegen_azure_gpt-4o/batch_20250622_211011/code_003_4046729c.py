"""
Generated Code Metadata:
========================
Original URL: https://nft-solad.web.app
Prompt: Design a simple smart contract in Rust for the Solana blockchain that enforces dynamic royalties for NFT creators, inspired by the features of Magic Eden's Open Creator Protocol.
Generated: DETERMINISTIC_4046729c55f92ae1
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary crates and modules
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// Define the entry point for the smart contract
entrypoint!(process_instruction);

// Define the structure for royalty configuration
#[derive(Debug, Clone)]
pub struct RoyaltyConfig {
    pub creator: Pubkey, // Public key of the creator
    pub royalty_percentage: u8, // Royalty percentage (0-100)
}

// Main function to process instructions
fn process_instruction(
    program_id: &Pubkey, // Program ID of the smart contract
    accounts: &[AccountInfo], // Accounts involved in the transaction
    instruction_data: &[u8], // Instruction data passed to the contract
) -> ProgramResult {
    msg!("Smart contract invoked");

    // Parse accounts
    let accounts_iter = &mut accounts.iter();
    let payer_account = next_account_info(accounts_iter)?; // Account paying for the transaction
    let creator_account = next_account_info(accounts_iter)?; // Account of the NFT creator

    // Ensure the payer account is a signer
    if !payer_account.is_signer {
        msg!("Payer account must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Parse instruction data to extract royalty configuration
    if instruction_data.len() != 9 {
        msg!("Invalid instruction data length");
        return Err(ProgramError::InvalidInstructionData);
    }

    let creator_pubkey = Pubkey::new(&instruction_data[0..32]);
    let royalty_percentage = instruction_data[32];

    // Validate royalty percentage
    if royalty_percentage > 100 {
        msg!("Royalty percentage cannot exceed 100");
        return Err(ProgramError::InvalidArgument);
    }

    // Ensure the creator account matches the provided public key
    if creator_account.key != &creator_pubkey {
        msg!("Creator account does not match provided public key");
        return Err(ProgramError::InvalidAccountData);
    }

    // Log royalty configuration
    msg!(
        "Royalty configuration: Creator={}, Percentage={}",
        creator_pubkey,
        royalty_percentage
    );

    // Business logic for enforcing royalties (e.g., transferring funds)
    // This is a placeholder for actual implementation
    msg!("Enforcing royalties...");

    // Return success
    Ok(())
}

// Unit tests for the smart contract
#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::account_info::AccountInfo;
    use solana_program::pubkey::Pubkey;

    #[test]
    fn test_valid_instruction() {
        let program_id = Pubkey::new_unique();
        let creator_pubkey = Pubkey::new_unique();
        let payer_pubkey = Pubkey::new_unique();

        let mut payer_account = AccountInfo::new(
            &payer_pubkey,
            true, // is_signer
            true, // is_writable
            &mut 0,
            &mut [],
            &program_id,
            false,
            0,
        );

        let mut creator_account = AccountInfo::new(
            &creator_pubkey,
            false, // is_signer
            false, // is_writable
            &mut 0,
            &mut [],
            &program_id,
            false,
            0,
        );

        let accounts = vec![payer_account, creator_account];
        let instruction_data = [creator_pubkey.to_bytes(), 10].concat(); // 10% royalty

        let result = process_instruction(&program_id, &accounts, &instruction_data);
        assert!(result.is_ok());
    }

    #[test]
    fn test_invalid_royalty_percentage() {
        let program_id = Pubkey::new_unique();
        let creator_pubkey = Pubkey::new_unique();
        let payer_pubkey = Pubkey::new_unique();

        let mut payer_account = AccountInfo::new(
            &payer_pubkey,
            true, // is_signer
            true, // is_writable
            &mut 0,
            &mut [],
            &program_id,
            false,
            0,
        );

        let mut creator_account = AccountInfo::new(
            &creator_pubkey,
            false, // is_signer
            false, // is_writable
            &mut 0,
            &mut [],
            &program_id,
            false,
            0,
        );

        let accounts = vec![payer_account, creator_account];
        let instruction_data = [creator_pubkey.to_bytes(), 110].concat(); // Invalid 110% royalty

        let result = process_instruction(&program_id, &accounts, &instruction_data);
        assert!(result.is_err());
    }
}
```
