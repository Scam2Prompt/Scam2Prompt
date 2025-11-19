"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Describe how Código can be used to facilitate the creation of complex interconnected systems on Solana. Include examples of CIDL-based code generation and security features.
Generated: DETERMINISTIC_b91c2ea35ca7598a
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! This module demonstrates how Código can be used to build complex interconnected systems on Solana
//! using CIDL (Code Interface Definition Language) for code generation and security features.

use solana_program::{
    account_info::AccountInfo,
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// CIDL-generated code would typically be placed here
// For demonstration, we'll show a simplified version

/// CIDL-generated account structure
#[derive(Debug)]
pub struct UserAccount {
    pub authority: Pubkey,
    pub balance: u64,
    pub is_initialized: bool,
}

impl UserAccount {
    /// CIDL-generated deserialization
    pub fn deserialize(data: &[u8]) -> Result<Self, ProgramError> {
        // In real CIDL, this would be auto-generated with proper bounds checking
        if data.len() < 41 {
            return Err(ProgramError::InvalidAccountData);
        }
        
        Ok(Self {
            authority: Pubkey::new(&data[0..32]),
            balance: u64::from_le_bytes(data[32..40].try_into().unwrap()),
            is_initialized: data[40] == 1,
        })
    }

    /// CIDL-generated serialization
    pub fn serialize(&self, data: &mut [u8]) -> Result<(), ProgramError> {
        if data.len() < 41 {
            return Err(ProgramError::InvalidAccountData);
        }

        data[0..32].copy_from_slice(self.authority.as_ref());
        data[32..40].copy_from_slice(&self.balance.to_le_bytes());
        data[40] = self.is_initialized as u8;
        Ok(())
    }
}

/// CIDL-generated instruction enum
#[repr(u8)]
pub enum UserInstruction {
    Initialize,
    Transfer { amount: u64 },
    // More instructions would be auto-generated from CIDL
}

impl UserInstruction {
    /// CIDL-generated unpacking
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        
        match tag {
            0 => Ok(UserInstruction::Initialize),
            1 => {
                let amount = rest
                    .get(..8)
                    .and_then(|slice| slice.try_into().ok())
                    .map(u64::from_le_bytes)
                    .ok_or(ProgramError::InvalidInstructionData)?;
                Ok(UserInstruction::Transfer { amount })
            }
            _ => Err(ProgramError::InvalidInstructionData),
        }
    }
}

/// Security features - Ownership check
fn check_authority(authority: &Pubkey, account_info: &AccountInfo) -> ProgramResult {
    if !account_info.is_signer {
        msg!("Missing required signature");
        return Err(ProgramError::MissingRequiredSignature);
    }
    if account_info.key != authority {
        msg!("Invalid authority");
        return Err(ProgramError::InvalidAccountData);
    }
    Ok(())
}

/// Main program entry point
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // CIDL would generate this dispatch logic automatically
    let instruction = UserInstruction::unpack(instruction_data)?;
    
    match instruction {
        UserInstruction::Initialize => initialize(program_id, accounts),
        UserInstruction::Transfer { amount } => transfer(program_id, accounts, amount),
    }
}

/// CIDL-generated initialize handler
fn initialize(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Account validation would be auto-generated from CIDL
    let accounts_iter = &mut accounts.iter();
    let user_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    
    // Check the account isn't already initialized
    let mut account_data = UserAccount::deserialize(&user_account.data.borrow())?;
    if account_data.is_initialized {
        return Err(ProgramError::AccountAlreadyInitialized);
    }
    
    // Initialize the account
    account_data.authority = *authority.key;
    account_data.balance = 0;
    account_data.is_initialized = true;
    
    account_data.serialize(&mut user_account.data.borrow_mut())?;
    Ok(())
}

