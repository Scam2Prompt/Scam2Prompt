"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getmeme.pages.dev
Prompt: Write a Solidity or Rust program to implement a digital collectible card system inspired by "$TRUMP" Trump Memes, incorporating historical moments and community engagement features as described on GetTrumpMemes.com.
Generated: DETERMINISTIC_142677f19432c18d
Batch ID: 20250612_154757
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title TrumpMemes - A Digital Collectible Card System
// @dev This contract allows users to mint, transfer, and manage collectible cards inspired by Trump memes.
contract TrumpMemes is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Structure to hold data for each meme card
    struct MemeCard {
        string name; // Name of the meme card
        string description; // Description of the meme
        string imageUrl; // URL of the meme image
        uint256 creationTime; // Timestamp when the card was created
    }

    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    mapping(uint256 => MemeCard) private _memeCards; // Mapping of token ID to MemeCard

    // Event emitted when a new meme card is created
    event MemeCardCreated(uint256 indexed tokenId, string name, string description, string imageUrl);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("TrumpMemes", "TMEME") {}

    // @notice Function to mint a new meme card
    // @param _name Name of the meme card
    // @param _description Description of the meme
    // @param _imageUrl URL of the meme image
    function mintMemeCard(string memory _name, string memory _description, string memory _imageUrl) external onlyOwner {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(bytes(_imageUrl).length > 0, "Image URL cannot be empty");

        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the token ID counter
        
        // Mint the new token and assign it to the owner
        _mint(msg.sender, tokenId);

        // Create a new MemeCard and save it
        _memeCards[tokenId] = MemeCard({
            name: _name,
            description: _description,
            imageUrl: _imageUrl,
            creationTime: block.timestamp
        });

        emit MemeCardCreated(tokenId, _name, _description, _imageUrl); // Emit the event
    }

    // @notice Function to retrieve meme card details
    // @param tokenId Token ID of the meme card
    // @return MemeCard details
    function getMemeCard(uint256 tokenId) external view returns (MemeCard memory) {
        require(_exists(tokenId), "Meme card does not exist");
        return _memeCards[tokenId];
    }

    // @notice Function to transfer a meme card
    // @param from Address sending the meme card
    // @param to Address receiving the meme card
    // @param tokenId Token ID of the meme card
    function transferMemeCard(address from, address to, uint256 tokenId) external {
        // Only the owner or approved address can transfer the card
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the card
        _transfer(from, to, tokenId);
    }
}
```

This Solidity contract implements a basic digital collectible card system inspired by Trump memes, using best practices for security, efficiency, and maintainability. Each card can be minted by the owner, and details can be queried by users.
