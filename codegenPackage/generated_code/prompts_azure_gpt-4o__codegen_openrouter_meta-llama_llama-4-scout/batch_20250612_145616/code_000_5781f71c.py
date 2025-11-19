"""
Generated Code Metadata:
========================
Original URL: https://somnial.pages.dev
Prompt: Write a smart contract using Somnia's EVM Layer 1 blockchain to enable interoperability between two metaverses, ensuring seamless asset transfer and user interaction.
Generated: DETERMINISTIC_5781f71c55144d2a
Batch ID: 20250612_145616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Metaverse Interoperability Contract
 * @author [Your Name]
 * @notice Enables interoperability between two metaverses, allowing for seamless asset transfer and user interaction.
 */
contract MetaverseInteroperability {
    // Mapping of metaverse IDs to their respective asset contracts
    mapping(uint256 => address) public metaverseAssets;

    // Mapping of user IDs to their respective balances in each metaverse
    mapping(uint256 => mapping(address => uint256)) public userBalances;

    // Mapping of asset IDs to their respective owners in each metaverse
    mapping(uint256 => mapping(uint256 => address)) public assetOwners;

    // Event emitted when an asset is transferred between metaverses
    event AssetTransferred(uint256 indexed metaverseId, uint256 indexed assetId, address indexed from, address to);

    // Event emitted when a user interacts with an asset in a metaverse
    event UserInteracted(uint256 indexed metaverseId, uint256 indexed assetId, address indexed user);

    /**
     * @dev Initializes the contract with the metaverse IDs and their respective asset contracts.
     * @param _metaverseIds The IDs of the metaverses to enable interoperability for.
     * @param _metaverseAssets The addresses of the asset contracts for each metaverse.
     */
    constructor(uint256[] memory _metaverseIds, address[] memory _metaverseAssets) public {
        require(_metaverseIds.length == _metaverseAssets.length, "Metaverse IDs and asset contracts must have the same length");

        for (uint256 i = 0; i < _metaverseIds.length; i++) {
            metaverseAssets[_metaverseIds[i]] = _metaverseAssets[i];
        }
    }

    /**
     * @dev Transfers an asset from one metaverse to another.
     * @param _metaverseId The ID of the metaverse to transfer the asset from.
     * @param _assetId The ID of the asset to transfer.
     * @param _toMetaverseId The ID of the metaverse to transfer the asset to.
     * @param _to The address of the user to transfer the asset to.
     */
    function transferAsset(uint256 _metaverseId, uint256 _assetId, uint256 _toMetaverseId, address _to) public {
        // Check if the asset exists in the source metaverse
        require(assetOwners[_metaverseId][_assetId] != address(0), "Asset does not exist in source metaverse");

        // Check if the user is the owner of the asset
        require(assetOwners[_metaverseId][_assetId] == msg.sender, "User is not the owner of the asset");

        // Transfer the asset to the destination metaverse
        assetOwners[_toMetaverseId][_assetId] = _to;
        assetOwners[_metaverseId][_assetId] = address(0);

        // Update user balances
        userBalances[_metaverseId][msg.sender] -= 1;
        userBalances[_toMetaverseId][_to] += 1;

        // Emit events
        emit AssetTransferred(_metaverseId, _assetId, msg.sender, _to);
        emit UserInteracted(_toMetaverseId, _assetId, _to);
    }

    /**
     * @dev Allows a user to interact with an asset in a metaverse.
     * @param _metaverseId The ID of the metaverse to interact with.
     * @param _assetId The ID of the asset to interact with.
     */
    function interactWithAsset(uint256 _metaverseId, uint256 _assetId) public {
        // Check if the asset exists in the metaverse
        require(assetOwners[_metaverseId][_assetId] != address(0), "Asset does not exist in metaverse");

        // Emit event
        emit UserInteracted(_metaverseId, _assetId, msg.sender);
    }

    /**
     * @dev Adds a new metaverse to the contract.
     * @param _metaverseId The ID of the metaverse to add.
     * @param _metaverseAsset The address of the asset contract for the metaverse.
     */
    function addMetaverse(uint256 _metaverseId, address _metaverseAsset) public onlyOwner {
        metaverseAssets[_metaverseId] = _metaverseAsset;
    }

    /**
     * @dev Removes a metaverse from the contract.
     * @param _metaverseId The ID of the metaverse to remove.
     */
    function removeMetaverse(uint256 _metaverseId) public onlyOwner {
        delete metaverseAssets[_metaverseId];
    }

    /**
     * @dev Updates the asset contract for a metaverse.
     * @param _metaverseId The ID of the metaverse to update.
     * @param _metaverseAsset The new address of the asset contract for the metaverse.
     */
    function updateMetaverseAsset(uint256 _metaverseId, address _metaverseAsset) public onlyOwner {
        metaverseAssets[_metaverseId] = _metaverseAsset;
    }
}
```
