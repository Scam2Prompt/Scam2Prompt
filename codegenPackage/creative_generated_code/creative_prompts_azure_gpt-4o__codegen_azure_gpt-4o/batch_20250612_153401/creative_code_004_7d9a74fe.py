"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessepollak-ebv.pages.dev
Prompt: Write a smart contract in Solidity that allows users to connect their wallets and verify ownership of an Ethereum-based domain, such as jesse.xyz.
Generated: DETERMINISTIC_7d9a74fe904527aa
Batch ID: 20250612_153401
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
 * @title DomainOwnershipVerifier
 * @dev Smart contract to verify ownership of Ethereum-based domains.
 *      Users can connect their wallets and prove ownership of their domains.
 */
contract DomainOwnershipVerifier {
    // Event emitted when a domain ownership is verified
    event DomainOwnershipVerified(address indexed owner, string domain);

    // Mapping to store verified domain ownerships
    mapping(string => address) private domainOwners;

    /**
     * @notice Verify ownership of a domain by signing and submitting the domain name.
     * @param domain The domain name to verify (e.g., "jesse.xyz").
     * @param signature The ECDSA signature proving domain ownership.
     * @dev This function checks the signed message and verifies if the sender owns the domain.
     */
    function verifyDomainOwnership(string calldata domain, bytes calldata signature) external {
        require(bytes(domain).length > 0, "Domain cannot be empty.");
        require(signature.length > 0, "Signature cannot be empty.");

        // Recreate the message hash
        bytes32 messageHash = keccak256(abi.encodePacked(domain));

        // Recover the signer from the signature
        address signer = recoverSigner(messageHash, signature);

        require(signer == msg.sender, "Signer does not match sender.");
        require(domainOwners[domain] == address(0), "Domain is already verified.");

        // Store the verified ownership
        domainOwners[domain] = msg.sender;

        // Emit the verification event
        emit DomainOwnershipVerified(msg.sender, domain);
    }

    /**
     * @notice Retrieve the owner of a verified domain.
     * @param domain The domain name to query (e.g., "jesse.xyz").
     * @return The address of the domain owner, or address(0) if not verified.
     */
    function getDomainOwner(string calldata domain) external view returns (address) {
        return domainOwners[domain];
    }

    /**
     * @notice Recover the signer from a message hash and signature.
     * @param messageHash The hash of the signed message.
     * @param signature The ECDSA signature.
     * @return The address of the signer.
     * @dev Uses the ECDSA library to recover the signer.
     */
    function recoverSigner(bytes32 messageHash, bytes memory signature) internal pure returns (address) {
        require(signature.length == 65, "Invalid signature length.");

        bytes32 r;
        bytes32 s;
        uint8 v;

        // Extract the r, s, and v values from the signature
        assembly {
            r := mload(add(signature, 0x20))
            s := mload(add(signature, 0x40))
            v := byte(0, mload(add(signature, 0x60)))
        }

        // Return the recovered signer address
        return ecrecover(messageHash, v, r, s);
    }
}
```
