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

// Royalty data structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct RoyaltyData {
    pub creator: Pubkey,
    pub basis_points: u16, // Royalty percentage in basis points (1% = 100 basis points)
    pub updated_at: i64,   // Timestamp of last update
}

// Program state
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct CreatorProtocol {
    pub royalties: Vec<RoyaltyData>,
    pub version: u8,
}

// Instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum CreatorProtocolInstruction {
    Initialize,
    UpdateRoyalty {
        creator: Pubkey,
        new_basis_points: u16,
    },
    GetRoyalties,
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = CreatorProtocolInstruction::try_from_slice(instruction_data)
        .map_err(|_| ProgramError::InvalidInstructionData)?;

    match instruction {
        CreatorProtocolInstruction::Initialize => initialize(program_id, accounts),
        CreatorProtocolInstruction::UpdateRoyalty {
            creator,
            new_basis_points,
        } => update_royalty(program_id, accounts, creator, new_basis_points),
        CreatorProtocolInstruction::GetRoyalties => get_royalties(program_id, accounts),
    }
}

fn initialize(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let protocol_account = next_account_info(accounts_iter)?;

    if protocol_account.owner != program_id {
        msg!("Protocol account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let mut protocol_data = CreatorProtocol {
        royalties: Vec::new(),
        version: 1,
    };

    protocol_data.serialize(&mut &mut protocol_account.data.borrow_mut()[..])?;
    Ok(())
}

fn update_royalty(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    creator: Pubkey,
    new_basis_points: u16,
) -> ProgramResult {
    if new_basis_points > 10000 {
        msg!("Royalty basis points cannot exceed 10000 (100%)");
        return Err(ProgramError::InvalidArgument);
    }

    let accounts_iter = &mut accounts.iter();
    let protocol_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;

    if protocol_account.owner != program_id {
        msg!("Protocol account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    if !authority.is_signer {
        msg!("Authority must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    let clock = Clock::get()?;
    let mut protocol_data = CreatorProtocol::try_from_slice(&protocol_account.data.borrow())?;

    if let Some(existing_royalty) = protocol_data
        .royalties
        .iter_mut()
        .find(|r| r.creator == creator)
    {
        existing_royalty.basis_points = new_basis_points;
        existing_royalty.updated_at = clock.unix_timestamp;
    } else {
        protocol_data.royalties.push(RoyaltyData {
            creator,
            basis_points: new_basis_points,
            updated_at: clock.unix_timestamp,
        });
    }

    protocol_data.serialize(&mut &mut protocol_account.data.borrow_mut()[..])?;
    Ok(())
}

fn get_royalties(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let protocol_account = next_account_info(accounts_iter)?;

    if protocol_account.owner != program_id {
        msg!("Protocol account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let protocol_data = CreatorProtocol::try_from_slice(&protocol_account.data.borrow())?;
    
    // In a real implementation, you would return the royalties data
    // For this example, we'll just log them
    for royalty in protocol_data.royalties {
        msg!(
            "Creator: {}, Royalty: {} bps, Updated at: {}",
            royalty.creator,
            royalty.basis_points,
            royalty.updated_at
        );
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_program_test::*;
    use solana_sdk::{
        account::Account,
        signature::Signer,
        transaction::Transaction,
    };

    #[tokio::test]
    async fn test_initialize() {
        let program_id = Pubkey::new_unique();
        let protocol_account = Pubkey::new_unique();

        let mut program_test = ProgramTest::new(
            "creator_protocol",
            program_id,
            processor!(process_instruction),
        );

        let mut accounts = vec![
            (
                protocol_account,
                Account {
                    lamports: 1000000000,
                    data: vec![0; 1024],
                    owner: program_id,
                    executable: false,
                    rent_epoch: Epoch::default(),
                },
            ),
        ];

        program_test.add_accounts(accounts);

        let (mut banks_client, payer, recent_blockhash) = program_test.start().await;

        let mut transaction = Transaction::new_with_payer(
            &[solana_program::system_instruction::create_account(
                &payer.pubkey(),
                &protocol_account,
                1000000000,
                1024,
                &program_id,
            )],
            Some(&payer.pubkey()),
        );

        transaction.sign(&[&payer], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();

        let instruction = CreatorProtocolInstruction::Initialize;
        let mut instruction_data = vec![];
        instruction.serialize(&mut instruction_data).unwrap();

        let mut transaction = Transaction::new_with_payer(
            &[solana_program::instruction::Instruction {
                program_id,
                accounts: vec![solana_program::instruction::AccountMeta::new(
                    protocol_account,
                    false,
                )],
                data: instruction_data,
            }],
            Some(&payer.pubkey()),
        );

        transaction.sign(&[&payer], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();
    }
}
```
