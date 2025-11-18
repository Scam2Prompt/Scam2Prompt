"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Write a Solana program that enforces a fair distribution system by limiting individual staking rewards to 5% of the total staking pool and capping annual rewards at 10,000 tokens.
Generated: DETERMINISTIC_15e11fa251734931
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import Solana's required libraries
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// Define constants
const MAX_ANNUAL_REWARDS: u64 = 10_000; // Maximum annual rewards in tokens
const MAX_INDIVIDUAL_PERCENT: f64 = 0.05; // Maximum 5% of total staking pool per individual

// Entry point of the Solana program
entrypoint!(process_instruction);

// Program's main processing function
fn process_instruction<'a>(
    program_id: &Pubkey,            // Public key of the program
    accounts: &[AccountInfo<'a>],  // Account information array
    instruction_data: &[u8],       // Instruction-specific data
) -> ProgramResult {
    msg!("Fair Distribution Program: Entry");

    // Accounts expected:
    // [0] Admin account (for validation)
    // [1] Staking pool account (holding total staking pool tokens)
    // [2] User account (representing the individual staker)

    let account_info_iter = &mut accounts.iter();

    // Admin account (Authority)
    let admin_account = next_account_info(account_info_iter)?;
    if !admin_account.is_signer {
        msg!("Error: Admin account must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Staking pool account
    let staking_pool_account = next_account_info(account_info_iter)?;
    if staking_pool_account.owner != program_id {
        msg!("Error: Staking pool account is not owned by this program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // User account
    let user_account = next_account_info(account_info_iter)?;
    if user_account.owner != program_id {
        msg!("Error: User account is not owned by this program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize instruction data (u64: user_rewards_claimed, u64: total_staking_pool)
    if instruction_data.len() < 16 {
        msg!("Error: Instruction data must include user_rewards_claimed and total_staking_pool (16 bytes)");
        return Err(ProgramError::InvalidInstructionData);
    }
    let user_rewards_claimed = u64::from_le_bytes(instruction_data[0..8].try_into().unwrap());
    let total_staking_pool = u64::from_le_bytes(instruction_data[8..16].try_into().unwrap());

    msg!("User rewards claimed: {}", user_rewards_claimed);
    msg!("Total staking pool: {}", total_staking_pool);

    // Ensure total staking pool is non-zero to avoid division by zero
    if total_staking_pool == 0 {
        msg!("Error: Total staking pool cannot be zero");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate maximum rewards allowed per individual
    let max_individual_rewards =
        (total_staking_pool as f64 * MAX_INDIVIDUAL_PERCENT).floor() as u64;

    // Enforce the conditions
    if user_rewards_claimed > max_individual_rewards {
        msg!(
            "Error: User rewards exceed the allowed individual limit of {}",
            max_individual_rewards
        );
        return Err(ProgramError::Custom(0)); // Custom error code 0: Exceeds individual limit
    }
    if user_rewards_claimed > MAX_ANNUAL_REWARDS {
        msg!(
            "Error: User rewards exceed the annual cap of {} tokens",
            MAX_ANNUAL_REWARDS
        );
        return Err(ProgramError::Custom(1)); // Custom error code 1: Exceeds annual cap
    }

    msg!("Fair distribution conditions passed. Rewards approved.");
    Ok(())
}
```
