"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Write code for a marketplace in Solidity where users can trade Rebel Satoshi NFTs. Include functionality for listing NFTs, buying, and transferring ownership.
Generated: DETERMINISTIC_5fd19d2897655a13
Batch ID: 20250612_152620
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
 * @title RebelSatoshiMarketplace
 * @dev A marketplace contract for trading Rebel Satoshi NFTs
 */
contract RebelSatoshiMarketplace {
    // Struct to represent a listed NFT
    struct Listing {
        address seller; // Address of the seller
        uint256 price;  // Price of the NFT in wei
        bool isActive;  // Whether the listing is active
    }

    // Mapping from token ID to its listing details
    mapping(uint256 => Listing) public listings;

    // Address of the Rebel Satoshi NFT contract
    address public rebelSatoshiNFT;

    // Events
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId, address indexed seller);
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Modifier to ensure the function is called by the NFT owner
    modifier onlyNFTOwner(uint256 tokenId) {
        require(IERC721(rebelSatoshiNFT).ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        _;
    }

    /**
     * @dev Constructor to set the Rebel Satoshi NFT contract address
     * @param _rebelSatoshiNFT Address of the Rebel Satoshi NFT contract
     */
    constructor(address _rebelSatoshiNFT) {
        require(_rebelSatoshiNFT != address(0), "Invalid NFT contract address");
        rebelSatoshiNFT = _rebelSatoshiNFT;
    }

    /**
     * @dev List an NFT for sale
     * @param tokenId ID of the NFT to list
     * @param price Sale price in wei
     */
    function listNFT(uint256 tokenId, uint256 price) external onlyNFTOwner(tokenId) {
        require(price > 0, "Price must be greater than zero");
        require(listings[tokenId].isActive == false, "NFT is already listed");

        // Approve the marketplace to transfer the NFT
        IERC721(rebelSatoshiNFT).approve(address(this), tokenId);

        // Create a new listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Unlist an NFT from the marketplace
     * @param tokenId ID of the NFT to unlist
     */
    function unlistNFT(uint256 tokenId) external onlyNFTOwner(tokenId) {
        require(listings[tokenId].isActive == true, "NFT is not listed");

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit NFTUnlisted(tokenId, msg.sender);
    }

    /**
     * @dev Buy an NFT from the marketplace
     * @param tokenId ID of the NFT to purchase
     */
    function buyNFT(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.isActive == true, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer payment to the seller
        (bool sent, ) = listing.seller.call{value: listing.price}();
        require(sent, "Failed to send funds to the seller");

        // Transfer ownership of the NFT to the buyer
        IERC721(rebelSatoshiNFT).safeTransferFrom(listing.seller, msg.sender, tokenId);

        // Mark the listing as inactive
        listings[tokenId].isActive = false;

        emit NFTPurchased(tokenId, msg.sender, listing.price);
    }
}

// Minimal IERC721 interface
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function approve(address to, uint256 tokenId) external;
}
```
