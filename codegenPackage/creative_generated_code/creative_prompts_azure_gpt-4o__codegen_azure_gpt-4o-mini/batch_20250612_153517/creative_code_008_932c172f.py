"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Create a tutorial for building an NFT marketplace within the HEHE ecosystem that utilizes $HEHE tokens for transactions.
Generated: DETERMINISTIC_932c172f352ecaef
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title HEHE NFT Marketplace
 * @dev This contract allows users to mint, buy, and sell NFTs using $HEHE tokens.
 */
contract HEHENFTMarketplace is ERC721, Ownable {
    // State variable for the HEHE token contract
    IERC20 public heheToken;

    // Counter for NFT IDs
    uint256 private _nextTokenId;

    // Struct to store NFT sale information
    struct Sale {
        uint256 price; // Sale price in HEHE tokens
        address seller; // Address of the seller
        bool isActive;  // Sale status
    }

    // Mapping from token ID to sale information
    mapping(uint256 => Sale) public sales;

    // Event emitted when an NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is put up for sale
    event NFTListed(uint256 indexed tokenId, uint256 price, address indexed seller);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    /**
     * @dev Constructor to initialize the NFT marketplace with the HEHE token contract address.
     * @param _heheToken Address of the $HEHE token contract.
     */
    constructor(IERC20 _heheToken) ERC721("HEHE NFT", "HEHE") {
        heheToken = _heheToken;
    }

    /**
     * @dev Mint a new NFT.
     * @param to Address that will receive the minted NFT.
     */
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = _nextTokenId++;
        _mint(to, tokenId);
        emit NFTMinted(tokenId, to);
    }

    /**
     * @dev List an NFT for sale.
     * @param tokenId The ID of the NFT to list.
     * @param price The sale price in HEHE tokens.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner");
        require(price > 0, "Price must be greater than zero");

        sales[tokenId] = Sale(price, msg.sender, true);
        emit NFTListed(tokenId, price, msg.sender);
    }

    /**
     * @dev Purchase an NFT.
     * @param tokenId The ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external {
        Sale memory sale = sales[tokenId];
        require(sale.isActive, "NFT is not for sale");
        require(heheToken.transferFrom(msg.sender, sale.seller, sale.price), "Payment failed");

        _transfer(sale.seller, msg.sender, tokenId);
        sales[tokenId].isActive = false; // Mark the sale as inactive

        emit NFTPurchased(tokenId, msg.sender, sale.seller, sale.price);
    }

    /**
     * @dev Remove an NFT from sale.
     * @param tokenId The ID of the NFT to remove from sale.
     */
    function removeNFTFromSale(uint256 tokenId) external {
        Sale memory sale = sales[tokenId];
        require(sale.seller == msg.sender, "You are not the seller");
        require(sale.isActive, "NFT is not for sale");

        sales[tokenId].isActive = false; // Mark the sale as inactive
    }
}
```

This code represents a basic NFT marketplace where users can mint NFTs, list them for sale using $HEHE tokens, and purchase them. The code includes proper error handling, events for tracking actions, and follows Solidity best practices.
