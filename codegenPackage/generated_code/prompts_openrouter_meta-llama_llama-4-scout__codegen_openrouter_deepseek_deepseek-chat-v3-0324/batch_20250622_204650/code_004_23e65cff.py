"""
Generated Code Metadata:
========================
Original URL: https://base-org.pages.dev
Prompt: Create a smart contract on Base using Base Camp resources, focusing on implementing CB Verifications for on-chain experiences.
Generated: DETERMINISTIC_23e65cff006c4a3a
Batch ID: 20250622_204650
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
 * @title CBVerification
 * @dev Smart contract for Coinbase Verifications on Base chain
 */
contract CBVerification is Ownable {
    using ECDSA for bytes32;

    // Verification status for each address
    mapping(address => bool) public isVerified;

    // Coinbase verification server address
    address public verificationServer;

    // Events
    event Verified(address indexed user);
    event VerificationRevoked(address indexed user);
    event VerificationServerUpdated(address newServer);

    /**
     * @dev Constructor
     * @param _verificationServer Address of the Coinbase verification server
     */
    constructor(address _verificationServer) {
        verificationServer = _verificationServer;
    }

    /**
     * @dev Verify a user's CB status using a signature from the verification server
     * @param signature Signature from the verification server
     * @param deadline Expiration timestamp for the signature
     */
    function verify(bytes memory signature, uint256 deadline) external {
        require(block.timestamp <= deadline, "CBVerification: Signature expired");
        require(!isVerified[msg.sender], "CBVerification: Already verified");

        bytes32 messageHash = keccak256(
            abi.encodePacked(msg.sender, deadline, address(this))
        );
        bytes32 ethSignedMessage = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessage.recover(signature);

        require(signer == verificationServer, "CBVerification: Invalid signature");

        isVerified[msg.sender] = true;
        emit Verified(msg.sender);
    }

    /**
     * @dev Revoke verification status (only callable by owner)
     * @param user Address to revoke verification from
     */
    function revokeVerification(address user) external onlyOwner {
        require(isVerified[user], "CBVerification: Not verified");
        isVerified[user] = false;
        emit VerificationRevoked(user);
    }

    /**
     * @dev Update the verification server address (only callable by owner)
     * @param newServer New verification server address
     */
    function updateVerificationServer(address newServer) external onlyOwner {
        require(newServer != address(0), "CBVerification: Invalid address");
        verificationServer = newServer;
        emit VerificationServerUpdated(newServer);
    }

    /**
     * @dev Check if an address is verified
     * @param user Address to check
     * @return bool True if verified, false otherwise
     */
    function checkVerification(address user) external view returns (bool) {
        return isVerified[user];
    }
}
```
