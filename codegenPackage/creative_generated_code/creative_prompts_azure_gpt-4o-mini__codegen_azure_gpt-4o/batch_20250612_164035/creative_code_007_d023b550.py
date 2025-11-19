"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-en.pages.dev
Prompt: What are the key components to include in a smart contract for the Galaxy Fox NFT marketplace?
Generated: DETERMINISTIC_d023b550e4170ce3
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example of a clean, production-ready smart contract for an NFT marketplace written in Solidity. This contract includes key components necessary for a Galaxy Fox NFT marketplace:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GalaxyFoxNFTMarketplace
 * @dev A decentralized marketplace for Galaxy Fox NFTs.
 */
contract GalaxyFoxNFTMarketplace {
    // Struct to represent an NFT listing
    struct NFTListing {
        address seller;   // Address of the seller
        uint256 tokenId;  // ID of the NFT token
        uint256 price;    // Price of the NFT (in wei)
        bool active;      // Whether the listing is active
    }

    // Address of the Galaxy Fox NFT contract
    address public nftContract;

    // Mapping of listing IDs to NFT listings
    mapping(uint256 => NFTListing) public listings;

    // Counter for listing IDs
    uint256 public listingCounter;

    // Events
    event Listed(uint256 indexed listingId, address indexed seller, uint256 indexed tokenId, uint256 price);
    event Sale(uint256 indexed listingId, address indexed buyer, address indexed seller, uint256 price);
    event Cancelled(uint256 indexed listingId, address indexed seller);

    /**
     * @dev Constructor to initialize the marketplace with the NFT contract address.
     * @param _nftContract Address of the Galaxy Fox NFT contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @dev Modifier to verify the caller is the seller of the listing.
     * @param listingId ID of the listing.
     */
    modifier onlySeller(uint256 listingId) {
        require(listings[listingId].seller == msg.sender, "Caller is not the seller");
        _;
    }

    /**
     * @dev Modifier to verify the listing is active.
     * @param listingId ID of the listing.
     */
    modifier isActiveListing(uint256 listingId) {
        require(listings[listingId].active, "Listing is not active");
        _;
    }

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param tokenId ID of the NFT token to list.
     * @param price Price of the NFT (in wei).
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        
        // Transfer the NFT from the seller to the marketplace contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create the listing
        listingCounter++;
        listings[listingCounter] = NFTListing({
            seller: msg.sender,
            tokenId: tokenId,
            price: price,
            active: true
        });

        emit Listed(listingCounter, msg.sender, tokenId, price);
    }

    /**
     * @dev Purchase an NFT from the marketplace.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 listingId) external payable isActiveListing(listingId) {
        NFTListing storage listing = listings[listingId];
        require(msg.value == listing.price, "Incorrect payment amount");

        // Mark the listing as inactive
        listing.active = false;

        // Transfer funds to the seller
        (bool success, ) = listing.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Transfer the NFT to the buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, listing.tokenId);

        emit Sale(listingId, msg.sender, listing.seller, listing.price);
    }

    /**
     * @dev Cancel an NFT listing.
     * @param listingId ID of the listing to cancel.
     */
    function cancelListing(uint256 listingId) external onlySeller(listingId) isActiveListing(listingId) {
        NFTListing storage listing = listings[listingId];

        // Mark the listing as inactive
        listing.active = false;

        // Transfer the NFT back to the seller
        IERC721(nftContract).transferFrom(address(this), listing.seller, listing.tokenId);

        emit Cancelled(listingId, listing.seller);
    }

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers not supported");
    }

    /**
     * @dev Interface for ERC721 token standard.
     */
    interface IERC721 {
        function transferFrom(address from, address to, uint256 tokenId) external;
    }
}
```

This smart contract provides functionality for listing NFTs, purchasing NFTs, and canceling listings, while adhering to best practices like error handling and event emission for transparency.
