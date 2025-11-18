"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Create a smart contract in Solidity to manage NFT sales on the Artyfact marketplace, ensuring 50% of profits are allocated to the prize pool for monthly leaderboard rewards.
Generated: DETERMINISTIC_a07a415b8a80ddb7
Batch ID: 20250612_152441
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title ArtyfactNFTMarketplace
/// @dev Smart contract to manage NFT sales with a prize pool allocation
contract ArtyfactNFTMarketplace is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Represents an NFT for sale
    struct Sale {
        uint256 price; // Selling price of the NFT
        bool isActive; // Sale status
    }

    // Mapping from NFT token ID to Sale info
    mapping(uint256 => Sale) public sales;
    uint256 public prizePool; // Total prize pool for rewards

    event SaleCreated(uint256 indexed tokenId, uint256 price);
    event SaleCancelled(uint256 indexed tokenId);
    event SaleSuccessful(uint256 indexed tokenId, address buyer, uint256 price);
    event PrizePoolUpdated(uint256 newAmount);

    constructor() ERC721("ArtyfactNFT", "ARTY") {}

    /// @dev Create a new NFT and set it for sale.
    /// @param tokenURI The URI for the NFT metadata.
    /// @param price The sale price for the NFT.
    function createNFT(string memory tokenURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        sales[tokenId] = Sale(price, true);

        _tokenIdCounter.increment();

        emit SaleCreated(tokenId, price);
    }

    /// @dev Purchase an NFT from the marketplace.
    /// @param tokenId The ID of the NFT to purchase.
    function purchaseNFT(uint256 tokenId) external payable {
        Sale storage sale = sales[tokenId];
        require(sale.isActive, "Sale is not active");
        require(msg.value == sale.price, "Incorrect price sent");

        // Transfer the NFT to the buyer
        _transfer(owner(), msg.sender, tokenId);

        // Calculate profit and update prize pool
        uint256 profit = msg.value;
        uint256 prizeAllocation = profit / 2;
        prizePool += prizeAllocation;

        // Update the sale status
        sale.isActive = false;

        emit SaleSuccessful(tokenId, msg.sender, msg.value);
        emit PrizePoolUpdated(prizePool);
    }

    /// @dev Cancel an active sale.
    /// @param tokenId The ID of the NFT to cancel the sale.
    function cancelSale(uint256 tokenId) external onlyOwner {
        Sale storage sale = sales[tokenId];
        require(sale.isActive, "Sale is not active");
        
        sale.isActive = false;
        
        emit SaleCancelled(tokenId);
    }

    /// @dev Withdraw the prize pool funds to the owner's address.
    function withdrawPrizePool() external onlyOwner {
        uint256 amount = prizePool;
        require(amount > 0, "No funds in prize pool");
        prizePool = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    /// @dev Allows the contract to receive Ether.
    receive() external payable {}
    
    /// @dev Fallback function to accept Ether.
    fallback() external payable {}
}
```
