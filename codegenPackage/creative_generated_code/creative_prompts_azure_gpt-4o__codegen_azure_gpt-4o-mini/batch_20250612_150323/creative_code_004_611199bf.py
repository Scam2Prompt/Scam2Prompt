"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Write a script to automate proxy sales for NFTs using a contract structure similar to the Proxy Sales Contract mentioned on the CryptoTitties site.
Generated: DETERMINISTIC_611199bfcdaf87e1
Batch ID: 20250612_150323
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

// Importing necessary libraries from OpenZeppelin for safe math and access control
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

// ProxySales contract allows for NFT sales through a proxy mechanism
contract ProxySales is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold sale information
    struct Sale {
        address seller;         // Address of the seller
        address nftContract;    // Address of the NFT contract
        uint256 tokenId;        // ID of the NFT
        uint256 price;          // Price of the NFT in wei
        bool isActive;          // Status of the sale
    }

    // Mapping from sale ID to Sale struct
    mapping(uint256 => Sale) public sales;
    Counters.Counter private saleIdCounter;

    // Event emitted when a sale is created
    event SaleCreated(uint256 indexed saleId, address indexed seller, address indexed nftContract, uint256 tokenId, uint256 price);
    
    // Event emitted when a sale is executed
    event SaleExecuted(uint256 indexed saleId, address indexed buyer, address indexed seller, uint256 tokenId, uint256 price);
    
    // Event emitted when a sale is canceled
    event SaleCancelled(uint256 indexed saleId);

    // Function to create a new sale
    function createSale(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        // Transfer NFT to this contract to ensure the seller has it
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Increment sale ID counter and create sale
        saleIdCounter.increment();
        uint256 saleId = saleIdCounter.current();
        sales[saleId] = Sale({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit SaleCreated(saleId, msg.sender, nftContract, tokenId, price);
    }

    // Function to execute a sale
    function executeSale(uint256 saleId) external payable {
        Sale storage sale = sales[saleId];
        require(sale.isActive, "Sale is not active");
        require(msg.value >= sale.price, "Insufficient payment");

        // Mark the sale as inactive
        sale.isActive = false;

        // Transfer the NFT to the buyer
        IERC721(sale.nftContract).transferFrom(address(this), msg.sender, sale.tokenId);

        // Transfer payment to the seller
        payable(sale.seller).transfer(sale.price);

        emit SaleExecuted(saleId, msg.sender, sale.seller, sale.tokenId, sale.price);
    }

    // Function to cancel a sale
    function cancelSale(uint256 saleId) external {
        Sale storage sale = sales[saleId];
        require(sale.isActive, "Sale is not active");
        require(sale.seller == msg.sender, "Only the seller can cancel the sale");

        // Mark the sale as inactive
        sale.isActive = false;

        // Transfer NFT back to the seller
        IERC721(sale.nftContract).transferFrom(address(this), msg.sender, sale.tokenId);

        emit SaleCancelled(saleId);
    }
}
```
