"""
Generated Code Metadata:
========================
Original URL: https://solanaclaims.web.app
Prompt: Generate code to create a decentralized application (dApp) on Solana for climate-related projects, targeting the $5K USDC Climate Award track.
Generated: DETERMINISTIC_fccd93e05530c7ec
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Solana dApp for Climate Awards
//! This program handles climate-related project submissions and voting for the $5K USDC Climate Award.

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

// Program state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct ClimateProject {
    pub id: u64,
    pub title: String,
    pub description: String,
    pub submitter: Pubkey,
    pub votes: u64,
    pub submission_time: i64,
    pub is_approved: bool,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct ClimateAwardProgram {
    pub projects: Vec<ClimateProject>,
    pub total_votes: u64,
    pub award_amount: u64, // in USDC lamports (1 USDC = 1_000_000 lamports)
    pub admin: Pubkey,
}

impl ClimateAwardProgram {
    pub fn new(admin: Pubkey) -> Self {
        Self {
            projects: Vec::new(),
            total_votes: 0,
            award_amount: 5_000_000_000, // $5K USDC in lamports
            admin,
        }
    }

    pub fn submit_project(
        &mut self,
        title: String,
        description: String,
        submitter: Pubkey,
        clock: &Clock,
    ) -> ProgramResult {
        if title.is_empty() || description.is_empty() {
            return Err(ProgramError::InvalidInstructionData);
        }

        let project = ClimateProject {
            id: self.projects.len() as u64 + 1,
            title,
            description,
            submitter,
            votes: 0,
            submission_time: clock.unix_timestamp,
            is_approved: false,
        };

        self.projects.push(project);
        Ok(())
    }

    pub fn vote_for_project(&mut self, project_id: u64) -> ProgramResult {
        if let Some(project) = self.projects.iter_mut().find(|p| p.id == project_id) {
            project.votes += 1;
            self.total_votes += 1;
            Ok(())
        } else {
            Err(ProgramError::InvalidAccountData)
        }
    }

    pub fn approve_project(&mut self, project_id: u64, caller: &Pubkey) -> ProgramResult {
        if caller != &self.admin {
            return Err(ProgramError::IllegalOwner);
        }

        if let Some(project) = self.projects.iter_mut().find(|p| p.id == project_id) {
            project.is_approved = true;
            Ok(())
        } else {
            Err(ProgramError::InvalidAccountData)
        }
    }

    pub fn distribute_award(&mut self, project_id: u64, caller: &Pubkey) -> ProgramResult {
        if caller != &self.admin {
            return Err(ProgramError::IllegalOwner);
        }

        if let Some(project) = self.projects.iter_mut().find(|p| p.id == project_id) {
            if !project.is_approved {
                return Err(ProgramError::InvalidAccountData);
            }

            // In a real implementation, this would transfer USDC to the submitter
            msg!("Distributing {} lamports to {}", self.award_amount, project.submitter);
            Ok(())
        } else {
            Err(ProgramError::InvalidAccountData)
        }
    }
}

// Entry point for the program
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let program_account = next_account_info(accounts_iter)?;

    // Deserialize the program state
    let mut program = ClimateAwardProgram::try_from_slice(&program_account.data.borrow())?;

    // Get clock
    let clock = Clock::get()?;

    // Parse instruction
    let instruction = Instruction::try_from_slice(instruction_data)?;

    match instruction {
        Instruction::SubmitProject { title, description } => {
            let submitter = next_account_info(accounts_iter)?;
            program.submit_project(title, description, *submitter.key, &clock)?;
        }
        Instruction::Vote { project_id } => {
            program.vote_for_project(project_id)?;
        }
        Instruction::ApproveProject { project_id } => {
            let admin = next_account_info(accounts_iter)?;
            program.approve_project(project_id, admin.key)?;
        }
        Instruction::DistributeAward { project_id } => {
            let admin = next_account_info(accounts_iter)?;
            program.distribute_award(project_id, admin.key)?;
        }
    }

    // Serialize the updated program state
    program.serialize(&mut &mut program_account.data.borrow_mut()[..])?;

    Ok(())
}

// Instruction enum for the program
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum Instruction {
    SubmitProject {
        title: String,
        description: String,
    },
    Vote {
        project_id: u64,
    },
    ApproveProject {
        project_id: u64,
    },
    DistributeAward {
        project_id: u64,
    },
}

// Tests
#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{account_info::AccountInfo, pubkey::Pubkey};

    #[test]
    fn test_submit_project() {
        let admin = Pubkey::new_unique();
        let mut program = ClimateAwardProgram::new(admin);

        let clock = Clock {
            epoch: 0,
            epoch_start_timestamp: 0,
            leader_schedule_epoch: 0,
            unix_timestamp: 1234567890,
            slot: 0,
        };

        let submitter = Pubkey::new_unique();
        program
            .submit_project(
                "Test Project".to_string(),
                "Test Description".to_string(),
                submitter,
                &clock,
            )
            .unwrap();

        assert_eq!(program.projects.len(), 1);
        assert_eq!(program.projects[0].title, "Test Project");
    }

    #[test]
    fn test_vote() {
        let admin = Pubkey::new_unique();
        let mut program = ClimateAwardProgram::new(admin);

        let clock = Clock {
            epoch: 0,
            epoch_start_timestamp: 0,
            leader_schedule_epoch: 0,
            unix_timestamp: 1234567890,
            slot: 0,
        };

        let submitter = Pubkey::new_unique();
        program
            .submit_project(
                "Test Project".to_string(),
                "Test Description".to_string(),
                submitter,
                &clock,
            )
            .unwrap();

        program.vote_for_project(1).unwrap();
        assert_eq!(program.projects[0].votes, 1);
        assert_eq!(program.total_votes, 1);
    }
}
```
