"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: Develop a Solidity contract for a decentralized NFT marketplace similar to the one in the Catgirl ecosystem, including features for buying and selling CATGIRL¢-based NFTs.
Generated: DETERMINISTIC_2fe5474c3898dfe8
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Decentralized NFT Marketplace for CATGIRL-based NFTs
 * @dev This contract allows users to list, buy, and sell NFTs using CATGIRL tokens.
 */
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NFTMarketplace {
    // Struct representing an NFT listing
    struct Listing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
    }

    // Mapping from listing ID to a listing
    mapping(uint256 => Listing) public listings;

    // Counter for generating unique listing IDs
    uint256 private listingCounter;

    // Address of the CATGIRL token contract
    address public immutable catgirlToken;

    // Events
    event Listed(uint256 listingId, address indexed seller, address indexed nftContract, uint256 indexed tokenId, uint256 price);
    event Sold(uint256 listingId, address indexed buyer, address indexed nftContract, uint256 indexed tokenId, uint256 price);
    event Cancelled(uint256 listingId, address indexed seller, address indexed nftContract, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with the CATGIRL token address.
     * @param _catgirlToken Address of the CATGIRL token contract.
     */
    constructor(address _catgirlToken) {
        require(_catgirlToken != address(0), "Invalid CATGIRL token address");
        catgirlToken = _catgirlToken;
    }

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     * @param price Price of the NFT in CATGIRL tokens.
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");

        // Increment listing counter and create the listing
        listingCounter++;
        listings[listingCounter] = Listing(msg.sender, nftContract, tokenId, price);

        emit Listed(listingCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Cancel an NFT listing.
     * @param listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external {
        Listing memory listing = listings[listingId];
        require(listing.seller == msg.sender, "You are not the seller");
        require(listing.price > 0, "Listing does not exist");

        // Remove the listing
        delete listings[listingId];

        emit Cancelled(listingId, msg.sender, listing.nftContract, listing.tokenId);
    }

    /**
     * @dev Buy an NFT from the marketplace.
     * @param listingId ID of the listing to buy.
     */
    function buyNFT(uint256 listingId) external {
        Listing memory listing = listings[listingId];
        require(listing.price > 0, "Listing does not exist");

        // Transfer CATGIRL tokens from buyer to seller
        require(IERC20(catgirlToken).transferFrom(msg.sender, listing.seller, listing.price), "Token transfer failed");

        // Transfer NFT from seller to buyer
        IERC721(listing.nftContract).transferFrom(listing.seller, msg.sender, listing.tokenId);

        // Remove the listing
        delete listings[listingId];

        emit Sold(listingId, msg.sender, listing.nftContract, listing.tokenId, listing.price);
    }

    /**
     * @dev Fetch details of a specific listing.
     * @param listingId ID of the listing to fetch.
     * @return seller Address of the seller.
     * @return nftContract Address of the NFT contract.
     * @return tokenId ID of the NFT token.
     * @return price Price of the NFT in CATGIRL tokens.
     */
    function getListing(uint256 listingId) external view returns (address seller, address nftContract, uint256 tokenId, uint256 price) {
        Listing memory listing = listings[listingId];
        return (listing.seller, listing.nftContract, listing.tokenId, listing.price);
    }
}
```
