"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: "Write a Solidity function to handle NFT minting and trading on the Bitcoin blockchain, similar to the features described for the 10k Ordinals NFT Club on Bitcoin Dogs."
Generated: DETERMINISTIC_a59a5f7938d5eb89
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BitcoinNFTClub is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public mintPrice = 0.01 ether;
    bool public mintingActive = false;

    mapping(uint256 => Listing) public listings;

    event NFTMinted(address indexed owner, uint256 indexed tokenId);
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTSold(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTUnlisted(address indexed seller, uint256 indexed tokenId);

    constructor() ERC721("BitcoinNFTClub", "BNC") {}

    modifier whenMintingActive() {
        require(mintingActive, "Minting is not active");
        _;
    }

    function toggleMinting() external onlyOwner {
        mintingActive = !mintingActive;
    }

    function setMintPrice(uint256 _newPrice) external onlyOwner {
        mintPrice = _newPrice;
    }

    function mintNFT() external payable whenMintingActive nonReentrant {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        if (msg.value > mintPrice) {
            payable(msg.sender).transfer(msg.value - mintPrice);
        }

        emit NFTMinted(msg.sender, tokenId);
    }

    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");

        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(msg.sender, tokenId, price);
    }

    function buyNFT(uint256 tokenId) external payable nonReentrant {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "NFT is not for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        address seller = listing.seller;
        _transfer(seller, msg.sender, tokenId);

        payable(seller).transfer(listing.price);
        if (msg.value > listing.price) {
            payable(msg.sender).transfer(msg.value - listing.price);
        }

        delete listings[tokenId];

        emit NFTSold(msg.sender, seller, tokenId, listing.price);
    }

    function unlistNFT(uint256 tokenId) external {
        require(listings[tokenId].seller == msg.sender, "Not the seller");
        require(listings[tokenId].isActive, "NFT is not listed");

        delete listings[tokenId];

        emit NFTUnlisted(msg.sender, tokenId);
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
