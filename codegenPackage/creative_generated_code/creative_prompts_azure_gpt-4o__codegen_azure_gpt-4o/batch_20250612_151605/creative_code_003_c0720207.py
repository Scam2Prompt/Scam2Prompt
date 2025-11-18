"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra.naynacodes.com
Prompt: Create a smart contract in Solidity for the updater contract in zkBridge that maintains a light-client state and updates the main chain based on verified proofs.
Generated: DETERMINISTIC_c072020756b86b2b
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Updater Contract for zkBridge
 * @dev This smart contract maintains a light-client state and updates the main chain based on verified proofs. 
 * It follows best practices for Solidity development, includes error handling, and is well-documented.
 */
contract ZkBridgeUpdater {
    // State variables
    address public owner; // Contract owner
    mapping(bytes32 => bool) public verifiedProofs; // Stores verified proof hashes
    bytes32 public latestState; // The latest light-client state

    // Events
    event ProofVerified(bytes32 indexed proofHash, bytes32 newState);
    event StateUpdated(bytes32 indexed oldState, bytes32 newState);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the sender as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Verifies a proof and updates the light-client state if valid.
     * @param proofHash The hash of the proof to verify.
     * @param newState The new light-client state to set if the proof is valid.
     */
    function verifyAndUpdateState(bytes32 proofHash, bytes32 newState) external onlyOwner {
        require(!verifiedProofs[proofHash], "Proof has already been verified");
        
        // Simulate proof verification (replace with actual verification logic)
        bool isProofValid = simulateProofVerification(proofHash);
        require(isProofValid, "Invalid proof");

        // Update the verified proofs mapping
        verifiedProofs[proofHash] = true;

        // Emit ProofVerified event
        emit ProofVerified(proofHash, newState);

        // Update the light-client state
        updateState(newState);
    }

    /**
     * @dev Updates the light-client state.
     * @param newState The new state to set.
     */
    function updateState(bytes32 newState) internal {
        bytes32 oldState = latestState;
        latestState = newState;

        // Emit StateUpdated event
        emit StateUpdated(oldState, newState);
    }

    /**
     * @dev Simulates proof verification logic (placeholder for actual zk-SNARK/zk-STARK verification).
     * @param proofHash The hash of the proof to verify.
     * @return bool True if the proof is valid, false otherwise.
     */
    function simulateProofVerification(bytes32 proofHash) internal pure returns (bool) {
        // Placeholder logic for proof verification (replace with real implementation)
        return proofHash != bytes32(0);
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
