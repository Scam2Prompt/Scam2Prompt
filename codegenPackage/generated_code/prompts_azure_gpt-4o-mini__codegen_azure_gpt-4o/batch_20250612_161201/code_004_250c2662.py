"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: Illustrate how to implement a KYC verification process in a decentralized application like DeeLance using blockchain technology.
Generated: DETERMINISTIC_250c2662685fa67c
Batch ID: 20250612_161201
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

/**
 * @title KYCVerification
 * @dev A smart contract for implementing KYC verification in a decentralized application.
 *      This contract allows users to submit their KYC data, which is verified by an admin.
 */
contract KYCVerification {
    // Struct to store user KYC data
    struct KYCData {
        string fullName; // Full name of the user
        string documentHash; // Hash of the KYC document (e.g., IPFS hash)
        bool isVerified; // Verification status
    }

    // Mapping to store KYC data for each user (address => KYCData)
    mapping(address => KYCData) public kycRecords;

    // Address of the admin responsible for verifying KYC data
    address public admin;

    // Event emitted when a user submits KYC data
    event KYCSubmitted(address indexed user, string fullName, string documentHash);

    // Event emitted when KYC data is verified by the admin
    event KYCVerified(address indexed user);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Modifier to ensure the user has submitted KYC data
    modifier hasSubmittedKYC(address user) {
        require(bytes(kycRecords[user].fullName).length > 0, "KYC data not submitted");
        _;
    }

    /**
     * @dev Constructor to set the admin address.
     * @param _admin Address of the admin.
     */
    constructor(address _admin) {
        require(_admin != address(0), "Invalid admin address");
        admin = _admin;
    }

    /**
     * @dev Function for users to submit their KYC data.
     * @param _fullName Full name of the user.
     * @param _documentHash Hash of the KYC document (e.g., IPFS hash).
     */
    function submitKYC(string memory _fullName, string memory _documentHash) external {
        require(bytes(_fullName).length > 0, "Full name cannot be empty");
        require(bytes(_documentHash).length > 0, "Document hash cannot be empty");

        // Store the KYC data in the mapping
        kycRecords[msg.sender] = KYCData({
            fullName: _fullName,
            documentHash: _documentHash,
            isVerified: false
        });

        emit KYCSubmitted(msg.sender, _fullName, _documentHash);
    }

    /**
     * @dev Function for the admin to verify a user's KYC data.
     * @param user Address of the user whose KYC data is to be verified.
     */
    function verifyKYC(address user) external onlyAdmin hasSubmittedKYC(user) {
        // Mark the user's KYC data as verified
        kycRecords[user].isVerified = true;

        emit KYCVerified(user);
    }

    /**
     * @dev Function to check if a user's KYC data is verified.
     * @param user Address of the user.
     * @return True if the user's KYC data is verified, false otherwise.
     */
    function isKYCVerified(address user) external view returns (bool) {
        return kycRecords[user].isVerified;
    }
}
```
