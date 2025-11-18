"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-9dc.pages.dev
Prompt: Write code in Solidity to implement an ERC-721 contract for Pepe 2.0 NFTs with metadata that reflects the "legend of the sequel" theme described on the website.
Generated: DETERMINISTIC_00ad966669235ed9
Batch ID: 20250612_151605
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Pepe2Token is an ERC721 contract representing Pepe 2.0 NFTs
contract Pepe2Token is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Counter for generating unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for the metadata
    string private _baseTokenURI;

    // Mapping from token ID to metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string metadata);

    // Constructor to initialize the contract with the token name and symbol
    constructor(string memory baseURI) ERC721("Pepe 2.0", "PEPE2") {
        _baseTokenURI = baseURI;
    }

    // Function to mint a new NFT
    function mintNFT(address to, string memory metadata) external onlyOwner {
        require(to != address(0), "Invalid address");

        // Increment the token ID counter to get a unique ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        _mint(to, tokenId);

        // Store the metadata associated with the token ID
        _tokenMetadata[tokenId] = metadata;

        // Emit an event indicating the NFT was minted
        emit NFTMinted(to, tokenId, metadata);
    }

    // Function to get the token URI for a specific token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");

        // Construct the full URI using the base URI and token ID
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    // Function to set a new base URI (only callable by the contract owner)
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Function to retrieve metadata for a specific token ID
    function getTokenMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenMetadata[tokenId];
    }
}
```

This code implements an ERC-721 token representing Pepe 2.0 NFTs, with functionality to mint new tokens, set base URIs, and retrieve metadata. It includes event emissions for minting, proper error handling, and adheres to best practices in Solidity programming.
