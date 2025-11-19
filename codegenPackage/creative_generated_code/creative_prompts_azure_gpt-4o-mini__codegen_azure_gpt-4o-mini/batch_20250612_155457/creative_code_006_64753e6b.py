"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipmbway.pages.dev
Prompt: Write a Solidity contract that facilitates the minting of GEM NFTs backed by physical gold allocations.
Generated: DETERMINISTIC_64753e6b68cfb1cf
Batch ID: 20250612_155457
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GEMNFT
 * @dev A contract that facilitates the minting of GEM NFTs backed by physical gold allocations
 */
contract GEMNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a GEM NFT with associated gold allocation
    struct GoldAllocation {
        uint256 amount; // Amount of gold allocated (in grams)
        string location; // Storage location of the physical gold
        bool isActive; // Status of the gold allocation
    }

    // Mapping from token ID to gold allocation details
    mapping(uint256 => GoldAllocation) private _goldAllocations;

    // Event emitted when a new GEM NFT is minted
    event GEMMinted(address indexed owner, uint256 indexed tokenId, uint256 amount, string location);

    /**
     * @dev Constructor that sets the name and symbol of the NFT
     */
    constructor() ERC721("GEMNFT", "GEM") {}

    /**
     * @dev Mint a new GEM NFT backed by a specific gold allocation
     * @param amount The amount of gold allocated (in grams)
     * @param location The storage location of the physical gold
     */
    function mint(uint256 amount, string memory location) external onlyOwner {
        require(amount > 0, "Amount of gold must be greater than zero");
        require(bytes(location).length > 0, "Location must be provided");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        // Create a new gold allocation
        _goldAllocations[tokenId] = GoldAllocation({
            amount: amount,
            location: location,
            isActive: true
        });

        emit GEMMinted(msg.sender, tokenId, amount, location);

        // Increment the token ID counter
        _tokenIdCounter.increment();
    }

    /**
     * @dev Retrieve gold allocation details for a specific token ID
     * @param tokenId The ID of the token to query
     * @return amount The amount of gold allocated
     * @return location The location of the physical gold
     * @return isActive The status of the gold allocation
     */
    function getGoldAllocation(uint256 tokenId) external view returns (uint256 amount, string memory location, bool isActive) {
        GoldAllocation memory allocation = _goldAllocations[tokenId];
        require(allocation.isActive, "This gold allocation is not active");

        return (allocation.amount, allocation.location, allocation.isActive);
    }

    /**
     * @dev Deactivate a gold allocation for a specific token ID (only the owner can do this)
     * @param tokenId The ID of the token to deactivate
     */
    function deactivateGoldAllocation(uint256 tokenId) external onlyOwner {
        GoldAllocation storage allocation = _goldAllocations[tokenId];
        require(allocation.isActive, "This gold allocation is already inactive");
        
        allocation.isActive = false; // Mark as inactive
    }
}
```
