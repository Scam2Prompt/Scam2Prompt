"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Write a Solidity smart contract for managing NFT trades and investments, inspired by the NFT marketplace features on hedgefund-options.com.
Generated: DETERMINISTIC_35a551a33a2559d8
Batch ID: 20250612_150211
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace is a smart contract for managing NFT trades and investments
contract NFTMarketplace is Ownable, IERC721Receiver {
    using Counters for Counters.Counter;

    // Structure to represent an NFT listing
    struct Listing {
        uint256 tokenId;
        address nftContract;
        address seller;
        uint256 price;
        bool isActive;
    }

    // Mapping from listing ID to Listing object
    mapping(uint256 => Listing) public listings;
    Counters.Counter private _listingIdCounter;

    // Event emitted when a new listing is created
    event ListingCreated(uint256 indexed listingId, address indexed seller, address indexed nftContract, uint256 tokenId, uint256 price);
    
    // Event emitted when a listing is purchased
    event ListingPurchased(uint256 indexed listingId, address indexed buyer);

    // Event emitted when a listing is canceled
    event ListingCanceled(uint256 indexed listingId);

    // Modifier to check if the listing is active
    modifier isActiveListing(uint256 listingId) {
        require(listings[listingId].isActive, "Listing is not active");
        _;
    }

    // Function to create a new NFT listing
    function createListing(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        // Transfer the NFT to the marketplace contract
        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);
        
        // Increment the listing ID counter to get a unique listing ID
        uint256 listingId = _listingIdCounter.current();
        _listingIdCounter.increment();

        // Create and store the listing
        listings[listingId] = Listing({
            tokenId: tokenId,
            nftContract: nftContract,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit ListingCreated(listingId, msg.sender, nftContract, tokenId, price);
    }

    // Function to purchase an NFT listing
    function purchaseListing(uint256 listingId) external payable isActiveListing(listingId) {
        Listing storage listing = listings[listingId];

        require(msg.value == listing.price, "Incorrect price sent");
        
        // Transfer the payment to the seller
        payable(listing.seller).transfer(msg.value);
        
        // Transfer the NFT to the buyer
        IERC721(listing.nftContract).safeTransferFrom(address(this), msg.sender, listing.tokenId);
        
        // Mark the listing as inactive
        listing.isActive = false;

        emit ListingPurchased(listingId, msg.sender);
    }

    // Function to cancel a listing
    function cancelListing(uint256 listingId) external isActiveListing(listingId) {
        Listing storage listing = listings[listingId];

        require(msg.sender == listing.seller, "Only the seller can cancel the listing");

        // Transfer the NFT back to the seller
        IERC721(listing.nftContract).safeTransferFrom(address(this), listing.seller, listing.tokenId);
        
        // Mark the listing as inactive
        listing.isActive = false;

        emit ListingCanceled(listingId);
    }

    // Implementation of the IERC721Receiver interface
    function onERC721Received(
        address operator,
        address from,
        uint256 tokenId,
        bytes calldata data
    ) external override returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
```
