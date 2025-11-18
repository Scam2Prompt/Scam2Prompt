"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealworldcoin.com
Prompt: Create a Solidity smart contract that enables fractional ownership of real-world assets, inspired by the TRW platform's tokenization model.
Generated: DETERMINISTIC_866ca997101b54d6
Batch ID: 20250612_151624
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
 * @title FractionalOwnership
 * @dev A smart contract to facilitate fractional ownership of real-world assets.
 */
contract FractionalOwnership {
    // Struct to represent an asset
    struct Asset {
        string name; // Name of the asset
        uint256 totalShares; // Total shares available for the asset
        uint256 pricePerShare; // Price per share in wei
        address owner; // Owner of the asset
    }

    // Mapping of asset IDs to Asset details
    mapping(uint256 => Asset) public assets;

    // Mapping of asset IDs to shareholders and their share balances
    mapping(uint256 => mapping(address => uint256)) public shareholders;

    // Counter for asset IDs
    uint256 private assetCounter;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 assetId, string name, uint256 totalShares, uint256 pricePerShare, address owner);

    // Event emitted when shares are purchased
    event SharesPurchased(uint256 assetId, address buyer, uint256 shares);

    // Event emitted when shares are transferred
    event SharesTransferred(uint256 assetId, address from, address to, uint256 shares);

    /**
     * @notice Create a new asset for fractional ownership.
     * @param name Name of the asset.
     * @param totalShares Total shares available for the asset.
     * @param pricePerShare Price per share in wei.
     * @dev Only the creator of the asset becomes the initial owner.
     */
    function createAsset(
        string memory name,
        uint256 totalShares,
        uint256 pricePerShare
    ) external {
        require(totalShares > 0, "Total shares must be greater than zero.");
        require(pricePerShare > 0, "Price per share must be greater than zero.");

        assetCounter++;
        assets[assetCounter] = Asset({
            name: name,
            totalShares: totalShares,
            pricePerShare: pricePerShare,
            owner: msg.sender
        });

        // Assign all shares to the creator initially
        shareholders[assetCounter][msg.sender] = totalShares;

        emit AssetCreated(assetCounter, name, totalShares, pricePerShare, msg.sender);
    }

    /**
     * @notice Purchase shares of an asset.
     * @param assetId ID of the asset to purchase shares from.
     * @param shares Number of shares to purchase.
     */
    function purchaseShares(uint256 assetId, uint256 shares) external payable {
        require(assets[assetId].owner != address(0), "Asset does not exist.");
        require(shares > 0, "Shares must be greater than zero.");
        require(msg.value == shares * assets[assetId].pricePerShare, "Incorrect payment amount.");

        // Check if enough shares are available
        require(shareholders[assetId][assets[assetId].owner] >= shares, "Not enough shares available.");

        // Transfer shares to the buyer
        shareholders[assetId][assets[assetId].owner] -= shares;
        shareholders[assetId][msg.sender] += shares;

        // Transfer payment to the asset owner
        payable(assets[assetId].owner).transfer(msg.value);

        emit SharesPurchased(assetId, msg.sender, shares);
    }

    /**
     * @notice Transfer shares of an asset to another address.
     * @param assetId ID of the asset whose shares are being transferred.
     * @param to Address of the recipient.
     * @param shares Number of shares to transfer.
     */
    function transferShares(uint256 assetId, address to, uint256 shares) external {
        require(assets[assetId].owner != address(0), "Asset does not exist.");
        require(shares > 0, "Shares must be greater than zero.");
        require(shareholders[assetId][msg.sender] >= shares, "Insufficient shares.");

        // Update balances
        shareholders[assetId][msg.sender] -= shares;
        shareholders[assetId][to] += shares;

        emit SharesTransferred(assetId, msg.sender, to, shares);
    }

    /**
     * @notice Get the share balance of a specific address for a given asset.
     * @param assetId ID of the asset.
     * @param shareholder Address of the shareholder.
     * @return The share balance of the shareholder for the asset.
     */
    function getShareBalance(uint256 assetId, address shareholder) external view returns (uint256) {
        return shareholders[assetId][shareholder];
    }

    /**
     * @notice Get details of an asset.
     * @param assetId ID of the asset.
     * @return name Name of the asset.
     * @return totalShares Total shares of the asset.
     * @return pricePerShare Price per share of the asset.
     * @return owner Owner of the asset.
     */
    function getAssetDetails(uint256 assetId)
        external
        view
        returns (
            string memory name,
            uint256 totalShares,
            uint256 pricePerShare,
            address owner
        )
    {
        Asset memory asset = assets[assetId];
        require(asset.owner != address(0), "Asset does not exist.");
        return (asset.name, asset.totalShares, asset.pricePerShare, asset.owner);
    }
}
```
