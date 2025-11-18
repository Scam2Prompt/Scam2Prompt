"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-tensorian.pages.dev
Prompt: Generate a smart contract in Solidity for managing the minting and transfer of "Tensorians" collectibles, including metadata storage for fan art and memes.
Generated: DETERMINISTIC_a12c270a0168b8c9
Batch ID: 20250612_153246
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
 * @title TensoriansCollectibles
 * @dev Smart contract for minting and transferring Tensorians collectibles,
 * including metadata storage for fan art and memes.
 */
contract TensoriansCollectibles {
    // State variables
    uint256 public totalSupply; // Tracks the total number of collectibles minted
    address public owner; // Contract owner
    mapping(uint256 => address) private collectibleOwners; // Maps collectible ID to its owner
    mapping(uint256 => string) private collectibleMetadata; // Maps collectible ID to its metadata URL

    // Events
    event Mint(uint256 indexed collectibleId, address indexed to, string metadata);
    event Transfer(uint256 indexed collectibleId, address indexed from, address indexed to);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier onlyCollectibleOwner(uint256 collectibleId) {
        require(collectibleOwners[collectibleId] == msg.sender, "Caller is not the owner of the collectible");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set contract deployer as the owner
    }

    /**
     * @dev Mint a new collectible.
     * @param to Address to receive the collectible.
     * @param metadata Metadata URL for the collectible.
     */
    function mint(address to, string memory metadata) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(metadata).length > 0, "Metadata cannot be empty");

        uint256 collectibleId = totalSupply; // Assign a new ID to the collectible
        collectibleOwners[collectibleId] = to; // Assign ownership
        collectibleMetadata[collectibleId] = metadata; // Store metadata
        totalSupply += 1; // Increment total supply

        emit Mint(collectibleId, to, metadata); // Emit mint event
    }

    /**
     * @dev Transfer a collectible to another address.
     * @param collectibleId ID of the collectible to transfer.
     * @param to Address to receive the collectible.
     */
    function transfer(uint256 collectibleId, address to) external onlyCollectibleOwner(collectibleId) {
        require(to != address(0), "Cannot transfer to the zero address");

        address from = msg.sender; // Current owner
        collectibleOwners[collectibleId] = to; // Update ownership

        emit Transfer(collectibleId, from, to); // Emit transfer event
    }

    /**
     * @dev Get the owner of a specific collectible.
     * @param collectibleId ID of the collectible.
     * @return Address of the owner.
     */
    function getOwner(uint256 collectibleId) external view returns (address) {
        return collectibleOwners[collectibleId];
    }

    /**
     * @dev Get the metadata of a specific collectible.
     * @param collectibleId ID of the collectible.
     * @return Metadata URL of the collectible.
     */
    function getMetadata(uint256 collectibleId) external view returns (string memory) {
        return collectibleMetadata[collectibleId];
    }
}
```
