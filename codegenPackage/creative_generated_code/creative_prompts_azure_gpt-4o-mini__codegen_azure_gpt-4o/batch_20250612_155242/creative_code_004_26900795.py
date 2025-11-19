"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://borroefinance-ai.web.app
Prompt: Generate a code snippet for a smart contract that facilitates the sale of future recurring revenue NFTs on Borroe Finance.
Generated: DETERMINISTIC_26900795a125ad15
Batch ID: 20250612_155242
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

/**
 * @title FutureRecurringRevenueNFT
 * @dev A smart contract for facilitating the sale of future recurring revenue NFTs on Borroe Finance platform.
 */
contract FutureRecurringRevenueNFT {
    // Struct to define an NFT Sale
    struct RevenueNFT {
        uint256 id;               // Unique identifier for the NFT
        address seller;           // Address of the seller
        uint256 price;            // Sale price of the NFT
        uint256 recurringRevenue; // Future recurring revenue associated with the NFT
        bool isSold;              // Status of the NFT sale
    }

    // Mapping to store NFTs
    mapping(uint256 => RevenueNFT) public nfts;

    // Counter to track NFT IDs
    uint256 private nextNFTId;

    // Event declarations
    event NFTCreated(uint256 indexed nftId, address indexed seller, uint256 price, uint256 recurringRevenue);
    event NFTSold(uint256 indexed nftId, address indexed buyer, uint256 price);

    // Modifier to check if the caller is the seller
    modifier onlySeller(uint256 nftId) {
        require(nfts[nftId].seller == msg.sender, "Caller is not the seller");
        _;
    }

    // Modifier to check if the NFT exists
    modifier nftExists(uint256 nftId) {
        require(nfts[nftId].seller != address(0), "NFT does not exist");
        _;
    }

    /**
     * @dev Function to create a new NFT for sale.
     * @param price Sale price of the NFT.
     * @param recurringRevenue Future recurring revenue associated with the NFT.
     */
    function createNFT(uint256 price, uint256 recurringRevenue) external {
        require(price > 0, "Price must be greater than zero");
        require(recurringRevenue > 0, "Recurring revenue must be greater than zero");

        uint256 nftId = nextNFTId++;
        nfts[nftId] = RevenueNFT({
            id: nftId,
            seller: msg.sender,
            price: price,
            recurringRevenue: recurringRevenue,
            isSold: false
        });

        emit NFTCreated(nftId, msg.sender, price, recurringRevenue);
    }

    /**
     * @dev Function to buy an NFT.
     * @param nftId The ID of the NFT to purchase.
     */
    function buyNFT(uint256 nftId) external payable nftExists(nftId) {
        RevenueNFT storage nft = nfts[nftId];
        require(!nft.isSold, "NFT is already sold");
        require(msg.value == nft.price, "Incorrect payment amount");

        nft.isSold = true;

        // Transfer funds to the seller
        (bool success,) = nft.seller.call{value: msg.value}("");
        require(success, "Failed to transfer funds to seller");

        emit NFTSold(nftId, msg.sender, nft.price);
    }

    /**
     * @dev Function to get NFT details.
     * @param nftId The ID of the NFT to fetch.
     * @return NFT details as (id, seller, price, recurringRevenue, isSold).
     */
    function getNFTDetails(uint256 nftId)
        external
        view
        nftExists(nftId)
        returns (uint256, address, uint256, uint256, bool)
    {
        RevenueNFT memory nft = nfts[nftId];
        return (nft.id, nft.seller, nft.price, nft.recurringRevenue, nft.isSold);
    }
}
```
