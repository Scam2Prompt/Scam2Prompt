"""
Generated Code Metadata:
========================
Original URL: https://deepseachain.online
Prompt: Generate a smart contract code snippet in Solidity to create a simple NFT with provable authenticity and ownership, similar to those on DeepSea.
Generated: DETERMINISTIC_b4fd07c1c6d4785e
Batch ID: 20250622_212702
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title SimpleNFT
/// @dev A basic NFT contract with provable authenticity and ownership
contract SimpleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @notice Constructor to initialize the NFT contract
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /// @notice Function to mint a new NFT
    /// @dev Only the owner of the contract can mint new tokens
    /// @param to Address to receive the minted NFT
    function mintNFT(address to) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);
    }

    /// @notice Override the base URI function to return the custom base URI
    /// @return Base URI for the metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Function to update the base URI for metadata
    /// @dev Only the owner of the contract can update the base URI
    /// @param baseURI New base URI for the metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Function to get the current token ID counter value
    /// @return Current token ID counter value
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

This code snippet uses OpenZeppelin's libraries for secure and standardized implementation of ERC721 (NFT) functionality. It includes features for minting NFTs, setting a base URI for metadata, and tracking token IDs.
