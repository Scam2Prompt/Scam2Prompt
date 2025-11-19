"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-farm-and-airdrop-project.nfts2.me
Prompt: How can I implement a smart contract to verify the authenticity of NFTs to avoid scams like the one reported on zksync-farm-and-airdrop-project?
Generated: DETERMINISTIC_382441c3683eb013
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFTVerifier
 * @dev A smart contract to verify the authenticity of NFTs to prevent scams and fraud
 */
contract NFTVerifier {
    // Mapping to track verified collections
    mapping(address => bool) public verifiedCollections;

    // Owner of the contract
    address public owner;

    // Event emitted when a collection is verified
    event CollectionVerified(address indexed collectionAddress);

    // Event emitted when a collection is revoked
    event CollectionRevoked(address indexed collectionAddress);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor that sets the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Verify an NFT collection as authentic
     * @param collectionAddress The address of the NFT collection contract
     */
    function verifyCollection(address collectionAddress) external onlyOwner {
        require(collectionAddress != address(0), "Invalid collection address");
        require(!verifiedCollections[collectionAddress], "Collection already verified");

        verifiedCollections[collectionAddress] = true;
        emit CollectionVerified(collectionAddress);
    }

    /**
     * @dev Revoke the verification of an NFT collection
     * @param collectionAddress The address of the NFT collection contract
     */
    function revokeCollection(address collectionAddress) external onlyOwner {
        require(collectionAddress != address(0), "Invalid collection address");
        require(verifiedCollections[collectionAddress], "Collection is not verified");

        verifiedCollections[collectionAddress] = false;
        emit CollectionRevoked(collectionAddress);
    }

    /**
     * @dev Check whether an NFT collection is verified
     * @param collectionAddress The address of the NFT collection contract
     * @return true if the collection is verified, false otherwise
     */
    function isCollectionVerified(address collectionAddress) external view returns (bool) {
        return verifiedCollections[collectionAddress];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
