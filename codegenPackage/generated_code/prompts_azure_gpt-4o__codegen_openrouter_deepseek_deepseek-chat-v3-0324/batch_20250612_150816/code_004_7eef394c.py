"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Provide an example of how to implement a "trusted by uForce" verification system in a DeFi application, as referenced on the DefyApps website.
Generated: DETERMINISTIC_7eef394c2b43c8ac
Batch ID: 20250612_150816
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
 * @title TrustedByUForceVerifier
 * @dev Implements a verification system for DeFi applications to check if they are trusted by uForce
 */
contract TrustedByUForceVerifier is Ownable {
    using ECDSA for bytes32;

    // Address of the uForce verification signer
    address public uForceSigner;

    // Mapping of verified contracts
    mapping(address => bool) public isVerified;

    // Events
    event ContractVerified(address indexed contractAddress);
    event VerificationRevoked(address indexed contractAddress);
    event SignerUpdated(address indexed newSigner);

    /**
     * @dev Constructor sets the initial uForce signer address
     * @param _uForceSigner The address authorized to sign verification messages
     */
    constructor(address _uForceSigner) {
        require(_uForceSigner != address(0), "Invalid signer address");
        uForceSigner = _uForceSigner;
    }

    /**
     * @dev Verifies a contract using a signature from uForce
     * @param _contractAddress The address of the contract to verify
     * @param _signature The signature from uForce
     */
    function verifyContract(address _contractAddress, bytes memory _signature) external {
        require(_contractAddress != address(0), "Invalid contract address");
        require(!isVerified[_contractAddress], "Contract already verified");

        bytes32 messageHash = keccak256(abi.encodePacked(_contractAddress));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();

        address recoveredSigner = ethSignedMessageHash.recover(_signature);
        require(recoveredSigner == uForceSigner, "Invalid signature");

        isVerified[_contractAddress] = true;
        emit ContractVerified(_contractAddress);
    }

    /**
     * @dev Revokes verification for a contract (only owner)
     * @param _contractAddress The address of the contract to revoke
     */
    function revokeVerification(address _contractAddress) external onlyOwner {
        require(isVerified[_contractAddress], "Contract not verified");
        isVerified[_contractAddress] = false;
        emit VerificationRevoked(_contractAddress);
    }

    /**
     * @dev Updates the uForce signer address (only owner)
     * @param _newSigner The new signer address
     */
    function updateSigner(address _newSigner) external onlyOwner {
        require(_newSigner != address(0), "Invalid signer address");
        uForceSigner = _newSigner;
        emit SignerUpdated(_newSigner);
    }

    /**
     * @dev Checks if a contract is verified by uForce
     * @param _contractAddress The address to check
     * @return bool Whether the contract is verified
     */
    function checkVerification(address _contractAddress) external view returns (bool) {
        return isVerified[_contractAddress];
    }
}
```
