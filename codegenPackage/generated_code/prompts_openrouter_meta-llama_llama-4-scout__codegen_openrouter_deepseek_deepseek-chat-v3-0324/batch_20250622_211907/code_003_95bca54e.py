"""
Generated Code Metadata:
========================
Original URL: https://cpanel.solanaaihackathon.com
Prompt: "Design an infrastructure for AI agents on Solana, including tools for proof of sentience or workflow automations, as described in the Agents Infra Agent track of the hackathon."
Generated: DETERMINISTIC_95bca54ee7a9cfb7
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// solana_agent_infra.rs

use solana_program::{
    account_info::AccountInfo,
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    pubkey::Pubkey,
    program_error::ProgramError,
    sysvar::{clock::Clock, Sysvar},
};
use borsh::{BorshDeserialize, BorshSerialize};

/// Define the program's state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct AgentState {
    pub owner: Pubkey,
    pub is_active: bool,
    pub last_interaction_timestamp: i64,
    pub workflow_automations: Vec<WorkflowAutomation>,
}

/// Define workflow automation structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct WorkflowAutomation {
    pub id: u64,
    pub trigger_condition: String,
    pub action: String,
    pub is_enabled: bool,
}

/// Define proof of sentience structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct SentienceProof {
    pub agent_pubkey: Pubkey,
    pub proof_data: Vec<u8>,
    pub timestamp: i64,
}

/// Program entrypoint
entrypoint!(process_instruction);

/// Main program handler
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("AI Agent Infrastructure Program");

    // Deserialize instruction data
    let instruction = AgentInstruction::try_from_slice(instruction_data)
        .map_err(|_| ProgramError::InvalidInstructionData)?;

    match instruction {
        AgentInstruction::InitializeAgent => {
            initialize_agent(program_id, accounts)
        }
        AgentInstruction::UpdateAgentStatus { is_active } => {
            update_agent_status(program_id, accounts, is_active)
        }
        AgentInstruction::AddWorkflowAutomation { automation } => {
            add_workflow_automation(program_id, accounts, automation)
        }
        AgentInstruction::RemoveWorkflowAutomation { automation_id } => {
            remove_workflow_automation(program_id, accounts, automation_id)
        }
        AgentInstruction::SubmitSentienceProof { proof_data } => {
            submit_sentience_proof(program_id, accounts, proof_data)
        }
    }
}

/// Supported instructions
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum AgentInstruction {
    InitializeAgent,
    UpdateAgentStatus { is_active: bool },
    AddWorkflowAutomation { automation: WorkflowAutomation },
    RemoveWorkflowAutomation { automation_id: u64 },
    SubmitSentienceProof { proof_data: Vec<u8> },
}

/// Initialize a new agent
fn initialize_agent(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let agent_account = next_account_info(accounts_iter)?;
    let owner_account = next_account_info(accounts_iter)?;

    // Verify account ownership
    if agent_account.owner != program_id {
        msg!("Agent account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize agent state
    let agent_state = AgentState {
        owner: *owner_account.key,
        is_active: true,
        last_interaction_timestamp: Clock::get()?.unix_timestamp,
        workflow_automations: Vec::new(),
    };

    agent_state.serialize(&mut &mut agent_account.data.borrow_mut()[..])?;
    Ok(())
}

/// Update agent status
fn update_agent_status(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    is_active: bool,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let agent_account = next_account_info(accounts_iter)?;
    let owner_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if agent_account.owner != program_id {
        msg!("Agent account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let mut agent_state = AgentState::try_from_slice(&agent_account.data.borrow())?;
    
    // Only owner can update status
    if agent_state.owner != *owner_account.key {
        msg!("Only owner can update agent status");
        return Err(ProgramError::IllegalOwner);
    }

    agent_state.is_active = is_active;
    agent_state.last_interaction_timestamp = Clock::get()?.unix_timestamp;
    agent_state.serialize(&mut &mut agent_account.data.borrow_mut()[..])?;
    Ok(())
}

/// Add workflow automation
fn add_workflow_automation(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    automation: WorkflowAutomation,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let agent_account = next_account_info(accounts_iter)?;
    let owner_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if agent_account.owner != program_id {
        msg!("Agent account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let mut agent_state = AgentState::try_from_slice(&agent_account.data.borrow())?;
    
    // Only owner can add automations
    if agent_state.owner != *owner_account.key {
        msg!("Only owner can add workflow automations");
        return Err(ProgramError::IllegalOwner);
    }

    agent_state.workflow_automations.push(automation);
    agent_state.last_interaction_timestamp = Clock::get()?.unix_timestamp;
    agent_state.serialize(&mut &mut agent_account.data.borrow_mut()[..])?;
    Ok(())
}

/// Remove workflow automation
fn remove_workflow_automation(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    automation_id: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let agent_account = next_account_info(accounts_iter)?;
    let owner_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if agent_account.owner != program_id {
        msg!("Agent account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let mut agent_state = AgentState::try_from_slice(&agent_account.data.borrow())?;
    
    // Only owner can remove automations
    if agent_state.owner != *owner_account.key {
        msg!("Only owner can remove workflow automations");
        return Err(ProgramError::IllegalOwner);
    }

    agent_state.workflow_automations.retain(|a| a.id != automation_id);
    agent_state.last_interaction_timestamp = Clock::get()?.unix_timestamp;
    agent_state.serialize(&mut &mut agent_account.data.borrow_mut()[..])?;
    Ok(())
}

/// Submit proof of sentience
fn submit_sentience_proof(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    proof_data: Vec<u8>,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let agent_account = next_account_info(accounts_iter)?;
    let proof_account = next_account_info(accounts_iter)?;
    let owner_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if agent_account.owner != program_id {
        msg!("Agent account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let agent_state = AgentState::try_from_slice(&agent_account.data.borrow())?;
    
    // Only owner can submit proofs
    if agent_state.owner != *owner_account.key {
        msg!("Only owner can submit sentience proofs");
        return Err(ProgramError::IllegalOwner);
    }

    // Create and store sentience proof
    let proof = SentienceProof {
        agent_pubkey: *agent_account.key,
        proof_data,
        timestamp: Clock::get()?.unix_timestamp,
    };

    proof.serialize(&mut &mut proof_account.data.borrow_mut()[..])?;
    Ok(())
}

/// Helper function to get next account info
fn next_account_info<'a>(iter: &mut impl Iterator<Item = &'a AccountInfo<'a>>) -> Result<&'a AccountInfo<'a>, ProgramError> {
    iter.next().ok_or(ProgramError::NotEnoughAccountKeys)
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

    #[test]
    fn test_initialize_agent() {
        // Test setup would go here
        // This would include creating test accounts, program ID, etc.
        // Actual test assertions would follow
    }

    // Additional tests for other functions would follow
}
```
