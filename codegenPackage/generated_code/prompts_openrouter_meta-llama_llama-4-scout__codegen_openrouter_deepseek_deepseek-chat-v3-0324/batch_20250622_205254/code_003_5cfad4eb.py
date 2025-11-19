"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: "Implement a block header relay network and updater contract using Expander, a fast ZK proof system, for a blockchain interoperability application."
Generated: DETERMINISTIC_5cfad4eb4d80ccb6
Batch ID: 20250622_205254
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title BlockHeaderRelay
 * @dev A contract for relaying and verifying block headers between chains using Expander ZK proofs
 */
contract BlockHeaderRelay is Ownable {
    using ECDSA for bytes32;

    // Struct representing a block header
    struct BlockHeader {
        bytes32 parentHash;
        bytes32 stateRoot;
        bytes32 transactionsRoot;
        bytes32 receiptsRoot;
        uint256 blockNumber;
        uint256 timestamp;
        address submitter;
    }

    // Mapping from chainId to latest block number
    mapping(uint256 => uint256) public latestBlockNumbers;

    // Mapping from chainId to block number to BlockHeader
    mapping(uint256 => mapping(uint256 => BlockHeader)) public blockHeaders;

    // Mapping of authorized relayers
    mapping(address => bool) public authorizedRelayers;

    // Events
    event BlockHeaderUpdated(
        uint256 indexed chainId,
        uint256 indexed blockNumber,
        bytes32 stateRoot,
        address indexed submitter
    );
    event RelayerAuthorized(address relayer);
    event RelayerDeauthorized(address relayer);

    /**
     * @dev Modifier to check if caller is authorized
     */
    modifier onlyAuthorized() {
        require(authorizedRelayers[msg.sender] || msg.sender == owner(), "Unauthorized");
        _;
    }

    /**
     * @dev Authorize a relayer
     * @param relayer Address to authorize
     */
    function authorizeRelayer(address relayer) external onlyOwner {
        authorizedRelayers[relayer] = true;
        emit RelayerAuthorized(relayer);
    }

    /**
     * @dev Deauthorize a relayer
     * @param relayer Address to deauthorize
     */
    function deauthorizeRelayer(address relayer) external onlyOwner {
        authorizedRelayers[relayer] = false;
        emit RelayerDeauthorized(relayer);
    }

    /**
     * @dev Submit a new block header with ZK proof
     * @param chainId The chain ID this header belongs to
     * @param parentHash Parent block hash
     * @param stateRoot State root hash
     * @param transactionsRoot Transactions root hash
     * @param receiptsRoot Receipts root hash
     * @param blockNumber Block number
     * @param timestamp Block timestamp
     * @param zkProof Expander ZK proof bytes
     */
    function submitBlockHeader(
        uint256 chainId,
        bytes32 parentHash,
        bytes32 stateRoot,
        bytes32 transactionsRoot,
        bytes32 receiptsRoot,
        uint256 blockNumber,
        uint256 timestamp,
        bytes calldata zkProof
    ) external onlyAuthorized {
        require(blockNumber > latestBlockNumbers[chainId], "Block number must be higher than latest");

        // In production, this would verify the Expander ZK proof
        // For this example, we're simulating the verification
        bool proofValid = _verifyExpanderProof(
            chainId,
            parentHash,
            stateRoot,
            transactionsRoot,
            receiptsRoot,
            blockNumber,
            timestamp,
            zkProof
        );
        require(proofValid, "Invalid ZK proof");

        BlockHeader memory newHeader = BlockHeader({
            parentHash: parentHash,
            stateRoot: stateRoot,
            transactionsRoot: transactionsRoot,
            receiptsRoot: receiptsRoot,
            blockNumber: blockNumber,
            timestamp: timestamp,
            submitter: msg.sender
        });

        blockHeaders[chainId][blockNumber] = newHeader;
        latestBlockNumbers[chainId] = blockNumber;

        emit BlockHeaderUpdated(chainId, blockNumber, stateRoot, msg.sender);
    }

    /**
     * @dev Simulates Expander ZK proof verification
     * @notice In a real implementation, this would verify the proof using Expander's verifier
     */
    function _verifyExpanderProof(
        uint256 /*chainId*/,
        bytes32 /*parentHash*/,
        bytes32 /*stateRoot*/,
        bytes32 /*transactionsRoot*/,
        bytes32 /*receiptsRoot*/,
        uint256 /*blockNumber*/,
        uint256 /*timestamp*/,
        bytes calldata /*zkProof*/
    ) internal pure returns (bool) {
        // Placeholder for actual Expander proof verification
        // In production, this would call the Expander verifier contract
        return true;
    }

    /**
     * @dev Get the latest block header for a chain
     * @param chainId The chain ID to query
     * @return BlockHeader The latest block header
     */
    function getLatestBlockHeader(uint256 chainId) external view returns (BlockHeader memory) {
        uint256 latest = latestBlockNumbers[chainId];
        require(latest > 0, "No blocks submitted for this chain");
        return blockHeaders[chainId][latest];
    }

    /**
     * @dev Get a specific block header
     * @param chainId The chain ID to query
     * @param blockNumber The block number to query
     * @return BlockHeader The requested block header
     */
    function getBlockHeader(uint256 chainId, uint256 blockNumber) external view returns (BlockHeader memory) {
        require(blockHeaders[chainId][blockNumber].blockNumber != 0, "Block header not found");
        return blockHeaders[chainId][blockNumber];
    }
}

/**
 * @title BlockHeaderUpdater
 * @dev Contract that consumes block headers from the relay
 */
contract BlockHeaderUpdater {
    BlockHeaderRelay public immutable relay;

    // Mapping from chainId to block number to state root
    mapping(uint256 => mapping(uint256 => bytes32)) public stateRoots;

    event StateRootUpdated(uint256 indexed chainId, uint256 indexed blockNumber, bytes32 stateRoot);

    constructor(address _relay) {
        relay = BlockHeaderRelay(_relay);
    }

    /**
     * @dev Update state root from relayed block header
     * @param chainId The chain ID to update
     * @param blockNumber The block number to update
     */
    function updateStateRoot(uint256 chainId, uint256 blockNumber) external {
        BlockHeaderRelay.BlockHeader memory header = relay.getBlockHeader(chainId, blockNumber);
        
        require(stateRoots[chainId][blockNumber] == bytes32(0), "State root already updated");
        require(header.blockNumber == blockNumber, "Invalid block number");

        stateRoots[chainId][blockNumber] = header.stateRoot;
        emit StateRootUpdated(chainId, blockNumber, header.stateRoot);
    }

    /**
     * @dev Verify a state root exists for a given chain and block
     * @param chainId The chain ID to verify
     * @param blockNumber The block number to verify
     * @param stateRoot The state root to verify
     * @return bool True if the state root matches
     */
    function verifyStateRoot(
        uint256 chainId,
        uint256 blockNumber,
        bytes32 stateRoot
    ) external view returns (bool) {
        return stateRoots[chainId][blockNumber] == stateRoot;
    }
}
```
