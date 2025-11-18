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

// Interface for the ERC721 standard
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Smart contract for listing NFTs on RayonnaNFT
contract RayonnaNFTMarketplace {
    // Enum representing listing types
    enum ListingType { FixedPrice, Auction, DecliningPrice }

    // Struct to represent an NFT listing
    struct Listing {
        address seller;
        uint256 tokenId;
        ListingType listingType;
        uint256 price; // Fixed price or starting price for auction
        uint256 endTime; // End time for auction or decline duration
        uint256 decrement; // Decrement amount for declining price
    }

    // Mapping of tokenId to its listing
    mapping(uint256 => Listing) public listings;

    // Event emitted when a new listing is created
    event ListingCreated(uint256 indexed tokenId, address indexed seller, ListingType listingType, uint256 price);
    
    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Modifier to check if the caller is the seller
    modifier onlySeller(uint256 tokenId) {
        require(listings[tokenId].seller == msg.sender, "Not the seller");
        _;
    }

    // Function to create a new NFT listing
    function createListing(
        uint256 tokenId,
        address nftAddress,
        ListingType listingType,
        uint256 price,
        uint256 duration, // For auctions or declining price duration
        uint256 decrement // For declining price
    ) external {
        require(price > 0, "Price must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        
        // Transfer the NFT to this contract
        IERC721(nftAddress).transferFrom(msg.sender, address(this), tokenId);

        // Create the listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            tokenId: tokenId,
            listingType: listingType,
            price: price,
            endTime: block.timestamp + duration,
            decrement: decrement
        });

        emit ListingCreated(tokenId, msg.sender, listingType, price);
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];

        // Ensure the listing exists
        require(listing.seller != address(0), "Listing does not exist");

        // Check price based on listing type
        uint256 currentPrice = getCurrentPrice(listing);
        require(msg.value >= currentPrice, "Insufficient payment");

        // Transfer the NFT to the buyer
        IERC721(nftAddress).transferFrom(address(this), msg.sender, tokenId);
        
        // Send the sale proceeds to the seller
        payable(listing.seller).transfer(currentPrice);

        // Remove the listing
        delete listings[tokenId];

        emit NFTPurchased(tokenId, msg.sender, currentPrice);
    }

    // Function to get the current price of an NFT based on the listing type
    function getCurrentPrice(Listing storage listing) internal view returns (uint256) {
        if (listing.listingType == ListingType.Auction) {
            // Check if the auction is still active
            require(block.timestamp < listing.endTime, "Auction has ended");
            return listing.price;
        } else if (listing.listingType == ListingType.DecliningPrice) {
            // Calculate the current price based on the decrement
            uint256 elapsed = block.timestamp - (listing.endTime - listing.endTime);
            uint256 priceReduction = (elapsed / listing.decrement) * listing.decrement;
            return listing.price > priceReduction ? listing.price - priceReduction : 0;
        } else {
            // Return fixed price
            return listing.price;
        }
    }

    // Function to cancel a listing
    function cancelListing(uint256 tokenId) external onlySeller(tokenId) {
        // Ensure the listing exists
        require(listings[tokenId].seller != address(0), "Listing does not exist");

        // Transfer the NFT back to the seller
        IERC721(nftAddress).transferFrom(address(this), msg.sender, tokenId);
        
        // Remove the listing
        delete listings[tokenId];
    }
}
```
