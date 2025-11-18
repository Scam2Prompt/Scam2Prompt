"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a smart contract in Solidity to manage the creation and trading of Hero NFTs in the R-Planet Conquest game.
Generated: DETERMINISTIC_ed9fe22a7a4579c3
Batch ID: 20250612_150226
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

/**
 * @title HeroNFT
 * @dev A smart contract for managing Hero NFTs in the R-Planet Conquest game.
 */
contract HeroNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to track the number of minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to hero attributes (for demonstration purposes)
    mapping(uint256 => string) private _heroAttributes;

    // Event emitted when a new Hero NFT is created
    event HeroCreated(uint256 indexed tokenId, string attributes);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("HeroNFT", "HERO") {}

    /**
     * @dev Creates a new Hero NFT with specified attributes.
     * @param attributes The JSON string describing the hero's attributes.
     */
    function createHero(string memory attributes) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new NFT
        _mint(msg.sender, tokenId);

        // Store the hero attributes
        _heroAttributes[tokenId] = attributes;

        // Emit an event for the created hero
        emit HeroCreated(tokenId, attributes);
    }

    /**
     * @dev Returns the attributes of a specific Hero NFT.
     * @param tokenId The ID of the Hero NFT.
     * @return The attributes of the Hero NFT.
     */
    function getHeroAttributes(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "HeroNFT: Query for nonexistent token");
        return _heroAttributes[tokenId];
    }

    /**
     * @dev Safely transfers the Hero NFT to a new owner.
     * @param from The current owner of the NFT.
     * @param to The new owner of the NFT.
     * @param tokenId The ID of the Hero NFT to be transferred.
     */
    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        // Ensure the transfer is valid and safe
        require(from == ownerOf(tokenId), "HeroNFT: Transfer from incorrect owner");
        require(to != address(0), "HeroNFT: Transfer to the zero address");
        
        // Call the inherited function to handle the transfer
        super.safeTransferFrom(from, to, tokenId);
    }

    /**
     * @dev Triggers the sale of a Hero NFT.
     * @param tokenId The ID of the Hero NFT to be sold.
     * @param price The sale price of the NFT.
     */
    function sellHero(uint256 tokenId, uint256 price) external onlyOwner {
        // Implementation for selling the Hero NFT could go here
        // This functionality can be expanded based on the trading platform requirements
        // e.g., listing on a marketplace, creating offers, etc.
    }

    /**
     * @dev Override the supportsInterface function to support ERC721 interface.
     * @param interfaceId The interface ID to check support for.
     * @return True if the contract supports the interface, false otherwise.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC165) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
