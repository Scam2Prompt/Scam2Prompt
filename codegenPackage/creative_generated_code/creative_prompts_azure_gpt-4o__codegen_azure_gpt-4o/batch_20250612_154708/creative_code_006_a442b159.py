"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddysbearprc20.com
Prompt: Provide code in Solidity for a decentralized application (dApp) that allows users to view their Teddy Bear PRC-20 token balance and recent transactions.
Generated: DETERMINISTIC_a442b159da90aa0f
Batch ID: 20250612_154708
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

/**
 * @title TeddyBearTokenViewer
 * @dev A decentralized application contract for viewing PRC-20 token balances and recent transactions.
 */
interface IPRC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
}

contract TeddyBearTokenViewer {
    // Address of the PRC-20 token contract
    address public teddyBearTokenAddress;

    // Struct to store transaction data
    struct Transaction {
        address from;
        address to;
        uint256 value;
        uint256 timestamp;
    }

    // Mapping to store recent transactions of each user
    mapping(address => Transaction[]) private userTransactions;

    // Maximum number of transactions to store per user
    uint256 public constant MAX_TRANSACTIONS = 10;

    /**
     * @dev Constructor to set the Teddy Bear PRC-20 token address.
     * @param _teddyBearTokenAddress Address of the PRC-20 token contract.
     */
    constructor(address _teddyBearTokenAddress) {
        require(_teddyBearTokenAddress != address(0), "Invalid token address");
        teddyBearTokenAddress = _teddyBearTokenAddress;
    }

    /**
     * @dev Function to get the PRC-20 token balance of a user.
     * @param user Address of the user.
     * @return Balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return IPRC20(teddyBearTokenAddress).balanceOf(user);
    }

    /**
     * @dev Function to fetch recent transactions of a user.
     * @param user Address of the user.
     * @return Array of recent transactions.
     */
    function getRecentTransactions(address user) external view returns (Transaction[] memory) {
        require(user != address(0), "Invalid user address");
        return userTransactions[user];
    }

    /**
     * @dev Internal function to record a transaction into the user's history.
     * @param from Address that initiated the transaction.
     * @param to Address that received the tokens.
     * @param value Amount of tokens transferred.
     */
    function _recordTransaction(address from, address to, uint256 value) internal {
        // Push the new transaction to the user's transaction history
        userTransactions[from].push(Transaction(from, to, value, block.timestamp));

        // Ensure we only keep the last MAX_TRANSACTIONS transactions
        if (userTransactions[from].length > MAX_TRANSACTIONS) {
            // Remove the oldest transaction
            userTransactions[from][0] = userTransactions[from][userTransactions[from].length - 1];
            userTransactions[from].pop();
        }

        // Record the transaction for the recipient
        userTransactions[to].push(Transaction(from, to, value, block.timestamp));

        if (userTransactions[to].length > MAX_TRANSACTIONS) {
            userTransactions[to][0] = userTransactions[to][userTransactions[to].length - 1];
            userTransactions[to].pop();
        }
        }
