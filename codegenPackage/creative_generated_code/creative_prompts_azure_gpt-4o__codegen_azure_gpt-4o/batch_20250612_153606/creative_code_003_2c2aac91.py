"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneymintpinnacles.firebaseapp.com
Prompt: Write a smart contract in Solidity for minting NFTs, referencing the Disney Pinnacle use case of exclusive digital pins.
Generated: DETERMINISTIC_2c2aac9192e9e333
Batch ID: 20250612_153606
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
 * @title DisneyPinnacleNFT
 * @dev This contract allows minting of exclusive digital pins (NFTs) inspired by the Disney Pinnacle use case.
 *      It is based on the ERC721 standard, with functionality for minting, ownership, and metadata management.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract DisneyPinnacleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Mapping to track NFT properties (e.g., rarity)
    mapping(uint256 => string) public tokenProperties;

    /**
     * @dev Constructor to set up the contract name, symbol, and maximum supply.
     * @param name Name of the NFT collection (e.g., "Disney Pinnacle Pins").
     * @param symbol Symbol representing the NFT collection (e.g., "DPP").
     * @param _maxSupply Maximum number of NFTs that can be minted.
     */
    constructor(string memory name, string memory symbol, uint256 _maxSupply) ERC721(name, symbol) {
        require(_maxSupply > 0, "Max supply must be greater than 0");
        maxSupply = _maxSupply;
    }

    /**
     * @dev Sets the base URI for metadata.
     * @param baseURI URI prefix to be used for all token metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override _baseURI to return the set base URI.
     * @return Base URI string for token metadata.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT with optional properties.
     * @param to Address to receive the NFT.
     * @param properties Optional metadata or properties for the token (e.g., rarity).
     */
    function mint(address to, string memory properties) external onlyOwner {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(to, tokenId);

        // Assign properties to the token
        tokenProperties[tokenId] = properties;
    }

    /**
     * @dev Get the total number of minted tokens so far.
     * @return Total number of tokens minted.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
