"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles-baby-ape-club.nfts2.me
Prompt: Generate a code snippet for a smart contract that verifies NFT ownership and checks for intellectual property rights compliance.
Generated: DETERMINISTIC_d8d15e0f70ce7a44
Batch ID: 20250612_140255
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
 * @title NFTIPComplianceChecker
 * @dev A smart contract for verifying NFT ownership and intellectual property rights compliance.
 * This contract assumes that the NFT follows ERC721 standard.
 */
contract NFTIPComplianceChecker {

    // Event to log compliance checks
    event ComplianceChecked(address indexed owner, uint256 indexed tokenId, bool isCompliant);

    // Interface for ERC721 NFT contract
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    // Mapping to hold intellectual property rights compliance data per token
    mapping(address => mapping(uint256 => bool)) public ipComplianceRegistry;

    /**
     * @dev Function to set intellectual property compliance for an NFT.
     * @param nftContract Address of the ERC721 contract.
     * @param tokenId ID of the token.
     * @param isCompliant Boolean flag indicating compliance.
     */
    function setCompliance(
        address nftContract,
        uint256 tokenId,
        bool isCompliant
    ) external {
        require(nftContract != address(0), "Invalid contract address");
        require(tokenId > 0, "Invalid token ID");

        // Update compliance registry
        ipComplianceRegistry[nftContract][tokenId] = isCompliant;
    }

    /**
     * @dev Function to verify NFT ownership and intellectual property compliance.
     * @param nftContract Address of the ERC721 contract.
     * @param tokenId ID of the token.
     * @return isOwner Boolean indicating ownership.
     * @return isCompliant Boolean indicating compliance.
     */
    function verifyNFTCompliance(
        address nftContract,
        uint256 tokenId
    ) external view returns (bool isOwner, bool isCompliant) {
        require(nftContract != address(0), "Invalid contract address");
        require(tokenId > 0, "Invalid token ID");

        try IERC721(nftContract).ownerOf(tokenId) returns (address owner) {
            // Check ownership
            isOwner = (owner == msg.sender);

            // Check compliance
            isCompliant = ipComplianceRegistry[nftContract][tokenId];

        } catch {
            // Handle error if the NFT contract does not implement ownerOf properly
            isOwner = false;
            isCompliant = false;
        }

        // Emit event for compliance check
        emit ComplianceChecked(msg.sender, tokenId, isOwner && isCompliant);
    }
}
```
