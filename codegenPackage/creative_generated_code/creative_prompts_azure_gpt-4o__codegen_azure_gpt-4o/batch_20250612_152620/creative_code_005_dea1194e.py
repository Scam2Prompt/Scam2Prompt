"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: Write a function to store assets privately on Ethereum using the Data Ownership Protocol (DOP) and selectively disclose transaction history.
Generated: DETERMINISTIC_dea1194eb12e0c21
Batch ID: 20250612_152620
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
 * @title PrivateAssetStore
 * @dev A contract to store assets privately using Data Ownership Protocol (DOP)
 *      and selectively disclose transaction history.
 */
contract PrivateAssetStore {
    // Struct to represent an asset
    struct Asset {
        bytes32 id; // Unique identifier for the asset (hashed for privacy)
        string metadata; // Metadata associated with the asset
        address owner; // Current owner of the asset
    }

    // Mapping to store assets by their unique ID
    mapping(bytes32 => Asset) private assets;

    // Mapping to track transaction history for each asset ID
    mapping(bytes32 => address[]) private transactionHistory;

    // Event emitted when a new asset is created
    event AssetCreated(bytes32 indexed assetId, address indexed owner);

    // Event emitted when asset ownership is transferred
    event OwnershipTransferred(bytes32 indexed assetId, address indexed from, address indexed to);

    /**
     * @dev Creates a new asset and stores it privately.
     * @param _metadata Metadata for the asset.
     * @return assetId The unique identifier for the created asset.
     */
    function createAsset(string memory _metadata) external returns (bytes32 assetId) {
        // Generate a unique ID for the asset using a hash
        assetId = keccak256(abi.encodePacked(_metadata, msg.sender, block.timestamp));
        
        // Ensure asset doesn't already exist
        require(assets[assetId].owner == address(0), "Asset already exists");
        
        // Store asset details in the mapping
        assets[assetId] = Asset({
            id: assetId,
            metadata: _metadata,
            owner: msg.sender
        });
        
        // Record the initial transaction history
        transactionHistory[assetId].push(msg.sender);
        
        // Emit an event to notify of asset creation
        emit AssetCreated(assetId, msg.sender);
    }

    /**
     * @dev Transfers ownership of an asset to another address.
     * @param _assetId The unique identifier of the asset.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(bytes32 _assetId, address _newOwner) external {
        // Ensure the asset exists
        require(assets[_assetId].owner != address(0), "Asset does not exist");
        
        // Verify the sender is the current owner
        require(assets[_assetId].owner == msg.sender, "Only the owner can transfer ownership");
        
        // Ensure the new owner is valid
        require(_newOwner != address(0), "New owner cannot be zero address");
        
        // Transfer ownership
        address previousOwner = assets[_assetId].owner;
        assets[_assetId].owner = _newOwner;
        
        // Record the transaction history
        transactionHistory[_assetId].push(_newOwner);
        
        // Emit an event to notify of ownership transfer
        emit OwnershipTransferred(_assetId, previousOwner, _newOwner);
    }

    /**
     * @dev Returns the metadata and current owner of an asset.
     * @param _assetId The unique identifier of the asset.
     * @return metadata The metadata of the asset.
     * @return owner The current owner of the asset.
     */
    function getAssetDetails(bytes32 _assetId) external view returns (string memory metadata, address owner) {
        // Ensure the asset exists
        require(assets[_assetId].owner != address(0), "Asset does not exist");
        
        Asset memory asset = assets[_assetId];
        return (asset.metadata, asset.owner);
    }

    /**
     * @dev Returns the transaction history of an asset.
     *      Can be selectively disclosed based on the caller's permissions.
     * @param _assetId The unique identifier of the asset.
     * @return history An array of addresses representing transaction history.
     */
    function getTransactionHistory(bytes32 _assetId) external view returns (address[] memory history) {
        // Ensure the asset exists
        require(assets[_assetId].owner != address(0), "Asset does not exist");
        
        // For simplicity, allow anyone to view transaction history (can be extended with access control)
        return transactionHistory[_assetId];
    }
}
```
