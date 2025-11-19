"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Write a smart contract for a blockchain-based marketplace for software engineers that enables the creation and trading of NFTs.
Generated: DETERMINISTIC_ec444bc34c5383d9
Batch ID: 20250622_211052
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EngineerMarketplace is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Listing {
        uint256 price;
        address seller;
        bool isActive;
    }

    mapping(uint256 => Listing) public listings;
    uint256 public platformFeePercentage = 5; // 5% platform fee

    event NFTMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId, address indexed seller);

    constructor() ERC721("EngineerNFT", "ENFT") {}

    function mintNFT(string memory tokenURI) public returns (uint256) {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        emit NFTMinted(tokenId, msg.sender, tokenURI);
        return tokenId;
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        require(!listings[tokenId].isActive, "Already listed");

        listings[tokenId] = Listing({
            price: price,
            seller: msg.sender,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    function buyNFT(uint256 tokenId) public payable nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds");

        uint256 platformFee = (listing.price * platformFeePercentage) / 100;
        uint256 sellerProceeds = listing.price - platformFee;

        // Transfer ownership
        _transfer(listing.seller, msg.sender, tokenId);
        
        // Transfer funds
        payable(listing.seller).transfer(sellerProceeds);
        payable(owner()).transfer(platformFee);

        // Remove listing
        delete listings[tokenId];

        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    function unlistNFT(uint256 tokenId) public {
        require(listings[tokenId].isActive, "NFT not listed");
        require(listings[tokenId].seller == msg.sender, "Not the seller");

        delete listings[tokenId];
        emit NFTUnlisted(tokenId, msg.sender);
    }

    function updatePlatformFee(uint256 newFeePercentage) public onlyOwner {
        require(newFeePercentage <= 20, "Fee too high");
        platformFeePercentage = newFeePercentage;
    }

    function withdrawFunds() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override required by Solidity
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
