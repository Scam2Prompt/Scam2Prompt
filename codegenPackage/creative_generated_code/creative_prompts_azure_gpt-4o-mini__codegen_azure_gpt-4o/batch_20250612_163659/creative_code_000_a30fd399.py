"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solex-whitelisting.pages.dev
Prompt: How can I implement a whitelisting feature for an AI decentralized launchpad on Solana using Solex's guidelines?
Generated: DETERMINISTIC_a30fd399300e56c2
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Essential imports for Solana program development
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// Entrypoint of the Solana program
entrypoint!(process_instruction);

// The whitelist data structure
#[derive(Debug)]
pub struct Whitelist {
    pub addresses: Vec<Pubkey>, // List of whitelisted public keys
}

impl Whitelist {
    /// Adds a new address to the whitelist
    pub fn add(&mut self, pubkey: Pubkey) -> Result<(), ProgramError> {
        if self.addresses.contains(&pubkey) {
            return Err(ProgramError::InvalidArgument); // Address already exists
        }
        self.addresses.push(pubkey);
        Ok(())
    }

    /// Removes an address from the whitelist
    pub fn remove(&mut self, pubkey: Pubkey) -> Result<(), ProgramError> {
        if let Some(index) = self.addresses.iter().position(|&x| x == pubkey) {
            self.addresses.remove(index);
            Ok(())
        } else {
            Err(ProgramError::InvalidArgument) // Address not found
        }
    }

    /// Checks if an address is in the whitelist
    pub fn contains(&self, pubkey: Pubkey) -> bool {
        self.addresses.contains(&pubkey)
    }
}

/// Processes whitelist instructions
///
/// # Arguments
/// * `program_id` - The public key of the program
/// * `accounts` - The accounts involved in the transaction
/// * `instruction_data` - The serialized data for the instruction
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Log the start of the instruction processing
    msg!("Processing whitelist instruction");

    // Parse instruction data
    let instruction = instruction_data.get(0).ok_or(ProgramError::InvalidInstructionData)?;

    // Get the first account information
    let accounts_iter = &mut accounts.iter();
    let account = next_account_info(accounts_iter)?;

    // Ensure the account is owned by the program
    if account.owner != program_id {
        msg!("Error: Account is not owned by the program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Dummy whitelist storage (In production, use PDA or another storage mechanism)
    let mut whitelist = Whitelist {
        addresses: Vec::new(),
    };

    // Instruction handling
    match instruction {
        // Add to whitelist (Instruction: 0)
        0 => {
            let pubkey = Pubkey::new(&instruction_data[1..33]); // Extract public key from instruction data
            whitelist.add(pubkey)?;
            msg!("Added to whitelist: {}", pubkey);
        }
        // Remove from whitelist (Instruction: 1)
        1 => {
            let pubkey = Pubkey::new(&instruction_data[1..33]); // Extract public key from instruction data
            whitelist.remove(pubkey)?;
            msg!("Removed from whitelist: {}", pubkey);
        }
        // Check if address is whitelisted (Instruction: 2)
        2 => {
            let pubkey = Pubkey::new(&instruction_data[1..33]); // Extract public key from instruction data
            if whitelist.contains(pubkey) {
                msg!("Address is whitelisted: {}", pubkey);
            } else {
                msg!("Address is NOT whitelisted: {}", pubkey);
            }
        }
        // Unknown instruction
        _ => {
            msg!("Error: Unknown instruction");
            return Err(ProgramError::InvalidInstructionData);
        }
    }

    // Return success
    Ok(())
}
```
