"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Create a Solidity contract for minting 9,999 unique Rebel Satoshi NFTs, ensuring each NFT has distinct metadata and represents the categories "Citizens," "Warriors," "Rebels," "Monarchs," and "Recusants."
Generated: DETERMINISTIC_8b8d51e55b018dab
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Rebel Satoshi NFT Contract
/// @author Your Name
/// @notice This contract mints unique Rebel Satoshi NFTs
/// @dev Inherits from ERC721Enumerable and Ownable, ensures uniqueness through mappings and arrays
contract RebelSatoshiNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking minted NFT IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs allowed
    uint256 public constant MAX_SUPPLY = 9999;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to store metadata categories for each token
    mapping(uint256 => string) private _tokenCategories;

    // Array of possible categories
    string[] private _categories = ["Citizens", "Warriors", "Rebels", "Monarchs", "Recusants"];

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, string category);

    /// @dev Constructor to set the token name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /// @dev Mint a new NFT, ensuring unique metadata and category assignment
    /// @param to Address to receive the minted NFT
    /// @return tokenId The ID of the minted token
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        // Increment the token ID counter
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Select a random category for the NFT
        string memory category = _selectRandomCategory(tokenId);
        _tokenCategories[tokenId] = category;

        // Mint the NFT and assign it to the specified address
        _safeMint(to, tokenId);
        emit NFTMinted(tokenId, category);
    }

    /// @dev Selects a category based on the token ID
    /// @param tokenId The ID of the token to assign a category
    /// @return The selected category as a string
    function _selectRandomCategory(uint256 tokenId) internal view returns (string memory) {
        // Simple random selection based on modulo operation
        uint256 categoryIndex = tokenId % _categories.length;
        return _categories[categoryIndex];
    }

    /// @dev Returns the base URI for the NFT metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Updates the base URI for token metadata
    /// @param newBaseTokenURI The new base URI string
    function setBaseTokenURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI;
    }

    /// @dev Returns the category of a given token ID
    /// @param tokenId The ID of the token to query
    /// @return The category associated with the token ID
    function getTokenCategory(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _tokenCategories[tokenId];
    }
}
```
