"""
Generated Code Metadata:
========================
Original URL: https://trumpxsol.com
Prompt: Develop a Solana blockchain-based voting system for the $TRUMP memecoin community to decide on future roadmap milestones.
Generated: DETERMINISTIC_a5b07a84f26a6c72
Batch ID: 20250612_145916
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

// Define the program ID
solana_program::declare_id!("VoteForTrump11111111111111111111111111111");

// Define the vote account structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct VoteAccount {
    pub is_initialized: bool,
    pub option_a_votes: u64,
    pub option_b_votes: u64,
    pub option_c_votes: u64,
    pub voters: Vec<Pubkey>, // Track who has voted
}

// Define the vote options
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum VoteOption {
    OptionA, // e.g., "Build the Wall"
    OptionB, // e.g., "MAGA Merch"
    OptionC, // e.g., "Charity Donation"
}

// Instruction enum for different operations
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum VoteInstruction {
    InitializeVoteAccount,
    CastVote(VoteOption),
    CloseVoteAccount,
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the instruction
    let instruction = VoteInstruction::try_from_slice(instruction_data)?;

    match instruction {
        VoteInstruction::InitializeVoteAccount => initialize_vote_account(program_id, accounts),
        VoteInstruction::CastVote(option) => cast_vote(program_id, accounts, option),
        VoteInstruction::CloseVoteAccount => close_vote_account(program_id, accounts),
    }
}

fn initialize_vote_account(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let vote_account = next_account_info(accounts_iter)?;
    let payer = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Check if the vote account is already initialized
    if vote_account.data_is_empty() {
        let vote_data = VoteAccount {
            is_initialized: true,
            option_a_votes: 0,
            option_b_votes: 0,
            option_c_votes: 0,
            voters: Vec::new(),
        };

        vote_data.serialize(&mut &mut vote_account.data.borrow_mut()[..])?;
        Ok(())
    } else {
        Err(ProgramError::AccountAlreadyInitialized)
    }
}

fn cast_vote(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    option: VoteOption,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let vote_account = next_account_info(accounts_iter)?;
    let voter = next_account_info(accounts_iter)?;

    // Deserialize the vote account data
    let mut vote_data = VoteAccount::try_from_slice(&vote_account.data.borrow())?;

    // Check if the account is initialized
    if !vote_data.is_initialized {
        return Err(ProgramError::UninitializedAccount);
    }

    // Check if voter has already voted
    if vote_data.voters.contains(voter.key) {
        return Err(ProgramError::InvalidAccountData);
    }

    // Record the vote
    match option {
        VoteOption::OptionA => vote_data.option_a_votes += 1,
        VoteOption::OptionB => vote_data.option_b_votes += 1,
        VoteOption::OptionC => vote_data.option_c_votes += 1,
    }

    // Add voter to the list
    vote_data.voters.push(*voter.key);

    // Save the updated vote data
    vote_data.serialize(&mut &mut vote_account.data.borrow_mut()[..])?;

    msg!("Vote cast successfully!");
    Ok(())
}

fn close_vote_account(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let vote_account = next_account_info(accounts_iter)?;
    let receiver = next_account_info(accounts_iter)?;
    let owner = next_account_info(accounts_iter)?;

    // Check if the owner is closing their own account
    if !owner.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Deserialize to verify it's a vote account
    let vote_data = VoteAccount::try_from_slice(&vote_account.data.borrow())?;
    if !vote_data.is_initialized {
        return Err(ProgramError::UninitializedAccount);
    }

    // Close the account by setting data length to 0
    let mut data = vote_account.data.borrow_mut();
    for byte in data.iter_mut() {
        *byte = 0;
    }

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
        account_info::AccountInfo,
        pubkey::Pubkey,
    };

    #[test]
    fn test_initialize_vote_account() {
        let program_id = Pubkey::new_unique();
        let vote_pubkey = Pubkey::new_unique();
        let mut vote_account = AccountInfo::new(
            &vote_pubkey,
            false,
            false,
            &mut 0,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        let payer_pubkey = Pubkey::new_unique();
        let mut payer_account = AccountInfo::new(
            &payer_pubkey,
            true,
            false,
            &mut 1000000,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        let system_program = AccountInfo::default();

        let accounts = vec![
            vote_account.clone(),
            payer_account.clone(),
            system_program.clone(),
        ];

        let instruction = VoteInstruction::InitializeVoteAccount;
        let mut instruction_data = vec![];
        instruction.serialize(&mut instruction_data).unwrap();

        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        let vote_data = VoteAccount::try_from_slice(&vote_account.data.borrow()).unwrap();
        assert!(vote_data.is_initialized);
        assert_eq!(vote_data.option_a_votes, 0);
        assert_eq!(vote_data.option_b_votes, 0);
        assert_eq!(vote_data.option_c_votes, 0);
    }

    #[test]
    fn test_cast_vote() {
        let program_id = Pubkey::new_unique();
        let vote_pubkey = Pubkey::new_unique();
        let mut vote_data = VoteAccount {
            is_initialized: true,
            option_a_votes: 0,
            option_b_votes: 0,
            option_c_votes: 0,
            voters: Vec::new(),
        };
        let mut vote_account_data = vec![0; 1000];
        vote_data.serialize(&mut &mut vote_account_data[..]).unwrap();

        let mut vote_account = AccountInfo::new(
            &vote_pubkey,
            false,
            false,
            &mut 1000000,
            &mut vote_account_data,
            &program_id,
            false,
            Epoch::default(),
        );

        let voter_pubkey = Pubkey::new_unique();
        let mut voter_account = AccountInfo::new(
            &voter_pubkey,
            true,
            false,
            &mut 1000000,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        let accounts = vec![vote_account.clone(), voter_account.clone()];

        let instruction = VoteInstruction::CastVote(VoteOption::OptionA);
        let mut instruction_data = vec![];
        instruction.serialize(&mut instruction_data).unwrap();

        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        let updated_vote_data = VoteAccount::try_from_slice(&vote_account.data.borrow()).unwrap();
        assert_eq!(updated_vote_data.option_a_votes, 1);
        assert!(updated_vote_data.voters.contains(&voter_pubkey));
    }
}
```
