"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a function in Solidity to randomly assign rare traits to NFTs during minting, inspired by the rare traits mentioned in Pumpkin Spice Moonbirds.
Generated: DETERMINISTIC_e49181fbfdaed75c
Batch ID: 20250612_151550
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract RareTraitsNFT is ERC721Enumerable, Ownable {
    // Struct to hold the traits of each NFT
    struct Traits {
        string color;
        string pattern;
        string accessory;
    }

    // Mapping from token ID to its traits
    mapping(uint256 => Traits) private _tokenTraits;

    // Arrays containing possible rare traits
    string[] private _colors = ["Red", "Blue", "Green", "Purple"]; // Add more colors
    string[] private _patterns = ["Striped", "Dotted", "Plain", "Checkered"]; // Add more patterns
    string[] private _accessories = ["Hat", "Sunglasses", "Scarf", "Earmuffs"]; // Add more accessories

    // Events
    event Minted(uint256 indexed tokenId, Traits traits);

    // Constructor that sets the name and symbol of the NFT collection
    constructor() ERC721("RareTraitsNFT", "RTNFT") {}

    /**
     * @dev Function to mint a new NFT with random traits.
     * @param to The address to receive the minted NFT. 
     */
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Get the next token ID
        require(to != address(0), "Cannot mint to zero address");

        // Assign random traits to the NFT
        Traits memory newTraits = _assignRandomTraits(tokenId);
        _tokenTraits[tokenId] = newTraits;

        // Mint the NFT
        _mint(to, tokenId);

        // Emit the Minted event with the traits
        emit Minted(tokenId, newTraits);
    }

    /**
     * @dev Internal function to assign random traits to an NFT.
     * @param tokenId The ID of the NFT being minted.
     * @return Traits The randomly assigned traits.
     */
    function _assignRandomTraits(uint256 tokenId) internal view returns (Traits memory) {
        // Seed the randomness using the block's timestamp and the tokenId
        uint256 randomness = uint256(keccak256(abi.encodePacked(block.timestamp, tokenId)));

        return Traits({
            color: _colors[randomness % _colors.length],
            pattern: _patterns[randomness % _patterns.length],
            accessory: _accessories[randomness % _accessories.length]
        });
    }

    /**
     * @dev Function to get the traits of a specific NFT.
     * @param tokenId The ID of the NFT to fetch traits for.
     * @return Traits The traits of the specified NFT.
     */
    function getTraits(uint256 tokenId) external view returns (Traits memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _tokenTraits[tokenId];
    }
}
```
