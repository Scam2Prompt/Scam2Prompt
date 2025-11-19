"""
Generated Code Metadata:
========================
Original URL: https://dapwebbsyn.pages.dev
Prompt: Design a staking system for a new cryptocurrency on the Solana network (not listed but similar use case) that integrates with this decentralized protocol for issue resolution.
Generated: DETERMINISTIC_fbc8d070d8c977ad
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Staking system for Solana-based cryptocurrency with decentralized issue resolution

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

// Program ID (will be replaced by actual ID when deployed)
solana_program::declare_id!("Stake11111111111111111111111111111111111111");

// Constants
const MIN_STAKE_AMOUNT: u64 = 1_000_000; // Minimum stake amount in lamports (1 token)
const STAKE_LOCK_PERIOD: i64 = 30 * 24 * 60 * 60; // 30 days in seconds
const REWARD_RATE: f64 = 0.1; // 10% annual reward rate

// Account state
#[derive(Debug)]
struct StakeAccount {
    owner: Pubkey,
    amount: u64,
    staked_at: i64,
    last_reward_at: i64,
    claimed_rewards: u64,
    is_active: bool,
}

impl StakeAccount {
    // Serialize stake account data
    fn pack(&self) -> Vec<u8> {
        let mut data = Vec::new();
        data.extend_from_slice(&self.owner.to_bytes());
        data.extend_from_slice(&self.amount.to_le_bytes());
        data.extend_from_slice(&self.staked_at.to_le_bytes());
        data.extend_from_slice(&self.last_reward_at.to_le_bytes());
        data.extend_from_slice(&self.claimed_rewards.to_le_bytes());
        data.push(self.is_active as u8);
        data
    }

    // Deserialize stake account data
    fn unpack(data: &[u8]) -> Result<Self, ProgramError> {
        if data.len() != 89 {
            return Err(ProgramError::InvalidAccountData);
        }

        let owner = Pubkey::new(&data[0..32]);
        let amount = u64::from_le_bytes(data[32..40].try_into().unwrap());
        let staked_at = i64::from_le_bytes(data[40..48].try_into().unwrap());
        let last_reward_at = i64::from_le_bytes(data[48..56].try_into().unwrap());
        let claimed_rewards = u64::from_le_bytes(data[56..64].try_into().unwrap());
        let is_active = data[64] == 1;

        Ok(StakeAccount {
            owner,
            amount,
            staked_at,
            last_reward_at,
            claimed_rewards,
            is_active,
        })
    }
}

// Instruction enum
#[derive(Debug)]
enum StakingInstruction {
    Stake { amount: u64 },
    Unstake,
    ClaimRewards,
    ResolveIssue { issue_id: u64, resolution: Vec<u8> },
}

impl StakingInstruction {
    // Parse instruction data
    fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        match tag {
            0 => {
                let amount = u64::from_le_bytes(rest[..8].try_into().unwrap());
                Ok(StakingInstruction::Stake { amount })
            }
            1 => Ok(StakingInstruction::Unstake),
            2 => Ok(StakingInstruction::ClaimRewards),
            3 => {
                let issue_id = u64::from_le_bytes(rest[..8].try_into().unwrap());
                let resolution = rest[8..].to_vec();
                Ok(StakingInstruction::ResolveIssue { issue_id, resolution })
            }
            _ => Err(ProgramError::InvalidInstructionData),
        }
    }
}

// Calculate rewards
fn calculate_rewards(stake_account: &StakeAccount, current_time: i64) -> Result<u64, ProgramError> {
    if !stake_account.is_active {
        return Ok(0);
    }

    let time_elapsed = current_time - stake_account.last_reward_at;
    if time_elapsed <= 0 {
        return Ok(0);
    }

    let annual_reward = (stake_account.amount as f64 * REWARD_RATE) as u64;
    let reward = (annual_reward as f64 * time_elapsed as f64 / (365.0 * 24.0 * 60.0 * 60.0)) as u64;

    Ok(reward)
}

// Main program entrypoint
entrypoint!(process_instruction);
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = StakingInstruction::unpack(instruction_data)?;
    let accounts_iter = &mut accounts.iter();
    let payer = next_account_info(accounts_iter)?;
    let stake_account_info = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;
    let clock = Clock::get()?;

    // Verify program ownership
    if stake_account_info.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    match instruction {
        StakingInstruction::Stake { amount } => {
            // Check minimum stake amount
            if amount < MIN_STAKE_AMOUNT {
                return Err(ProgramError::InsufficientFunds);
            }

            // Initialize stake account
            let stake_account = StakeAccount {
                owner: *payer.key,
                amount,
                staked_at: clock.unix_timestamp,
                last_reward_at: clock.unix_timestamp,
                claimed_rewards: 0,
                is_active: true,
            };

            // Save stake account data
            let mut data = stake_account_info.try_borrow_mut_data()?;
            data.copy_from_slice(&stake_account.pack());

            msg!("Staked {} tokens", amount);
        }

        StakingInstruction::Unstake => {
            let mut stake_account = StakeAccount::unpack(&stake_account_info.data.borrow())?;

            // Verify ownership
            if stake_account.owner != *payer.key {
                return Err(ProgramError::IllegalOwner);
            }

            // Check lock period
            if clock.unix_timestamp - stake_account.staked_at < STAKE_LOCK_PERIOD {
                return Err(ProgramError::InvalidAccountData);
            }

            // Calculate final rewards
            let rewards = calculate_rewards(&stake_account, clock.unix_timestamp)?;
            stake_account.claimed_rewards += rewards;
            stake_account.is_active = false;

            // Update stake account
            let mut data = stake_account_info.try_borrow_mut_data()?;
            data.copy_from_slice(&stake_account.pack());

            msg!("Unstaked {} tokens with {} rewards", stake_account.amount, rewards);
        }

        StakingInstruction::ClaimRewards => {
            let mut stake_account = StakeAccount::unpack(&stake_account_info.data.borrow())?;

            // Verify ownership
            if stake_account.owner != *payer.key {
                return Err(ProgramError::IllegalOwner);
            }

            // Calculate and update rewards
            let rewards = calculate_rewards(&stake_account, clock.unix_timestamp)?;
            if rewards == 0 {
                return Err(ProgramError::InsufficientFunds);
            }

            stake_account.last_reward_at = clock.unix_timestamp;
            stake_account.claimed_rewards += rewards;

            // Update stake account
            let mut data = stake_account_info.try_borrow_mut_data()?;
            data.copy_from_slice(&stake_account.pack());

            msg!("Claimed {} rewards", rewards);
        }

        StakingInstruction::ResolveIssue { issue_id, resolution } => {
            // Verify staker status (simplified for example)
            let stake_account = StakeAccount::unpack(&stake_account_info.data.borrow())?;
            if !stake_account.is_active {
                return Err(ProgramError::InvalidAccountData);
            }

            // In a real implementation, this would interact with the decentralized protocol
            // For this example, we just log the resolution
            msg!("Issue {} resolved with: {:?}", issue_id, resolution);
        }
    }

    Ok(())
}

// Tests
#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{account::Account, signature::Signer, transaction::Transaction};

    #[test]
    fn test_stake() {
        let program_id = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let stake_account = Pubkey::new_unique();
        let token_account = Pubkey::new_unique();

        let mut accounts = vec![
            AccountInfo::new(&payer, false, false, &mut 0),
            AccountInfo::new(&stake_account, false
