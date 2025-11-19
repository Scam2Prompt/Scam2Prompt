"""
Generated Code Metadata:
========================
Original URL: https://the-cryptodezire.com
Prompt: Generate code to simulate NFT trading options using Ethereum's programming language, incorporating features inspired by Crypto Dezire's platform.
Generated: DETERMINISTIC_c0bb7ac85b545adf
Batch ID: 20250612_150048
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTTrading is a contract for simulating NFT trading options
contract NFTTrading is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
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

    // Event emitted when a new NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("NFTTradingToken", "NTT") {}

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than zero");

        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT from the seller to the buyer
        _transfer(listing.seller, msg.sender, tokenId);

        // Transfer the sale amount to the seller
        payable(listing.seller).transfer(msg.value);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    // Function to cancel a listing
    function cancelListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.seller == msg.sender, "You are not the seller");
        require(listing.isActive, "NFT is not listed for sale");

        // Mark the listing as inactive
        listings[tokenId].isActive = false;
    }

    // Function to get the details of a listing
    function getListing(uint256 tokenId) external view returns (Listing memory) {
        return listings[tokenId];
    }
}
```
