"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-8sr.pages.dev
Prompt: Create a smart contract that supports trading ordinals and NFTs using Blum's self-custody wallet integration.
Generated: DETERMINISTIC_bd46af18a7109f1a
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for trading Ordinals and NFTs
contract OrdinalNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to its ordinal value
    mapping(uint256 => uint256) private _ordinalValues;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, uint256 ordinal);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT with a given ordinal
    function mintNFT(uint256 ordinal) external {
        require(ordinal > 0, "Ordinal must be greater than zero");

        // Increment the token ID counter to get a new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new NFT to the caller
        _mint(msg.sender, tokenId);

        // Store the ordinal value for the minted token
        _ordinalValues[tokenId] = ordinal;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, ordinal);
    }

    // Function to get the ordinal value of a given token ID
    function getOrdinal(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _ordinalValues[tokenId];
    }

    // Function to trade an NFT (transfers ownership)
    function tradeNFT(address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Cannot transfer to the zero address");

        // Transfer the NFT to the specified address
        _transfer(msg.sender, to, tokenId);
    }

    // Function to safely transfer NFT, ensuring the receiving contract can handle it
    function safeTradeNFT(address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Cannot transfer to the zero address");

        // Safe transfer, ensuring the recipient can accept the NFT
        safeTransferFrom(msg.sender, to, tokenId);
    }

    // Function to burn an NFT (only callable by the owner)
    function burnNFT(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Burning nonexistent token");
        _burn(tokenId);
        delete _ordinalValues[tokenId]; // Clear the ordinal value upon burn
    }
}
```
