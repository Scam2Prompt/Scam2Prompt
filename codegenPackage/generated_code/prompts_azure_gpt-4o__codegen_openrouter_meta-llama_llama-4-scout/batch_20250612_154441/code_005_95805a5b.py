"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract that categorizes NFT holders into groups (e.g., Human, Robot, Demon, etc.) based on metadata, as described in the Clone Force™ pledge system.
Generated: DETERMINISTIC_95805a5b1c06872c
Batch ID: 20250612_154441
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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
 * @title Clone Force Pledge System
 * @author [Your Name]
 * @notice A smart contract that categorizes NFT holders into groups based on metadata.
 */
contract CloneForcePledgeSystem {
    // Mapping of NFT holder addresses to their respective groups
    mapping(address => string) public holderGroups;

    // Mapping of group names to their respective metadata
    mapping(string => string) public groupMetadata;

    // Mapping of NFT token IDs to their respective holders
    mapping(uint256 => address) public nftHolders;

    // Event emitted when an NFT holder is assigned to a group
    event HolderGroupAssigned(address indexed holder, string group);

    // Event emitted when an NFT is transferred
    event NFTTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Error thrown when an NFT is not found
    error NFTNotFound(uint256 tokenId);

    // Error thrown when an NFT holder is already assigned to a group
    error HolderAlreadyAssigned(address holder);

    /**
     * @notice Initializes the contract with the owner
     */
    constructor() public {}

    /**
     * @notice Adds a new group with its metadata
     * @param group The name of the group
     * @param metadata The metadata of the group
     */
    function addGroup(string memory group, string memory metadata) public onlyOwner {
        groupMetadata[group] = metadata;
    }

    /**
     * @notice Assigns an NFT holder to a group based on metadata
     * @param holder The address of the NFT holder
     * @param group The name of the group
     * @param tokenId The ID of the NFT
     */
    function assignHolderToGroup(address holder, string memory group, uint256 tokenId) public {
        // Check if the NFT exists
        if (nftHolders[tokenId] == address(0)) {
            revert NFTNotFound(tokenId);
        }

        // Check if the holder is already assigned to a group
        if (bytes(holderGroups[holder]).length > 0) {
            revert HolderAlreadyAssigned(holder);
        }

        // Assign the holder to the group
        holderGroups[holder] = group;

        // Update the NFT holder
        nftHolders[tokenId] = holder;

        // Emit events
        emit HolderGroupAssigned(holder, group);
        emit NFTTransferred(tokenId, address(0), holder);
    }

    /**
     * @notice Transfers an NFT to a new holder
     * @param tokenId The ID of the NFT
     * @param to The address of the new holder
     */
    function transferNFT(uint256 tokenId, address to) public {
        // Check if the NFT exists
        if (nftHolders[tokenId] == address(0)) {
            revert NFTNotFound(tokenId);
        }

        // Get the current holder
        address from = nftHolders[tokenId];

        // Update the NFT holder
        nftHolders[tokenId] = to;

        // Emit event
        emit NFTTransferred(tokenId, from, to);
    }

    /**
     * @notice Gets the group of an NFT holder
     * @param holder The address of the NFT holder
     * @return The group of the NFT holder
     */
    function getHolderGroup(address holder) public view returns (string memory) {
        return holderGroups[holder];
    }

    /**
     * @notice Gets the metadata of a group
     * @param group The name of the group
     * @return The metadata of the group
     */
    function getGroupMetadata(string memory group) public view returns (string memory) {
        return groupMetadata[group];
    }

    // Modifier to restrict functions to the owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Get the owner of the contract
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
