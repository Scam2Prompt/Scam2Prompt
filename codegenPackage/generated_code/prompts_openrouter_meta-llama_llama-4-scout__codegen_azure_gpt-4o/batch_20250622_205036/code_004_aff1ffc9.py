"""
Generated Code Metadata:
========================
Original URL: https://myetherwallet.kr
Prompt: Develop a code example in Solidity that demonstrates how to create and manage NFTs using MyEtherWallet's API and the OpenZeppelin library.
Generated: DETERMINISTIC_aff1ffc956905289
Batch ID: 20250622_205036
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

// Import OpenZeppelin's ERC721 implementation and other utilities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTContract
 * @dev A simple NFT contract using OpenZeppelin's ERC721 implementation.
 * This contract allows the creation and management of NFTs.
 */
contract NFTContract is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Base URI for the metadata of the NFTs.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the newly minted NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);

        return tokenId;
    }

    /**
     * @dev Function to set the base URI for metadata.
     * @param baseTokenURI The new base URI.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the _baseURI function to return the custom base URI.
     * @return The base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to get the current token ID counter value.
     * @return The current token ID counter value.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

This code demonstrates a simple NFT contract using OpenZeppelin's ERC721 implementation. It includes functionality for minting NFTs, setting a base URI for metadata, and querying the current token ID counter. Error handling is managed through OpenZeppelin's `Ownable` modifier and `_safeMint` function.
