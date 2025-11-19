"""
Generated Code Metadata:
========================
Original URL: https://solana10x.com
Prompt: Write a Solana program that enforces a fair distribution system by limiting individual staking rewards to 5% of the total staking pool and capping annual rewards at 10,000 tokens.
Generated: DETERMINISTIC_15e11fa251734931
Batch ID: 20250612_145459
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

// Define the program's constants
const MAX_INDIVIDUAL_SHARE: f64 = 0.05; // 5% max individual share
const ANNUAL_REWARD_CAP: u64 = 10_000; // 10,000 tokens annual cap

// Define the program's state structure
#[derive(Debug)]
struct StakingPool {
    total_staked: u64,
    annual_rewards_distributed: u64,
    stakers: Vec<Staker>,
}

#[derive(Debug)]
struct Staker {
    pubkey: Pubkey,
    amount_staked: u64,
    rewards_claimed: u64,
}

// Program entrypoint
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let staking_pool_account = next_account_info(accounts_iter)?;
    let staker_account = next_account_info(accounts_iter)?;
    let clock_account = next_account_info(accounts_iter)?;

    // Verify the clock sysvar account
    if !clock_account.is_sysvar() {
        msg!("Invalid clock sysvar account");
        return Err(ProgramError::InvalidAccountData);
    }

    // Deserialize the staking pool data
    let mut staking_pool = deserialize_staking_pool(staking_pool_account)?;

    // Get current timestamp from clock
    let clock = Clock::from_account_info(clock_account)?;
    let current_timestamp = clock.unix_timestamp;

    // Process stake or claim instruction
    match instruction_data[0] {
        0 => stake_tokens(&mut staking_pool, staker_account, instruction_data)?,
        1 => claim_rewards(&mut staking_pool, staker_account, current_timestamp)?,
        _ => return Err(ProgramError::InvalidInstructionData),
    }

    // Serialize the updated staking pool data
    serialize_staking_pool(staking_pool_account, &staking_pool)?;

    Ok(())
}

fn stake_tokens(
    staking_pool: &mut StakingPool,
    staker_account: &AccountInfo,
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the stake amount from instruction data
    let stake_amount = u64::from_le_bytes(
        instruction_data[1..9]
            .try_into()
            .map_err(|_| ProgramError::InvalidInstructionData)?,
    );

    // Check if staker already exists
    let staker_index = staking_pool
        .stakers
        .iter()
        .position(|s| s.pubkey == *staker_account.key);

    if let Some(index) = staker_index {
        // Update existing staker
        staking_pool.stakers[index].amount_staked += stake_amount;
    } else {
        // Add new staker
        staking_pool.stakers.push(Staker {
            pubkey: *staker_account.key,
            amount_staked: stake_amount,
            rewards_claimed: 0,
        });
    }

    // Update total staked amount
    staking_pool.total_staked += stake_amount;

    Ok(())
}

fn claim_rewards(
    staking_pool: &mut StakingPool,
    staker_account: &AccountInfo,
    current_timestamp: i64,
) -> ProgramResult {
    // Find the staker
    let staker_index = staking_pool
        .stakers
        .iter()
        .position(|s| s.pubkey == *staker_account.key)
        .ok_or(ProgramError::InvalidAccountData)?;

    let staker = &mut staking_pool.stakers[staker_index];

    // Calculate rewards based on staker's share
    let staker_share = staker.amount_staked as f64 / staking_pool.total_staked as f64;
    if staker_share > MAX_INDIVIDUAL_SHARE {
        msg!("Staker exceeds maximum individual share");
        return Err(ProgramError::Custom(1)); // Custom error for exceeding share
    }

    // Calculate annual rewards (simplified calculation)
    let annual_rewards = (staker_share * ANNUAL_REWARD_CAP as f64) as u64;

    // Check if claiming would exceed annual cap
    if staking_pool.annual_rewards_distributed + annual_rewards > ANNUAL_REWARD_CAP {
        msg!("Annual reward cap reached");
        return Err(ProgramError::Custom(2)); // Custom error for exceeding cap
    }

    // Update staker's claimed rewards and pool's distributed rewards
    staker.rewards_claimed += annual_rewards;
    staking_pool.annual_rewards_distributed += annual_rewards;

    // Reset annual rewards if a year has passed (simplified check)
    if current_timestamp % (365 * 24 * 60 * 60) == 0 {
        staking_pool.annual_rewards_distributed = 0;
    }

    Ok(())
}

fn deserialize_staking_pool(account: &AccountInfo) -> Result<StakingPool, ProgramError> {
    let data = account.try_borrow_data()?;
    if data.is_empty() {
        return Ok(StakingPool {
            total_staked: 0,
            annual_rewards_distributed: 0,
            stakers: Vec::new(),
        });
    }

    bincode::deserialize(&data).map_err(|_| ProgramError::InvalidAccountData)
}

fn serialize_staking_pool(account: &AccountInfo, staking_pool: &StakingPool) -> ProgramResult {
    let serialized = bincode::serialize(staking_pool)
        .map_err(|_| ProgramError::InvalidAccountData)?;
    
    let mut data = account.try_borrow_mut_data()?;
    if data.len() < serialized.len() {
        msg!("Account data too small for serialization");
        return Err(ProgramError::AccountDataTooSmall);
    }
    
    data[..serialized.len()].copy_from_slice(&serialized);
    Ok(())
}
```
