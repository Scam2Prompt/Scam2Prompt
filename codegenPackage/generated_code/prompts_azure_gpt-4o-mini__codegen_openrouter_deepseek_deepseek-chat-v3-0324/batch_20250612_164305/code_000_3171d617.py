"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: How can I use the Hemi Bitcoin Kit (hBK) to build EVM-compatible applications that leverage Bitcoin's security?
Generated: DETERMINISTIC_3171d6173004709f
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation using the Hemi Bitcoin Kit (hBK) to build EVM-compatible applications with Bitcoin's security:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for hBK's core functionality
interface IHemiBitcoinKit {
    function verifyBitcoinTransaction(
        bytes32 txid,
        uint256 blockHeight,
        uint256 index,
        bytes calldata merkleProof,
        bytes calldata txBytes
    ) external returns (bool);

    function lockBitcoinForEvm(
        address evmRecipient,
        uint256 amount,
        uint256 lockDuration
    ) external returns (bytes32);

    function unlockBitcoinFromEvm(
        bytes32 lockId,
        bytes calldata bitcoinAddress,
        uint256 amount
    ) external returns (bool);
}

contract BitcoinSecuredEVMApp {
    IHemiBitcoinKit public hbk;
    address public owner;
    
    // Events for tracking important contract actions
    event BitcoinLocked(bytes32 indexed lockId, address indexed evmRecipient, uint256 amount);
    event BitcoinUnlocked(bytes32 indexed lockId, address indexed evmRecipient, uint256 amount);
    event BitcoinTxVerified(bytes32 indexed txid, address indexed verifier);

    // Error definitions
    error Unauthorized();
    error InvalidBitcoinTx();
    error LockNotFound();
    error InsufficientLockDuration();

    // Mapping to track bitcoin locks
    mapping(bytes32 => LockDetails) public bitcoinLocks;

    struct LockDetails {
        address evmRecipient;
        uint256 amount;
        uint256 lockTimestamp;
        uint256 lockDuration;
        bool unlocked;
    }

    constructor(address _hbkAddress) {
        hbk = IHemiBitcoinKit(_hbkAddress);
        owner = msg.sender;
    }

    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }

    /**
     * @dev Locks Bitcoin for use in EVM applications
     * @param evmRecipient The EVM address that will receive access to the locked BTC
     * @param amount The amount of BTC to lock (in satoshis)
     * @param lockDuration The duration to lock the BTC (in seconds)
     */
    function lockBitcoin(
        address evmRecipient,
        uint256 amount,
        uint256 lockDuration
    ) external onlyOwner returns (bytes32) {
        if (lockDuration < 1 days) revert InsufficientLockDuration();
        
        bytes32 lockId = hbk.lockBitcoinForEvm(evmRecipient, amount, lockDuration);
        
        bitcoinLocks[lockId] = LockDetails({
            evmRecipient: evmRecipient,
            amount: amount,
            lockTimestamp: block.timestamp,
            lockDuration: lockDuration,
            unlocked: false
        });
        
        emit BitcoinLocked(lockId, evmRecipient, amount);
        return lockId;
    }

    /**
     * @dev Unlocks Bitcoin from EVM back to Bitcoin network
     * @param lockId The ID of the lock to unlock
     * @param bitcoinAddress The Bitcoin address to receive the unlocked funds
     */
    function unlockBitcoin(
        bytes32 lockId,
        bytes calldata bitcoinAddress
    ) external onlyOwner returns (bool) {
        LockDetails storage lock = bitcoinLocks[lockId];
        if (lock.evmRecipient == address(0)) revert LockNotFound();
        if (lock.unlocked) revert LockNotFound();

        bool success = hbk.unlockBitcoinFromEvm(lockId, bitcoinAddress, lock.amount);
        require(success, "Unlock failed");
        
        lock.unlocked = true;
        emit BitcoinUnlocked(lockId, lock.evmRecipient, lock.amount);
        return true;
    }

    /**
     * @dev Verifies a Bitcoin transaction using hBK's SPV proof system
     * @param txid The Bitcoin transaction ID to verify
     * @param blockHeight The block height containing the transaction
     * @param index The index of the transaction in the block
     * @param merkleProof The merkle proof for the transaction
     * @param txBytes The raw transaction bytes
     */
    function verifyBitcoinTransaction(
        bytes32 txid,
        uint256 blockHeight,
        uint256 index,
        bytes calldata merkleProof,
        bytes calldata txBytes
    ) external returns (bool) {
        bool isValid = hbk.verifyBitcoinTransaction(
            txid,
            blockHeight,
            index,
            merkleProof,
            txBytes
        );
        
        if (!isValid) revert InvalidBitcoinTx();
        
        emit BitcoinTxVerified(txid, msg.sender);
        return true;
    }

    /**
     * @dev Checks if a Bitcoin lock is valid and active
     * @param lockId The ID of the lock to check
     */
    function isLockActive(bytes32 lockId) external view returns (bool) {
        LockDetails memory lock = bitcoinLocks[lockId];
        return (lock.evmRecipient != address(0) && 
                !lock.unlocked && 
                block.timestamp < lock.lockTimestamp + lock.lockDuration);
    }
}
```

```javascript
// Frontend integration example (using ethers.js)
const { ethers } = require('ethers');

class HBKIntegration {
  constructor(contractAddress, provider, signer) {
    this.contract = new ethers.Contract(
      contractAddress,
      [
        'function lockBitcoin(address,uint256,uint256) returns (bytes32)',
        'function unlockBitcoin(bytes32,bytes) returns (bool)',
        'function verifyBitcoinTransaction(bytes32,uint256,uint256,bytes,bytes) returns (bool)',
        'function isLockActive(bytes32) view returns (bool)',
        'event BitcoinLocked(bytes32 indexed,address indexed,uint256)',
        'event BitcoinUnlocked(bytes32 indexed,address indexed,uint256)'
      ],
      signer
    );
  }

  async lockBitcoin(recipient, amount, duration) {
    const tx = await this.contract.lockBitcoin(recipient, amount, duration);
    const receipt = await tx.wait();
    const event = receipt.events?.find(e => e.event === 'BitcoinLocked');
    return event.args.lockId;
  }

  async unlockBitcoin(lockId, bitcoinAddress) {
    const tx = await this.contract.unlockBitcoin(lockId, ethers.utils.arrayify(bitcoinAddress));
    await tx.wait();
    return true;
  }

  async verifyBitcoinTx(txid, blockHeight, index, merkleProof, txBytes) {
    const tx = await this.contract.verifyBitcoinTransaction(
      txid,
      blockHeight,
      index,
      merkleProof,
      txBytes
    );
    await tx.wait();
    return true;
  }

  async checkLockStatus(lockId) {
    return await this.contract.isLockActive(lockId);
  }
}
```

This implementation includes:
1. A Solidity smart contract that interfaces with hBK
2. Proper error handling and events
3. Security checks and access control
4. A JavaScript frontend integration example
5. Comprehensive function documentation
