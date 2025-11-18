"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayonnanft.com
Prompt: Create a smart contract in Solidity for listing NFTs on RayonnaNFT with options for fixed-price, auction, and declining-price sales.
Generated: DETERMINISTIC_94581bb974b76e45
Batch ID: 20250612_154542
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
 * @title RayonnaNFT Marketplace Contract
 * @notice This contract allows users to list NFTs for sale on RayonnaNFT
 *         with options for fixed-price, auction, and declining-price sales.
 */
contract RayonnaNFTMarketplace {

    // Struct representing an NFT listing
    struct Listing {
        address seller;        // Address of the seller
        address nftContract;   // Address of the NFT contract
        uint256 tokenId;       // ID of the NFT token
        uint256 price;         // Fixed price or starting bid (if auction)
        uint256 duration;      // Sale duration for auctions/declining price sales
        uint256 startTime;     // Start time for the listing
        SaleType saleType;     // Type of sale: FIXED_PRICE, AUCTION, DECLINING_PRICE
        bool isSold;           // Flag to check if the NFT is sold
    }

    // Enum representing the type of sale
    enum SaleType {
        FIXED_PRICE,
        AUCTION,
        DECLINING_PRICE
    }

    // Mapping to store all listings
    mapping(uint256 => Listing) public listings;

    // Counter for unique listing IDs
    uint256 public listingCounter;

    // Events
    event NFTListed(
        uint256 indexed listingId,
        address indexed seller,
        address indexed nftContract,
        uint256 tokenId,
        uint256 price,
        SaleType saleType,
        uint256 duration
    );

    event NFTSold(
        uint256 indexed listingId,
        address indexed buyer,
        address nftContract,
        uint256 tokenId,
        uint256 finalPrice
    );

    event ListingCancelled(uint256 indexed listingId);

    /**
     * @notice List an NFT for sale
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT token
     * @param price Fixed price or starting bid (if auction)
     * @param duration Sale duration for auctions/declining price sales
     * @param saleType Type of sale: FIXED_PRICE, AUCTION, DECLINING_PRICE
     */
    function listNFT(
        address nftContract,
        uint256 tokenId,
        uint256 price,
        uint256 duration,
        SaleType saleType
    ) external {
        require(price > 0, "Price must be greater than zero");
        require(duration > 0 || saleType == SaleType.FIXED_PRICE, "Duration required for auctions or declining price sales");

        // Transfer NFT to the marketplace for escrow
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create a new listing
        listings[listingCounter] = Listing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            duration: duration,
            startTime: block.timestamp,
            saleType: saleType,
            isSold: false
        });

        // Emit an event for the new listing
        emit NFTListed(listingCounter, msg.sender, nftContract, tokenId, price, saleType, duration);

        // Increment the listing counter
        listingCounter++;
    }

    /**
     * @notice Buy an NFT from a fixed-price listing
     * @param listingId ID of the listing to buy
     */
    function buyNFT(uint256 listingId) external payable {
        Listing storage listing = listings[listingId];
        require(listing.saleType == SaleType.FIXED_PRICE, "Not a fixed-price listing");
        require(!listing.isSold, "NFT already sold");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Mark the listing as sold
        listing.isSold = true;

        // Transfer payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer NFT to the buyer
        IERC721(listing.nftContract).transferFrom(address(this), msg.sender, listing.tokenId);

        // Emit an event for the sale
        emit NFTSold(listingId, msg.sender, listing.nftContract, listing.tokenId, listing.price);
    }

    /**
     * @notice Cancel an NFT listing
     * @param listingId ID of the listing to cancel
     */
    function cancelListing(uint256 listingId) external {
        Listing storage listing = listings[listingId];
        require(listing.seller == msg.sender, "Only the seller can cancel the listing");
        require(!listing.isSold, "Cannot cancel a sold listing");

        // Transfer the NFT back to the seller
        IERC721(listing.nftContract).transferFrom(address(this), listing.seller, listing.tokenId);

        // Emit an event for the cancellation
        emit ListingCancelled(listingId);

        // Delete the listing
        delete listings[listingId];
    }
}

// Interface for ERC721 NFTs
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
