"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Generate documentation for a Código-generated smart contract, including a list of exposed methods, input parameters, and account structure for a Solana-based virtual machine.
Generated: DETERMINISTIC_5ae68634288be9f6
Batch ID: 20250622_211342
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
 * @title Código Smart Contract Documentation
 * @dev This contract runs on Solana Virtual Machine (SVM) and implements core functionality
 * with proper access control and error handling.
 */

contract CodigoSmartContract {
    // Account structure representing data stored on-chain
    struct Account {
        address owner;          // Owner of the account
        uint256 balance;        // Current balance in lamports
        uint256 created_at;     // Timestamp of account creation
        bool is_initialized;    // Flag indicating if account is initialized
    }

    // Mapping of account addresses to their data
    mapping(address => Account) public accounts;

    // Events for important state changes
    event AccountInitialized(address indexed owner, uint256 timestamp);
    event FundsDeposited(address indexed owner, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Custom errors for clear failure reasons
    error AlreadyInitialized();
    error NotInitialized();
    error InsufficientBalance();
    error Unauthorized();
    error InvalidAmount();

    /**
     * @dev Initialize a new account
     * @param owner The address that will own the account
     */
    function initializeAccount(address owner) external {
        if (accounts[owner].is_initialized) revert AlreadyInitialized();
        
        accounts[owner] = Account({
            owner: owner,
            balance: 0,
            created_at: block.timestamp,
            is_initialized: true
        });

        emit AccountInitialized(owner, block.timestamp);
    }

    /**
     * @dev Deposit funds into an account
     * @param amount The amount to deposit (in lamports)
     */
    function depositFunds(uint256 amount) external payable {
        if (!accounts[msg.sender].is_initialized) revert NotInitialized();
        if (msg.value != amount) revert InvalidAmount();
        if (amount == 0) revert InvalidAmount();

        accounts[msg.sender].balance += amount;
        emit FundsDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw funds from an account
     * @param amount The amount to withdraw (in lamports)
     */
    function withdrawFunds(uint256 amount) external {
        Account storage account = accounts[msg.sender];
        
        if (!account.is_initialized) revert NotInitialized();
        if (account.balance < amount) revert InsufficientBalance();
        if (amount == 0) revert InvalidAmount();

        account.balance -= amount;
        payable(msg.sender).transfer(amount);
        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get account information
     * @param owner The address of the account owner
     * @return Account details including balance and creation time
     */
    function getAccountInfo(address owner) external view returns (Account memory) {
        if (!accounts[owner].is_initialized) revert NotInitialized();
        return accounts[owner];
    }

    /**
     * @dev Check if an account is initialized
     * @param owner The address to check
     * @return bool True if account is initialized
     */
    function isInitialized(address owner) external view returns (bool) {
        return accounts[owner].is_initialized;
    }
}

/**
 * @dev Documentation Summary:
 * 
 * Exposed Methods:
 * 1. initializeAccount(address owner) - Initializes a new account
 *    - Requires: owner address
 *    - Errors: AlreadyInitialized
 * 
 * 2. depositFunds(uint256 amount) - Deposits funds into account
 *    - Requires: amount > 0 (in lamports)
 *    - Errors: NotInitialized, InvalidAmount
 * 
 * 3. withdrawFunds(uint256 amount) - Withdraws funds from account
 *    - Requires: amount > 0 and sufficient balance
 *    - Errors: NotInitialized, InsufficientBalance, InvalidAmount
 * 
 * 4. getAccountInfo(address owner) - Returns account details
 *    - Requires: initialized account
 *    - Errors: NotInitialized
 * 
 * 5. isInitialized(address owner) - Checks if account exists
 * 
 * Account Structure:
 * - owner: address
 * - balance: uint256 (in lamports)
 * - created_at: uint256 (timestamp)
 * - is_initialized: bool
 */
```