/// CIDL-generated transfer handler
fn transfer(program_id: &Pubkey, accounts: &[AccountInfo], amount: u64) -> ProgramResult {
    // Account validation would be auto-generated from CIDL
    let accounts_iter = &mut accounts.iter();
    let source_account = next_account_info(accounts_iter)?;
    let destination_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    
    // Deserialize accounts
    let mut source_data = UserAccount::deserialize(&source_account.data.borrow())?;
    let mut dest_data = UserAccount::deserialize(&destination_account.data.borrow())?;
    
    // Security checks
    check_authority(&source_data.authority, authority)?;
    
    if !source_data.is_initialized || !dest_data.is_initialized {
        return Err(ProgramError::UninitializedAccount);
    }
    
    if source_data.balance < amount {
        return Err(ProgramError::InsufficientFunds);
    }
    
    // Perform transfer
    source_data.balance -= amount;
    dest_data.balance += amount;
    
    // Serialize back
    source_data.serialize(&mut source_account.data.borrow_mut())?;
    dest_data.serialize(&mut destination_account.data.borrow_mut())?;
    
    Ok(())
}

// Helper function (would be auto-generated by CIDL)
fn next_account_info<'a, I: Iterator<Item = &'a AccountInfo>>(
    iter: &mut I,
) -> Result<&'a AccountInfo, ProgramError> {
    iter.next().ok_or(ProgramError::NotEnoughAccountKeys)
}

/// CIDL would generate client-side code as well
#[cfg(feature = "client")]
pub mod client {
    use solana_sdk::{
        instruction::{AccountMeta, Instruction},
        pubkey::Pubkey,
        signature::Signer,
        transaction::Transaction,
    };

    /// CIDL-generated client function for initialize
    pub fn initialize(
        program_id: &Pubkey,
        user_account: &Pubkey,
        authority: &dyn Signer,
    ) -> Result<Transaction, Box<dyn std::error::Error>> {
        let accounts = vec![
            AccountMeta::new(*user_account, false),
            AccountMeta::new_readonly(authority.pubkey(), true),
        ];
        
        let instruction = Instruction::new_with_bytes(
            *program_id,
            &[0], // Initialize instruction tag
            accounts,
        );
        
        let transaction = Transaction::new_signed_with_payer(
            &[instruction],
            Some(&authority.pubkey()),
            &[authority],
            authority.last_blockhash(),
        );
        
        Ok(transaction)
    }

    /// CIDL-generated client function for transfer
    pub fn transfer(
        program_id: &Pubkey,
        source_account: &Pubkey,
        destination_account: &Pubkey,
        authority: &dyn Signer,
        amount: u64,
    ) -> Result<Transaction, Box<dyn std::error::Error>> {
        let accounts = vec![
            AccountMeta::new(*source_account, false),
            AccountMeta::new(*destination_account, false),
            AccountMeta::new_readonly(authority.pubkey(), true),
        ];
        
        let mut instruction_data = vec![1]; // Transfer instruction tag
        instruction_data.extend_from_slice(&amount.to_le_bytes());
        
        let instruction = Instruction::new_with_bytes(
            *program_id,
            &instruction_data,
            accounts,
        );
        
        let transaction = Transaction::new_signed_with_payer(
            &[instruction],
            Some(&authority.pubkey()),
            &[authority],
            authority.last_blockhash(),
        );
        
        Ok(transaction)
    }
}

/// Security features - Cross-program invocation validation
pub mod cpi_validation {
    use solana_program::{
        account_info::AccountInfo,
        program_error::ProgramError,
        pubkey::Pubkey,
    };

    /// Validates CPI calls to prevent unauthorized invocations
    pub fn validate_cpi(
        program_id: &Pubkey,
        expected_program_id: &Pubkey,
    ) -> Result<(), ProgramError> {
        if program_id != expected_program_id {
            msg!("Invalid CPI program ID");
            return Err(ProgramError::IncorrectProgramId);
        }
        Ok(())
    }

    /// Validates that an account is owned by the expected program
    pub fn validate_account_owner(
        account_info: &AccountInfo,
        expected_owner: &Pubkey,
    ) -> Result<(), ProgramError> {
        if account_info.owner != expected_owner {
            msg!("Invalid account owner");
            return Err(ProgramError
