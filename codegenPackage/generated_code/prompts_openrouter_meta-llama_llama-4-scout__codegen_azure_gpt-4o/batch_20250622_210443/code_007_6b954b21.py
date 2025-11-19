"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Write a Solidity function to create and manage NFT items, like the lootbox keys and loot, used in the Meme Moguls platform.
Generated: DETERMINISTIC_6b954b21a0a6dd35
Batch ID: 20250622_210443
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFTManager - A contract to create and manage NFT items for Meme Moguls platform
/// @author Your Name
/// @notice This contract allows the creation and management of NFTs like lootbox keys and loot
/// @dev Inherits from OpenZeppelin's ERC721URIStorage and Ownable for secure and efficient NFT management

contract NFTManager is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    /// @notice Event emitted when a new NFT is minted
    /// @param tokenId The ID of the newly minted NFT
    /// @param recipient The address that received the NFT
    /// @param tokenURI The metadata URI of the NFT
    event NFTMinted(uint256 indexed tokenId, address indexed recipient, string tokenURI);

    /// @dev Constructor to initialize the NFT contract with a name and symbol
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new NFT
    /// @dev Only the owner of the contract can call this function
    /// @param recipient The address that will receive the minted NFT
    /// @param tokenURI The metadata URI for the NFT
    /// @return tokenId The ID of the newly minted NFT
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the recipient
        _mint(recipient, _currentTokenId);

        // Set the token URI for the minted NFT
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(_currentTokenId, recipient, tokenURI);

        return _currentTokenId;
    }

    /// @notice Function to get the current token ID
    /// @return The current token ID
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
