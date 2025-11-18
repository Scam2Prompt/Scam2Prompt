"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundaktion.org
Prompt: Write a Solidity contract for a decentralized treasury management system that aligns with the Ondo Foundation’s focus on strategic ecosystem growth.
Generated: DETERMINISTIC_e80f5c412bd6b9ac
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title DecentralizedTreasury
 * @notice A treasury management system for managing funds in an ecosystem.
 * @dev This contract allows the owner to deposit, withdraw, and manage funds.
 */
contract DecentralizedTreasury is Ownable {
    // Mapping to track the balance of each token
    mapping(address => uint256) private _balances;

    // Event emitted when funds are deposited
    event Deposited(address indexed token, uint256 amount);

    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed token, uint256 amount);
    
    // Event emitted when funds are allocated to a project
    event FundAllocated(address indexed project, address indexed token, uint256 amount);

    /**
     * @notice Deposit tokens into the treasury.
     * @param token The address of the ERC20 token to deposit.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the balance mapping
        _balances[token] += amount;

        emit Deposited(token, amount);
    }

    /**
     * @notice Withdraw tokens from the treasury.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(_balances[token] >= amount, "Insufficient balance");

        // Update the balance mapping
        _balances[token] -= amount;

        // Transfer the tokens back to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(token, amount);
    }

    /**
     * @notice Allocate funds to a specific project.
     * @param project The address of the project to allocate funds to.
     * @param token The address of the ERC20 token to allocate.
     * @param amount The amount of tokens to allocate.
     */
    function allocateFunds(address project, address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Allocation amount must be greater than zero");
        require(_balances[token] >= amount, "Insufficient balance for allocation");

        // Update the balance mapping
        _balances[token] -= amount;

        // Transfer the allocated tokens to the project
        require(IERC20(token).transfer(project, amount), "Transfer failed");

        emit FundAllocated(project, token, amount);
    }

    /**
     * @notice Get the current balance of a specific token in the treasury.
     * @param token The address of the ERC20 token.
     * @return The balance of the specified token.
     */
    function getBalance(address token) external view returns (uint256) {
        return _balances[token];
    }
}
```
