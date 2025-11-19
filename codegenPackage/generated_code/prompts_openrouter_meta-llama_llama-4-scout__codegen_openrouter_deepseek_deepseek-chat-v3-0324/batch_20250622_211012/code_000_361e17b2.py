"""
Generated Code Metadata:
========================
Original URL: https://loyalnft3.web.app
Prompt: Write a Solidity or Rust code snippet to interact with the Solana blockchain for a loyalty program like $LOYAL (Loyalty Labs).
Generated: DETERMINISTIC_361e17b2109b66cf
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract for a loyalty program on Ethereum (since Solidity is primarily for Ethereum, not Solana). For Solana, I'll provide a Rust program next.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LoyaltyToken
 * @dev ERC20 token for a loyalty rewards program
 */
contract LoyaltyToken is ERC20, Ownable {
    mapping(address => bool) public merchants;
    mapping(address => uint256) public pointsEarned;
    mapping(address => uint256) public pointsRedeemed;

    event MerchantAdded(address indexed merchant);
    event MerchantRemoved(address indexed merchant);
    event PointsEarned(address indexed user, uint256 amount);
    event PointsRedeemed(address indexed user, uint256 amount);

    /**
     * @dev Constructor that initializes the token
     */
    constructor() ERC20("Loyalty Token", "LOYAL") {
        _mint(msg.sender, 1000000 * 10**decimals()); // Initial supply
    }

    /**
     * @dev Add a merchant who can award points
     * @param merchant Address of the merchant to add
     */
    function addMerchant(address merchant) external onlyOwner {
        merchants[merchant] = true;
        emit MerchantAdded(merchant);
    }

    /**
     * @dev Remove a merchant
     * @param merchant Address of the merchant to remove
     */
    function removeMerchant(address merchant) external onlyOwner {
        merchants[merchant] = false;
        emit MerchantRemoved(merchant);
    }

    /**
     * @dev Award points to a customer
     * @param customer Address of the customer
     * @param amount Amount of points to award
     */
    function earnPoints(address customer, uint256 amount) external {
        require(merchants[msg.sender], "Only merchants can award points");
        pointsEarned[customer] += amount;
        _mint(customer, amount);
        emit PointsEarned(customer, amount);
    }

    /**
     * @dev Redeem points from a customer
     * @param amount Amount of points to redeem
     */
    function redeemPoints(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient points");
        pointsRedeemed[msg.sender] += amount;
        _burn(msg.sender, amount);
        emit PointsRedeemed(msg.sender, amount);
    }
}
```

And here's a Rust program for Solana:

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
use borsh::{BorshDeserialize, BorshSerialize};

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct LoyaltyAccount {
    pub points_earned: u64,
    pub points_redeemed: u64,
    pub is_merchant: bool,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum LoyaltyInstruction {
    Initialize,
    AddMerchant,
    RemoveMerchant,
    EarnPoints { amount: u64 },
    RedeemPoints { amount: u64 },
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = LoyaltyInstruction::try_from_slice(instruction_data)?;
    
    match instruction {
        LoyaltyInstruction::Initialize => initialize(program_id, accounts),
        LoyaltyInstruction::AddMerchant => add_merchant(program_id, accounts),
        LoyaltyInstruction::RemoveMerchant => remove_merchant(program_id, accounts),
        LoyaltyInstruction::EarnPoints { amount } => earn_points(program_id, accounts, amount),
        LoyaltyInstruction::RedeemPoints { amount } => redeem_points(program_id, accounts, amount),
    }
}

fn initialize(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let loyalty_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    
    if loyalty_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }
    
    let mut account_data = LoyaltyAccount::try_from_slice(&loyalty_account.data.borrow())?;
    account_data.points_earned = 0;
    account_data.points_redeemed = 0;
    account_data.is_merchant = false;
    
    account_data.serialize(&mut &mut loyalty_account.data.borrow_mut()[..])?;
    Ok(())
}

fn add_merchant(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let loyalty_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    
    if !authority.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }
    
    let mut account_data = LoyaltyAccount::try_from_slice(&loyalty_account.data.borrow())?;
    account_data.is_merchant = true;
    
    account_data.serialize(&mut &mut loyalty_account.data.borrow_mut()[..])?;
    Ok(())
}

fn remove_merchant(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let loyalty_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;
    
    if !authority.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }
    
    let mut account_data = LoyaltyAccount::try_from_slice(&loyalty_account.data.borrow())?;
    account_data.is_merchant = false;
    
    account_data.serialize(&mut &mut loyalty_account.data.borrow_mut()[..])?;
    Ok(())
}

fn earn_points(program_id: &Pubkey, accounts: &[AccountInfo], amount: u64) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let merchant_account = next_account_info(accounts_iter)?;
    let customer_account = next_account_info(accounts_iter)?;
    
    let merchant_data = LoyaltyAccount::try_from_slice(&merchant_account.data.borrow())?;
    if !merchant_data.is_merchant {
        return Err(ProgramError::InvalidAccountData);
    }
    
    let mut customer_data = LoyaltyAccount::try_from_slice(&customer_account.data.borrow())?;
    customer_data.points_earned += amount;
    
    customer_data.serialize(&mut &mut customer_account.data.borrow_mut()[..])?;
    Ok(())
}

fn redeem_points(program_id: &Pubkey, accounts: &[AccountInfo], amount: u64) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let customer_account = next_account_info(accounts_iter)?;
    
    let mut customer_data = LoyaltyAccount::try_from_slice(&customer_account.data.borrow())?;
    if customer_data.points_earned - customer_data.points_redeemed < amount {
        return Err(ProgramError::InsufficientFunds);
    }
    
    customer_data.points_redeemed += amount;
    customer_data.serialize(&mut &mut customer_account.data.borrow_mut()[..])?;
    Ok(())
}
```
