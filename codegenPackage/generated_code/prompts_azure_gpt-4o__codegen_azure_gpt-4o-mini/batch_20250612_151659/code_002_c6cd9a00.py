"""
Generated Code Metadata:
========================
Original URL: https://enterart.rpmltech.com
Prompt: Develop a smart contract in Solidity for minting NFTs with metadata fields such as artist username, price, and type (visual, audio, video), as seen on enter.art.
Generated: DETERMINISTIC_c6cd9a003cec1392
Batch ID: 20250612_151659
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

// @title: NFTMintingContract
// @description: A smart contract for minting NFTs with metadata fields such as artist username, price, and type.

contract NFTMintingContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold NFT metadata
    struct NFTMetadata {
        string artistUsername;
        uint256 price;
        string mediaType; // e.g., "visual", "audio", "video"
    }

    // Mapping from token ID to NFT metadata
    mapping(uint256 => NFTMetadata) private _nftMetadata;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, string artistUsername, uint256 price, string mediaType);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("ArtNFT", "ANFT") {}

    // @notice: Mint a new NFT
    // @param artistUsername: The username of the artist
    // @param price: The price of the NFT
    // @param mediaType: The type of media (visual, audio, video)
    function mintNFT(string memory artistUsername, uint256 price, string memory mediaType) external onlyOwner {
        require(bytes(artistUsername).length > 0, "Artist username cannot be empty");
        require(price > 0, "Price must be greater than zero");
        require(keccak256(abi.encodePacked(mediaType)) == keccak256(abi.encodePacked("visual")) || 
                keccak256(abi.encodePacked(mediaType)) == keccak256(abi.encodePacked("audio")) || 
                keccak256(abi.encodePacked(mediaType)) == keccak256(abi.encodePacked("video")), 
                "Invalid media type");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store the metadata
        _nftMetadata[tokenId] = NFTMetadata(artistUsername, price, mediaType);

        // Emit the NFTMinted event
        emit NFTMinted(tokenId, artistUsername, price, mediaType);
    }

    // @notice: Retrieve NFT metadata by token ID
    // @param tokenId: The ID of the NFT
    // @return artistUsername: The username of the artist
    // @return price: The price of the NFT
    // @return mediaType: The type of media
    function getNFTMetadata(uint256 tokenId) external view returns (string memory artistUsername, uint256 price, string memory mediaType) {
        require(_exists(tokenId), "Token ID does not exist");

        NFTMetadata memory metadata = _nftMetadata[tokenId];
        return (metadata.artistUsername, metadata.price, metadata.mediaType);
    }
}
```
