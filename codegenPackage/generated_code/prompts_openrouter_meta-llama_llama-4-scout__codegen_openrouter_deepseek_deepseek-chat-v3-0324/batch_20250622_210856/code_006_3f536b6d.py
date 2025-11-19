"""
Generated Code Metadata:
========================
Original URL: https://holddao.web.app
Prompt: Develop a smart contract on Solana to create, buy, and sell NFTs, considering the features and functionalities observed on https://holddao.web.app.
Generated: DETERMINISTIC_3f536b6d457a83a1
Batch ID: 20250622_210856
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
    system_instruction,
    sysvar::{rent::Rent, Sysvar},
};
use borsh::{BorshDeserialize, BorshSerialize};
use spl_token::state::Account as TokenAccount;

// Define the program ID
solana_program::declare_id!("NFTProgram111111111111111111111111111111111");

// NFT Metadata structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct NFTMetadata {
    pub name: String,
    pub symbol: String,
    pub uri: String, // Link to off-chain metadata
    pub seller_fee_basis_points: u16,
    pub creators: Vec<Creator>,
    pub primary_sale_happened: bool,
    pub is_mutable: bool,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Creator {
    pub address: Pubkey,
    pub verified: bool,
    pub share: u8,
}

// NFT structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct NFT {
    pub metadata: NFTMetadata,
    pub owner: Pubkey,
    pub price: u64,
    pub for_sale: bool,
}

// Instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum NFTInstruction {
    CreateNFT {
        name: String,
        symbol: String,
        uri: String,
        seller_fee_basis_points: u16,
        creators: Vec<Creator>,
    },
    BuyNFT {
        price: u64,
    },
    SellNFT {
        price: u64,
    },
    UpdateNFT {
        new_uri: String,
        is_mutable: bool,
    },
}

// Entry point
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = NFTInstruction::try_from_slice(instruction_data)?;

    match instruction {
        NFTInstruction::CreateNFT {
            name,
            symbol,
            uri,
            seller_fee_basis_points,
            creators,
        } => create_nft(
            program_id,
            accounts,
            name,
            symbol,
            uri,
            seller_fee_basis_points,
            creators,
        ),
        NFTInstruction::BuyNFT { price } => buy_nft(program_id, accounts, price),
        NFTInstruction::SellNFT { price } => sell_nft(program_id, accounts, price),
        NFTInstruction::UpdateNFT { new_uri, is_mutable } => {
            update_nft(program_id, accounts, new_uri, is_mutable)
        }
    }
}

fn create_nft(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    name: String,
    symbol: String,
    uri: String,
    seller_fee_basis_points: u16,
    creators: Vec<Creator>,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let payer = next_account_info(accounts_iter)?;
    let nft_account = next_account_info(accounts_iter)?;
    let mint_account = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let rent = &Rent::from_account_info(next_account_info(accounts_iter)?)?;
    let system_program = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Check if the program owns the NFT account
    if nft_account.owner != program_id {
        msg!("NFT account does not have the correct program owner");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Create NFT metadata
    let metadata = NFTMetadata {
        name,
        symbol,
        uri,
        seller_fee_basis_points,
        creators,
        primary_sale_happened: false,
        is_mutable: true,
    };

    // Create NFT
    let nft = NFT {
        metadata,
        owner: *payer.key,
        price: 0,
        for_sale: false,
    };

    // Serialize and store NFT
    nft.serialize(&mut &mut nft_account.data.borrow_mut()[..])?;

    Ok(())
}

fn buy_nft(program_id: &Pubkey, accounts: &[AccountInfo], price: u64) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let buyer = next_account_info(accounts_iter)?;
    let seller = next_account_info(accounts_iter)?;
    let nft_account = next_account_info(accounts_iter)?;
    let buyer_token_account = next_account_info(accounts_iter)?;
    let seller_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Deserialize NFT
    let mut nft = NFT::try_from_slice(&nft_account.data.borrow())?;

    // Check if NFT is for sale
    if !nft.for_sale {
        msg!("NFT is not for sale");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if price matches
    if nft.price != price {
        msg!("Price does not match");
        return Err(ProgramError::InvalidArgument);
    }

    // Transfer funds
    let transfer_instruction = system_instruction::transfer(
        buyer.key,
        seller.key,
        price,
    );
    solana_program::program::invoke(
        &transfer_instruction,
        &[
            buyer.clone(),
            seller.clone(),
        ],
    )?;

    // Update NFT ownership
    nft.owner = *buyer.key;
    nft.for_sale = false;
    nft.metadata.primary_sale_happened = true;
    nft.serialize(&mut &mut nft_account.data.borrow_mut()[..])?;

    Ok(())
}

fn sell_nft(program_id: &Pubkey, accounts: &[AccountInfo], price: u64) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let owner = next_account_info(accounts_iter)?;
    let nft_account = next_account_info(accounts_iter)?;

    // Deserialize NFT
    let mut nft = NFT::try_from_slice(&nft_account.data.borrow())?;

    // Check ownership
    if nft.owner != *owner.key {
        msg!("Only the owner can sell the NFT");
        return Err(ProgramError::InvalidAccountData);
    }

    // Update NFT sale status
    nft.price = price;
    nft.for_sale = true;
    nft.serialize(&mut &mut nft_account.data.borrow_mut()[..])?;

    Ok(())
}

fn update_nft(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    new_uri: String,
    is_mutable: bool,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let owner = next_account_info(accounts_iter)?;
    let nft_account = next_account_info(accounts_iter)?;

    // Deserialize NFT
    let mut nft = NFT::try_from_slice(&nft_account.data.borrow())?;

    // Check ownership
    if nft.owner != *owner.key {
        msg!("Only the owner can update the NFT");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if NFT is mutable
    if !nft.metadata.is_mutable {
        msg!("NFT metadata is immutable");
        return Err(ProgramError::InvalidAccountData);
    }

    // Update NFT metadata
    nft.metadata.uri = new_uri;
    nft.metadata.is_mutable = is_mutable;
    nft.serialize(&mut &mut nft_account.data.borrow_mut()[..])?;

    Ok(())
}
```
