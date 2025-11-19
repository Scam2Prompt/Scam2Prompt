"""
Generated Code Metadata:
========================
Original URL: https://lombardfinance.online
Prompt: "Generate a smart contract code snippet for a DeFi product similar to Bitcoin Bera Vault, incorporating risk management for smart contract and economic risks."
Generated: DETERMINISTIC_986993cadce9bbff
Batch ID: 20250622_212519
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeFi Vault Contract
 * @dev This contract allows users to deposit and withdraw tokens while implementing risk management strategies.
 */
contract DeFiVault is Ownable, ReentrancyGuard {
    // Token to be managed by the vault
    IERC20 public immutable token;

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Total amount of tokens in the vault
    uint256 public totalSupply;

    // Risk management parameters
    uint256 public constant MAX_WITHDRAWAL_LIMIT = 1000 * 10**18; // Maximum withdrawal limit per transaction
    uint256 public constant MIN_DEPOSIT_AMOUNT = 1 * 10**18; // Minimum deposit amount

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the vault with the token address.
     * @param _token Address of the ERC20 token to be managed.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Deposit tokens into the vault.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount >= MIN_DEPOSIT_AMOUNT, "Deposit amount too low");

        // Transfer tokens from user to the vault
        token.transferFrom(msg.sender, address(this), amount);

        // Update user balance and total supply
        balances[msg.sender] += amount;
        totalSupply += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the vault.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount <= balances[msg.sender], "Insufficient balance");
        require(amount <= MAX_WITHDRAWAL_LIMIT, "Withdrawal exceeds limit");

        // Update user balance and total supply
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        // Transfer tokens from the vault to the user
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param user Address of the user.
     * @return The balance of the user in the vault.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Emergency withdrawal function to allow the owner to withdraw tokens in case of a critical issue.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient vault balance");
        token.transfer(owner(), amount);
    }
}
```
