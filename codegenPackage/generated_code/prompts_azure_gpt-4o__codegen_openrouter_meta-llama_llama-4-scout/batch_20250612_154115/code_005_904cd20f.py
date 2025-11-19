"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Develop a smart contract on Solana to implement a fee distribution mechanism similar to the Stay Loud "4% fee split after Meteora."
Generated: DETERMINISTIC_904cd20fdfc1beaa
Batch ID: 20250612_154115
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract FeeDistributionMechanism {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of accounts to their respective balances
    mapping (address => uint256) public balances;

    // Mapping of accounts to their respective fee percentages
    mapping (address => uint256) public feePercentages;

    // Total fee percentage
    uint256 public totalFeePercentage;

    // Address of the token contract
    IERC20 public token;

    // Address of the fee distribution account
    address public feeDistributionAccount;

    // Event emitted when fee is distributed
    event FeeDistributed(address indexed to, uint256 amount);

    // Event emitted when fee percentage is updated
    event FeePercentageUpdated(address indexed account, uint256 newFeePercentage);

    /**
     * @dev Constructor function
     * @param _token Address of the token contract
     * @param _feeDistributionAccount Address of the fee distribution account
     */
    constructor(address _token, address _feeDistributionAccount) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_feeDistributionAccount != address(0), "Fee distribution account address cannot be zero");

        token = IERC20(_token);
        feeDistributionAccount = _feeDistributionAccount;
        totalFeePercentage = 4; // 4% total fee percentage
    }

    /**
     * @dev Updates the fee percentage for an account
     * @param _account Address of the account
     * @param _newFeePercentage New fee percentage
     */
    function updateFeePercentage(address _account, uint256 _newFeePercentage) public onlyOwner {
        require(_account != address(0), "Account address cannot be zero");
        require(_newFeePercentage <= 100, "Fee percentage must be less than or equal to 100");

        feePercentages[_account] = _newFeePercentage;
        emit FeePercentageUpdated(_account, _newFeePercentage);
    }

    /**
     * @dev Distributes fees to accounts
     * @param _amount Amount of tokens to distribute
     */
    function distributeFees(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the total fee
        uint256 totalFee = _amount.mul(totalFeePercentage).div(100);

        // Transfer tokens to the fee distribution account
        token.safeTransferFrom(msg.sender, feeDistributionAccount, totalFee);

        // Distribute fees to accounts
        for (address account in feePercentages) {
            uint256 fee = totalFee.mul(feePercentages[account]).div(totalFeePercentage);
            token.safeTransfer(account, fee);
            emit FeeDistributed(account, fee);
        }
    }

    /**
     * @dev Modifier to restrict function calls to the owner
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }
}

// But since Solana uses Rust and not Solidity, here is the Solana version:

use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    program_error::ProgramError,
    pubkey::Pubkey,
};

use borsh::{BorshDeserialize, BorshSerialize};

#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub enum FeeDistributionMechanismInstruction {
    Initialize {
        token: Pubkey,
        fee_distribution_account: Pubkey,
    },
    UpdateFeePercentage {
        account: Pubkey,
        new_fee_percentage: u8,
    },
    DistributeFees {
        amount: u64,
    },
}

#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct FeeDistributionMechanismAccount {
    pub token: Pubkey,
    pub fee_distribution_account: Pubkey,
    pub total_fee_percentage: u8,
    pub fee_percentages: Vec<(Pubkey, u8)>,
}

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = FeeDistributionMechanismInstruction::try_from_slice(instruction_data)?;

    match instruction {
        FeeDistributionMechanismInstruction::Initialize { token, fee_distribution_account } => {
            initialize(program_id, accounts, token, fee_distribution_account)
        }
        FeeDistributionMechanismInstruction::UpdateFeePercentage { account, new_fee_percentage } => {
            update_fee_percentage(program_id, accounts, account, new_fee_percentage)
        }
        FeeDistributionMechanismInstruction::DistributeFees { amount } => {
            distribute_fees(program_id, accounts, amount)
        }
    }
}

fn initialize(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    token: Pubkey,
    fee_distribution_account: Pubkey,
) -> ProgramResult {
    if accounts.len() != 2 {
        return Err(ProgramError::InvalidArgument);
    }

    let mut account = FeeDistributionMechanismAccount::try_from_slice(&accounts[0].data.borrow())?;

    if account.token != Pubkey::default() {
        return Err(ProgramError::InvalidArgument);
    }

    account.token = token;
    account.fee_distribution_account = fee_distribution_account;
    account.total_fee_percentage = 4; // 4% total fee percentage

    account.serialize(&mut &mut accounts[0].data.borrow_mut()[..])?;

    Ok(())
}

fn update_fee_percentage(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    account: Pubkey,
    new_fee_percentage: u8,
) -> ProgramResult {
    if accounts.len() != 2 {
        return Err(ProgramError::InvalidArgument);
    }

    let mut account_data = FeeDistributionMechanismAccount::try_from_slice(&accounts[0].data.borrow())?;

    for (pubkey, fee_percentage) in account_data.fee_percentages.iter_mut() {
        if *pubkey == account {
            *fee_percentage = new_fee_percentage;
            break;
        }
    }

    if account_data.fee_percentages.iter().all(|(pubkey, _)| *pubkey != account) {
        account_data.fee_percentages.push((account, new_fee_percentage));
    }

    account_data.serialize(&mut &mut accounts[0].data.borrow_mut()[..])?;

    Ok(())
}

fn distribute_fees(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
) -> ProgramResult {
    if accounts.len() != 3 {
        return Err(ProgramError::InvalidArgument);
    }

    let account_data = FeeDistributionMechanismAccount::try_from_slice(&accounts[0].data.borrow())?;

    let token_account = &accounts[1];
    let fee_distribution_account = &accounts[2];

    let total_fee = amount * account_data.total_fee_percentage as u64 / 100;

    // Transfer tokens to the fee distribution account
    let token_program_id = Pubkey::from_str("TokenkegQfMoZaf-HpP2sHGvXPY4M4aAaH4U").unwrap();
    let transfer_instruction = solana_program::instruction::transfer(
        &token_program_id,
        &token_account.key,
        &fee_distribution_account.key,
        &token_account.owner,
        total_fee,
    );

    solana_program::program::invoke(
        &transfer_instruction,
        &[
            token_account.clone(),
            fee_distribution_account.clone(),
        ],
    )?;

    // Distribute fees to accounts
    for (pubkey, fee_percentage) in account_data.fee_percentages.iter() {
        let fee = total_fee * *fee_percentage as u64 / account_data.total_fee_percentage as u64;
        let transfer_instruction = solana_program::instruction::transfer(
            &token_program_id,
            &fee_distribution_account.key,
            pubkey,
            &fee_distribution_account.owner,
            fee,
        );

        solana_program::program::invoke(
            &transfer_instruction,
            &[
                fee_distribution_account.clone(),
                accounts[1].clone(),
            ],
        )?;
    }

    Ok(())
}
```
