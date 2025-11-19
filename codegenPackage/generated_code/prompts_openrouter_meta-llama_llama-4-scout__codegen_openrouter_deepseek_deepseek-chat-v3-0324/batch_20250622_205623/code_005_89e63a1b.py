"""
Generated Code Metadata:
========================
Original URL: https://wenwencoins.web.app
Prompt: Create an open-source NFT standard, like Wen's WNS, for community expansion on Solana.
Generated: DETERMINISTIC_89e63a1b8546be68
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Solana Community NFT Standard (SCNS)
//! A flexible NFT standard for community expansion on Solana.

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
use borsh::{BorshDeserialize, BorshSerialize};

/// Program ID for the SCNS program
pub const SCNS_PROGRAM_ID: &str = "SCNS1111111111111111111111111111111111111";

/// Maximum length of community metadata URI
pub const MAX_URI_LENGTH: usize = 200;

/// NFT state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Nft {
    /// Mint authority
    pub mint_authority: Pubkey,
    /// Current owner
    pub owner: Pubkey,
    /// Community ID this NFT belongs to
    pub community_id: Pubkey,
    /// Metadata URI
    pub uri: String,
    /// Royalty basis points (0-10000)
    pub royalty_basis_points: u16,
    /// Creation timestamp
    pub created_at: i64,
    /// Is burned
    pub burned: bool,
}

/// Community state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Community {
    /// Community admin
    pub admin: Pubkey,
    /// Community name
    pub name: String,
    /// Community symbol
    pub symbol: String,
    /// Total NFTs minted
    pub total_minted: u64,
    /// Total NFTs burned
    pub total_burned: u64,
    /// Royalty basis points (0-10000)
    pub default_royalty_basis_points: u16,
    /// Is frozen (prevents further modifications)
    pub is_frozen: bool,
}

/// Instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum ScnsInstruction {
    /// Initialize a new community
    /// Accounts expected:
    /// 0. [signer] Admin account
    /// 1. [writable] Community account
    /// 2. [] Rent sysvar
    /// 3. [] System program
    InitializeCommunity {
        name: String,
        symbol: String,
        default_royalty_basis_points: u16,
    },

    /// Mint a new NFT
    /// Accounts expected:
    /// 0. [signer] Admin account
    /// 1. [writable] NFT account
    /// 2. [writable] Community account
    /// 3. [writable] Owner account
    /// 4. [] Rent sysvar
    /// 5. [] System program
    MintNft {
        uri: String,
        royalty_basis_points: Option<u16>,
    },

    /// Transfer NFT ownership
    /// Accounts expected:
    /// 0. [signer] Current owner
    /// 1. [writable] NFT account
    /// 2. [writable] New owner account
    TransferNft,

    /// Burn an NFT
    /// Accounts expected:
    /// 0. [signer] Owner
    /// 1. [writable] NFT account
    /// 2. [writable] Community account
    BurnNft,

    /// Update community settings
    /// Accounts expected:
    /// 0. [signer] Admin
    /// 1. [writable] Community account
    UpdateCommunity {
        name: Option<String>,
        symbol: Option<String>,
        default_royalty_basis_points: Option<u16>,
    },

    /// Freeze community (prevents further modifications)
    /// Accounts expected:
    /// 0. [signer] Admin
    /// 1. [writable] Community account
    FreezeCommunity,
}

/// Entrypoint for SCNS program
entrypoint!(process_instruction);

/// Program entrypoint implementation
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("SCNS program entrypoint");

    // Deserialize instruction
    let instruction = ScnsInstruction::try_from_slice(instruction_data)?;

    match instruction {
        ScnsInstruction::InitializeCommunity {
            name,
            symbol,
            default_royalty_basis_points,
        } => initialize_community(program_id, accounts, name, symbol, default_royalty_basis_points),
        ScnsInstruction::MintNft {
            uri,
            royalty_basis_points,
        } => mint_nft(program_id, accounts, uri, royalty_basis_points),
        ScnsInstruction::TransferNft => transfer_nft(program_id, accounts),
        ScnsInstruction::BurnNft => burn_nft(program_id, accounts),
        ScnsInstruction::UpdateCommunity {
            name,
            symbol,
            default_royalty_basis_points,
        } => update_community(program_id, accounts, name, symbol, default_royalty_basis_points),
        ScnsInstruction::FreezeCommunity => freeze_community(program_id, accounts),
    }
}

/// Initialize a new community
fn initialize_community(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    name: String,
    symbol: String,
    default_royalty_basis_points: u16,
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let admin = next_account_info(account_info_iter)?;
    let community_account = next_account_info(account_info_iter)?;
    let rent_sysvar = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Validate admin is signer
    if !admin.is_signer {
        msg!("Admin must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Validate royalty basis points
    if default_royalty_basis_points > 10000 {
        msg!("Royalty basis points must be <= 10000");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate required rent
    let rent = &Rent::from_account_info(rent_sysvar)?;
    let required_lamports = rent.minimum_balance(Community::LEN);

    // Create community account
    invoke_signed(
        &system_instruction::create_account(
            admin.key,
            community_account.key,
            required_lamports,
            Community::LEN as u64,
            program_id,
        ),
        &[
            admin.clone(),
            community_account.clone(),
            system_program.clone(),
        ],
        &[],
    )?;

    // Initialize community data
    let community = Community {
        admin: *admin.key,
        name,
        symbol,
        total_minted: 0,
        total_burned: 0,
        default_royalty_basis_points,
        is_frozen: false,
    };

    community.serialize(&mut &mut community_account.data.borrow_mut()[..])?;

    Ok(())
}

/// Mint a new NFT
fn mint_nft(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    uri: String,
    royalty_basis_points: Option<u16>,
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let admin = next_account_info(account_info_iter)?;
    let nft_account = next_account_info(account_info_iter)?;
    let community_account = next_account_info(account_info_iter)?;
    let owner = next_account_info(account_info_iter)?;
    let rent_sysvar = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;

    // Validate admin is signer
    if !admin.is_signer {
        msg!("Admin must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Validate URI length
    if uri.len() > MAX_URI_LENGTH {
        msg!("URI too long");
        return Err(ProgramError::InvalidArgument);
    }

    // Load community data
    let mut community = Community::try_from_slice(&community_account.data.borrow())?;

    // Validate community admin
    if community.admin != *admin.key {
        msg!("Invalid community admin");
        return Err(ProgramError::IllegalOwner);
    }

    // Validate community is not frozen
    if community.is_frozen {
        msg!("Community is frozen");
        return Err(ProgramError::InvalidAccountData);
    }

    // Use provided royalty or community default
    let royalty = royalty_basis_points.unwrap_or(community.default_royalty_basis_points);
    if royalty > 10000 {
        msg!("Royalty basis points must be <= 10000");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate required rent
    let rent = &Rent::from_account_info(rent_sysvar)?;
    let required_lamports = rent.minimum_balance(Nft::LEN);

    // Create NFT account
    invoke_signed(
        &system_instruction::create_account(
            admin.key,
            nft_account
