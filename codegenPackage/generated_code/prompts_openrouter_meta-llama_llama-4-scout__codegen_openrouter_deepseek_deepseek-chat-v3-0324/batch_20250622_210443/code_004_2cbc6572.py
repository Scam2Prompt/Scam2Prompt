"""
Generated Code Metadata:
========================
Original URL: https://methlab-xyz.pages.dev
Prompt: Implement a transaction reversion mechanism in Solidity that checks for pending transaction duration and price slippage, similar to the one described on the Methlab swap page.
Generated: DETERMINISTIC_2cbc6572cfe2811f
Batch ID: 20250622_210443
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TransactionReverser is Ownable {
    using SafeMath for uint256;

    // Struct to store transaction details
    struct Transaction {
        address user;
        address token;
        uint256 amount;
        uint256 timestamp;
        uint256 expectedPrice;
        uint256 slippageTolerance;
        uint256 maxDuration;
        bool isReverted;
    }

    // Mapping to store transactions by their IDs
    mapping(bytes32 => Transaction) public transactions;

    // Events
    event TransactionRegistered(
        bytes32 indexed txId,
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 expectedPrice,
        uint256 slippageTolerance,
        uint256 maxDuration
    );

    event TransactionReverted(
        bytes32 indexed txId,
        address indexed user,
        address indexed token,
        uint256 amount
    );

    // Modifier to check if transaction exists
    modifier transactionExists(bytes32 txId) {
        require(transactions[txId].user != address(0), "Transaction does not exist");
        _;
    }

    // Modifier to check if transaction is not already reverted
    modifier notReverted(bytes32 txId) {
        require(!transactions[txId].isReverted, "Transaction already reverted");
        _;
    }

    /**
     * @dev Register a new transaction
     * @param txId Unique transaction ID
     * @param token Token address involved in the transaction
     * @param amount Amount of tokens
     * @param expectedPrice Expected price at time of transaction
     * @param slippageTolerance Allowed slippage percentage (e.g., 5 for 5%)
     * @param maxDuration Maximum allowed duration in seconds before reverting
     */
    function registerTransaction(
        bytes32 txId,
        address token,
        uint256 amount,
        uint256 expectedPrice,
        uint256 slippageTolerance,
        uint256 maxDuration
    ) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(expectedPrice > 0, "Expected price must be greater than zero");
        require(slippageTolerance <= 100, "Slippage tolerance cannot exceed 100%");
        require(maxDuration > 0, "Max duration must be greater than zero");
        require(transactions[txId].user == address(0), "Transaction ID already exists");

        transactions[txId] = Transaction({
            user: msg.sender,
            token: token,
            amount: amount,
            timestamp: block.timestamp,
            expectedPrice: expectedPrice,
            slippageTolerance: slippageTolerance,
            maxDuration: maxDuration,
            isReverted: false
        });

        emit TransactionRegistered(
            txId,
            msg.sender,
            token,
            amount,
            expectedPrice,
            slippageTolerance,
            maxDuration
        );
    }

    /**
     * @dev Check if transaction should be reverted based on current price and duration
     * @param txId Transaction ID to check
     * @param currentPrice Current market price of the token
     * @return shouldRevert Boolean indicating if transaction should be reverted
     */
    function shouldRevertTransaction(bytes32 txId, uint256 currentPrice)
        public
        view
        transactionExists(txId)
        notReverted(txId)
        returns (bool)
    {
        Transaction memory transaction = transactions[txId];

        // Check if transaction has exceeded max duration
        if (block.timestamp > transaction.timestamp.add(transaction.maxDuration)) {
            return true;
        }

        // Calculate price difference percentage
        uint256 priceDifference;
        if (currentPrice > transaction.expectedPrice) {
            priceDifference = currentPrice.sub(transaction.expectedPrice).mul(100).div(transaction.expectedPrice);
        } else {
            priceDifference = transaction.expectedPrice.sub(currentPrice).mul(100).div(transaction.expectedPrice);
        }

        // Check if price slippage exceeds tolerance
        if (priceDifference > transaction.slippageTolerance) {
            return true;
        }

        return false;
    }

    /**
     * @dev Revert a transaction and return funds to user
     * @param txId Transaction ID to revert
     * @param currentPrice Current market price of the token
     */
    function revertTransaction(bytes32 txId, uint256 currentPrice)
        external
        transactionExists(txId)
        notReverted(txId)
    {
        require(shouldRevertTransaction(txId, currentPrice), "Transaction does not meet revert conditions");

        Transaction storage transaction = transactions[txId];
        transaction.isReverted = true;

        // Transfer tokens back to user
        IERC20 token = IERC20(transaction.token);
        require(token.transfer(transaction.user, transaction.amount), "Token transfer failed");

        emit TransactionReverted(txId, transaction.user, transaction.token, transaction.amount);
    }

    /**
     * @dev Emergency function to withdraw tokens stuck in contract
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
