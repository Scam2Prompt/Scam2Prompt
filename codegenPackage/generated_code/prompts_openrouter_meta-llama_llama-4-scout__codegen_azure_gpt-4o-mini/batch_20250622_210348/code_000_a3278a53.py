"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Write a smart contract code for minting NFTs with specific traits, similar to KevinLands, which has 10k unique NFTs generated from dozens of different traits.
Generated: DETERMINISTIC_a3278a534325ceec
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFTMintingContract
/// @dev A smart contract for minting unique NFTs with specific traits
contract NFTMintingContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Structure to hold NFT traits
    struct Trait {
        string name;
        string value;
    }

    // Mapping from token ID to its traits
    mapping(uint256 => Trait[]) private _tokenTraits;

    // Total supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, Trait[] traits);

    /// @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("UniqueNFT", "UNFT") {}

    /// @dev Function to mint a new NFT with specific traits
    /// @param traits An array of Trait structs representing the NFT's traits
    function mintNFT(Trait[] memory traits) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenTraits[tokenId] = traits;

        emit NFTMinted(tokenId, traits);
        _tokenIdCounter.increment();
    }

    /// @dev Function to retrieve the traits of a specific NFT
    /// @param tokenId The ID of the NFT
    /// @return An array of Trait structs associated with the NFT
    function getNFTTraits(uint256 tokenId) external view returns (Trait[] memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }

    /// @dev Function to get the total number of minted NFTs
    /// @return The total number of minted NFTs
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
