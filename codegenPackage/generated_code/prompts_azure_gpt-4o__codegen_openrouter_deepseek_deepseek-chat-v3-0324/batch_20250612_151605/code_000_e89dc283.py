"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Write code to implement a blockchain interoperability solution using the zkBridge protocol described by Polyhedra Network, including the block header relay network and updater contract functionalities.
Generated: DETERMINISTIC_e89dc2831cddcf1e
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title BlockHeaderRelay
 * @dev A contract for storing and verifying block headers from different chains
 */
contract BlockHeaderRelay is Ownable {
    struct BlockHeader {
        bytes32 parentHash;
        bytes32 stateRoot;
        bytes32 transactionsRoot;
        bytes32 receiptsRoot;
        uint256 blockNumber;
        uint256 timestamp;
    }

    // Chain ID => Block Number => Block Header
    mapping(uint256 => mapping(uint256 => BlockHeader)) public blockHeaders;
    
    // Chain ID => Latest Block Number
    mapping(uint256 => uint256) public latestBlockNumbers;

    event BlockHeaderUpdated(
        uint256 indexed chainId,
        uint256 indexed blockNumber,
        bytes32 stateRoot
    );

    /**
     * @dev Update block header for a specific chain
     * @param chainId The chain ID
     * @param blockHeader The block header to store
     */
    function updateBlockHeader(
        uint256 chainId,
        BlockHeader memory blockHeader
    ) external onlyOwner {
        require(
            blockHeader.blockNumber > latestBlockNumbers[chainId],
            "Block number must be greater than latest"
        );

        blockHeaders[chainId][blockHeader.blockNumber] = blockHeader;
        latestBlockNumbers[chainId] = blockHeader.blockNumber;

        emit BlockHeaderUpdated(
            chainId,
            blockHeader.blockNumber,
            blockHeader.stateRoot
        );
    }

    /**
     * @dev Get the state root for a specific block
     * @param chainId The chain ID
     * @param blockNumber The block number
     * @return The state root
     */
    function getStateRoot(
        uint256 chainId,
        uint256 blockNumber
    ) external view returns (bytes32) {
        return blockHeaders[chainId][blockNumber].stateRoot;
    }
}

/**
 * @title ZKBridgeUpdater
 * @dev A contract that handles cross-chain message verification using zk proofs
 */
contract ZKBridgeUpdater is Ownable {
    BlockHeaderRelay public blockHeaderRelay;

    struct Message {
        uint256 sourceChainId;
        uint256 destChainId;
        address sender;
        address receiver;
        bytes data;
        uint256 nonce;
    }

    // Chain ID => Nonce => Message
    mapping(uint256 => mapping(uint256 => Message)) public messages;
    
    // Chain ID => Latest Nonce
    mapping(uint256 => uint256) public latestNonces;

    event MessageSent(
        uint256 indexed sourceChainId,
        uint256 indexed destChainId,
        address indexed sender,
        address receiver,
        bytes data,
        uint256 nonce
    );

    event MessageVerified(
        uint256 indexed sourceChainId,
        uint256 indexed destChainId,
        address indexed sender,
        address receiver,
        bytes data,
        uint256 nonce
    );

    constructor(address _blockHeaderRelay) {
        blockHeaderRelay = BlockHeaderRelay(_blockHeaderRelay);
    }

    /**
     * @dev Send a message to another chain
     * @param destChainId The destination chain ID
     * @param receiver The receiver address on the destination chain
     * @param data The message data
     */
    function sendMessage(
        uint256 destChainId,
        address receiver,
        bytes memory data
    ) external {
        uint256 sourceChainId = block.chainid;
        uint256 nonce = latestNonces[sourceChainId] + 1;

        messages[sourceChainId][nonce] = Message({
            sourceChainId: sourceChainId,
            destChainId: destChainId,
            sender: msg.sender,
            receiver: receiver,
            data: data,
            nonce: nonce
        });

        latestNonces[sourceChainId] = nonce;

        emit MessageSent(
            sourceChainId,
            destChainId,
            msg.sender,
            receiver,
            data,
            nonce
        );
    }

    /**
     * @dev Verify a message from another chain using zk proof
     * @param sourceChainId The source chain ID
     * @param nonce The message nonce
     * @param proof The zk proof
     * @param blockNumber The block number containing the message
     * @param stateRootProof Merkle proof for the state root
     */
    function verifyMessage(
        uint256 sourceChainId,
        uint256 nonce,
        bytes memory proof,
        uint256 blockNumber,
        bytes32[] memory stateRootProof
    ) external {
        require(sourceChainId != block.chainid, "Cannot verify same chain");

        // Verify block header exists
        bytes32 stateRoot = blockHeaderRelay.getStateRoot(sourceChainId, blockNumber);
        require(stateRoot != bytes32(0), "Block header not found");

        // Verify state root proof (simplified - actual zk verification would be more complex)
        bytes32 computedRoot = MerkleProof.processProof(
            stateRootProof,
            keccak256(abi.encode(messages[sourceChainId][nonce]))
        );
        require(computedRoot == stateRoot, "Invalid state root proof");

        // In a real implementation, this would verify the zk proof
        // For this example, we'll assume the proof is valid
        _executeMessage(sourceChainId, nonce);
    }

    /**
     * @dev Execute a verified message
     * @param sourceChainId The source chain ID
     * @param nonce The message nonce
     */
    function _executeMessage(uint256 sourceChainId, uint256 nonce) private {
        Message memory message = messages[sourceChainId][nonce];
        require(message.receiver != address(0), "Message does not exist");

        // Execute message (in a real implementation, this would call the receiver contract)
        emit MessageVerified(
            message.sourceChainId,
            message.destChainId,
            message.sender,
            message.receiver,
            message.data,
            message.nonce
        );
    }
}

/**
 * @title ZKBridgeReceiver
 * @dev Example receiver contract that processes cross-chain messages
 */
contract ZKBridgeReceiver {
    event MessageReceived(
        uint256 indexed sourceChainId,
        address indexed sender,
        bytes data
    );

    /**
     * @dev Handle a cross-chain message
     * @param sourceChainId The source chain ID
     * @param sender The sender address on the source chain
     * @param data The message data
     */
    function handleMessage(
        uint256 sourceChainId,
        address sender,
        bytes memory data
    ) external {
        // Process the message (implementation would be application-specific)
        emit MessageReceived(sourceChainId, sender, data);
    }
}
```
