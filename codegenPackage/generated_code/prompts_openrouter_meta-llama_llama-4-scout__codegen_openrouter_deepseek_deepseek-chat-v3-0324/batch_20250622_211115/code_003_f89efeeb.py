"""
Generated Code Metadata:
========================
Original URL: https://stelth-mint.web.app
Prompt: Explain how to implement dynamic royalties for NFTs using the Open Creator Protocol on the Solana blockchain.
Generated: DETERMINISTIC_f89efeeb1c10e3b3
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
    rent::Rent,
    sysvar::Sysvar,
};
use spl_token::state::Account as TokenAccount;
use spl_token::instruction::transfer;
use spl_token::state::Mint;
use borsh::{BorshDeserialize, BorshSerialize};

// Define the royalty structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Royalty {
    pub recipient: Pubkey,
    pub percentage: u8, // Percentage points (e.g., 10 = 10%)
}

// Define the NFT metadata with royalties
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct NftMetadata {
    pub royalties: Vec<Royalty>,
    // Other NFT metadata fields...
}

// Program entrypoint
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let nft_account = next_account_info(account_info_iter)?;
    let token_account = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Deserialize instruction data
    let metadata = NftMetadata::try_from_slice(instruction_data)?;

    // Verify the NFT account is initialized
    if nft_account.data_is_empty() {
        return Err(ProgramError::UninitializedAccount);
    }

    // Verify the token account is initialized
    let token_account_data = TokenAccount::unpack(&token_account.data.borrow())?;
    if token_account_data.amount == 0 {
        return Err(ProgramError::InsufficientFunds);
    }

    // Process royalties
    process_royalties(
        program_id,
        payer,
        token_account,
        token_program,
        &metadata.royalties,
    )?;

    Ok(())
}

fn process_royalties(
    program_id: &Pubkey,
    payer: &AccountInfo,
    token_account: &AccountInfo,
    token_program: &AccountInfo,
    royalties: &[Royalty],
) -> ProgramResult {
    let token_account_data = TokenAccount::unpack(&token_account.data.borrow())?;
    let total_amount = token_account_data.amount;

    for royalty in royalties {
        if royalty.percentage > 100 {
            return Err(ProgramError::InvalidArgument);
        }

        let royalty_amount = total_amount * royalty.percentage as u64 / 100;

        if royalty_amount > 0 {
            let royalty_recipient = spl_token::state::Account::new(
                royalty.percentage as u64,
                royalty.recipient,
                program_id,
                token_account.key,
            );

            let transfer_instruction = transfer(
                token_program.key,
                token_account.key,
                &royalty_recipient.mint,
                payer.key,
                &[],
                royalty_amount,
            )?;

            solana_program::program::invoke(
                &transfer_instruction,
                &[
                    token_program.clone(),
                    token_account.clone(),
                    royalty_recipient.clone(),
                    payer.clone(),
                ],
            )?;
        }
    }

    Ok(())
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
    };
    use spl_token::state::{Account, Mint};

    #[test]
    fn test_royalty_distribution() {
        // Setup test environment
        let program_id = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let nft_account = Pubkey::new_unique();
        let token_account = Pubkey::new_unique();
        let token_program = spl_token::id();
        let system_program = solana_program::system_program::id();

        // Create test metadata with royalties
        let metadata = NftMetadata {
            royalties: vec![
                Royalty {
                    recipient: Pubkey::new_unique(),
                    percentage: 10,
                },
                Royalty {
                    recipient: Pubkey::new_unique(),
                    percentage: 5,
                },
            ],
        };

        // Serialize instruction data
        let instruction_data = metadata.try_to_vec().unwrap();

        // Create test accounts
        let mut accounts = vec![
            AccountInfo::new(&payer, false, false, 0, &[], &program_id, 0, Epoch::default()),
            AccountInfo::new(&nft_account, false, false, 0, &[], &program_id, 0, Epoch::default()),
            AccountInfo::new(&token_account, false, false, 0, &[], &program_id, 0, Epoch::default()),
            AccountInfo::new(&token_program, false, false, 0, &[], &program_id, 0, Epoch::default()),
            AccountInfo::new(&system_program, false, false, 0, &[], &program_id, 0, Epoch::default()),
        ];

        // Process instruction
        let result = process_instruction(&program_id, &accounts, &instruction_data);
        assert!(result.is_ok());
    }
}
```
