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

contract Updater {
    // Event emitted when the state is updated
    event StateUpdated(address indexed updater, uint256 newState);

    // Mapping to store the state of the light client
    mapping(uint256 => bytes32) public lightClientStates;
    uint256 public latestBlock;

    // Modifier to ensure the caller is a verifier
    modifier onlyVerifier() {
        require(msg.sender == verifier, "Not authorized: caller is not the verifier");
        _;
    }

    // Address of the verifier (could be a contract or an address)
    address public verifier;

    // Constructor to set the verifier
    constructor(address _verifier) {
        require(_verifier != address(0), "Invalid verifier address");
        verifier = _verifier;
    }

    // Function to update the light client state based on verified proof
    function updateState(uint256 blockNumber, bytes32 newState, bytes32 proof) external onlyVerifier {
        // Validate the proof (In a real-world scenario, you'd have more complex proof validation)
        require(validateProof(proof), "Invalid proof");

        // Update the light client state and latest block
        lightClientStates[blockNumber] = newState;
        latestBlock = blockNumber;

        emit StateUpdated(msg.sender, blockNumber);
    }

    // Dummy proof validation function (replace with actual implementation)
    function validateProof(bytes32 proof) internal pure returns (bool) {
        // Placeholder logic for proof validation
        // In production, implement actual proof verification logic
        return proof != bytes32(0);
    }

    // Function to retrieve the light client state for a specific block
    function getState(uint256 blockNumber) external view returns (bytes32) {
        return lightClientStates[blockNumber];
    }
}
```
