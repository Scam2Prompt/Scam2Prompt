"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: "Write a code snippet to verify proofs on Ethereum using Linea's zkEVM ecosystem, with a focus on saving gas fees and leveraging Linea's cryptographically secure zk infrastructure."
Generated: DETERMINISTIC_b8411fec6807f53e
Batch ID: 20250622_205751
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

// Import Linea's zkEVM verification interface
interface ILineaVerifier {
    function verifyProof(
        uint256[2] memory a,
        uint256[2][2] memory b,
        uint256[2] memory c,
        uint256[] memory input
    ) external view returns (bool);
}

contract LineaProofVerifier {
    address public lineaVerifierAddress;
    
    // Events for logging
    event ProofVerified(address indexed prover, bool isValid);
    event VerifierAddressUpdated(address newAddress);

    /**
     * @dev Constructor to set the initial Linea verifier address
     * @param _verifierAddress The address of Linea's zkEVM verifier contract
     */
    constructor(address _verifierAddress) {
        require(_verifierAddress != address(0), "Invalid verifier address");
        lineaVerifierAddress = _verifierAddress;
    }

    /**
     * @dev Updates the Linea verifier address
     * @param _newVerifierAddress The new address of Linea's zkEVM verifier contract
     */
    function updateVerifierAddress(address _newVerifierAddress) external {
        require(_newVerifierAddress != address(0), "Invalid verifier address");
        lineaVerifierAddress = _newVerifierAddress;
        emit VerifierAddressUpdated(_newVerifierAddress);
    }

    /**
     * @dev Verifies a zk proof using Linea's zkEVM infrastructure
     * @param a The first part of the proof
     * @param b The second part of the proof
     * @param c The third part of the proof
     * @param input The public inputs to the proof
     * @return isValid True if the proof is valid, false otherwise
     */
    function verifyProof(
        uint256[2] memory a,
        uint256[2][2] memory b,
        uint256[2] memory c,
        uint256[] memory input
    ) external returns (bool) {
        require(lineaVerifierAddress != address(0), "Verifier address not set");
        
        bool isValid = ILineaVerifier(lineaVerifierAddress).verifyProof(
            a,
            b,
            c,
            input
        );
        
        emit ProofVerified(msg.sender, isValid);
        return isValid;
    }

    /**
     * @dev Gas-efficient version of verifyProof that doesn't emit events
     * @param a The first part of the proof
     * @param b The second part of the proof
     * @param c The third part of the proof
     * @param input The public inputs to the proof
     * @return isValid True if the proof is valid, false otherwise
     */
    function verifyProofSilent(
        uint256[2] memory a,
        uint256[2][2] memory b,
        uint256[2] memory c,
        uint256[] memory input
    ) external view returns (bool) {
        require(lineaVerifierAddress != address(0), "Verifier address not set");
        return ILineaVerifier(lineaVerifierAddress).verifyProof(
            a,
            b,
            c,
            input
        );
    }
}
```
