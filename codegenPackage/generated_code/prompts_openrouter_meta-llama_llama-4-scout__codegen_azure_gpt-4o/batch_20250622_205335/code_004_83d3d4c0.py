"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Develop a smart contract to manage the commercial rights and licensing of unique digital assets, such as Nakamigos and Nakamigos-CLOAKS.
Generated: DETERMINISTIC_83d3d4c0fa41f755
Batch ID: 20250622_205335
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
 * @title DigitalAssetRightsManager
 * @dev A smart contract to manage commercial rights and licensing of unique digital assets.
 */
contract DigitalAssetRightsManager {
    // Struct to represent a digital asset
    struct DigitalAsset {
        string name; // Name of the asset
        string metadataURI; // URI pointing to metadata of the asset
        address owner; // Current owner of the asset
        bool isLicensed; // Whether the asset is licensed
        uint256 licenseFee; // Fee for licensing the asset
    }

    // Mapping to store digital assets by their unique ID
    mapping(uint256 => DigitalAsset) private assets;

    // Event emitted when a new asset is registered
    event AssetRegistered(uint256 indexed assetId, string name, address indexed owner);

    // Event emitted when an asset is licensed
    event AssetLicensed(uint256 indexed assetId, address indexed licensee, uint256 fee);

    // Event emitted when ownership of an asset is transferred
    event OwnershipTransferred(uint256 indexed assetId, address indexed previousOwner, address indexed newOwner);

    // Modifier to ensure only the owner of an asset can perform certain actions
    modifier onlyOwner(uint256 assetId) {
        require(assets[assetId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    /**
     * @dev Register a new digital asset.
     * @param assetId Unique ID of the asset.
     * @param name Name of the asset.
     * @param metadataURI URI pointing to metadata of the asset.
     */
    function registerAsset(uint256 assetId, string memory name, string memory metadataURI) external {
        require(assets[assetId].owner == address(0), "Asset ID already exists");

        assets[assetId] = DigitalAsset({
            name: name,
            metadataURI: metadataURI,
            owner: msg.sender,
            isLicensed: false,
            licenseFee: 0
        });

        emit AssetRegistered(assetId, name, msg.sender);
    }

    /**
     * @dev License a digital asset.
     * @param assetId Unique ID of the asset.
     */
    function licenseAsset(uint256 assetId) external payable {
        DigitalAsset storage asset = assets[assetId];
        require(asset.owner != address(0), "Asset does not exist");
        require(asset.isLicensed, "Asset is not available for licensing");
        require(msg.value >= asset.licenseFee, "Insufficient license fee");

        // Transfer license fee to the asset owner
        payable(asset.owner).transfer(msg.value);

        emit AssetLicensed(assetId, msg.sender, msg.value);
    }

    /**
     * @dev Set licensing details for an asset.
     * @param assetId Unique ID of the asset.
     * @param isLicensed Whether the asset is available for licensing.
     * @param licenseFee Fee for licensing the asset.
     */
    function setLicensingDetails(uint256 assetId, bool isLicensed, uint256 licenseFee) external onlyOwner(assetId) {
        DigitalAsset storage asset = assets[assetId];
        asset.isLicensed = isLicensed;
        asset.licenseFee = licenseFee;
    }

    /**
     * @dev Transfer ownership of an asset to another address.
     * @param assetId Unique ID of the asset.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(uint256 assetId, address newOwner) external onlyOwner(assetId) {
        require(newOwner != address(0), "New owner address cannot be zero");

        address previousOwner = assets[assetId].owner;
        assets[assetId].owner = newOwner;

        emit OwnershipTransferred(assetId, previousOwner, newOwner);
    }

    /**
     * @dev Get details of a digital asset.
     * @param assetId Unique ID of the asset.
     * @return name Name of the asset.
     * @return metadataURI URI pointing to metadata of the asset.
     * @return owner Current owner of the asset.
     * @return isLicensed Whether the asset is licensed.
     * @return licenseFee Fee for licensing the asset.
     */
    function getAssetDetails(uint256 assetId)
        external
        view
        returns (
            string memory name,
            string memory metadataURI,
            address owner,
            bool isLicensed,
            uint256 licenseFee
        )
    {
        DigitalAsset storage asset = assets[assetId];
        require(asset.owner != address(0), "Asset does not exist");

        return (asset.name, asset.metadataURI, asset.owner, asset.isLicensed, asset.licenseFee);
    }
}
```
