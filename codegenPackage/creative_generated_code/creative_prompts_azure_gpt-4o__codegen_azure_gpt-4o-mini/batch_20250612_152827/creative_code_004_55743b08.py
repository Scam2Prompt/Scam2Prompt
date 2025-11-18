"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Develop a smart contract in Solidity that incorporates rarity traits for NFTs, similar to the KevinLand approach of generating NFTs from dozens of traits.
Generated: DETERMINISTIC_55743b0871d548d0
Batch ID: 20250612_152827
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title RarityNFT
// @dev A smart contract for minting NFTs with rarity traits
contract RarityNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to define rarity traits
    struct Trait {
        string name;          // Name of the trait
        uint256 rarity;      // Rarity score (higher means rarer)
    }

    // Mapping from token ID to its traits
    mapping(uint256 => Trait[]) private _tokenTraits;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, Trait[] traits);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("RarityNFT", "RNFT") {}

    // Function to mint a new NFT with traits
    // @param traits The array of traits associated with the NFT
    function mintNFT(Trait[] calldata traits) external onlyOwner {
        require(traits.length > 0, "Must have at least one trait");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new NFT
        _safeMint(msg.sender, tokenId);

        // Store the traits for the newly minted NFT
        _tokenTraits[tokenId] = traits;

        // Emit the token minted event
        emit TokenMinted(tokenId, traits);
    }

    // Function to retrieve traits for a given token ID
    // @param tokenId The ID of the token to retrieve traits for
    // @return traits The array of traits associated with the token
    function getTokenTraits(uint256 tokenId) external view returns (Trait[] memory traits) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }

    // Function to get the total number of minted NFTs
    // @return count Total number of minted NFTs
    function totalSupply() public view returns (uint256 count) {
        return _tokenIdCounter.current();
    }

    // Override the base URI for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.example.com/metadata/";
    }
}
```
