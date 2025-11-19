"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity that incorporates DOP's flexible transparency mechanism to allow users to selectively share asset data.
Generated: DETERMINISTIC_b04b70b74530439f
Batch ID: 20250612_150234
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title FlexibleTransparencyContract
 * @dev A smart contract that implements DOP's flexible transparency mechanism
 * allowing users to selectively share asset data with specific addresses.
 */
contract FlexibleTransparencyContract is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    struct Asset {
        address owner;
        string data;
        bool isPublic;
    }

    // Mapping from asset ID to Asset
    mapping(uint256 => Asset) private _assets;

    // Mapping from asset ID to authorized viewers
    mapping(uint256 => EnumerableSet.AddressSet) private _authorizedViewers;

    // Counter for asset IDs
    uint256 private _assetCounter;

    // Events
    event AssetCreated(uint256 indexed assetId, address indexed owner);
    event AssetVisibilityChanged(uint256 indexed assetId, bool isPublic);
    event ViewerAdded(uint256 indexed assetId, address indexed viewer);
    event ViewerRemoved(uint256 indexed assetId, address indexed viewer);

    /**
     * @dev Creates a new asset with the given data.
     * @param data The asset data to store.
     * @return The ID of the newly created asset.
     */
    function createAsset(string memory data) external returns (uint256) {
        uint256 assetId = _assetCounter++;
        _assets[assetId] = Asset({
            owner: msg.sender,
            data: data,
            isPublic: false
        });

        emit AssetCreated(assetId, msg.sender);
        return assetId;
    }

    /**
     * @dev Sets the public visibility of an asset.
     * @param assetId The ID of the asset.
     * @param isPublic Whether the asset should be public or not.
     */
    function setAssetVisibility(uint256 assetId, bool isPublic) external {
        require(_assets[assetId].owner == msg.sender, "Not the asset owner");
        _assets[assetId].isPublic = isPublic;
        emit AssetVisibilityChanged(assetId, isPublic);
    }

    /**
     * @dev Authorizes an address to view a private asset.
     * @param assetId The ID of the asset.
     * @param viewer The address to authorize.
     */
    function addAuthorizedViewer(uint256 assetId, address viewer) external {
        require(_assets[assetId].owner == msg.sender, "Not the asset owner");
        require(!_assets[assetId].isPublic, "Asset is already public");
        require(_authorizedViewers[assetId].add(viewer), "Viewer already authorized");
        emit ViewerAdded(assetId, viewer);
    }

    /**
     * @dev Revokes authorization from an address to view a private asset.
     * @param assetId The ID of the asset.
     * @param viewer The address to revoke.
     */
    function removeAuthorizedViewer(uint256 assetId, address viewer) external {
        require(_assets[assetId].owner == msg.sender, "Not the asset owner");
        require(_authorizedViewers[assetId].remove(viewer), "Viewer not authorized");
        emit ViewerRemoved(assetId, viewer);
    }

    /**
     * @dev Retrieves asset data if the caller is authorized.
     * @param assetId The ID of the asset.
     * @return The asset data if authorized, otherwise reverts.
     */
    function getAssetData(uint256 assetId) external view returns (string memory) {
        Asset storage asset = _assets[assetId];
        require(
            asset.isPublic || 
            asset.owner == msg.sender || 
            _authorizedViewers[assetId].contains(msg.sender),
            "Not authorized to view this asset"
        );
        return asset.data;
    }

    /**
     * @dev Checks if an address is authorized to view an asset.
     * @param assetId The ID of the asset.
     * @param viewer The address to check.
     * @return True if authorized, false otherwise.
     */
    function isAuthorizedViewer(uint256 assetId, address viewer) external view returns (bool) {
        return _assets[assetId].isPublic || 
               _assets[assetId].owner == viewer || 
               _authorizedViewers[assetId].contains(viewer);
    }

    /**
     * @dev Gets the owner of an asset.
     * @param assetId The ID of the asset.
     * @return The owner's address.
     */
    function getAssetOwner(uint256 assetId) external view returns (address) {
        return _assets[assetId].owner;
    }

    /**
     * @dev Gets the public status of an asset.
     * @param assetId The ID of the asset.
     * @return True if public, false otherwise.
     */
    function isAssetPublic(uint256 assetId) external view returns (bool) {
        return _assets[assetId].isPublic;
    }
}
```
