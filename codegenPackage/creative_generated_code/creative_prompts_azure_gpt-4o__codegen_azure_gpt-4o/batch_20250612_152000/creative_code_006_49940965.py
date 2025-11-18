"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Write a smart contract in Solidity that utilizes the Metis Layer 2 infrastructure to enable affordable on-chain storage for NFT metadata.
Generated: DETERMINISTIC_499409653649197d
Batch ID: 20250612_152000
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
 * @title NFTMetadataStorage
 * @dev A smart contract to utilize Metis Layer 2 infrastructure for affordable on-chain storage of NFT metadata.
 *      This contract stores and manages metadata for NFTs on-chain in an economical way.
 *      Metis Layer 2 provides scalability and reduced gas fees for such operations.
 */
contract NFTMetadataStorage {
    // Event emitted whenever metadata is added or updated for an NFT
    event MetadataUpdated(uint256 indexed tokenId, string metadata);

    // Mapping to store metadata for each NFT (tokenId => metadata)
    mapping(uint256 => string) private _metadataStorage;

    // Owner of the contract (for administrative purposes)
    address private _owner;

    /**
     * @dev Modifier to restrict access to only the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == _owner, "Access denied: Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor that sets the deployer as the owner of the contract.
     */
    constructor() {
        _owner = msg.sender;
    }

    /**
     * @dev Function to store or update metadata for a specific NFT.
     * @param tokenId The unique identifier of the NFT.
     * @param metadata The metadata string to be stored for the NFT.
     */
    function setMetadata(uint256 tokenId, string memory metadata) external onlyOwner {
        // Input validation to ensure metadata is non-empty
        require(bytes(metadata).length > 0, "Metadata cannot be empty");

        // Store or update metadata in the mapping
        _metadataStorage[tokenId] = metadata;

        // Emit event to notify metadata update
        emit MetadataUpdated(tokenId, metadata);
    }

    /**
     * @dev Function to retrieve metadata for a specific NFT.
     * @param tokenId The unique identifier of the NFT.
     * @return metadata The metadata string associated with the given NFT.
     */
    function getMetadata(uint256 tokenId) external view returns (string memory metadata) {
        // Check if metadata exists for the given tokenId
        require(bytes(_metadataStorage[tokenId]).length > 0, "No metadata found for the given token ID");

        // Return the metadata for the given NFT
        return _metadataStorage[tokenId];
    }

    /**
     * @dev Function to transfer ownership of the contract to another address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        // Ensure the new owner address is valid
        require(newOwner != address(0), "New owner address cannot be zero");

        // Update the owner of the contract
        _owner = newOwner;
    }

    /**
     * @dev Function to retrieve the current owner of the contract.
     * @return owner The address of the current owner.
     */
    function getOwner() external view returns (address owner) {
        return _owner;
    }
}
```
