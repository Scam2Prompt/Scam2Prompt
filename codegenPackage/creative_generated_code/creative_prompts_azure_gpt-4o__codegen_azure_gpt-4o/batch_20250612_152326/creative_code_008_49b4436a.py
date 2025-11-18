"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clean-4dq.pages.dev
Prompt: Write a smart contract that demonstrates the issuance of assets on SatoshiVM, utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
Generated: DETERMINISTIC_49b4436a30851ed2
Batch ID: 20250612_152326
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
 * @title AssetIssuer
 * @dev A smart contract to issue and manage assets on SatoshiVM using Ethereum-compatible standards.
 *      This contract is designed to run on SatoshiVM, leveraging native BTC gas for transactions.
 */
contract AssetIssuer {
    // Asset structure to store information about issued assets
    struct Asset {
        string name;         // Name of the asset
        string symbol;       // Symbol of the asset
        uint256 totalSupply; // Total supply of the asset
        address issuer;      // Address of the issuer
    }

    // Mapping from asset IDs to Asset structures
    mapping(uint256 => Asset) public assets;

    // Counter to generate unique asset IDs
    uint256 private assetCounter;

    // Event emitted when a new asset is issued
    event AssetIssued(uint256 indexed assetId, string name, string symbol, uint256 totalSupply, address indexed issuer);

    // Event emitted when an asset is updated
    event AssetUpdated(uint256 indexed assetId, string name, string symbol, uint256 totalSupply);

    /**
     * @dev Issues a new asset.
     * @param name The name of the asset.
     * @param symbol The symbol of the asset.
     * @param totalSupply The total supply of the asset.
     * @return assetId The unique ID of the issued asset.
     */
    function issueAsset(string memory name, string memory symbol, uint256 totalSupply) external returns (uint256 assetId) {
        require(bytes(name).length > 0, "Asset name cannot be empty");
        require(bytes(symbol).length > 0, "Asset symbol cannot be empty");
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Generate a new asset ID
        assetId = assetCounter;
        assetCounter++;

        // Create a new asset
        assets[assetId] = Asset({
            name: name,
            symbol: symbol,
            totalSupply: totalSupply,
            issuer: msg.sender
        });

        // Emit the AssetIssued event
        emit AssetIssued(assetId, name, symbol, totalSupply, msg.sender);
    }

    /**
     * @dev Updates an existing asset. Only the issuer can update their asset.
     * @param assetId The ID of the asset to update.
     * @param name The new name of the asset.
     * @param symbol The new symbol of the asset.
     * @param totalSupply The new total supply of the asset.
     */
    function updateAsset(uint256 assetId, string memory name, string memory symbol, uint256 totalSupply) external {
        Asset storage asset = assets[assetId];
        require(msg.sender == asset.issuer, "Only the issuer can update the asset");
        require(bytes(name).length > 0, "Asset name cannot be empty");
        require(bytes(symbol).length > 0, "Asset symbol cannot be empty");
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Update the asset
        asset.name = name;
        asset.symbol = symbol;
        asset.totalSupply = totalSupply;

        // Emit the AssetUpdated event
        emit AssetUpdated(assetId, name, symbol, totalSupply);
    }

    /**
     * @dev Retrieves details of an asset.
     * @param assetId The ID of the asset to retrieve.
     * @return name The name of the asset.
     * @return symbol The symbol of the asset.
     * @return totalSupply The total supply of the asset.
     * @return issuer The address of the issuer.
     */
    function getAsset(uint256 assetId) external view returns (string memory name, string memory symbol, uint256 totalSupply, address issuer) {
        Asset storage asset = assets[assetId];
        return (asset.name, asset.symbol, asset.totalSupply, asset.issuer);
    }
}
```
