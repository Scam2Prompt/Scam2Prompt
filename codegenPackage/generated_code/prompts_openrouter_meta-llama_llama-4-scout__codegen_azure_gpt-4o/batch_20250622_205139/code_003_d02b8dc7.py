"""
Generated Code Metadata:
========================
Original URL: https://opensea.com
Prompt: Design a smart contract using Solidity to create and manage an NFT collection on OpenSea, including functions for minting and transferring NFTs.
Generated: DETERMINISTIC_d02b8dc76e0ec740
Batch ID: 20250622_205139
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

// Importing OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFTCollection
/// @dev A smart contract for creating and managing an NFT collection compatible with OpenSea.
contract NFTCollection is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @notice Constructor to initialize the NFT collection
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Function to mint a new NFT
    /// @dev Only the owner can mint new NFTs
    /// @param to Address to receive the minted NFT
    function mint(address to) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);
    }

    /// @notice Function to set the base URI for metadata
    /// @dev Only the owner can set the base URI
    /// @param baseTokenURI The new base URI
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Override function to return the base URI
    /// @return The base URI for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Function to transfer an NFT
    /// @dev Wrapper around the ERC721 transferFrom function
    /// @param from Address of the current owner
    /// @param to Address of the new owner
    /// @param tokenId ID of the token to transfer
    function transferNFT(address from, address to, uint256 tokenId) external {
        // Ensure the caller is the owner of the token or approved
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the token
        transferFrom(from, to, tokenId);
    }

    /// @notice Function to get the current token ID counter
    /// @return The current token ID
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
