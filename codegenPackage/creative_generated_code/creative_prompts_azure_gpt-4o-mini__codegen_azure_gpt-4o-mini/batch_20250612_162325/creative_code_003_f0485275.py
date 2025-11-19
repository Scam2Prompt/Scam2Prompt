"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Describe how to use the ERC404 standard in the context of evolving NFTs through on-chain activity in the Monarch Dungeon.
Generated: DETERMINISTIC_f048527539a1c026
Batch ID: 20250612_162325
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC404 standard
interface IERC404 {
    function evolve(uint256 tokenId, uint256 newPower) external;
}

// The Monarch Dungeon contract implementing the ERC404 standard for evolving NFTs
contract MonarchDungeon is IERC404, IERC721Metadata, Ownable {
    using Counters for Counters.Counter;

    // Struct representing an NFT
    struct NFT {
        string name;
        string description;
        uint256 power;
    }

    // Mapping from token ID to NFT data
    mapping(uint256 => NFT) private _nfts;
    // Mapping to track owner of each token
    mapping(uint256 => address) private _owners;
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Event to emit when an NFT evolves
    event NFTEvolved(uint256 indexed tokenId, uint256 newPower);

    // Returns the name of the token
    function name() external pure override returns (string memory) {
        return "Monarch Dungeon NFT";
    }

    // Returns the symbol of the token
    function symbol() external pure override returns (string memory) {
        return "MDNFT";
    }

    // Function to mint a new NFT
    function mint(string memory name_, string memory description_) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _nfts[tokenId] = NFT(name_, description_, 1); // Start with a base power of 1
        _owners[tokenId] = msg.sender;
        _tokenIdCounter.increment();
    }

    // Function to evolve an NFT's power
    function evolve(uint256 tokenId, uint256 newPower) external override {
        require(_owners[tokenId] == msg.sender, "You do not own this NFT");
        require(newPower > _nfts[tokenId].power, "New power must be greater than current power");

        // Update the power of the NFT
        _nfts[tokenId].power = newPower;

        // Emit an event for the evolution
        emit NFTEvolved(tokenId, newPower);
    }

    // Function to get NFT details
    function getNFT(uint256 tokenId) external view returns (string memory, string memory, uint256) {
        require(tokenId < _tokenIdCounter.current(), "NFT does not exist");
        NFT memory nft = _nfts[tokenId];
        return (nft.name, nft.description, nft.power);
    }

    // Function to get the owner of an NFT
    function ownerOf(uint256 tokenId) external view returns (address) {
        require(tokenId < _tokenIdCounter.current(), "NFT does not exist");
        return _owners[tokenId];
    }
}
```
