"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Write a smart contract to implement merchandising royalties for NFT holders, as mentioned in phase 3 of the "Cats World" roadmap.
Generated: DETERMINISTIC_6214c7f8ca7d803b
Batch ID: 20250612_150040
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
 * @title MerchandisingRoyalties
 * @dev Smart contract to implement merchandising royalties for NFT holders.
 * @dev This contract is designed for the "Cats World" roadmap, phase 3.
 */
contract MerchandisingRoyalties {
    // Struct to keep track of royalty distribution
    struct RoyaltyInfo {
        address nftHolder;
        uint256 percentage; // Percentage of the royalties (e.g., 5 for 5%)
    }

    // Mapping to store NFT holders' royalty information
    mapping(address => RoyaltyInfo) public royalties;

    // Event emitted when royalties are distributed
    event RoyaltyDistributed(address indexed nftHolder, uint256 amount);

    // Event emitted when a new royalty record is added
    event RoyaltyRecordAdded(address indexed nftHolder, uint256 percentage);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Modifier to ensure NFT holder exists
    modifier validRoyaltyHolder(address nftHolder) {
        require(royalties[nftHolder].percentage > 0, "NFT holder does not have a royalty record");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add or update royalty information for an NFT holder.
     * @param nftHolder Address of the NFT holder.
     * @param percentage Royalty percentage (e.g., 5 for 5%).
     */
    function addRoyaltyRecord(address nftHolder, uint256 percentage) external onlyOwner {
        require(nftHolder != address(0), "Invalid NFT holder address");
        require(percentage > 0 && percentage <= 100, "Percentage must be between 1 and 100");

        royalties[nftHolder] = RoyaltyInfo(nftHolder, percentage);

        emit RoyaltyRecordAdded(nftHolder, percentage);
    }

    /**
     * @dev Function to distribute royalties to all eligible NFT holders.
     * @param totalRevenue Total merchandising revenue to be distributed.
     */
    function distributeRoyalties(uint256 totalRevenue) external onlyOwner {
        require(totalRevenue > 0, "Revenue must be greater than zero");

        // Loop through all royalty holders and distribute their share
        for (address nftHolderAddress = address(0); nftHolderAddress < royalties.length!
