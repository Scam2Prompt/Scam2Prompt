"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://join-satoshivm.pages.dev
Prompt: Write a Solidity contract that integrates with SatoshiVM's fraud-proof mechanism to ensure secure off-chain computations.
Generated: DETERMINISTIC_8ddde96f07c388fd
Batch ID: 20250612_153517
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

// Import necessary interfaces for SatoshiVM fraud-proof mechanism
interface ISatoshiVM {
    function submitProof(bytes calldata proof) external returns (bool);
    function verifyProof(bytes calldata proof) external view returns (bool);
}

contract SecureOffChainComputation {
    // State variable to hold the address of the SatoshiVM contract
    ISatoshiVM public satoshiVM;

    // Event emitted when a computation is reported
    event ComputationReported(address indexed reporter, bytes proof);

    // Constructor to set the SatoshiVM contract address
    constructor(address _satoshiVMAddress) {
        require(_satoshiVMAddress != address(0), "Invalid SatoshiVM address");
        satoshiVM = ISatoshiVM(_satoshiVMAddress);
    }

    // Function to report a computation's proof
    function reportComputation(bytes calldata proof) external {
        // Ensure the proof is not empty
        require(proof.length > 0, "Proof cannot be empty");

        // Submit the proof to the SatoshiVM
        bool success = satoshiVM.submitProof(proof);
        require(success, "Failed to submit proof");

        // Emit an event for the reported computation
        emit ComputationReported(msg.sender, proof);
    }

    // Function to verify a submitted proof
    function verifyComputation(bytes calldata proof) external view returns (bool) {
        // Ensure the proof is not empty
        require(proof.length > 0, "Proof cannot be empty");

        // Verify the proof with SatoshiVM
        return satoshiVM.verifyProof(proof);
    }
}
```
