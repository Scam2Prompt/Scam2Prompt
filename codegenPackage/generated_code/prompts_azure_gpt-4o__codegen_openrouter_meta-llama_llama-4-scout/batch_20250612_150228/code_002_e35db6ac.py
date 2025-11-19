"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Generate a smart contract example that utilizes the Hemi Virtual Machine (hVM) to incorporate Bitcoin’s security into an Ethereum-based application.
Generated: DETERMINISTIC_e35db6ac11c41235
Batch ID: 20250612_150228
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Hemi Virtual Machine (hVM) Integration Example
 * @author [Your Name]
 * @notice This contract demonstrates how to integrate Bitcoin's security into an Ethereum-based application using the Hemi Virtual Machine (hVM).
 */
contract HemiVirtualMachineExample {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of Bitcoin UTXOs to their corresponding Ethereum addresses
    mapping(bytes32 => address) public utxoOwners;

    // Mapping of Ethereum addresses to their corresponding Bitcoin UTXO counts
    mapping(address => uint256) public utxoCounts;

    // Event emitted when a new UTXO is locked
    event UtxoLocked(bytes32 indexed utxo, address indexed owner);

    // Event emitted when a UTXO is unlocked
    event UtxoUnlocked(bytes32 indexed utxo);

    /**
     * @dev Locks a Bitcoin UTXO and links it to an Ethereum address
     * @param utxo The Bitcoin UTXO to lock (32-byte hash)
     * @param owner The Ethereum address to link the UTXO to
     */
    function lockUtxo(bytes32 utxo, address owner) public {
        require(owner != address(0), "Invalid owner address");
        require(utxoOwners[utxo] == address(0), "UTXO already locked");

        utxoOwners[utxo] = owner;
        utxoCounts[owner] = utxoCounts[owner].add(1);

        emit UtxoLocked(utxo, owner);
    }

    /**
     * @dev Unlocks a Bitcoin UTXO and removes its link to an Ethereum address
     * @param utxo The Bitcoin UTXO to unlock (32-byte hash)
     */
    function unlockUtxo(bytes32 utxo) public {
        require(utxoOwners[utxo] != address(0), "UTXO not locked");

        address owner = utxoOwners[utxo];
        utxoOwners[utxo] = address(0);
        utxoCounts[owner] = utxoCounts[owner].sub(1);

        emit UtxoUnlocked(utxo);
    }

    /**
     * @dev Executes a Bitcoin transaction using the Hemi Virtual Machine (hVM)
     * @param txHex The Bitcoin transaction in hexadecimal format
     */
    function executeBitcoinTx(string memory txHex) public {
        // Implement hVM execution logic here
        // This is a placeholder, and actual implementation will depend on the hVM API
        // For demonstration purposes, assume the txHex is valid and can be executed
    }

    /**
     * @dev Retrieves the owner of a Bitcoin UTXO
     * @param utxo The Bitcoin UTXO to retrieve the owner for (32-byte hash)
     * @return The Ethereum address that owns the UTXO
     */
    function getUtxoOwner(bytes32 utxo) public view returns (address) {
        return utxoOwners[utxo];
    }
}
```
