"""
Generated Code Metadata:
========================
Original URL: https://multihelp.pages.dev
Prompt: Develop a Solidity smart contract for a decentralized application that ensures immutability and secure asset transactions, following DAPP SHIELD's decentralized framework.
Generated: DETERMINISTIC_c928462ed47cb5c0
Batch ID: 20250612_151310
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
 * @title DAppShield
 * @dev A secure and immutable decentralized application contract for asset transactions
 * following DAPP SHIELD's decentralized framework.
 */
contract DAppShield {
    // Contract owner
    address private immutable owner;

    // Asset structure
    struct Asset {
        uint256 id;
        address owner;
        string metadata;
        bool isLocked;
    }

    // Mapping of asset ID to Asset
    mapping(uint256 => Asset) private assets;

    // Mapping of owner to their asset IDs
    mapping(address => uint256[]) private ownerAssets;

    // Event declarations
    event AssetCreated(uint256 indexed id, address indexed owner, string metadata);
    event AssetTransferred(uint256 indexed id, address indexed from, address indexed to);
    event AssetLocked(uint256 indexed id, bool locked);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to check if caller is owner
    modifier onlyOwner() {
        require(msg.sender == owner, "DAppShield: caller is not the owner");
        _;
    }

    // Modifier to check if asset exists
    modifier assetExists(uint256 _id) {
        require(assets[_id].id != 0, "DAppShield: asset does not exist");
        _;
    }

    // Modifier to check if asset is not locked
    modifier notLocked(uint256 _id) {
        require(!assets[_id].isLocked, "DAppShield: asset is locked");
        _;
    }

    /**
     * @dev Constructor sets the deployer as the initial owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new asset with the given metadata
     * @param _metadata Metadata associated with the asset
     * @return The ID of the newly created asset
     */
    function createAsset(string memory _metadata) external returns (uint256) {
        uint256 newId = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, _metadata)));
        
        require(assets[newId].id == 0, "DAppShield: asset ID collision");
        
        assets[newId] = Asset({
            id: newId,
            owner: msg.sender,
            metadata: _metadata,
            isLocked: false
        });

        ownerAssets[msg.sender].push(newId);
        
        emit AssetCreated(newId, msg.sender, _metadata);
        return newId;
    }

    /**
     * @dev Transfers ownership of an asset to another address
     * @param _id ID of the asset to transfer
     * @param _to Address to transfer the asset to
     */
    function transferAsset(uint256 _id, address _to) external assetExists(_id) notLocked(_id) {
        require(assets[_id].owner == msg.sender, "DAppShield: caller is not the asset owner");
        require(_to != address(0), "DAppShield: cannot transfer to zero address");

        address previousOwner = assets[_id].owner;
        assets[_id].owner = _to;

        // Remove asset from previous owner's list
        uint256[] storage previousOwnerAssets = ownerAssets[previousOwner];
        for (uint256 i = 0; i < previousOwnerAssets.length; i++) {
            if (previousOwnerAssets[i] == _id) {
                previousOwnerAssets[i] = previousOwnerAssets[previousOwnerAssets.length - 1];
                previousOwnerAssets.pop();
                break;
            }
        }

        // Add asset to new owner's list
        ownerAssets[_to].push(_id);

        emit AssetTransferred(_id, previousOwner, _to);
    }

    /**
     * @dev Locks or unlocks an asset
     * @param _id ID of the asset to lock/unlock
     * @param _locked Boolean indicating whether to lock or unlock
     */
    function setAssetLock(uint256 _id, bool _locked) external assetExists(_id) {
        require(assets[_id].owner == msg.sender, "DAppShield: caller is not the asset owner");
        assets[_id].isLocked = _locked;
        emit AssetLocked(_id, _locked);
    }

    /**
     * @dev Gets asset details by ID
     * @param _id ID of the asset to retrieve
     * @return Asset details
     */
    function getAsset(uint256 _id) external view assetExists(_id) returns (Asset memory) {
        return assets[_id];
    }

    /**
     * @dev Gets all asset IDs owned by an address
     * @param _owner Address to query
     * @return Array of asset IDs
     */
    function getAssetsByOwner(address _owner) external view returns (uint256[] memory) {
        return ownerAssets[_owner];
    }

    /**
     * @dev Transfers contract ownership to a new address
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "DAppShield: new owner is the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        // Note: owner is immutable, so this is just for event logging
    }

    /**
     * @dev Returns the current owner of the contract
     * @return Address of the owner
     */
    function getOwner() external view returns (address) {
        return owner;
    }
}
```
