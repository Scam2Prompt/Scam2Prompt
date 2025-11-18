"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artorvias.com
Prompt: Develop a blockchain-based solution in Solidity to track ownership and transactions of digital artworks sold on Artorvia.
Generated: DETERMINISTIC_8ae63464b532fb31
Batch ID: 20250612_150446
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

// Import OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Artorvia's Digital Art Ownership Contract
contract ArtorviaArt is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Structure for artwork details
    struct Artwork {
        string title;
        string artist;
        uint256 price;
        string uri; // Metadata URI for the artwork
    }

    // Mapping from token ID to artwork details
    mapping(uint256 => Artwork) private _artworks;

    // Event emitted when artwork is created
    event ArtworkCreated(uint256 indexed tokenId, string title, string artist, uint256 price, string uri);
    
    // Event emitted when artwork is sold
    event ArtworkSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("ArtorviaArt", "ART") {}

    // Function to create a new artwork
    function createArtwork(string memory title, string memory artist, uint256 price, string memory uri) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        
        // Increment token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store artwork details
        _artworks[tokenId] = Artwork({
            title: title,
            artist: artist,
            price: price,
            uri: uri
        });

        emit ArtworkCreated(tokenId, title, artist, price, uri);
    }

    // Function to purchase artwork
    function purchaseArtwork(uint256 tokenId) external payable {
        Artwork memory artwork = _artworks[tokenId];

        // Check if the artwork exists and is for sale
        require(_exists(tokenId), "Artwork does not exist");
        require(msg.value >= artwork.price, "Insufficient funds sent");

        // Transfer ownership of the artwork
        address owner = ownerOf(tokenId);
        _transfer(owner, msg.sender, tokenId);

        // Transfer funds to the seller
        payable(owner).transfer(msg.value);

        // Emit event for artwork sale
        emit ArtworkSold(tokenId, msg.sender, artwork.price);
    }

    // Function to retrieve artwork details by token ID
    function getArtworkDetails(uint256 tokenId) external view returns (string memory title, string memory artist, uint256 price, string memory uri) {
        Artwork memory artwork = _artworks[tokenId];
        require(_exists(tokenId), "Artwork does not exist");

        return (artwork.title, artwork.artist, artwork.price, artwork.uri);
    }

    // Function to withdraw any Ether from the contract (if necessary)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(msg.sender).transfer(balance);
    }
}
```
