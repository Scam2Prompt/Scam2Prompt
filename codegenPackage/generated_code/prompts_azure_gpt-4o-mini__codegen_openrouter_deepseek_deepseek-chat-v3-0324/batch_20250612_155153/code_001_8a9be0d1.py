"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Write a code snippet that demonstrates how to set up the updater contract for the zkBridge on the receiver chain.
Generated: DETERMINISTIC_8a9be0d1e2a3cf8c
Batch ID: 20250612_155153
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
import "@openzeppelin/contracts/utils/Address.sol";

interface IReceiverUpdater {
    function updateReceiver(bytes32 blockHash, bytes32 receiptHash) external;
}

contract ReceiverUpdater is Ownable, IReceiverUpdater {
    using Address for address;

    // Address of the zkBridge contract
    address public zkBridge;

    // Mapping to store block hashes and their corresponding receipt hashes
    mapping(bytes32 => bytes32) public blockReceipts;

    // Event emitted when receiver is updated
    event ReceiverUpdated(bytes32 indexed blockHash, bytes32 receiptHash);

    /**
     * @dev Constructor that sets the initial zkBridge address
     * @param _zkBridge Address of the zkBridge contract
     */
    constructor(address _zkBridge) {
        require(_zkBridge != address(0), "Invalid zkBridge address");
        zkBridge = _zkBridge;
    }

    /**
     * @dev Updates the receiver with new block and receipt hashes
     * @param blockHash Hash of the block containing the transaction
     * @param receiptHash Hash of the transaction receipt
     */
    function updateReceiver(bytes32 blockHash, bytes32 receiptHash) external override {
        require(msg.sender == zkBridge, "Only zkBridge can call this");
        require(blockHash != bytes32(0), "Invalid block hash");
        require(receiptHash != bytes32(0), "Invalid receipt hash");

        blockReceipts[blockHash] = receiptHash;
        emit ReceiverUpdated(blockHash, receiptHash);
    }

    /**
     * @dev Updates the zkBridge address (only callable by owner)
     * @param newZkBridge New zkBridge address
     */
    function updateZkBridge(address newZkBridge) external onlyOwner {
        require(newZkBridge != address(0), "Invalid zkBridge address");
        zkBridge = newZkBridge;
    }

    /**
     * @dev Verifies if a block hash has a corresponding receipt hash
     * @param blockHash Hash of the block to verify
     * @param receiptHash Expected receipt hash
     * @return bool True if verification passes
     */
    function verifyReceipt(bytes32 blockHash, bytes32 receiptHash) external view returns (bool) {
        return blockReceipts[blockHash] == receiptHash;
    }
}
```
