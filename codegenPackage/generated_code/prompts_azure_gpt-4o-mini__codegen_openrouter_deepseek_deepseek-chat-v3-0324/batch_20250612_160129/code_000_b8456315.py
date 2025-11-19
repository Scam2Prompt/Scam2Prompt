"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: How can I implement zkBridge to enable trustless cross-chain interoperability using zero-knowledge proofs?
Generated: DETERMINISTIC_b845631590ab8b55
Batch ID: 20250612_160129
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

import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title zkBridge
 * @dev A contract for trustless cross-chain interoperability using zero-knowledge proofs
 */
contract zkBridge is Ownable {
    // Struct to represent a cross-chain message
    struct Message {
        uint256 sourceChainId;
        uint256 destChainId;
        address sender;
        address receiver;
        uint256 amount;
        bytes32 messageHash;
        bool executed;
    }

    // Mapping from message ID to Message
    mapping(bytes32 => Message) public messages;

    // Mapping of supported chains
    mapping(uint256 => bool) public supportedChains;

    // Merkle root of the current state
    bytes32 public merkleRoot;

    // Event emitted when a message is sent
    event MessageSent(
        bytes32 indexed messageId,
        uint256 sourceChainId,
        uint256 destChainId,
        address sender,
        address receiver,
        uint256 amount,
        bytes32 messageHash
    );

    // Event emitted when a message is received
    event MessageExecuted(bytes32 indexed messageId);

    /**
     * @dev Constructor to initialize supported chains
     * @param chainIds Array of supported chain IDs
     */
    constructor(uint256[] memory chainIds) {
        for (uint256 i = 0; i < chainIds.length; i++) {
            supportedChains[chainIds[i]] = true;
        }
    }

    /**
     * @dev Send a cross-chain message
     * @param destChainId Destination chain ID
     * @param receiver Address on destination chain
     * @param amount Amount to transfer
     * @param messageHash Hash of the message data
     */
    function sendMessage(
        uint256 destChainId,
        address receiver,
        uint256 amount,
        bytes32 messageHash
    ) external payable {
        require(supportedChains[destChainId], "Unsupported destination chain");
        require(receiver != address(0), "Invalid receiver address");

        bytes32 messageId = keccak256(
            abi.encodePacked(
                block.chainid,
                destChainId,
                msg.sender,
                receiver,
                amount,
                messageHash,
                block.timestamp
            )
        );

        messages[messageId] = Message({
            sourceChainId: block.chainid,
            destChainId: destChainId,
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            messageHash: messageHash,
            executed: false
        });

        emit MessageSent(
            messageId,
            block.chainid,
            destChainId,
            msg.sender,
            receiver,
            amount,
            messageHash
        );
    }

    /**
     * @dev Receive a cross-chain message with ZK proof
     * @param messageId ID of the message
     * @param proof Merkle proof for the message
     */
    function receiveMessage(
        bytes32 messageId,
        bytes32[] calldata proof
    ) external {
        Message storage message = messages[messageId];
        require(!message.executed, "Message already executed");
        require(supportedChains[message.sourceChainId], "Unsupported source chain");

        // Verify the message is included in the merkle tree
        bytes32 leaf = keccak256(
            abi.encodePacked(
                message.sourceChainId,
                message.destChainId,
                message.sender,
                message.receiver,
                message.amount,
                message.messageHash
            )
        );
        require(
            MerkleProof.verify(proof, merkleRoot, leaf),
            "Invalid merkle proof"
        );

        message.executed = true;
        emit MessageExecuted(messageId);
    }

    /**
     * @dev Update the merkle root (only callable by owner)
     * @param newRoot The new merkle root
     */
    function updateMerkleRoot(bytes32 newRoot) external onlyOwner {
        merkleRoot = newRoot;
    }

    /**
     * @dev Add a supported chain (only callable by owner)
     * @param chainId The chain ID to add
     */
    function addSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = true;
    }

    /**
     * @dev Remove a supported chain (only callable by owner)
     * @param chainId The chain ID to remove
     */
    function removeSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = false;
    }
}
```
