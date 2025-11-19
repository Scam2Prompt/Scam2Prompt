"""
Generated Code Metadata:
========================
Original URL: https://devnet-directory-one.vercel.app
Prompt: What are some best practices for creating and managing Dev Card NFTs on Solana, similar to those used in the Devnet Directory application?
Generated: DETERMINISTIC_f8dce13d9b202719
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solana program (Rust) for creating and managing Dev Card NFTs, following best practices:

```rust
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    system_instruction,
    sysvar::{clock::Clock, rent::Rent, Sysvar},
};
use spl_token::state::Account as TokenAccount;
use spl_token_2022::{
    extension::ExtensionType,
    instruction::{initialize_mint, mint_to},
    state::Mint,
};

// Program ID constant
pub const PROGRAM_ID: &str = "YourProgramIDHere";

// Dev Card structure
#[derive(Debug)]
pub struct DevCard {
    pub owner: Pubkey,
    pub username: String,
    pub skills: Vec<String>,
    pub mint: Pubkey,
    pub metadata: Pubkey,
}

// Instruction enum
pub enum DevCardInstruction {
    CreateDevCard {
        username: String,
        skills: Vec<String>,
    },
    UpdateDevCard {
        username: Option<String>,
        skills: Option<Vec<String>>,
    },
}

impl DevCardInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        Ok(match tag {
            0 => {
                let (username_len, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                let username = String::from_utf8(rest[..*username_len as usize].to_vec())
                    .map_err(|_| ProgramError::InvalidInstructionData)?;
                let rest = &rest[*username_len as usize..];
                let (skills_len, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                let mut skills = Vec::new();
                let mut offset = 0;
                for _ in 0..*skills_len {
                    let (skill_len, rest_skill) = rest[offset..].split_first().ok_or(ProgramError::InvalidInstructionData)?;
                    let skill = String::from_utf8(rest_skill[..*skill_len as usize].to_vec())
                        .map_err(|_| ProgramError::InvalidInstructionData)?;
                    skills.push(skill);
                    offset += 1 + *skill_len as usize;
                }
                Self::CreateDevCard { username, skills }
            }
            1 => {
                let (username_flag, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                let username = if *username_flag == 1 {
                    let (username_len, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                    let username = String::from_utf8(rest[..*username_len as usize].to_vec())
                        .map_err(|_| ProgramError::InvalidInstructionData)?;
                    Some(username)
                } else {
                    None
                };
                let rest = if *username_flag == 1 {
                    &rest[1 + username.as_ref().unwrap().len()..]
                } else {
                    rest
                };
                let (skills_flag, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                let skills = if *skills_flag == 1 {
                    let (skills_len, rest) = rest.split_first().ok_or(ProgramError::InvalidInstructionData)?;
                    let mut skills = Vec::new();
                    let mut offset = 0;
                    for _ in 0..*skills_len {
                        let (skill_len, rest_skill) = rest[offset..].split_first().ok_or(ProgramError::InvalidInstructionData)?;
                        let skill = String::from_utf8(rest_skill[..*skill_len as usize].to_vec())
                            .map_err(|_| ProgramError::InvalidInstructionData)?;
                        skills.push(skill);
                        offset += 1 + *skill_len as usize;
                    }
                    Some(skills)
                } else {
                    None
                };
                Self::UpdateDevCard { username, skills }
            }
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

// Entrypoint
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = DevCardInstruction::unpack(instruction_data)?;

    match instruction {
        DevCardInstruction::CreateDevCard { username, skills } => {
            create_dev_card(program_id, accounts, username, skills)
        }
        DevCardInstruction::UpdateDevCard { username, skills } => {
            update_dev_card(program_id, accounts, username, skills)
        }
    }
}

fn create_dev_card(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    username: String,
    skills: Vec<String>,
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    
    // Accounts expected:
    // 0. Payer
    // 1. Mint account
    // 2. Token account
    // 3. Metadata account
    // 4. System program
    // 5. Token program
    // 6. Rent sysvar
    
    let payer = next_account_info(account_info_iter)?;
    let mint_account = next_account_info(account_info_iter)?;
    let token_account = next_account_info(account_info_iter)?;
    let metadata_account = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let rent_sysvar = next_account_info(account_info_iter)?;
    
    // Verify program ownership
    if !payer.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }
    
    // Initialize mint
    let mint_authority = Pubkey::new_unique();
    let freeze_authority = Some(mint_authority);
    
    let rent = Rent::get()?;
    let mint_space = ExtensionType::get_account_len::<Mint>(&[ExtensionType::MintCloseAuthority]);
    let mint_lamports = rent.minimum_balance(mint_space);
    
    invoke_signed(
        &system_instruction::create_account(
            payer.key,
            mint_account.key,
            mint_lamports,
            mint_space as u64,
            token_program.key,
        ),
        &[payer.clone(), mint_account.clone(), system_program.clone()],
        &[],
    )?;
    
    invoke_signed(
        &initialize_mint(
            token_program.key,
            mint_account.key,
            &mint_authority,
            freeze_authority,
            0,
        )?,
        &[mint_account.clone(), token_program.clone()],
        &[],
    )?;
    
    // Create token account
    let token_space = Account::LEN;
    let token_lamports = rent.minimum_balance(token_space);
    
    invoke_signed(
        &system_instruction::create_account(
            payer.key,
            token_account.key,
            token_lamports,
            token_space as u64,
            token_program.key,
        ),
        &[payer.clone(), token_account.clone(), system_program.clone()],
        &[],
    )?;
    
    invoke_signed(
        &initialize_account(
            token_program.key,
            token_account.key,
            mint_account.key,
            payer.key,
        )?,
        &[token_account.clone(), mint_account.clone(), payer.clone(), token_program.clone()],
        &[],
    )?;
    
    // Mint token
    invoke_signed(
        &mint_to(
            token_program.key,
            mint_account.key,
            token_account.key,
            &mint_authority,
            &[],
            1,
        )?,
        &[
            mint_account.clone(),
            token_account.clone(),
            mint_authority_account.clone(),
            token_program.clone(),
        ],
        &[],
    )?;
    
    // Store metadata
    let dev_card = DevCard {
        owner: *payer.key,
        username,
        skills,
        mint: *mint_account.key,
        metadata: *metadata_account.key,
    };
    
    // Serialize and store dev card data in metadata account
    let mut metadata_data = metadata_account.try_borrow_mut_data()?;
    bincode::serialize_into(&mut *metadata_data, &dev_card)
        .map_err(|_| ProgramError::InvalidAccountData)?;
    
    Ok(())
}

fn update_dev_card(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    username: Option<String>,
    skills: Option<Vec<String>>,
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    
    // Accounts expected:
    // 0. Payer
    // 1. Metadata account
    // 2. Mint account
    
    let payer = next_account_info(account_info_iter)?;
    let metadata_account = next_account_info(account_info_iter)?;
    let mint_account =
