"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: "Explain the role of the Hemi Bitcoin Kit (hBK) in building Bitcoin-aware, EVM-compatible applications."
Generated: DETERMINISTIC_15976c07f354c3cc
Batch ID: 20250622_211614
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
 * @title Hemi Bitcoin Kit (hBK) Interface
 * @notice This interface defines the core functionality of the Hemi Bitcoin Kit (hBK)
 *         which enables Bitcoin-aware, EVM-compatible applications.
 * @dev The hBK facilitates interaction between Bitcoin and EVM chains by providing
 *      functions to verify Bitcoin transactions, manage Bitcoin addresses, and
 *      handle cross-chain operations.
 */
interface IHemiBitcoinKit {
    /**
     * @notice Verifies a Bitcoin transaction's inclusion in the blockchain
     * @param txid The Bitcoin transaction ID to verify
     * @param blockHash The block hash where the transaction is included
     * @param merkleProof The merkle proof for the transaction
     * @return isValid True if the transaction is valid and included in the block
     */
    function verifyBitcoinTransaction(
        bytes32 txid,
        bytes32 blockHash,
        bytes32[] calldata merkleProof
    ) external view returns (bool isValid);

    /**
     * @notice Converts a Bitcoin address to an EVM-compatible address
     * @param btcAddress The Bitcoin address to convert
     * @return evmAddress The corresponding EVM address
     */
    function bitcoinToEvmAddress(
        string calldata btcAddress
    ) external pure returns (address evmAddress);

    /**
     * @notice Locks Bitcoin for cross-chain operations
     * @param amount The amount of Bitcoin to lock (in satoshis)
     * @param recipient The EVM address to receive the wrapped Bitcoin
     * @return lockId A unique identifier for the lock operation
     */
    function lockBitcoin(
        uint256 amount,
        address recipient
    ) external returns (bytes32 lockId);

    /**
     * @notice Releases Bitcoin from a cross-chain lock
     * @param lockId The unique identifier of the lock operation
     * @param btcAddress The Bitcoin address to receive the unlocked funds
     */
    function releaseBitcoin(
        bytes32 lockId,
        string calldata btcAddress
    ) external;

    /**
     * @notice Event emitted when Bitcoin is locked for cross-chain operations
     * @param lockId The unique identifier for the lock operation
     * @param amount The amount locked (in satoshis)
     * @param recipient The EVM address that will receive the wrapped Bitcoin
     */
    event BitcoinLocked(
        bytes32 indexed lockId,
        uint256 amount,
        address indexed recipient
    );

    /**
     * @notice Event emitted when Bitcoin is released from a cross-chain lock
     * @param lockId The unique identifier for the lock operation
     * @param amount The amount released (in satoshis)
     * @param btcAddress The Bitcoin address that received the funds
     */
    event BitcoinReleased(
        bytes32 indexed lockId,
        uint256 amount,
        string indexed btcAddress
    );
}

/**
 * @title BitcoinAwareApp
 * @notice Example contract demonstrating how to build Bitcoin-aware EVM applications using hBK
 */
contract BitcoinAwareApp {
    IHemiBitcoinKit public hbk;

    constructor(address _hbkAddress) {
        hbk = IHemiBitcoinKit(_hbkAddress);
    }

    /**
     * @notice Processes a Bitcoin transaction by verifying it and performing actions
     * @param txid The Bitcoin transaction ID to process
     * @param blockHash The block hash where the transaction is included
     * @param merkleProof The merkle proof for the transaction
     */
    function processBitcoinTransaction(
        bytes32 txid,
        bytes32 blockHash,
        bytes32[] calldata merkleProof
    ) external {
        require(
            hbk.verifyBitcoinTransaction(txid, blockHash, merkleProof),
            "Invalid Bitcoin transaction"
        );

        // Custom application logic for verified Bitcoin transactions
        // ...
    }

    /**
     * @notice Wraps Bitcoin by locking it and minting a corresponding EVM token
     * @param amount The amount of Bitcoin to wrap (in satoshis)
     */
    function wrapBitcoin(uint256 amount) external {
        bytes32 lockId = hbk.lockBitcoin(amount, msg.sender);
        
        // Custom logic for handling wrapped Bitcoin
        // ...
    }

    /**
     * @notice Unwraps Bitcoin by burning tokens and releasing the locked Bitcoin
     * @param lockId The lock ID of the wrapped Bitcoin
     * @param btcAddress The Bitcoin address to receive the unwrapped funds
     */
    function unwrapBitcoin(bytes32 lockId, string calldata btcAddress) external {
        hbk.releaseBitcoin(lockId, btcAddress);
        
        // Custom logic for handling unwrapped Bitcoin
        // ...
    }
}
```
