"""
Generated Code Metadata:
========================
Original URL: https://ethcna.com
Prompt: Create a Solidity function for validating BTC pledge amounts and triggering events when pledges are successfully processed.
Generated: DETERMINISTIC_70f48a4e5d349cb1
Batch ID: 20250612_145619
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
 * @title BTC Pledge Manager
 * @dev Handles BTC pledge validation and event triggering
 */
contract BTCPledgeManager {
    // Event emitted when a BTC pledge is successfully processed
    event PledgeProcessed(
        address indexed pledger,
        uint256 amount,
        string btcTxHash,
        uint256 timestamp
    );

    // Minimum and maximum pledge amounts (in satoshis)
    uint256 public constant MIN_PLEDGE = 10000; // 0.0001 BTC
    uint256 public constant MAX_PLEDGE = 100000000; // 1 BTC

    // Mapping to track processed BTC transaction hashes to prevent duplicates
    mapping(string => bool) private _processedTransactions;

    /**
     * @dev Validates and processes a BTC pledge
     * @param amount The pledge amount in satoshis
     * @param btcTxHash The BTC transaction hash
     */
    function processPledge(uint256 amount, string memory btcTxHash) external {
        require(amount >= MIN_PLEDGE, "Pledge amount too small");
        require(amount <= MAX_PLEDGE, "Pledge amount too large");
        require(bytes(btcTxHash).length == 64, "Invalid BTC transaction hash");
        require(!_processedTransactions[btcTxHash], "Transaction already processed");

        // Mark transaction as processed
        _processedTransactions[btcTxHash] = true;

        // Emit successful pledge event
        emit PledgeProcessed(
            msg.sender,
            amount,
            btcTxHash,
            block.timestamp
        );
    }

    /**
     * @dev Checks if a BTC transaction has already been processed
     * @param btcTxHash The BTC transaction hash to check
     * @return bool True if the transaction has been processed
     */
    function isTransactionProcessed(string memory btcTxHash) external view returns (bool) {
        return _processedTransactions[btcTxHash];
    }
}
```
