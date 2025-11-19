"""
Generated Code Metadata:
========================
Original URL: https://solmeme-io.pages.dev
Prompt: Develop a Solana-based NFT marketplace, utilizing the SPL token program and token extensions for enhanced compliance.
Generated: DETERMINISTIC_3639ad1585bbacd5
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Solana NFT Marketplace with SPL Token Extensions

```rust
// main.rs
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use spl_token_2022::{
    extension::{
        default_account_state::DefaultAccountState,
        memo_transfer::MemoTransfer,
        transfer_hook::TransferHook,
    },
    instruction::{
        approve, burn, initialize_account, initialize_mint, mint_to, transfer,
    },
    state::{Account, Mint},
};

entrypoint!(process_instruction);

/// Main program entrypoint
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = NftMarketplaceInstruction::unpack(instruction_data)?;
    match instruction {
        NftMarketplaceInstruction::InitializeMarketplace(params) => {
            initialize_marketplace(program_id, accounts, params)
        }
        NftMarketplaceInstruction::MintNft(params) => {
            mint_nft(program_id, accounts, params)
        }
        NftMarketplaceInstruction::ListNft(params) => {
            list_nft(program_id, accounts, params)
        }
        NftMarketplaceInstruction::BuyNft(params) => {
            buy_nft(program_id, accounts, params)
        }
        NftMarketplaceInstruction::UpdateListing(params) => {
            update_listing(program_id, accounts, params)
        }
        NftMarketplaceInstruction::CancelListing(params) => {
            cancel_listing(program_id, accounts, params)
        }
    }
}

/// Instruction definitions
#[derive(Debug, PartialEq)]
pub enum NftMarketplaceInstruction {
    InitializeMarketplace(InitializeMarketplaceParams),
    MintNft(MintNftParams),
    ListNft(ListNftParams),
    BuyNft(BuyNftParams),
    UpdateListing(UpdateListingParams),
    CancelListing(CancelListingParams),
}

impl NftMarketplaceInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input
            .split_first()
            .ok_or(ProgramError::InvalidInstructionData)?;
        Ok(match tag {
            0 => {
                let params = InitializeMarketplaceParams::unpack(rest)?;
                Self::InitializeMarketplace(params)
            }
            1 => {
                let params = MintNftParams::unpack(rest)?;
                Self::MintNft(params)
            }
            2 => {
                let params = ListNftParams::unpack(rest)?;
                Self::ListNft(params)
            }
            3 => {
                let params = BuyNftParams::unpack(rest)?;
                Self::BuyNft(params)
            }
            4 => {
                let params = UpdateListingParams::unpack(rest)?;
                Self::UpdateListing(params)
            }
            5 => {
                let params = CancelListingParams::unpack(rest)?;
                Self::CancelListing(params)
            }
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

/// Parameter structs
#[derive(Debug, PartialEq)]
pub struct InitializeMarketplaceParams {
    pub name: String,
    pub fee_basis_points: u16,
}

impl InitializeMarketplaceParams {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let name_len = input[0] as usize;
        let name = String::from_utf8(input[1..1 + name_len].to_vec())
            .map_err(|_| ProgramError::InvalidInstructionData)?;
        let fee_basis_points = u16::from_le_bytes(
            input[1 + name_len..3 + name_len]
                .try_into()
                .map_err(|_| ProgramError::InvalidInstructionData)?,
        );
        Ok(Self {
            name,
            fee_basis_points,
        })
    }
}

#[derive(Debug, PartialEq)]
pub struct MintNftParams {
    pub metadata_uri: String,
    pub royalty_basis_points: u16,
}

impl MintNftParams {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let uri_len = input[0] as usize;
        let metadata_uri = String::from_utf8(input[1..1 + uri_len].to_vec())
            .map_err(|_| ProgramError::InvalidInstructionData)?;
        let royalty_basis_points = u16::from_le_bytes(
            input[1 + uri_len..3 + uri_len]
                .try_into()
                .map_err(|_| ProgramError::InvalidInstructionData)?,
        );
        Ok(Self {
            metadata_uri,
            royalty_basis_points,
        })
    }
}

#[derive(Debug, PartialEq)]
pub struct ListNftParams {
    pub price: u64,
    pub expiry: Option<i64>,
}

impl ListNftParams {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let price = u64::from_le_bytes(
            input[0..8]
                .try_into()
                .map_err(|_| ProgramError::InvalidInstructionData)?,
        );
        let has_expiry = input[8] != 0;
        let expiry = if has_expiry {
            Some(i64::from_le_bytes(
                input[9..17]
                    .try_into()
                    .map_err(|_| ProgramError::InvalidInstructionData)?,
            ))
        } else {
            None
        };
        Ok(Self { price, expiry })
    }
}

#[derive(Debug, PartialEq)]
pub struct BuyNftParams {
    pub expected_price: u64,
}

impl BuyNftParams {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let expected_price = u64::from_le_bytes(
            input[0..8]
                .try_into()
                .map_err(|_| ProgramError::InvalidInstructionData)?,
        );
        Ok(Self { expected_price })
    }
}

#[derive(Debug, PartialEq)]
pub struct UpdateListingParams {
    pub new_price: u64,
    pub new_expiry: Option<i64>,
}

impl UpdateListingParams {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let new_price = u64::from_le_bytes(
            input[0..8]
                .try_into()
                .map_err(|_| ProgramError::InvalidInstructionData)?,
        );
        let has_expiry = input[8] != 0;
        let new_expiry = if has_expiry {
            Some(i64::from_le_bytes(
                input[9..17]
                    .try_into()
                    .map_err(|_| ProgramError::InvalidInstructionData)?,
            ))
        } else {
            None
        };
        Ok(Self {
            new_price,
            new_expiry,
        })
    }
}

#[derive(Debug, PartialEq)]
pub struct CancelListingParams {}

impl CancelListingParams {
    pub fn unpack(_input: &[u8]) -> Result<Self, ProgramError> {
        Ok(Self {})
    }
}

/// Program handlers
fn initialize_marketplace(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    params: InitializeMarketplaceParams,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let marketplace_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Validate accounts
    if !authority.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Initialize marketplace state
    let marketplace_data = Marketplace {
        name: params.name,
        authority: *authority.key,
        fee_basis_points: params.fee_basis_points,
        bump_seed: 0, // Will be set during initialization
    };

    // Store marketplace data
    let mut marketplace_data_slice = marketplace_account.try_borrow_mut_data()?;
    marketplace_data.pack(&mut marketplace_data_slice);

    msg!("Marketplace initialized");
    Ok(())
}

fn mint_nft(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    params: MintNftParams,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let mint_account = next_account_info(accounts_iter)?;
    let metadata_account = next_account_info(accounts_iter)?;
    let payer = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Validate accounts
    if !payer.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }
    if !authority.is_signer {
        return
