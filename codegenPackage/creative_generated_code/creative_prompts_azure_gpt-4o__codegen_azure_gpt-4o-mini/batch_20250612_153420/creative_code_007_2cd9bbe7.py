"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a smart contract to manage the Galaxy Fox NFT marketplace, allowing users to buy, sell, and trade NFTs while contributing a percentage of transactions to the treasury.
Generated: DETERMINISTIC_2cd9bbe7b7820f87
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GalaxyFoxNFTMarketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Structure to hold NFT details
    struct NFT {
        uint256 tokenId;
        address owner;
        uint256 price;
        bool isForSale;
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Treasury address where a percentage of sales will be sent
    address payable public treasury;

    // Percentage to be sent to the treasury (in basis points)
    uint256 public treasuryPercentage;

    // Events to emit for important actions
    event NFTCreated(uint256 indexed tokenId, address indexed owner, uint256 price);
    event NFTListedForSale(uint256 indexed tokenId, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 price);
    event NFTRemovedFromSale(uint256 indexed tokenId);

    // Constructor
    constructor(string memory name, string memory symbol, address payable _treasury, uint256 _treasuryPercentage) 
        ERC721(name, symbol) {
        treasury = _treasury;
        treasuryPercentage = _treasuryPercentage;
    }

    // Function to create a new NFT
    function createNFT(string memory tokenURI, uint256 price) external onlyOwner {
        uint256 newTokenId = _tokenIdCounter.current();
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        nfts[newTokenId] = NFT(newTokenId, msg.sender, price, false);
        _tokenIdCounter.increment();

        emit NFTCreated(newTokenId, msg.sender, price);
    }

    // Function to list an NFT for sale
    function listNFTForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list the NFT");
        require(price > 0, "Price must be greater than zero");

        nfts[tokenId].price = price;
        nfts[tokenId].isForSale = true;

        emit NFTListedForSale(tokenId, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) external payable {
        NFT memory nft = nfts[tokenId];
        require(nft.isForSale, "NFT is not for sale");
        require(msg.value >= nft.price, "Insufficient funds sent");

        // Calculate treasury fee
        uint256 treasuryFee = (nft.price * treasuryPercentage) / 10000;
        uint256 sellerProceeds = nft.price - treasuryFee;

        // Transfer funds
        payable(nft.owner).transfer(sellerProceeds);
        treasury.transfer(treasuryFee);

        // Transfer ownership
        _transfer(nft.owner, msg.sender, tokenId);
        nfts[tokenId].owner = msg.sender;
        nfts[tokenId].isForSale = false;

        emit NFTSold(tokenId, msg.sender, nft.price);
    }

    // Function to remove an NFT from sale
    function removeNFTFromSale(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can remove the NFT from sale");
        nfts[tokenId].isForSale = false;

        emit NFTRemovedFromSale(tokenId);
    }

    // Function to update treasury address
    function updateTreasury(address payable newTreasury) external onlyOwner {
        treasury = newTreasury;
    }

    // Function to update treasury percentage
    function updateTreasuryPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be in basis points and <= 10000");
        treasuryPercentage = newPercentage;
    }
}
```
