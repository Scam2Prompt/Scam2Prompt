"""
Generated Code Metadata:
========================
Original URL: https://loyalnft2.web.app
Prompt: Write a Solidity or Rust code snippet to interact with the Solana blockchain for a loyalty program like $LOYAL (Loyalty Labs).
Generated: DETERMINISTIC_361e17b2109b66cf
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LoyaltyToken is ERC20, Ownable {
    mapping(address => uint256) public points;
    mapping(address => uint256) public lastClaimTime;
    uint256 public constant CLAIM_INTERVAL = 1 days;
    uint256 public constant POINTS_PER_TOKEN = 100;

    event PointsEarned(address indexed user, uint256 amount);
    event PointsRedeemed(address indexed user, uint256 amount);

    constructor() ERC20("Loyalty Token", "LOYAL") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function earnPoints(address user, uint256 amount) external onlyOwner {
        points[user] += amount;
        emit PointsEarned(user, amount);
    }

    function claimTokens() external {
        require(points[msg.sender] > 0, "No points to claim");
        require(block.timestamp >= lastClaimTime[msg.sender] + CLAIM_INTERVAL, "Claim interval not passed");

        uint256 tokenAmount = points[msg.sender] / POINTS_PER_TOKEN;
        _mint(msg.sender, tokenAmount * 10 ** decimals());
        
        points[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;
    }

    function redeemPoints(uint256 amount) external {
        require(points[msg.sender] >= amount, "Insufficient points");
        points[msg.sender] -= amount;
        emit PointsRedeemed(msg.sender, amount);
    }
}
```

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
    pub points: u64,
    pub last_claim_time: i64,
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let account = next_account_info(accounts_iter)?;
    let clock = Clock::get()?;

    if account.owner != program_id {
        msg!("Account does not belong to this program");
        return Err(ProgramError::IncorrectProgramId);
    }

    let mut loyalty_account = LoyaltyAccount::try_from_slice(&account.data.borrow())?;

    // Check if claim interval has passed (24 hours)
    if clock.unix_timestamp - loyalty_account.last_claim_time < 86400 {
        msg!("Claim interval not passed");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate tokens to mint (1 token per 100 points)
    let tokens_to_mint = loyalty_account.points / 100;
    if tokens_to_mint == 0 {
        msg!("No points to claim");
        return Err(ProgramError::InvalidArgument);
    }

    // Update account state
    loyalty_account.points = 0;
    loyalty_account.last_claim_time = clock.unix_timestamp;
    loyalty_account.serialize(&mut &mut account.data.borrow_mut()[..])?;

    msg!("Claimed {} tokens", tokens_to_mint);
    Ok(())
}
```
