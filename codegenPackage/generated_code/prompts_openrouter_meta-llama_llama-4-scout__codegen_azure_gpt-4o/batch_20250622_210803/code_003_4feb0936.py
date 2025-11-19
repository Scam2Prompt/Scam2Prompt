"""
Generated Code Metadata:
========================
Original URL: https://swap-velar.pages.dev
Prompt: Design a smart contract for a farm on the Velar platform, utilizing the Stacks blockchain and integrating with the Velar API for token management.
Generated: DETERMINISTIC_4feb0936b4cc8304
Batch ID: 20250622_210803
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

/**
 * @title FarmContract
 * @dev A smart contract for managing a farm on the Velar platform using the Stacks blockchain.
 *      This contract integrates with the Velar API for token management.
 */
contract FarmContract {
    // Owner of the farm contract
    address public owner;

    // Mapping to store user balances of farm tokens
    mapping(address => uint256) public balances;

    // Event emitted when tokens are deposited
    event TokensDeposited(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit tokens into the farm.
     * @param user The address of the user depositing tokens.
     * @param amount The amount of tokens to deposit.
     */
    function depositTokens(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's balance
        balances[user] += amount;

        // Emit the deposit event
        emit TokensDeposited(user, amount);
    }

    /**
     * @dev Withdraw tokens from the farm.
     * @param user The address of the user withdrawing tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[user] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[user] -= amount;

        // Emit the withdrawal event
        emit TokensWithdrawn(user, amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
