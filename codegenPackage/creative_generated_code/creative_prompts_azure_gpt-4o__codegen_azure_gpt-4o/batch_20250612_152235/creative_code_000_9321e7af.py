"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs with unique identifiers, inspired by the roadmap of the Cyber Lama NFT collection project. Ensure the contract includes mechanisms for limiting circulation and verifying uniqueness.
Generated: DETERMINISTIC_9321e7af94cf4825
Batch ID: 20250612_152235
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

/// @title CyberLamaNFT - A smart contract for minting unique NFTs inspired by the Cyber Lama roadmap.
/// @dev This contract uses OpenZeppelin's ERC721 implementation for NFT functionality.
contract CyberLamaNFT is ERC721, Ownable {
    // Maximum supply of NFTs that can ever be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Counter to track the total number of NFTs minted
    uint256 private _totalMinted;

    // Mapping to ensure each NFT is unique
    mapping(uint256 => bool) private _uniqueIdentifiers;

    // Event emitted when a new NFT is successfully minted
    event NFTMinted(address indexed to, uint256 tokenId);

    /// @notice Constructor to initialize the NFT contract with a name and symbol.
    /// @param name Name of the NFT collection.
    /// @param symbol Symbol for the NFT collection.
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new NFT with a unique identifier.
    /// @dev Only the contract owner can mint NFTs, and the number of NFTs minted cannot exceed MAX_SUPPLY.
    /// @param to The address to receive the minted NFT.
    /// @param tokenId A unique identifier for the NFT.
    function mint(address to, uint256 tokenId) external onlyOwner {
        // Ensure the total minted does not exceed the maximum supply
        require(_totalMinted < MAX_SUPPLY, "Maximum supply reached");

        // Ensure the tokenId is unique
        require(!_uniqueIdentifiers[tokenId], "Token ID already exists");

        // Mark the tokenId as used
        _uniqueIdentifiers[tokenId] = true;

        // Mint the NFT
        _safeMint(to, tokenId);

        // Increment the total minted counter
        _totalMinted++;

        // Emit the minting event
        emit NFTMinted(to, tokenId);
    }

    /// @notice Function to retrieve the total number of NFTs minted.
    /// @return The total number of NFTs minted so far.
    function totalMinted() external view returns (uint256) {
        return _totalMinted;
    }

    /// @notice Function to check if a tokenId has already been assigned.
    /// @param tokenId The identifier to check for uniqueness.
    /// @return True if the tokenId is already used, false otherwise.
    function isTokenIdUsed(uint256 tokenId) external view returns (bool) {
        return _uniqueIdentifiers[tokenId];
    }
}
```
