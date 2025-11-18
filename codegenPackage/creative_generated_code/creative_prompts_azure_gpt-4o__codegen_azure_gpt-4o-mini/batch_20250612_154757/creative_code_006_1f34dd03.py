"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap.shop
Prompt: Write code to implement a secure NFT trading mechanism using Ethereum smart contracts, referencing Grailswap's emphasis on security and authenticity.
Generated: DETERMINISTIC_1f34dd03058382ca
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

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace contract for secure NFT trading
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT listing
    struct NFTListing {
        address owner;
        uint256 price;
        bool isListed;
    }

    // Mapping from tokenId to its listing details
    mapping(uint256 => NFTListing) public listings;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer);

    // Constructor to set the token name and symbol
    constructor() ERC721("SecureNFT", "SNFT") {}

    // Function to create a new NFT
    function createNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit NFTCreated(tokenId, msg.sender);
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than zero");
        
        listings[tokenId] = NFTListing(msg.sender, price, true);
        emit NFTListed(tokenId, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        NFTListing memory listing = listings[tokenId];
        
        require(listing.isListed, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT from the seller to the buyer
        _transfer(listing.owner, msg.sender, tokenId);

        // Transfer the sale price to the seller
        payable(listing.owner).transfer(msg.value);

        // Remove the listing
        delete listings[tokenId];

        emit NFTSold(tokenId, msg.sender);
    }

    // Function to unlist an NFT
    function unlistNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(listings[tokenId].isListed, "NFT is not listed");
        
        // Remove the listing
        delete listings[tokenId];
    }

    // Function to get listing details
    function getListing(uint256 tokenId) external view returns (NFTListing memory) {
        return listings[tokenId];
    }
}
```
