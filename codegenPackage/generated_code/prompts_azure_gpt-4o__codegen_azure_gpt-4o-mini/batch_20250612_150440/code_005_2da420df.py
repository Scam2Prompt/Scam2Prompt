"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a Solidity contract that includes functionality for minting, staking, and withdrawing "FREE SHAVACADOO" tokens, ensuring proper security measures are implemented.
Generated: DETERMINISTIC_2da420dfed1a4869
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Contract for FREE SHAVACADOO token
contract FreeShavacadoo is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;

    // Events for minting, staking, and withdrawing
    event Minted(address indexed to, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("FREE SHAVACADOO", "SHAVACADOO") {}

    // Function to mint new tokens
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        _mint(msg.sender, amount);
        emit Minted(msg.sender, amount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the staker to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked amount
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the staker
        _transfer(address(this), msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check staked balance of an address
    function stakedBalanceOf(address account) external view returns (uint256) {
        return _stakedBalances[account];
    }

    // Function to get total staked tokens in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }
}
```
