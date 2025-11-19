"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: "Generate a Solidity smart contract for a decentralized application (dApp) on Mazze's EVM-compatible blockchain, incorporating ZK Proofs for enhanced privacy."
Generated: DETERMINISTIC_fa1ececcfac525a4
Batch ID: 20250622_211330
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

import "@matterlabs/zksync-contracts/l2/system-contracts/Constants.sol";
import "@matterlabs/zksync-contracts/l1/contracts/zksync/interfaces/IZkSync.sol";

/**
 * @title PrivateVoting
 * @dev A decentralized application (dApp) for private voting using ZK Proofs on Mazze's EVM-compatible blockchain.
 * This contract allows users to cast votes privately and verify them using zero-knowledge proofs.
 */
contract PrivateVoting {
    // Struct to represent a vote
    struct Vote {
        bytes32 commitment; // Commitment to the vote (using ZK Proof)
        uint256 timestamp;  // Timestamp when the vote was cast
    }

    // Mapping from voter address to their vote
    mapping(address => Vote) private votes;

    // Event emitted when a new vote is cast
    event VoteCast(address indexed voter, bytes32 commitment, uint256 timestamp);

    // Address of the ZK Sync contract for proof verification
    address public zkSyncContract;

    /**
     * @dev Constructor to initialize the ZK Sync contract address.
     * @param _zkSyncContract Address of the ZK Sync contract.
     */
    constructor(address _zkSyncContract) {
        require(_zkSyncContract != address(0), "Invalid ZK Sync contract address");
        zkSyncContract = _zkSyncContract;
    }

    /**
     * @dev Cast a vote with a ZK Proof commitment.
     * @param commitment The ZK Proof commitment representing the vote.
     */
    function castVote(bytes32 commitment) external {
        require(commitment != bytes32(0), "Invalid commitment");
        require(votes[msg.sender].commitment == bytes32(0), "Already voted");

        votes[msg.sender] = Vote({
            commitment: commitment,
            timestamp: block.timestamp
        });

        emit VoteCast(msg.sender, commitment, block.timestamp);
    }

    /**
     * @dev Verify a vote using a ZK Proof.
     * @param proof The ZK Proof to verify.
     * @param input The public input for the proof.
     * @return bool True if the proof is valid, false otherwise.
     */
    function verifyVote(bytes calldata proof, uint256[] calldata input) external view returns (bool) {
        require(proof.length > 0, "Proof cannot be empty");
        require(input.length > 0, "Input cannot be empty");

        // Use the ZK Sync contract to verify the proof
        (bool success, ) = zkSyncContract.staticcall(
            abi.encodeWithSignature("verifyProof(bytes,uint256[])", proof, input)
        );

        return success;
    }

    /**
     * @dev Get the vote commitment for a specific voter.
     * @param voter Address of the voter.
     * @return bytes32 The vote commitment.
     */
    function getVoteCommitment(address voter) external view returns (bytes32) {
        require(voter != address(0), "Invalid voter address");
        return votes[voter].commitment;
    }

    /**
     * @dev Check if a voter has already cast a vote.
     * @param voter Address of the voter.
     * @return bool True if the voter has voted, false otherwise.
     */
    function hasVoted(address voter) external view returns (bool) {
        require(voter != address(0), "Invalid voter address");
        return votes[voter].commitment != bytes32(0);
    }
}
```
