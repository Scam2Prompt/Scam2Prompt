"""
Generated Code Metadata:
========================
Original URL: https://alphaspherearts.com
Prompt: Develop a smart contract using Solidity to create, buy, and sell NFTs on a platform like Alpha Sphere Arts.
Generated: DETERMINISTIC_783f77ad8e05085b
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title: NFTMarketplace
// @dev: A smart contract for creating, buying, and selling NFTs
contract NFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT listing
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to its listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed creator, string tokenURI);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("AlphaSphereArtsNFT", "ASA") {}

    // @dev: Create a new NFT
    // @param tokenURI: The metadata URI for the NFT
    function createNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenIdCounter.increment();

        emit NFTCreated(tokenId, msg.sender, tokenURI);
    }

    // @dev: List an NFT for sale
    // @param tokenId: The ID of the NFT to list
    // @param price: The sale price of the NFT
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(price > 0, "Price must be greater than zero");

        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    // @dev: Buy an NFT
    // @param tokenId: The ID of the NFT to buy
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "This NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);

        // Transfer the funds to the seller
        payable(listing.seller).transfer(listing.price);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    // @dev: Cancel a listing
    // @param tokenId: The ID of the NFT to cancel
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You are not the seller of this NFT");
        require(listing.isActive, "This NFT is not listed for sale");

        // Mark the listing as inactive
        listings[tokenId].isActive = false;
    }

    // @dev: Get the details of a listing
    // @param tokenId: The ID of the NFT
    // @return: The listing details
    function getListing(uint256 tokenId) external view returns (Listing memory) {
        return listings[tokenId];
    }
}
```
