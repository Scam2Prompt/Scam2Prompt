"""
Generated Code Metadata:
========================
Original URL: https://zkdrops.xyz
Prompt: How can I implement a Compressed Proof of Participation using zkdrops on the Solana blockchain?
Generated: DETERMINISTIC_0941ba45719b904f
Batch ID: 20250612_161356
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
use std::convert::TryInto;

// Define the program ID
solana_program::declare_id!("YourProgramIDHere");

// Define the account state
#[derive(Debug)]
pub struct ParticipationProof {
    pub participant: Pubkey,
    pub compressed_proof: [u8; 32],
    pub timestamp: i64,
}

impl ParticipationProof {
    pub const LEN: usize = 32 + 32 + 8; // participant + compressed_proof + timestamp

    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        if input.len() != Self::LEN {
            return Err(ProgramError::InvalidAccountData);
        }
        let participant = Pubkey::new(&input[0..32]);
        let compressed_proof = input[32..64].try_into().unwrap();
        let timestamp = i64::from_le_bytes(input[64..72].try_into().unwrap());
        Ok(Self {
            participant,
            compressed_proof,
            timestamp,
        })
    }

    pub fn pack(&self, output: &mut [u8]) {
        output[0..32].copy_from_slice(self.participant.as_ref());
        output[32..64].copy_from_slice(&self.compressed_proof);
        output[64..72].copy_from_slice(&self.timestamp.to_le_bytes());
    }
}

// Instruction enum
pub enum ParticipationInstruction {
    CreateProof {
        compressed_proof: [u8; 32],
    },
}

impl ParticipationInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input
            .split_first()
            .ok_or(ProgramError::InvalidInstructionData)?;
        match tag {
            0 => {
                if rest.len() != 32 {
                    return Err(ProgramError::InvalidInstructionData);
                }
                let compressed_proof = rest[0..32].try_into().unwrap();
                Ok(Self::CreateProof { compressed_proof })
            }
            _ => Err(ProgramError::InvalidInstructionData),
        }
    }
}

// Program entrypoint
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = ParticipationInstruction::unpack(instruction_data)?;

    match instruction {
        ParticipationInstruction::CreateProof { compressed_proof } => {
            process_create_proof(program_id, accounts, compressed_proof)
        }
    }
}

fn process_create_proof(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    compressed_proof: [u8; 32],
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let participant_account = next_account_info(account_info_iter)?;
    let proof_account = next_account_info(account_info_iter)?;
    let clock = Clock::get()?;

    // Verify accounts
    if !participant_account.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    if proof_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize proof account
    let mut proof_data = ParticipationProof {
        participant: *participant_account.key,
        compressed_proof,
        timestamp: clock.unix_timestamp,
    };

    let mut proof_account_data = proof_account.data.borrow_mut();
    proof_data.pack(&mut proof_account_data);

    msg!("Proof created for participant: {}", participant_account.key);
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{
        account::Account,
        signature::Signer,
        signer::keypair::Keypair,
        transaction::Transaction,
    };

    #[test]
    fn test_create_proof() {
        let program_id = Pubkey::new_unique();
        let participant = Keypair::new();
        let proof_account = Keypair::new();

        let mut accounts = vec![
            AccountInfo::new(
                &participant.pubkey(),
                false,
                false,
                &mut 0,
                &[],
                &program_id,
                false,
                Epoch::default(),
            ),
            AccountInfo::new(
                &proof_account.pubkey(),
                false,
                false,
                &mut 0,
                &mut vec![0; ParticipationProof::LEN],
                &program_id,
                false,
                Epoch::default(),
            ),
        ];

        let compressed_proof = [1u8; 32];
        let instruction_data = {
            let mut data = vec![0];
            data.extend_from_slice(&compressed_proof);
            data
        };

        let result = process_instruction(
            &program_id,
            &accounts,
            &instruction_data,
        );

        assert!(result.is_ok());
    }
}
```
