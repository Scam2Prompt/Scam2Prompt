"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftnovamarket.com
Prompt: Generate a Solidity contract for managing NFT transactions on Nftnovamarket's platform, including buying, selling, and transferring ownership.
Generated: DETERMINISTIC_8d116db23b789470
Batch ID: 20250612_151626
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title NftnovaMarket - A contract for managing NFT transactions
// @author Your Name
// @notice This contract allows the buying, selling, and transferring of NFTs
contract NftnovaMarket is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking the token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from NFT ID to its price
    mapping(uint256 => uint256) private _prices;

    // Event emitted when an NFT is bought
    event NftBought(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Event emitted when an NFT is listed for sale
    event NftListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is delisted from sale
    event NftDelisted(uint256 indexed tokenId);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("NftnovaMarket", "NFTNM") {}

    // @notice Mint a new NFT to the specified address
    // @param to The address that will receive the minted NFT
    // @return tokenId The ID of the minted NFT
    function mint(address to) external onlyOwner returns (uint256 tokenId) {
        tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();
    }

    // @notice List an NFT for sale at a specific price
    // @param tokenId The ID of the NFT to list
    // @param price The selling price of the NFT
    function listNft(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Only the NFT owner can list it for sale");
        require(price > 0, "Price must be greater than zero");

        _prices[tokenId] = price;
        emit NftListed(tokenId, price);
    }

    // @notice Buy an NFT that is listed for sale
    // @param tokenId The ID of the NFT to buy
    function buyNft(uint256 tokenId) external payable {
        uint256 price = _prices[tokenId];
        require(price > 0, "NFT is not for sale");
        require(msg.value >= price, "Insufficient payment");

        address seller = ownerOf(tokenId);
        require(seller != msg.sender, "Seller cannot buy their own NFT");

        // Transfer the NFT from seller to buyer
        _transfer(seller, msg.sender, tokenId);
        
        // Transfer the funds to the seller
        payable(seller).transfer(price);

        // Clear the price for the token
        delete _prices[tokenId];

        emit NftBought(tokenId, msg.sender, price);
    }

    // @notice Delist an NFT from sale
    // @param tokenId The ID of the NFT to delist
    function delistNft(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Only the NFT owner can delist it");
        require(_prices[tokenId] > 0, "NFT is not listed for sale");

        delete _prices[tokenId];
        emit NftDelisted(tokenId);
    }

    // @notice Get the price of an NFT
    // @param tokenId The ID of the NFT
    // @return price The price of the NFT
    function getNftPrice(uint256 tokenId) external view returns (uint256 price) {
        price = _prices[tokenId];
    }
}
```
