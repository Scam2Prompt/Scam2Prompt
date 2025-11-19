"""
Generated Code Metadata:
========================
Original URL: https://swiftcoinlive.web.app
Prompt: Design a decentralized protocol for NFT management, including features like minting, buying, and selling of digital artworks.
Generated: DETERMINISTIC_83b412566d0a9827
Batch ID: 20250622_212712
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

// @title Decentralized NFT Management Protocol
// @notice This contract allows for minting, buying, and selling of digital artworks as NFTs.
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold NFT details
    struct Art {
        uint256 id;
        string name;
        string uri; // URI for the digital artwork
        address owner;
        uint256 price; // Price in wei
        bool isForSale; // Sale status
    }

    // Mapping from token ID to Art details
    mapping(uint256 => Art) public artworks;

    // Event emitted when a new NFT is minted
    event ArtMinted(uint256 indexed id, string name, string uri, address indexed owner);

    // Event emitted when an NFT is put up for sale
    event ArtForSale(uint256 indexed id, uint256 price);

    // Event emitted when an NFT is sold
    event ArtSold(uint256 indexed id, address indexed buyer, address indexed seller, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("DigitalArtNFT", "DANFT") {}

    // @notice Mint a new NFT
    // @param name The name of the artwork
    // @param uri The URI of the artwork
    function mintArt(string memory name, string memory uri) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        artworks[tokenId] = Art({
            id: tokenId,
            name: name,
            uri: uri,
            owner: msg.sender,
            price: 0,
            isForSale: false
        });

        _tokenIdCounter.increment();
        emit ArtMinted(tokenId, name, uri, msg.sender);
    }

    // @notice Put an NFT up for sale
    // @param tokenId The ID of the NFT
    // @param price The sale price in wei
    function putArtForSale(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can sell the NFT");
        require(price > 0, "Price must be greater than zero");

        artworks[tokenId].price = price;
        artworks[tokenId].isForSale = true;

        emit ArtForSale(tokenId, price);
    }

    // @notice Buy an NFT
    // @param tokenId The ID of the NFT to buy
    function buyArt(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(artworks[tokenId].isForSale, "NFT is not for sale");
        require(msg.value >= artworks[tokenId].price, "Insufficient funds sent");

        address seller = artworks[tokenId].owner;

        // Transfer ownership of the NFT
        _transfer(seller, msg.sender, tokenId);
        
        // Update the artwork details
        artworks[tokenId].owner = msg.sender;
        artworks[tokenId].isForSale = false;

        // Transfer funds to the seller
        payable(seller).transfer(msg.value);

        emit ArtSold(tokenId, msg.sender, seller, artworks[tokenId].price);
    }

    // @notice Get details of an NFT
    // @param tokenId The ID of the NFT
    // @return The details of the NFT
    function getArtDetails(uint256 tokenId) external view returns (Art memory) {
        require(_exists(tokenId), "NFT does not exist");
        return artworks[tokenId];
    }
}
```
