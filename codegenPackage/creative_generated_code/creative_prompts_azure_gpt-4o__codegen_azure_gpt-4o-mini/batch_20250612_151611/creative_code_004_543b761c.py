"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberkongz.live
Prompt: Write Solidity code for a smart contract that mimics the functionality of CyberKongz NFTs, including metadata storage and token minting.
Generated: DETERMINISTIC_543b761cf3186c94
Batch ID: 20250612_151611
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cyberkongz.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title CyberKongzNFT - A smart contract for minting CyberKongz-like NFTs
// @notice This contract allows for NFT minting and metadata storage
contract CyberKongzNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for generating token IDs
    Counters.Counter private _tokenIdCounter;

    // Structure to store metadata for each NFT
    struct KongzMetadata {
        string name;
        string description;
        string imageURI; // URI for the NFT image
    }

    // Mapping from token ID to its metadata
    mapping(uint256 => KongzMetadata) private _tokenMetadata;

    // Event emitted when a new NFT is minted
    event KongzMinted(uint256 indexed tokenId, address owner, string name);

    // @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("CyberKongz", "KONGZ") {}

    // @dev Function to mint a new NFT
    // @param name The name of the NFT
    // @param description The description of the NFT
    // @param imageURI The URI of the NFT image
    function mintKongz(string memory name, string memory description, string memory imageURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store the metadata
        _tokenMetadata[tokenId] = KongzMetadata(name, description, imageURI);

        // Emit the minting event
        emit KongzMinted(tokenId, msg.sender, name);
    }

    // @dev Function to get the metadata of a specific NFT by token ID
    // @param tokenId The ID of the token to retrieve metadata for
    // @return name The name of the NFT
    // @return description The description of the NFT
    // @return imageURI The URI of the NFT image
    function getKongzMetadata(uint256 tokenId) external view returns (string memory name, string memory description, string memory imageURI) {
        // Ensure the token exists
        require(_exists(tokenId), "Query for nonexistent token");

        KongzMetadata memory metadata = _tokenMetadata[tokenId];
        return (metadata.name, metadata.description, metadata.imageURI);
    }

    // @dev Override the base URI function for standardized metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.cyberkongz.com/metadata/";
    }

    // @dev Function to retrieve the total number of minted NFTs
    // @return The total count of minted NFTs
    function totalKongzMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
