"""
Generated Code Metadata:
========================
Original URL: https://whales-market.pages.dev
Prompt: Create a Solidity smart contract that includes a feature for users to cancel transactions and automatically claim collateral, similar to Whales Market's fraud prevention system.
Generated: DETERMINISTIC_9c6a4edd580983f2
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TransactionManager
 * @author [Your Name]
 * @notice A smart contract for managing transactions with a feature for users to cancel transactions and claim collateral.
 */
contract TransactionManager is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of transaction IDs to their respective states
    mapping (address => mapping (uint256 => Transaction)) public transactions;

    // Mapping of users to their collateral balances
    mapping (address => uint256) public collateralBalances;

    // Event emitted when a new transaction is created
    event NewTransaction(address indexed user, uint256 transactionId);

    // Event emitted when a transaction is cancelled
    event TransactionCancelled(address indexed user, uint256 transactionId);

    // Event emitted when collateral is claimed
    event CollateralClaimed(address indexed user, uint256 amount);

    // Struct representing a transaction
    struct Transaction {
        uint256 id;
        address user;
        uint256 amount;
        uint256 collateral;
        bool isCancelled;
        bool isClaimed;
    }

    /**
     * @notice Creates a new transaction
     * @param _transactionId The ID of the transaction
     * @param _amount The amount of the transaction
     * @param _collateral The collateral for the transaction
     */
    function createTransaction(uint256 _transactionId, uint256 _amount, uint256 _collateral) public {
        require(_amount > 0, "Transaction amount must be greater than 0");
        require(_collateral > 0, "Collateral must be greater than 0");

        // Deduct collateral from user's balance
        collateralBalances[msg.sender] = collateralBalances[msg.sender].sub(_collateral);

        // Initialize transaction
        transactions[msg.sender][_transactionId] = Transaction(
            _transactionId,
            msg.sender,
            _amount,
            _collateral,
            false,
            false
        );

        emit NewTransaction(msg.sender, _transactionId);
    }

    /**
     * @notice Cancels a transaction and claims collateral
     * @param _transactionId The ID of the transaction to cancel
     */
    function cancelTransaction(uint256 _transactionId) public {
        require(transactions[msg.sender][_transactionId].user == msg.sender, "Only the transaction owner can cancel");
        require(!transactions[msg.sender][_transactionId].isCancelled, "Transaction is already cancelled");

        // Mark transaction as cancelled
        transactions[msg.sender][_transactionId].isCancelled = true;

        // Claim collateral
        collateralBalances[msg.sender] = collateralBalances[msg.sender].add(transactions[msg.sender][_transactionId].collateral);

        emit TransactionCancelled(msg.sender, _transactionId);
        emit CollateralClaimed(msg.sender, transactions[msg.sender][_transactionId].collateral);
    }

    /**
     * @notice Deposits collateral
     * @param _amount The amount of collateral to deposit
     */
    function depositCollateral(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than 0");

        collateralBalances[msg.sender] = collateralBalances[msg.sender].add(_amount);
    }

    /**
     * @notice Withdraws collateral
     * @param _amount The amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(collateralBalances[msg.sender] >= _amount, "Insufficient collateral balance");

        collateralBalances[msg.sender] = collateralBalances[msg.sender].sub(_amount);
    }
}
```
