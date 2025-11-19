"""
Generated Code Metadata:
========================
Original URL: https://pushd-store-en.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates secure transactions on a decentralized marketplace like Pushd, utilizing Ethereum blockchain technology.
Generated: DETERMINISTIC_687dba9d89ca95e5
Batch ID: 20250612_161617
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

/**
 * @title Decentralized Marketplace Smart Contract
 * @dev Facilitates secure transactions between buyers and sellers on Ethereum blockchain
 */
contract DecentralizedMarketplace {
    // Struct to represent a listing
    struct Listing {
        uint256 id;
        address payable seller;
        string itemName;
        uint256 price;
        bool isSold;
    }

    // State variables
    uint256 private nextListingId; // Tracks the next listing ID
    mapping(uint256 => Listing) public listings; // Maps listing IDs to their details

    // Events
    event ListingCreated(uint256 id, address seller, string itemName, uint256 price);
    event ItemPurchased(uint256 id, address buyer, uint256 price);

    /**
     * @dev Creates a new listing on the marketplace
     * @param _itemName Name of the item being listed
     * @param _price Price of the item in wei
     */
    function createListing(string memory _itemName, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Create a new listing
        listings[nextListingId] = Listing({
            id: nextListingId,
            seller: payable(msg.sender),
            itemName: _itemName,
            price: _price,
            isSold: false
        });

        // Emit event for the new listing
        emit ListingCreated(nextListingId, msg.sender, _itemName, _price);

        // Increment the listing ID for the next listing
        nextListingId++;
    }

    /**
     * @dev Purchases an item from the marketplace
     * @param _listingId ID of the listing to purchase
     */
    function purchaseItem(uint256 _listingId) external payable {
        Listing storage listing = listings[_listingId];

        // Ensure the listing exists and is not sold
        require(listing.id == _listingId, "Listing does not exist");
        require(!listing.isSold, "Item already sold");

        // Ensure the buyer has sent enough Ether
        require(msg.value == listing.price, "Incorrect payment amount");

        // Mark the item as sold
        listing.isSold = true;

        // Transfer payment to the seller
        listing.seller.transfer(msg.value);

        // Emit event for the purchase
        emit ItemPurchased(_listingId, msg.sender, listing.price);
    }

    /**
     * @dev Fetches details of a listing
     * @param _listingId ID of the listing to fetch
     * @return Listing details
     */
    function getListing(uint256 _listingId) external view returns (Listing memory) {
        Listing memory listing = listings[_listingId];
        require(listing.id == _listingId, "Listing does not exist");
        return listing;
    }
}
```
