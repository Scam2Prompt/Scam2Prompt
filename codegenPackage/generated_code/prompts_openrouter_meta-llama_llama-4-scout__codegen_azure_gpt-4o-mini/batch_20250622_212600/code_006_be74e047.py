"""
Generated Code Metadata:
========================
Original URL: https://primeart.org
Prompt: "Design a basic smart contract for creating and trading digital art on a platform like Prime Art."
Generated: DETERMINISTIC_be74e0476ae701dc
Batch ID: 20250622_212600
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title DigitalArtMarketplace
// @dev A smart contract for creating and trading digital art as NFTs
contract DigitalArtMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a piece of digital art
    struct Art {
        uint256 id;
        string name;
        string artist;
        string uri; // URI for the digital art metadata
        uint256 price; // Price in wei
        address owner; // Current owner of the art
        bool isForSale; // Sale status
    }

    // Mapping from token ID to Art details
    mapping(uint256 => Art) private _arts;

    // Event emitted when a new art is created
    event ArtCreated(uint256 indexed id, string name, string artist, string uri, uint256 price);

    // Event emitted when art is put up for sale
    event ArtForSale(uint256 indexed id, uint256 price);

    // Event emitted when art is sold
    event ArtSold(uint256 indexed id, address indexed buyer, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("DigitalArt", "DART") {}

    // @dev Create a new piece of digital art
    // @param name The name of the art
    // @param artist The artist's name
    // @param uri The URI for the art's metadata
    // @param price The price in wei for the art
    function createArt(string memory name, string memory artist, string memory uri, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _arts[tokenId] = Art(tokenId, name, artist, uri, price, msg.sender, false);
        _mint(msg.sender, tokenId);

        emit ArtCreated(tokenId, name, artist, uri, price);
    }

    // @dev Put art up for sale
    // @param tokenId The ID of the art to put up for sale
    // @param price The sale price in wei
    function putArtForSale(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "Art does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can put art for sale");
        require(price > 0, "Price must be greater than zero");

        _arts[tokenId].isForSale = true;
        _arts[tokenId].price = price;

        emit ArtForSale(tokenId, price);
    }

    // @dev Buy art that is for sale
    // @param tokenId The ID of the art to buy
    function buyArt(uint256 tokenId) external payable {
        require(_exists(tokenId), "Art does not exist");
        require(_arts[tokenId].isForSale, "Art is not for sale");
        require(msg.value >= _arts[tokenId].price, "Insufficient funds sent");

        address seller = ownerOf(tokenId);
        require(seller != msg.sender, "Cannot buy your own art");

        // Transfer the art to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Transfer funds to the seller
        payable(seller).transfer(msg.value);

        // Update art ownership and sale status
        _arts[tokenId].owner = msg.sender;
        _arts[tokenId].isForSale = false;

        emit ArtSold(tokenId, msg.sender, msg.value);
    }

    // @dev Get details of a specific art piece
    // @param tokenId The ID of the art
    // @return Art details
    function getArtDetails(uint256 tokenId) external view returns (Art memory) {
        require(_exists(tokenId), "Art does not exist");
        return _arts[tokenId];
    }
}
```
