"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Create an example of a smart contract for managing transactions in the MBD Boulevard phygital marketplace, ensuring compliance with Web3 standards.
Generated: DETERMINISTIC_9866462a16da03ab
Batch ID: 20250612_163742
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

/**
 * @title PhygitalMarketplace
 * @dev A smart contract for managing transactions in the MBD Boulevard phygital marketplace.
 */
contract PhygitalMarketplace is Ownable {
    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }
    
    // Mapping from token ID to its listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when a new item is listed
    event ItemListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an item is sold
    event ItemSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);

    /**
     * @dev Lists an item for sale in the marketplace.
     * @param tokenId The ID of the token to be listed.
     * @param price The price of the item in tokens.
     */
    function listItem(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit ItemListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Purchases an item from the marketplace.
     * @param tokenId The ID of the token being purchased.
     * @param paymentToken The ERC20 token used for payment.
     */
    function purchaseItem(uint256 tokenId, address paymentToken) external {
        Listing memory listing = listings[tokenId];
        require(listing.isActive, "Item is not for sale");
        require(listing.seller != msg.sender, "Seller cannot buy their own item");

        // Transfer payment to the seller
        IERC20(paymentToken).transferFrom(msg.sender, listing.seller, listing.price);

        // Mark the item as inactive
        listings[tokenId].isActive = false;

        emit ItemSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    /**
     * @dev Cancels a listing for an item in the marketplace.
     * @param tokenId The ID of the token to be unlisted.
     */
    function cancelListing(uint256 tokenId) external {
        Listing storage listing = listings[tokenId];
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");
        require(listing.isActive, "Item is not listed");

        listing.isActive = false;
    }

    /**
     * @dev Returns the details of a listing.
     * @param tokenId The ID of the token to retrieve the listing for.
     * @return seller The address of the seller.
     * @return price The price of the item.
     * @return isActive Whether the item is currently for sale.
     */
    function getListing(uint256 tokenId) external view returns (address seller, uint256 price, bool isActive) {
        Listing memory listing = listings[tokenId];
        return (listing.seller, listing.price, listing.isActive);
    }
}
```
