"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnial.pages.dev
Prompt: Write a smart contract using Somnia's EVM Layer 1 blockchain to enable interoperability between two metaverses, ensuring seamless asset transfer and user interaction.
Generated: DETERMINISTIC_5781f71c55144d2a
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Smart contract to enable interoperability between two metaverses on Somnia's EVM Layer 1 blockchain
contract MetaverseBridge {
    // Events for logging asset transfers and interactions
    event AssetTransferred(
        address indexed user,
        uint256 assetId,
        string sourceMetaverse,
        string targetMetaverse,
        uint256 timestamp
    );
    event UserInteracted(
        address indexed user,
        string sourceMetaverse,
        string targetMetaverse,
        string interactionType,
        uint256 timestamp
    );

    // Struct to represent a transferable asset
    struct Asset {
        uint256 id;
        address owner;
        string metadataURI; // Metadata URI for asset information
    }

    // Mapping to store registered assets
    mapping(uint256 => Asset) public assets;

    // Mapping to track authorized metaverses
    mapping(string => bool) public authorizedMetaverses;

    // Owner of the contract for administrative control
    address public owner;

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only owner allowed");
        _;
    }

    // Modifier to check if metaverse is authorized
    modifier onlyAuthorizedMetaverse(string memory metaverse) {
        require(
            authorizedMetaverses[metaverse],
            "Error: Metaverse not authorized"
        );
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to authorize a metaverse
    function authorizeMetaverse(string memory metaverseName)
        public
        onlyOwner
    {
        authorizedMetaverses[metaverseName] = true;
    }

    // Function to revoke metaverse authorization
    function revokeMetaverseAuthorization(string memory metaverseName)
        public
        onlyOwner
    {
        authorizedMetaverses[metaverseName] = false;
    }

    // Function to register an asset
    function registerAsset(
        uint256 assetId,
        string memory metadataURI
    ) public {
        require(
            assets[assetId].owner == address(0),
            "Error: Asset already registered"
        );

        // Register asset
        assets[assetId] = Asset({
            id: assetId,
            owner: msg.sender,
            metadataURI: metadataURI
        });
    }

    // Function to transfer an asset between metaverses
    function transferAsset(
        uint256 assetId,
        string memory sourceMetaverse,
        string memory targetMetaverse
    ) public onlyAuthorizedMetaverse(targetMetaverse) {
        Asset memory asset = assets[assetId];

        // Ensure only the owner of the asset can transfer it
        require(
            msg.sender == asset.owner,
            "Error: Only asset owner can transfer"
        );

        // Emit event for asset transfer
        emit AssetTransferred(
            msg.sender,
            assetId,
            sourceMetaverse,
            targetMetaverse,
            block.timestamp
        );

        // Logic for cross-metaverse transfer (placeholder)
        // Actual implementation would depend on the specific requirements of Somnia's EVM Layer 1
    }

    // Function to log user interactions across metaverses
    function logInteraction(
        string memory sourceMetaverse,
        string memory targetMetaverse,
        string memory interactionType
    ) public onlyAuthorizedMetaverse(targetMetaverse) {
        // Emit event for user interaction
        emit UserInteracted(
            msg.sender,
            sourceMetaverse,
            targetMetaverse,
            interactionType,
            block.timestamp
        );
    }

    // Function to update the metadata URI of an asset
    function updateAssetMetadata(uint256 assetId, string memory newMetadataURI)
        public
    {
        Asset storage asset = assets[assetId];

        // Ensure only the owner of the asset can update metadata
        require(
            msg.sender == asset.owner,
            "Error: Only asset owner can update metadata"
        );

        // Update the metadata URI
        asset.metadataURI = newMetadataURI;
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Error: Invalid new owner address");
        owner = newOwner;
    }
}
```
