"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a script to automate proxy sales for NFTs using a contract structure similar to the Proxy Sales Contract mentioned on the CryptoTitties site.
Generated: DETERMINISTIC_611199bfcdaf87e1
Batch ID: 20250612_150323
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// ProxySalesContract allows users to purchase NFTs through a proxy mechanism
contract ProxySalesContract is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold NFT sale details
    struct Sale {
        address nftContract; // Address of the NFT contract
        uint256 tokenId;     // ID of the NFT
        uint256 price;       // Sale price in wei
        bool isActive;       // Sale status
    }

    // Mapping to store sales by their unique ID
    mapping(uint256 => Sale) public sales;
    Counters.Counter private saleIdCounter; // Counter for unique sale IDs

    // Event emitted when a new sale is created
    event SaleCreated(uint256 indexed saleId, address indexed nftContract, uint256 indexed tokenId, uint256 price);
    
    // Event emitted when an NFT is purchased
    event SalePurchased(uint256 indexed saleId, address indexed buyer);

    // Modifier to check if the sale is active
    modifier saleIsActive(uint256 saleId) {
        require(sales[saleId].isActive, "Sale is not active");
        _;
    }

    // Function to create a new sale
    function createSale(address nftContract, uint256 tokenId, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the sale ID counter and create a new sale
        uint256 saleId = saleIdCounter.current();
        saleIdCounter.increment();

        sales[saleId] = Sale({
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit SaleCreated(saleId, nftContract, tokenId, price);
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 saleId) external payable saleIsActive(saleId) {
        Sale storage sale = sales[saleId];

        // Check if the sent value matches the sale price
        require(msg.value == sale.price, "Incorrect value sent");

        // Transfer the NFT from the contract owner to the buyer
        IERC721(sale.nftContract).transferFrom(owner(), msg.sender, sale.tokenId);

        // Mark the sale as inactive
        sale.isActive = false;

        // Emit the purchase event
        emit SalePurchased(saleId, msg.sender);
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to deactivate a sale
    function deactivateSale(uint256 saleId) external onlyOwner saleIsActive(saleId) {
        sales[saleId].isActive = false;
    }

    // Function to get sale details
    function getSaleDetails(uint256 saleId) external view returns (Sale memory) {
        return sales[saleId];
    }
}
```
