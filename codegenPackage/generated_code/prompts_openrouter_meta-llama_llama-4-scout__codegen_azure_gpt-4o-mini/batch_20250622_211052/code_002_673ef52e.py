"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Generate code for a simple NFT marketplace using blockchain technology, inspired by OpenSwe's features.
Generated: DETERMINISTIC_673ef52e3f89d859
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract for creating and managing NFTs
contract NFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT listing
    struct Listing {
        uint256 tokenId;
        address payable seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to Listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed seller, uint256 price, string tokenURI);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("NFTMarketplace", "NFTM") {}

    // Function to create a new NFT
    function createNFT(string memory tokenURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Create a new listing for the NFT
        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: payable(msg.sender),
            price: price,
            isActive: true
        });

        emit NFTCreated(tokenId, msg.sender, price, tokenURI);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];

        // Ensure the listing is active and the price is correct
        require(listing.isActive, "NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT to the buyer
        _transfer(listing.seller, msg.sender, tokenId);

        // Transfer the funds to the seller
        listing.seller.transfer(msg.value);

        // Mark the listing as inactive
        listing.isActive = false;

        emit NFTSold(tokenId, msg.sender, listing.price);
    }

    // Function to fetch listing details
    function getListing(uint256 tokenId) external view returns (Listing memory) {
        return listings[tokenId];
    }

    // Function to withdraw funds from the contract (if needed)
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
