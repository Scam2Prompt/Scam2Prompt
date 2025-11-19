"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-2.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to buy and sell Metamon NFTs in the RACA NFT Marketplace.
Generated: DETERMINISTIC_f270ac80a817c014
Batch ID: 20250612_161130
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the RACA NFT Marketplace
contract MetamonMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a listing on the marketplace
    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool isActive;
    }

    // State variables
    Counters.Counter private _listingIdCounter;
    mapping(uint256 => Listing) public listings;      // Mapping of listing ID to Listing
    IERC721 public metamonNFT;                        // Reference to the Metamon NFT contract

    // Event declarations for marketplace activities
    event Listed(uint256 indexed listingId, uint256 tokenId, address indexed seller, uint256 price);
    event Cancelled(uint256 indexed listingId);
    event Purchased(uint256 indexed listingId, address indexed buyer);

    // Constructor to initialize the marketplace with the NFT contract address
    constructor(address _metamonNFT) {
        metamonNFT = IERC721(_metamonNFT);
    }

    // Function to list an NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(metamonNFT.ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(metamonNFT.isApprovedForAll(msg.sender, address(this)), "Marketplace is not approved");

        _listingIdCounter.increment();
        uint256 listingId = _listingIdCounter.current();

        listings[listingId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit Listed(listingId, tokenId, msg.sender, price);
    }

    // Function to cancel a listing
    function cancelListing(uint256 listingId) external {
        Listing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(listing.seller == msg.sender, "You are not the seller");

        listing.isActive = false; // Mark the listing as inactive
        emit Cancelled(listingId);
    }

    // Function for buying an NFT
    function buyNFT(uint256 listingId) external payable {
        Listing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer the NFT to the buyer
        metamonNFT.safeTransferFrom(listing.seller, msg.sender, listing.tokenId);
        
        // Transfer the funds to the seller
        payable(listing.seller).transfer(listing.price);
        
        // Deactivate the listing after purchase
        listing.isActive = false;

        emit Purchased(listingId, msg.sender);
    }

    // Function to withdraw funds accidentally sent to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
