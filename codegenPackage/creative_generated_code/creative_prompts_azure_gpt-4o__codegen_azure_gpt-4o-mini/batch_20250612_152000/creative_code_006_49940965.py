"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Write a smart contract in Solidity that utilizes the Metis Layer 2 infrastructure to enable affordable on-chain storage for NFT metadata.
Generated: DETERMINISTIC_499409653649197d
Batch ID: 20250612_152000
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for storing NFT metadata on the Metis Layer 2 infrastructure
contract NFTMetadataStorage is ERC721 {
    using Counters for Counters.Counter;

    // Counter for NFT IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when metadata is set for a token
    event MetadataSet(uint256 indexed tokenId, string metadataURI);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT with metadata
    function mintNFT(string memory metadataURI) external {
        // Increment the token ID counter to get a new token ID
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, newTokenId);
        
        // Set the metadata URI for the newly minted NFT
        _setTokenURI(newTokenId, metadataURI);
    }

    // Internal function to set the metadata URI for a given token ID
    function _setTokenURI(uint256 tokenId, string memory metadataURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = metadataURI;

        // Emit event for metadata update
        emit MetadataSet(tokenId, metadataURI);
    }

    // Function to retrieve the metadata URI for a specific token ID
    function getTokenURI(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // Override the tokenURI function from ERC721 to return the stored metadata URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _tokenURIs[tokenId].length > 0;
    }
}
```
