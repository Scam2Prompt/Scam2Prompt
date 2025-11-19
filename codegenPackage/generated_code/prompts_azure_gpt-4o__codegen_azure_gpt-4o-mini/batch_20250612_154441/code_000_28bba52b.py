"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract in Solidity that integrates a minting platform for NFTs, similar to the MintStone and Relic minting system described on Clone Force™.
Generated: DETERMINISTIC_28bba52bdab6d5b6
Batch ID: 20250612_154441
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

/**
 * @title NFTMintingPlatform
 * @dev A smart contract for minting NFTs with a simple minting platform.
 */
contract NFTMintingPlatform is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to track if a token is minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseTokenURI The base URI for the NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address that will own the minted NFT.
     * @return tokenId The ID of the minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Cannot mint to the zero address");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        tokenId = _tokenIdCounter.current();

        // Ensure the token ID is not already minted
        require(!_mintedTokens[tokenId], "Token ID already minted");

        // Mint the NFT
        _mint(to, tokenId);
        _mintedTokens[tokenId] = true;

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Function to set the base URI for the NFT metadata.
     * @param baseTokenURI The new base URI for the NFT metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to get the base URI for the NFT metadata.
     * @return The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
