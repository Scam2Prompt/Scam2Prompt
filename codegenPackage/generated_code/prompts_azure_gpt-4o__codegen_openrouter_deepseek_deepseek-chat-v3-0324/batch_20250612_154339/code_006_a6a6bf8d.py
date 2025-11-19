"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: Create a smart contract that leverages Hemi’s programmability to build Bitcoin-aware applications compatible with Ethereum’s EVM.
Generated: DETERMINISTIC_a6a6bf8d14055fb4
Batch ID: 20250612_154339
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

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BitcoinAwareContract
 * @dev A smart contract that interacts with Bitcoin data on Ethereum's EVM
 * using Hemi's programmability features.
 */
contract BitcoinAwareContract is Ownable {
    using Address for address payable;

    // Event emitted when Bitcoin data is received
    event BitcoinDataReceived(bytes32 indexed bitcoinTxHash, uint256 amount, address indexed receiver);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Mapping to store Bitcoin transaction hashes to prevent duplicates
    mapping(bytes32 => bool) private _processedBitcoinTxs;

    /**
     * @dev Process incoming Bitcoin transaction data
     * @param bitcoinTxHash The hash of the Bitcoin transaction
     * @param amount The amount of Bitcoin (in satoshis) converted to wei
     * @param receiver The Ethereum address that should receive the funds
     */
    function processBitcoinTransaction(
        bytes32 bitcoinTxHash,
        uint256 amount,
        address receiver
    ) external onlyOwner {
        require(!_processedBitcoinTxs[bitcoinTxHash], "BitcoinAwareContract: Transaction already processed");
        require(receiver != address(0), "BitcoinAwareContract: Invalid receiver address");
        require(amount > 0, "BitcoinAwareContract: Amount must be positive");

        _processedBitcoinTxs[bitcoinTxHash] = true;
        emit BitcoinDataReceived(bitcoinTxHash, amount, receiver);
    }

    /**
     * @dev Withdraw funds from the contract
     * @param amount The amount to withdraw in wei
     * @param recipient The address to receive the funds
     */
    function withdrawFunds(uint256 amount, address payable recipient) external onlyOwner {
        require(recipient != address(0), "BitcoinAwareContract: Invalid recipient address");
        require(amount > 0, "BitcoinAwareContract: Amount must be positive");
        require(address(this).balance >= amount, "BitcoinAwareContract: Insufficient balance");

        recipient.sendValue(amount);
        emit FundsWithdrawn(recipient, amount);
    }

    /**
     * @dev Check if a Bitcoin transaction has been processed
     * @param bitcoinTxHash The hash of the Bitcoin transaction to check
     * @return bool True if the transaction has been processed
     */
    function isBitcoinTransactionProcessed(bytes32 bitcoinTxHash) external view returns (bool) {
        return _processedBitcoinTxs[bitcoinTxHash];
    }

    // Allow the contract to receive Ether
    receive() external payable {}
}
```
