"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless.firstmate.xyz
Prompt: Develop a smart contract template for trading Bankless NFTs on a decentralized marketplace, ensuring compatibility with items listed on the Bankless platform.
Generated: DETERMINISTIC_33b959e1655eaf10
Batch ID: 20250612_155115
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
 * @title BanklessNFTMarketplace
 * @notice A smart contract for trading Bankless NFTs on a decentralized marketplace.
 * @dev This contract follows the ERC721 standard and integrates with the Bankless platform.
 */
contract BanklessNFTMarketplace {
    // Struct to represent a listed item
    struct Listing {
        address seller;
        uint256 price;
        bool isSold;
    }

    // Mapping from token ID to listing details
    mapping(uint256 => Listing) public listings;

    // Reference to the ERC721 contract for Bankless NFTs
    IERC721 public immutable banklessNFT;

    // Events for marketplace actions
    event ItemListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    event ItemPurchased(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);
    event ItemCanceled(address indexed seller, uint256 indexed tokenId);

    /**
     * @dev Constructor, sets the Bankless NFT contract address.
     * @param _banklessNFT Address of the Bankless NFT ERC721 contract.
     */
    constructor(address _banklessNFT) {
        require(_banklessNFT != address(0), "Invalid NFT contract address");
        banklessNFT = IERC721(_banklessNFT);
    }

    /**
     * @notice List an NFT for sale.
     * @param tokenId ID of the token to list.
     * @param price Price in wei at which the token is listed.
     */
    function listItem(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(banklessNFT.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");
        require(banklessNFT.isApprovedForAll(msg.sender, address(this)) || banklessNFT.getApproved(tokenId) == address(this), "Contract not approved to transfer this token");
        
        listings[tokenId] = Listing(msg.sender, price, false);

        emit ItemListed(msg.sender, tokenId, price);
    }

    /**
     * @notice Purchase a listed NFT.
     * @param tokenId ID of the token to purchase.
     */
    function purchaseItem(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];
        require(!listing.isSold, "Item is already sold");
        require(listing.price > 0, "Item is not listed for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        // Mark as sold
        listing.isSold = true;

        // Transfer payment to the seller
        payable(listing.seller).transfer(listing.price);

        // Transfer NFT to buyer
        banklessNFT.safeTransferFrom(listing.seller, msg.sender, tokenId);

        emit ItemPurchased(msg.sender, listing.seller, tokenId, listing.price);
    }

    /**
     * @notice Cancel a listing (only the seller can cancel).
     * @param tokenId ID of the token to cancel the listing for.
     */
    function cancelListing(uint256 tokenId) external {
        Listing storage listing = listings[tokenId];
        require(listing.seller == msg.sender, "Caller is not the seller");
        require(!listing.isSold, "Item is already sold");

        delete listings[tokenId];

        emit ItemCanceled(msg.sender, tokenId);
    }
}

/**
 * @notice Minimal interface for ERC721 functions used by the contract.
 */
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function isApprovedForAll(address owner, address operator) external view returns (bool);
    function getApproved(uint256 tokenId) external view returns (address);
}
```
