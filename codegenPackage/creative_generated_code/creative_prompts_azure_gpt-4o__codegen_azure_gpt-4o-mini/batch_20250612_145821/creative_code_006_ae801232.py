"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.now.sh
Prompt: Create a smart contract example for selling NFTs on PolyMarket 1.0 using the Polygon blockchain.
Generated: DETERMINISTIC_ae80123295642da0
Batch ID: 20250612_145821
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for an NFT marketplace
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for unique NFT IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent NFT details
    struct NFT {
        uint256 id;
        address owner;
        uint256 price;
        bool forSale;
    }

    // Mapping to store NFTs by their ID
    mapping(uint256 => NFT) public nfts;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner, uint256 price);
    
    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed newOwner, uint256 price);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("MyNFT", "MNFT") {}

    // Function to create a new NFT
    function createNFT(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Generate a new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Store the NFT details
        nfts[tokenId] = NFT({
            id: tokenId,
            owner: msg.sender,
            price: price,
            forSale: true
        });

        emit NFTCreated(tokenId, msg.sender, price);
    }

    // Function to purchase an NFT
    function buyNFT(uint256 tokenId) external payable {
        NFT storage nft = nfts[tokenId];

        require(nft.forSale, "NFT is not for sale");
        require(msg.value >= nft.price, "Insufficient funds sent");
        require(nft.owner != msg.sender, "Owner cannot buy their own NFT");

        // Transfer the NFT
        _transfer(nft.owner, msg.sender, tokenId);
        
        // Update NFT ownership and sale status
        nft.owner = msg.sender;
        nft.forSale = false;

        // Transfer funds to the previous owner
        payable(nft.owner).transfer(msg.value);

        emit NFTSold(tokenId, msg.sender, msg.value);
    }

    // Function to put an NFT up for sale
    function putNFTForSale(uint256 tokenId, uint256 price) external {
        NFT storage nft = nfts[tokenId];

        require(msg.sender == nft.owner, "Only the owner can put NFT for sale");
        require(price > 0, "Price must be greater than zero");
        require(!nft.forSale, "NFT is already for sale");

        nft.price = price;
        nft.forSale = true;
    }

    // Function to remove an NFT from sale
    function removeNFTFromSale(uint256 tokenId) external {
        NFT storage nft = nfts[tokenId];

        require(msg.sender == nft.owner, "Only the owner can remove NFT from sale");
        require(nft.forSale, "NFT is not for sale");

        nft.forSale = false;
    }
}
```
