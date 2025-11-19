"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a Solidity contract that generates NFTs with 170+ traits and varying rarity, similar to the algorithmic generation process described for Robotos on the Robots NFT Minting website.
Generated: DETERMINISTIC_72dd87c33d4fe582
Batch ID: 20250612_153606
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

/// @title NFTCollection
/// @dev A contract for generating NFTs with various traits and rarity
contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Structure to hold trait information
    struct Trait {
        string name;
        uint256 rarity; // Rarity percentage (0-100)
    }

    // Mapping from token ID to its traits
    mapping(uint256 => Trait[]) private _tokenTraits;

    // Array to hold all possible traits
    Trait[] private _allTraits;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, Trait[] traits);

    constructor() ERC721("NFTCollection", "NFTC") {
        // Initialize traits (example traits, should be expanded to 170+)
        _allTraits.push(Trait("Background1", 20));
        _allTraits.push(Trait("Background2", 30));
        _allTraits.push(Trait("Body1", 25));
        _allTraits.push(Trait("Body2", 15));
        // Add more traits as needed...
    }

    /// @dev Mint a new NFT with randomly generated traits
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Generate traits for the new NFT
        Trait[] memory traits = _generateTraits();

        // Mint the NFT
        _safeMint(msg.sender, tokenId);
        _tokenTraits[tokenId] = traits;

        emit NFTMinted(tokenId, traits);
    }

    /// @dev Generate traits for the NFT based on rarity
    /// @return traits An array of traits assigned to the NFT
    function _generateTraits() private view returns (Trait[] memory) {
        uint256 totalTraits = _allTraits.length;
        uint256 selectedTraitsCount = 5; // Number of traits to assign

        Trait[] memory selectedTraits = new Trait[](selectedTraitsCount);
        uint256 index = 0;

        // Randomly select traits based on rarity
        for (uint256 i = 0; i < selectedTraitsCount; i++) {
            uint256 randomIndex = _random() % totalTraits;
            selectedTraits[index] = _allTraits[randomIndex];
            index++;
        }

        return selectedTraits;
    }

    /// @dev Generate a pseudo-random number
    /// @return A random number
    function _random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, _tokenIdCounter.current())));
    }

    /// @dev Get the traits of a specific NFT
    /// @param tokenId The ID of the NFT
    /// @return traits An array of traits associated with the NFT
    function getTraits(uint256 tokenId) external view returns (Trait[] memory traits) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }
}
```
