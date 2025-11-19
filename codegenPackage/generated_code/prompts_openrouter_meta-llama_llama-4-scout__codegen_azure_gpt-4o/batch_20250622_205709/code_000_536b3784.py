"""
Generated Code Metadata:
========================
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Write a smart contract in Solidity for a basic NFT implementation using the ERC721 standard, similar to CyberKongz.
Generated: DETERMINISTIC_536b3784d771ca38
Batch ID: 20250622_205709
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

// Import the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Basic NFT Smart Contract
/// @dev Implements ERC721 standard for NFTs
contract BasicNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @notice Constructor to initialize the NFT contract
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new NFT to a specified address
    /// @param to Address to receive the minted NFT
    function mint(address to) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Safely mint the new token
        _safeMint(to, tokenId);
    }

    /// @notice Set the base URI for metadata
    /// @param baseURI The base URI string
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Override the base URI function from ERC721
    /// @return The base URI string
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Get the current total supply of NFTs
    /// @return The total number of minted NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
