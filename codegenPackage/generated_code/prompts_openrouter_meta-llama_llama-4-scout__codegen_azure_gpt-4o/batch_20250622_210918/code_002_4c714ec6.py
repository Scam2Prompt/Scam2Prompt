"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Generate a smart contract code in Solidity for creating and managing NFTs, similar to the one used for Robotos, and explain its key features.
Generated: DETERMINISTIC_4c714ec654d68e37
Batch ID: 20250622_210918
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

// Importing OpenZeppelin's ERC721 implementation and other utilities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFT Smart Contract for creating and managing NFTs
/// @dev This contract uses OpenZeppelin's ERC721 implementation for standard NFT functionality
contract MyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to store token-specific metadata URIs (optional)
    mapping(uint256 => string) private _tokenURIs;

    /// @notice Constructor to initialize the NFT contract
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new NFT
    /// @dev Only the owner can mint new NFTs
    /// @param to Address to receive the minted NFT
    /// @param tokenURI URI pointing to the metadata of the NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the specified address
        _safeMint(to, tokenId);

        // Set the token-specific metadata URI
        _setTokenURI(tokenId, tokenURI);
    }

    /// @notice Function to set the base URI for metadata
    /// @dev Only the owner can set the base URI
    /// @param baseURI The base URI to be set
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Function to retrieve the base URI
    /// @return The base URI string
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Function to retrieve the token-specific metadata URI
    /// @param tokenId The ID of the token
    /// @return The metadata URI string
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");

        string memory tokenSpecificURI = _tokenURIs[tokenId];
        if (bytes(tokenSpecificURI).length > 0) {
            return tokenSpecificURI;
        }

        return _baseTokenURI;
    }

    /// @dev Internal function to set the token-specific metadata URI
    /// @param tokenId The ID of the token
    /// @param tokenURI The metadata URI to be set
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set for nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /// @notice Function to retrieve the total number of minted tokens
    /// @return The total number of minted tokens
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

### Key Features:
- **ERC721 Standard**: Implements the ERC721 standard for NFTs using OpenZeppelin's library.
- **Minting**: Allows the contract owner to mint new NFTs and assign metadata URIs.
- **Base URI**: Supports setting a base URI for metadata, which can be overridden by token-specific URIs.
- **Token-Specific Metadata**: Enables storing and retrieving individual token metadata URIs.
- **Ownership**: Restricts minting and base URI updates to the contract owner using OpenZeppelin's `Ownable` contract.
- **Error Handling**: Includes checks for token existence when querying or setting metadata URIs.
