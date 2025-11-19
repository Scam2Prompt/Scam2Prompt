"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Propose an on-chain identity solution for permissioned and permissionless products on Singularity Finance, ensuring AML compliance."
Generated: DETERMINISTIC_7db9a641553cbdc3
Batch ID: 20250622_211721
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the identity verification service
interface IIdentityVerification {
    function verifyIdentity(address user) external returns (bool);
}

// On-chain identity solution for Singularity Finance
contract OnChainIdentity is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new identity is registered
    event IdentityRegistered(address indexed user, string identityHash);
    
    // Event emitted when an identity is verified
    event IdentityVerified(address indexed user, bool isVerified);

    // Struct to hold user identity information
    struct UserIdentity {
        string identityHash; // Hash of the user's identity document
        bool isVerified;      // Verification status
    }

    // Mapping of user addresses to their identity information
    mapping(address => UserIdentity) private identities;

    // Counter for tracking the number of registered identities
    Counters.Counter private identityCount;

    // Reference to the identity verification service
    IIdentityVerification public identityVerificationService;

    // Modifier to check if the identity is verified
    modifier onlyVerified() {
        require(identities[msg.sender].isVerified, "Identity not verified");
        _;
    }

    // Constructor to set the identity verification service
    constructor(address _identityVerificationService) {
        identityVerificationService = IIdentityVerification(_identityVerificationService);
    }

    // Function to register a new identity
    function registerIdentity(string memory _identityHash) external {
        require(bytes(_identityHash).length > 0, "Identity hash cannot be empty");
        require(bytes(identities[msg.sender].identityHash).length == 0, "Identity already registered");

        identities[msg.sender] = UserIdentity({
            identityHash: _identityHash,
            isVerified: false
        });

        identityCount.increment();
        emit IdentityRegistered(msg.sender, _identityHash);
    }

    // Function to verify the identity of a user
    function verifyIdentity() external onlyOwner {
        require(bytes(identities[msg.sender].identityHash).length > 0, "Identity not registered");

        bool isVerified = identityVerificationService.verifyIdentity(msg.sender);
        identities[msg.sender].isVerified = isVerified;

        emit IdentityVerified(msg.sender, isVerified);
    }

    // Function to get identity information of a user
    function getIdentity(address user) external view returns (string memory, bool) {
        UserIdentity memory userIdentity = identities[user];
        return (userIdentity.identityHash, userIdentity.isVerified);
    }

    // Function to update the identity hash (if needed)
    function updateIdentity(string memory _newIdentityHash) external onlyVerified {
        require(bytes(_newIdentityHash).length > 0, "New identity hash cannot be empty");
        identities[msg.sender].identityHash = _newIdentityHash;
    }

    // Function to remove identity (for compliance purposes)
    function removeIdentity() external onlyOwner {
        require(bytes(identities[msg.sender].identityHash).length > 0, "Identity not registered");
        delete identities[msg.sender];
        identityCount.decrement();
    }
}
```
