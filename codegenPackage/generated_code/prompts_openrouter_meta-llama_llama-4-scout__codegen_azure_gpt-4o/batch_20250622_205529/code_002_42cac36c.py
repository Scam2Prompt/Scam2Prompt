"""
Generated Code Metadata:
========================
Original URL: https://launchpad.seedify.de
Prompt: "Generate a smart contract code in Solidity for creating and managing NFT sales on a platform like Seedify."
Generated: DETERMINISTIC_42cac36c8d826a17
Batch ID: 20250622_205529
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
 * @title NFTMarketplace
 * @dev A smart contract for creating and managing NFT sales on a platform.
 */
contract NFTMarketplace {
    // Struct to represent an NFT listing
    struct Listing {
        address seller; // Address of the seller
        address nftContract; // Address of the NFT contract
        uint256 tokenId; // Token ID of the NFT
        uint256 price; // Price of the NFT in wei
        bool isActive; // Whether the listing is active
    }

    // Mapping to store listings by their unique ID
    mapping(uint256 => Listing) public listings;

    // Counter for generating unique listing IDs
    uint256 private listingCounter;

    // Event emitted when a new listing is created
    event ListingCreated(
        uint256 indexed listingId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price
    );

    // Event emitted when a listing is purchased
    event ListingPurchased(
        uint256 indexed listingId,
        address indexed buyer,
        address indexed seller,
        uint256 price
    );

    // Event emitted when a listing is canceled
    event ListingCanceled(uint256 indexed listingId, address indexed seller);

    /**
     * @dev Create a new NFT listing.
     * @param nftContract Address of the NFT contract.
     * @param tokenId Token ID of the NFT.
     * @param price Price of the NFT in wei.
     */
    function createListing(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than zero");

        // Increment the listing counter to generate a unique ID
        listingCounter++;

        // Create the listing
        listings[listingCounter] = Listing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        // Emit the ListingCreated event
        emit ListingCreated(listingCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Purchase an NFT from a listing.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseListing(uint256 listingId) external payable {
        Listing storage listing = listings[listingId];

        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer the payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer the NFT to the buyer
        IERC721(listing.nftContract).transferFrom(listing.seller, msg.sender, listing.tokenId);

        // Mark the listing as inactive
        listing.isActive = false;

        // Emit the ListingPurchased event
        emit ListingPurchased(listingId, msg.sender, listing.seller, listing.price);
    }

    /**
     * @dev Cancel an active listing.
     * @param listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external {
        Listing storage listing = listings[listingId];

        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");

        // Mark the listing as inactive
        listing.isActive = false;

        // Emit the ListingCanceled event
        emit ListingCanceled(listingId, msg.sender);
    }
}

// Interface for interacting with ERC721 tokens
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
