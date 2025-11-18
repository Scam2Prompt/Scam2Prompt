"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: Write a Solidity function that uses DOP to implement zero-knowledge KYC for identity verification while maintaining user privacy.
Generated: DETERMINISTIC_6bc744cf23186184
Batch ID: 20250612_151931
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

interface IDopKYC {
    function verifyIdentity(address user, bytes calldata proof) external returns (bool);
}

contract ZeroKnowledgeKYC {
    // Mapping to track verified identities
    mapping(address => bool) private verifiedUsers;

    // Instance of the DOP contract for KYC verification
    IDopKYC private dopKYC;

    // Event emitted when a user is verified
    event UserVerified(address indexed user);

    // Constructor to set the DOP KYC contract address
    constructor(address _dopKYCAddress) {
        require(_dopKYCAddress != address(0), "Invalid DOP KYC address");
        dopKYC = IDopKYC(_dopKYCAddress);
    }

    /**
     * @dev Function to verify user identity using zero-knowledge proof.
     * @param proof The zero-knowledge proof provided by the user.
     */
    function verifyUser(bytes calldata proof) external {
        // Check if the user is already verified
        require(!verifiedUsers[msg.sender], "User already verified");

        // Call the DOP contract to verify the identity
        bool isVerified = dopKYC.verifyIdentity(msg.sender, proof);
        require(isVerified, "Identity verification failed");

        // Mark the user as verified
        verifiedUsers[msg.sender] = true;

        // Emit a UserVerified event
        emit UserVerified(msg.sender);
    }

    /**
     * @dev Function to check if a user is verified.
     * @param user The address of the user to check.
     * @return bool indicating verification status.
     */
    function isUserVerified(address user) external view returns (bool) {
        return verifiedUsers[user];
    }
}
```
