"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Create a smart contract in Solidity for the updater contract in zkBridge that maintains a light-client state and updates the main chain based on verified proofs.
Generated: DETERMINISTIC_c072020756b86b2b
Batch ID: 20250612_151605
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

import "./ILightClient.sol";
import "./IZKBridge.sol";
import "./Merkle.sol";

/**
 * @title Updater Contract for zkBridge
 * @author [Your Name]
 * @notice This contract maintains a light-client state and updates the main chain based on verified proofs.
 */
contract Updater {
    // Mapping of block headers
    mapping(uint256 => BlockHeader) public blockHeaders;

    // Mapping of block header existence
    mapping(uint256 => bool) public blockHeaderExists;

    // Light client interface
    ILightClient public lightClient;

    // zkBridge interface
    IZKBridge public zkBridge;

    // Struct for block headers
    struct BlockHeader {
        bytes32 root;
        uint256 timestamp;
        bytes32[] proof;
    }

    /**
     * @notice Constructor for Updater contract
     * @param _lightClientAddress Address of the light client contract
     * @param _zkBridgeAddress Address of the zkBridge contract
     */
    constructor(address _lightClientAddress, address _zkBridgeAddress) {
        require(_lightClientAddress != address(0), "Light client address cannot be zero");
        require(_zkBridgeAddress != address(0), "zkBridge address cannot be zero");

        lightClient = ILightClient(_lightClientAddress);
        zkBridge = IZKBridge(_zkBridgeAddress);
    }

    /**
     * @notice Function to update the light client state
     * @param _blockNumber Block number to update
     * @param _blockHeader Block header to update
     */
    function updateLightClientState(uint256 _blockNumber, BlockHeader memory _blockHeader) public {
        require(msg.sender == address(zkBridge), "Only zkBridge can update light client state");

        // Verify block header proof
        bool isValid = verifyBlockHeaderProof(_blockNumber, _blockHeader);
        require(isValid, "Invalid block header proof");

        // Update block header
        blockHeaders[_blockNumber] = _blockHeader;
        blockHeaderExists[_blockNumber] = true;

        // Emit event
        emit UpdateLightClientState(_blockNumber, _blockHeader.root);
    }

    /**
     * @notice Function to verify block header proof
     * @param _blockNumber Block number to verify
     * @param _blockHeader Block header to verify
     * @return bool Whether the block header proof is valid
     */
    function verifyBlockHeaderProof(uint256 _blockNumber, BlockHeader memory _blockHeader) internal view returns (bool) {
        // Get previous block header
        uint256 prevBlockNumber = _blockNumber - 1;
        BlockHeader memory prevBlockHeader = blockHeaders[prevBlockNumber];

        // Check if previous block header exists
        require(blockHeaderExists[prevBlockNumber], "Previous block header does not exist");

        // Verify Merkle proof
        return Merkle.verifyMerkleProof(_blockHeader.root, prevBlockHeader.root, _blockHeader.proof);
    }

    /**
     * @notice Function to get block header
     * @param _blockNumber Block number to get
     * @return BlockHeader Block header at the given block number
     */
    function getBlockHeader(uint256 _blockNumber) public view returns (BlockHeader memory) {
        require(blockHeaderExists[_blockNumber], "Block header does not exist");

        return blockHeaders[_blockNumber];
    }

    // Event emitted when light client state is updated
    event UpdateLightClientState(uint256 blockNumber, bytes32 blockRoot);
}
```
