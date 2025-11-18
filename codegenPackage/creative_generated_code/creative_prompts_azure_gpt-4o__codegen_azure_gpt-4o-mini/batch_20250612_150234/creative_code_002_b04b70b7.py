"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity that incorporates DOP's flexible transparency mechanism to allow users to selectively share asset data.
Generated: DETERMINISTIC_b04b70b74530439f
Batch ID: 20250612_150234
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

// Importing the OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title AssetTransparency
 * @dev A smart contract that allows users to selectively share asset data using DOP's flexible transparency mechanism.
 */
contract AssetTransparency is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold asset information
    struct Asset {
        uint256 id;
        string data;
        address owner;
        bool isVisible;
    }

    // Mapping from asset ID to Asset struct
    mapping(uint256 => Asset) private assets;
    // Counter to generate unique asset IDs
    Counters.Counter private assetIdCounter;

    // Event emitted when an asset is created
    event AssetCreated(uint256 indexed assetId, address indexed owner, string data);
    
    // Event emitted when asset visibility is changed
    event AssetVisibilityChanged(uint256 indexed assetId, bool isVisible);

    /**
     * @dev Creates a new asset with the given data, visible by default.
     * @param _data The data associated with the asset.
     */
    function createAsset(string memory _data) public {
        // Increment the asset ID counter
        assetIdCounter.increment();
        uint256 newAssetId = assetIdCounter.current();

        // Create a new asset
        assets[newAssetId] = Asset({
            id: newAssetId,
            data: _data,
            owner: msg.sender,
            isVisible: true
        });

        // Emit the asset creation event
        emit AssetCreated(newAssetId, msg.sender, _data);
    }

    /**
     * @dev Changes the visibility of the asset.
     * @param _assetId The ID of the asset.
     * @param _isVisible The new visibility state of the asset.
     */
    function setAssetVisibility(uint256 _assetId, bool _isVisible) public {
        // Ensure the caller is the owner of the asset
        require(assets[_assetId].owner == msg.sender, "Only the asset owner can change visibility");
        // Update the asset's visibility
        assets[_assetId].isVisible = _isVisible;

        // Emit the visibility change event
        emit AssetVisibilityChanged(_assetId, _isVisible);
    }

    /**
     * @dev Retrieves asset data if the asset is visible.
     * @param _assetId The ID of the asset.
     * @return The asset data if visible, otherwise an empty string.
     */
    function getAssetData(uint256 _assetId) public view returns (string memory) {
        // Check if the asset is visible
        require(assets[_assetId].isVisible, "Asset data is not visible");
        
        // Return the asset data
        return assets[_assetId].data;
    }

    /**
     * @dev Retrieves the owner of the asset.
     * @param _assetId The ID of the asset.
     * @return The address of the asset owner.
     */
    function getAssetOwner(uint256 _assetId) public view returns (address) {
        // Return the asset owner's address
        return assets[_assetId].owner;
    }

    /**
     * @dev Checks if the asset is visible.
     * @param _assetId The ID of the asset.
     * @return True if the asset is visible, false otherwise.
     */
    function isAssetVisible(uint256 _assetId) public view returns (bool) {
        return assets[_assetId].isVisible;
    }
}
```
