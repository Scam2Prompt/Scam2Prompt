"""
Generated Code Metadata:
========================
Original URL: https://groovesup.pages.dev
Prompt: Write a Solidity contract for creating artist NFTs that can be sold in the GrooveUP marketplace, enabling artists to raise seed funds while rewarding fans for streaming and sharing their music.
Generated: DETERMINISTIC_d5096ed77f5cacc7
Batch ID: 20250612_145923
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ArtistNFT
 * @dev This contract allows artists to create NFTs that can be sold in the GrooveUP marketplace.
 *      It enables artists to raise seed funds while rewarding fans for streaming and sharing their music.
 */
contract ArtistNFT is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to artist's address
    mapping(uint256 => address) private _artists;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed artist, string tokenURI);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT collection.
     */
    constructor() ERC721("ArtistNFT", "ANFT") {}

    /**
     * @dev Function to create a new NFT for an artist.
     * @param artist The address of the artist creating the NFT.
     * @param tokenURI The metadata URI for the NFT.
     * @return tokenId The ID of the newly created NFT.
     */
    function createNFT(address artist, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        require(artist != address(0), "Artist address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and mint the NFT
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(artist, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _artists[tokenId] = artist;

        emit NFTCreated(tokenId, artist, tokenURI);
    }

    /**
     * @dev Function to get the artist of a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return artist The address of the artist.
     */
    function getArtist(uint256 tokenId) external view returns (address artist) {
        require(_exists(tokenId), "Token does not exist");
        return _artists[tokenId];
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the NFT.
     * @param tokenURI The metadata URI for the NFT.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        // This function can be overridden to implement a custom token URI storage
        // For simplicity, we are not implementing it here
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
